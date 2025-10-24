## Routes

**Routes folder handles most of the routes in this web app.** 

1. auth.py  
   Handles user authentication

Endpoints : /signup
Methods : GET, POST
Registers new users using their institute email.
-Validates email format.

-Hashes password before storing.

-Redirects to appropriate dashboard.

Endpoints : /signin
Methods : GET, POST
Logs in new users using their institute email.
-Validates email format.

-Hashes password and matches with the stored hashed password.

-Redirects to appropriate dashboard.

Notes

Uses Flask-Login for session management.

Returns error messages via flash() on failure.

1. dashboard
   Shows the current days schedule
Endpoints : POST
  


1. logout
   
   Logs the current user out. Clears out the session data.
   
