from flask import Flask, render_template, Response, jsonify, request
import cv2
import mediapipe as mp
import numpy as np
import threading

app = Flask(__name__)

# Initialize Mediapipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Global Variables
exercise = ""
target_reps = 0
counts = {"Push-Ups": 0, "Squats": 0, "Jumping Jacks": 0}
states = {"Push-Ups": None, "Squats": None, "Jumping Jacks": None}

# Helper function to calculate angles
def calculate_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    return 360 - angle if angle > 180 else angle

# Webcam feed generator
def generate_frame():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        # Draw pose landmarks
        frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Extract landmarks
            landmarks = results.pose_landmarks.landmark

            if exercise == "Push-Ups":
                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                angle = calculate_angle(shoulder, elbow, wrist)

                if angle > 160:  # Up position
                    states["Push-Ups"] = "up"
                if angle < 90 and states["Push-Ups"] == "up":  # Down position
                    counts["Push-Ups"] += 1
                    states["Push-Ups"] = "down"

            elif exercise == "Squats":
                hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                       landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                angle = calculate_angle(hip, knee, ankle)

                if angle > 160:  # Up position
                    states["Squats"] = "up"
                if angle < 100 and states["Squats"] == "up":  # Down position
                    counts["Squats"] += 1
                    states["Squats"] = "down"

            elif exercise == "Jumping Jacks":
                hand_distance = abs(landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x -
                                    landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x)
                foot_distance = abs(landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x -
                                    landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x)

                if hand_distance > 0.5 and foot_distance > 0.5:  # Wide position
                    states["Jumping Jacks"] = "wide"
                elif hand_distance < 0.3 and foot_distance < 0.3 and states["Jumping Jacks"] == "wide":
                    counts["Jumping Jacks"] += 1
                    states["Jumping Jacks"] = "narrow"

        # Display counts on the frame
        cv2.putText(frame, f"{exercise} Count: {counts[exercise]}/{target_reps}",
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Stop when target is reached
        if counts[exercise] >= target_reps:
            cv2.putText(frame, "Target Reached!", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            break

        # Convert frame to JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        if not ret:
            break
        frame_data = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n\r\n')

    cap.release()

# Start workout
@app.route('/start_workout', methods=["POST"])
def start_workout():
    global exercise, target_reps
    exercise = request.form.get("exercise")
    target_reps = int(request.form.get("target_reps"))
    return jsonify({"message": "Workout started!"})

# Video feed route
@app.route('/video_feed')
def video_feed():
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Main page
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
