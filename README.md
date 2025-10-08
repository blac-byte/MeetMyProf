## Models
1. User
2. Student
3. Teacher
4. Course
5. Time
6. Classes

   Users
   | id | email                                   | left(password_hash,3) | role    | is_active |
   |----|-----------------------------------------|-----------------------|---------|-----------|
   | 1  | blac.byte2025@vitstudent.ac.in | pbk                   | student | 1         |

   Users is the common database table where all the users are initially stored i.e. teachers and students. They are then referenced from the User table and written into their respective tables
   - Student
   - Teacher
     
