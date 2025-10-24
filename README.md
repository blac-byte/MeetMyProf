# 🎓 MeetMyProf

MeetMyProf is a **web application** designed to simplify and enhance the process of **scheduling appointments between students and teachers**.  
It provides a **seamless, all-in-one platform** for booking and managing appointments — ensuring a smooth and effortless experience for every user.

---

```
                                                                                                                              
88b           d88                                   88b           d88               88888888ba                              ad88  
888b         d888                            ,d     888b         d888               88      "8b                            d8"    
88`8b       d8'88                            88     88`8b       d8'88               88      ,8P                            88     
88 `8b     d8' 88   ,adPPYba,   ,adPPYba,  MM88MMM  88 `8b     d8' 88  8b       d8  88aaaaaa8P'  8b,dPPYba,   ,adPPYba,  MM88MMM  
88  `8b   d8'  88  a8P_____88  a8P_____88    88     88  `8b   d8'  88  `8b     d8'  88""""""'    88P'   "Y8  a8"     "8a   88     
88   `8b d8'   88  8PP"""""""  8PP"""""""    88     88   `8b d8'   88   `8b   d8'   88           88          8b       d8   88     
88    `888'    88  "8b,   ,aa  "8b,   ,aa    88,    88    `888'    88    `8b,d8'    88           88          "8a,   ,a8"   88     
88     `8'     88   `"Ybbd8"'   `"Ybbd8"'    "Y888  88     `8'     88      Y88'     88           88           `"YbbdP"'    88     
                                                                           d8'                                                    
                                                                          d8'
                                                                                     
```

---

## 🧩 Project Structure

```
app
├── __pycache__/
├── models/
├── routes/
├── services/
├── static/
├── templates/
├── utils/
├── env/
├── instance/
├── .gitignore
├── raw.txt
├── requirements.txt
└── run.py
```

Each directory in this structure plays a key role in maintaining a clean, modular Flask architecture.

---

## 📘 Folder Documentation

### 🧱 [Models](app/models/README.md)
Contains all the **database models** used in the project — including definitions for users, teachers, students, classes, bookings, and time schedules.

---

### 🌐 [Routes](app/routes/README.md)
Houses all the **Flask routes** that define the web app’s endpoints — handling authentication, dashboards, booking, and user session logic.

---

### ⚙️ [Services](app/services/README.md)
Includes the **business logic** of the web app.  
Contains:
- `booking.py` → manages booking functionality  
- `parser.py` → processes uploaded timetables  
- `schedule.py` → handles scheduling and time-based logic  

---

### 🧰 [Utils](app/utils/README.md)
Responsible for **error handling and utility functions**, including:
- Dynamic user role detection (student/teacher)  
- Application-wide exception handlers  

---

## 🧾 Requirements
All Python dependencies are listed in `requirements.txt`.  
To install them, run:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the App
Run the development server locally:
```bash
python run.py
```

Access it in your browser at:
```
http://127.0.0.1:5000
```

---

## 💡 Future Enhancements
- 🗓️ Google Calendar integration for real-time syncing  
- 📬 Email notifications for confirmed bookings  
- 📊 Admin analytics dashboard  

---

**Made with ❤️ using Flask, SQLAlchemy, and pure curiosity.**







     
