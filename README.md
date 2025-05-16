# AcademiaConnect – Research Collaboration Platform

UMBC MPS Software Engineering SENG645 Spring 2025 Group Project

Welcome to **AcademiaConnect**, a centralized platform transforming global research collaboration. Designed specifically for professors and students, it streamlines communication, simplifies project management, and fosters academic networking across disciplines.

## 🌐 Screenshots

<img width="1266" alt="Screenshot 2025-05-16 at 12 07 18 AM" src="https://github.com/user-attachments/assets/186e0cef-3e89-4e60-aeb9-67e18995442a" />
<img width="1271" alt="Screenshot 2025-05-16 at 12 07 34 AM" src="https://github.com/user-attachments/assets/ab935537-7b0a-4350-8f29-4c449a6a9012" />
<img width="1265" alt="Screenshot 2025-05-16 at 12 07 47 AM" src="https://github.com/user-attachments/assets/9bcd0869-edac-4d2d-9c35-d36e78696871" />
<img width="1268" alt="Screenshot 2025-05-16 at 12 08 04 AM" src="https://github.com/user-attachments/assets/07900cc0-a2d7-47e8-8a5e-446588f61be4" />
<img width="1267" alt="Screenshot 2025-05-16 at 12 08 17 AM" src="https://github.com/user-attachments/assets/70ffecfd-f822-47f7-a139-b5f3061fbfd7" />
<img width="1261" alt="Screenshot 2025-05-16 at 12 08 29 AM" src="https://github.com/user-attachments/assets/3270b4dd-8940-4a63-91ed-d2ca4466f4f8" />





---

## 🚀 Key Features

- **Profile-Specific Login**  
  Secure Firebase authentication tailored for students and professors.

- **Research & Project Feed**  
  Discover and post collaborative research opportunities in a centralized stream.

- **Instant Collaboration Requests**  
  One-click join requests and real-time status updates.

- **Project Management Dashboard**  
  Professors can easily post, edit, and track ongoing projects.

- **User Profile System**  
  Display research interests, academic background, and skillsets for collaboration.

---

## 🧠 Tech Stack

### Frontend
- `React` (with `Vite`)
- Progressive Web App (PWA) for mobile compatibility

### Backend
- `Django` (Python)
- `PostgreSQL` database

### Authentication
- `Firebase` NoSQL Auth

### DevOps & Tools
- `Docker` for containerization
- `JIRA` & `Confluence` for project & documentation management
- `Bitbucket` for source control
- Deployment via `Firebase` and `Render`

---



## 🔮 Future Scope

- AI-powered talent matching system  
- Integrated messaging & group chat  
- Virtual meetings (audio/video)  
- Webinar & academic conference hosting  
- Achievement badges and peer endorsements

---

## 🧑‍💻 How to Run Locally



```bash
git clone https://bitbucket.org/academia_connect/academia_connect.git
cd academia_connect
npm install
npm run dev


git clone https://bitbucket.org/academia_connect/academia_connect_backend.git
cd academia_connect_backend
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py runserver

