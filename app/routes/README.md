## Routes

**Routes folder handles most of the routes in this web app.** 

1. auth
   
  This takes care of the user signup and signin.
  In signin route, it first of all checks the email format to validate the email, then hashes the password and finally logs in the user.
  In signup route, it checks with the database, finds out whether the user is a teacher or a student and logs them in.


1. dashboard
   
   Just a route to load the dashboard.html


1. logout
   
   Logs out user
   
