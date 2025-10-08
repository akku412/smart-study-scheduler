🎓 AI-Powered Smart Study Scheduler 🚀



An intelligent AI-based study scheduling system that helps students plan their study sessions efficiently using logic-driven algorithms.

This project is a B.Tech Final Year Project showcasing full-stack development, AI rule-based planning, and data persistence.

🧠 Key Highlights

🕒 Smart AI Scheduling: Generates personalized weekly timetables using a custom priority formula.

⚡ Adaptive Logic: Auto-reschedules missed tasks with urgency boost.

📈 Progress Tracking: Mark sessions as Complete or Missed — the AI adapts accordingly.

💾 Offline & Free: Runs fully locally — no external APIs or internet needed.

🎨 Clean React UI: Simple and responsive dashboard for easy use.

🧩 Tech Stack

Layer	Technology

Frontend	React 18+, Axios, CSS

Backend	FastAPI (Python 3.12), SQLAlchemy, SQLite

Server	Uvicorn

AI Logic	Custom Python (no ML libraries)

⚙️ Installation & Setup

🖥️ Backend Setup

Open a terminal in the backend folder.

Install required packages:

pip install fastapi==0.104.1 uvicorn==0.24.0 sqlalchemy==2.0.23 pydantic==2.5.0


Run the backend:

python -m uvicorn main:app --reload


Backend runs at 👉 http://127.0.0.1:8000

Swagger Docs: http://127.0.0.1:8000/docs

💻 Frontend Setup

Open another terminal in the frontend_old folder.

Install dependencies:

npm install


Start the frontend:

npm start


Open http://localhost:3000

 in your browser.
 
(Ensure the backend is running first.)

📖 How It Works

Create Profile – Enter your name and study preference (morning/evening).

Add Subjects – Provide subject name, difficulty, and exam date.

AI Scheduling – The system automatically generates an optimal timetable.

Track Progress – Mark sessions completed or missed; AI adapts future plans.

View Results – Clean UI with data saved in study_scheduler.db.

🔢 Priority Formula

Priority = (0.4 × Urgency) + (0.3 × Difficulty) + (0.3 × Behind Factor)


📘 Explanation:

Urgency – Days remaining for the exam.

Difficulty – Subject complexity rating.

Behind Factor – Based on previous progress.

📂 Folder Structure

smart-study-scheduler/

│
├── backend/

│   ├── main.py

│   ├── ai_engine.py

│   ├── database.py

│   └── models.py
│

├── frontend_old/

│   ├── src/

│   │   ├── App.js

│   │   ├── api.js

│   │   └── schedule.js

│   └── public/

│

└── README.md

🧰 Troubleshooting

Issue	Cause	Solution

uvicorn not recognized	Uvicorn not added to PATH	Use python -m uvicorn main:app --reload

CORS/Network Error	Backend not running	Start backend before frontend

No Schedule Generated	Invalid or past exam dates	Add future dates only

Port Conflict	Port 8000 in use	Change port in main.py & api.js


 
🌱 Future Improvements

📧 Email/SMS reminders for study sessions

🤖 ML-based prediction of completion rates

📱 Mobile version using React Native

📊 Analytics dashboard with charts

☁️ Cloud DB integration (MongoDB or Firebase)

👩‍💻 Author

Aakanksha

🎓 B.Tech in Computer Science & Engineering

📍 AI-Powered Smart Study Scheduler (Final Year Project)

💡 Inspired by productivity science, adaptive learning, and time optimization.

⭐ If you found this project helpful, give it a star on GitHub!

📬 For queries or feedback, feel free to reach out via comments or issues.
