# 📁 Routes

This folder defines most of the **Flask route blueprints** used in the MeetMyProf web application.  
Each module handles a specific part of the site, such as authentication, dashboard rendering, or logout operations.

---

## 🔐 `auth.py`

Handles **user authentication** — including signup and signin processes.

### **Endpoints**

#### `/signup`
**Method:** `POST`, `GET`   
**Description:**  
Registers a new user (teacher or student) based on input data.  
- Validates only specific email format.  
- Hashes and stores the password securely. The password hashing is handled inside the models folder.  
- Checks the email to determine whether the user is a teacher or a student.  
- Logs in the user and redirects to their dashboard.  

#### `/signin`
**Method:** `POST`, `GET`    
**Description:**  
Authenticates an existing user.  
- Validates email and password.  
- Compares entered password with hashed password in the database.  
- Starts a user session using Flask-Login.  
- Redirects to the user’s dashboard upon success.  

### **Notes**
- Uses `Flask-Login` for session management.  
- Returns error messages via `flash()` when login or signup fails.
- The user type (student, teacher) is determined according to the email used by the user.

---

## 📊 `dashboard.py`

Responsible for **loading and displaying the user’s dashboard**.

### **Endpoints**

#### `/dashboard`
**Method:** `POST`  
**Description:**  
Renders `dashboard.html` and populates it with the current day’s schedule.  
- Retrieves the user’s schedule using `get_todays_schedule()`.  
- Displays classes and available slots.  
- If no classes exist, shows a “No classes scheduled today” message.

---

## 🚪 `logout.py`

Handles **logging the user out** of the application.

### **Endpoints**

#### `/logout`
**Method:** `POST`, `GET`    
**Description:**  
Ends the user session and redirects to the home or login page.  
- Clears all session data.  
- Logs out the user with `logout_user()` from `Flask-Login`.

---

## 🧩 Future Routes (Planned)

| File | Purpose |
|------|----------|
| `auth.py` | use 0Auth |
| `auth.py` | rate limiting |
| `auth.py` | remember me |
| `parser.py` | Processes uploaded timetable or CSV files. |


---

## 🧱 General Notes

- All routes use **Flask Blueprints** for modularity.  
- Common error handling is registered via `register_error_handlers()` from `app/utils/errors.py`.  
- Routes requiring authentication are protected with the `@login_required` decorator.

   
