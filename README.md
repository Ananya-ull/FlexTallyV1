<h1>FlexTally-Real Time Workout Tracker 🎯</h1>
<h2>Basic Details</h2>
<h3>Team Name: TechTitans</h3>
<h2>Team Members</h2>

    Member 1: Niyati Pradeep - TKM College of Engineering
    Member 2: Ananya Ullas - TKM College of Engineering
   
<h2>Hosted Project Link</h2>

[mention your project hosted project link here]
<h2>Project Description</h2>

Flextally is an innovative fitness web app that leverages cutting-edge computer vision technology to provide real-time workout tracking, form feedback, and personalized goal setting, helping users stay motivated and achieve their fitness goals efficiently.

<h2>The Problem statement</h2>

In the fast-paced digital age, many individuals face challenges in maintaining consistent fitness routines due to the lack of accessible, user-friendly, and cost-effective workout solutions. Existing fitness applications often rely on expensive wearables, require manual input for tracking, or fail to provide real-time feedback, resulting in less engaging and less effective fitness experiences. This gap makes it difficult for users to track their progress accurately, receive feedback on form, and stay motivated during their at-home workouts.

<h2>The Solution</h2>

Flextally addresses these challenges by providing an intuitive web-based fitness tracking platform that utilizes computer vision technology to offer real-time workout recognition and feedback. Using OpenCV and Mediapipe for pose detection, the app can accurately track predefined exercises such as push-ups, squats, and jumping jacks without requiring additional equipment. The platform provides real-time repetition counts, form correction feedback, and goal tracking, ensuring a safe and effective fitness experience. By eliminating the need for wearables and leveraging a user-friendly interface accessible via webcam, Flextally empowers users to enhance their fitness journey conveniently from the comfort of their homes.

<h2>Technical Details</h2>
Technologies/Components Used

<h2>For Software:</h2>
Frontend Technologies

    HTML, CSS, JavaScript: For creating a modern, responsive, and interactive user interface.
    Bootstrap/Tailwind CSS: For enhancing the UI with pre-designed components and styling.

Backend Technologies

    Flask/Django (Python): For managing the server-side logic and APIs.

Computer Vision Libraries

    OpenCV: For video processing and real-time workout recognition.
    MediaPipe: For pose detection and tracking during exercises.
Development Tools

    Visual Studio Code: For coding and debugging.
    Git and GitHub: For version control and collaboration.


<h2>Implementation</h2>

<h2>For Software:</h2>
 Frontend Implementation

    User Interface Design:
        Create responsive web pages using HTML, CSS, and JavaScript for key functionalities like login, signup, and workout tracking.
        Use frameworks like Tailwind CSS or Bootstrap to enhance the design and improve user experience.
        Implement real-time updates (e.g., repetition counts) using JavaScript.
Backend Implementation

    API Development:
        Develop RESTful APIs using Flask to handle user authentication, workout data storage, and goal tracking.
        Implement a secure login system with hashed passwords and session management.
 Computer Vision Integration

    Pose Detection:
        Use MediaPipe for real-time pose detection from the webcam feed.
        Process frames using OpenCV to extract key points for different exercises.

Installation

pip install mediapipe
pip install python-opencv
pip install numpy
pip install Flask

Run

python app.py

Project Documentation

For Software:
Screenshots (Add at least 3)

FlexTally Real time workout tracking ![Screenshot 2025-01-26 093302](https://github.com/user-attachments/assets/6abce1a6-0233-424a-a6dc-4794789748ba)

Processess Exercise And increments count on each of the repetion 


Celebration Page ![Screenshot 2025-01-26 093409](https://github.com/user-attachments/assets/3726bb74-9797-4dd6-b395-a76806c7f6fc)
This Page shows a Congratulation message on reaching target repetitions

Home Page ![Screenshot 2025-01-26 093318](https://github.com/user-attachments/assets/a812369d-81de-416b-abf4-300823a34e38)
This is a home page which is reached after login or signup

Login Page![Screenshot 2025-01-26 093334](https://github.com/user-attachments/assets/46ae5463-dc11-4fbf-9651-6325631d0bcd)

Sign Up Page![Screenshot 2025-01-26 093352](https://github.com/user-attachments/assets/c5b6115a-f711-4cbf-b54d-a12cbfaa5f78)

Diagrams

![Workflow](Add your workflow/architecture diagram here) Add caption explaining your workflow


Video

https://drive.google.com/file/d/1D7pe7CWicyLhKun8lnrrWv2Eyxhjyyt4/view?usp=drivesdk

Team Contributions

    Ananya Ullas : designed the interface of index.html
    Niyati Pradeep: designed the login,home and signup page
    Both :developed an opencv python script and integrated backend using Flask

Made with ❤️ at TinkerHub
