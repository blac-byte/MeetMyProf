## Models
Models folder consists of all the database models used in the project

1. User
2. Student
3. Teacher
4. Course
5. Time
6. Classes
7. Booking
8. Slot
---

- User
  
  User is the common database table where all the users(teacher, student) are initially stored. They are then referenced from the User table and written into their respective tables.

  
   | id | email                                   | hashed_password | role    | is_active |
   |----|-----------------------------------------|-----------------------|---------|-----------|
   | 1  | blac.byte2025@vitstudent.ac.in | pbk                   | student | 1         |
  
  id - auto incremented primary key
  
  email - only accepts vit domain email
  
  hashed_password - stores only hashed+salted passwords, this is only a VIEW
  
  role - enum between student and teacher
  
  is_active - boolean value
---   
- Student (notice the email format)
  
  Admin controlled table. Has no write interaction from the program.

  
  | reg_id | user_id | batch | email                                   |
  |--------|---------|-------|-----------------------------------------|
  | 1      | 1       | ALL03  | blac.byte2025@vitstudent.ac.in |
  
  reg_id - auto incremented primary key for now
  
  user_id - foreign key from User
  
  batch - taken from the parsed timetable and updated
  
  email - only accepts vit domain email
---
- Teacher (notice the differece in the email format)
  
  Admin controlled table. Has no write interaction from the program.

  
  | reg_id | user_id | batch | email                                   |
  |--------|---------|-------|-----------------------------------------|
  | 1      | 1       | ALL03  | blac.byte@vit.ac.in |  
---    
- Course
  
  Course contains all the courses offered by the institute. Admin controlled table. Has no write interaction from the program.
  
   | id | course_id | course_type | batch | building | room |
   |----|-----------|-------------|-------|----------|------|
   | 1  | BAEEE101  | ETH         | ALL03 | PRP      | 105  |
   | 2  | BACSE103  | ETH         | ALL03 | PRP      | 105  |
   | 3  | BAMAT101  | ETH         | ALL03 | PRP      | 105  |
   | 4  | BACHY105  | ETH         | ALL03 | PRP      | 105  |
   | 5  | BAMAT101  | ELA         | ALL03 | PRP      | 445  |
   | 6  | BACSE101  | LO          | ALL03 | PRP      | 117A |
   | 7  | BACHY105  | ELA         | ALL03 | PRP      | G07  |
   | 8  | BACSE103  | ELA         | ALL03 | PRP      | 356  |
   | 9  | BAEEE101  | ELA         | ALL03 | PRP      | 355  |
---
- Time
  
  Shows how the day is divided into slots. The time is stored in 24 hour system. 
  This table is assumed to be universal for the institute.
  
   | id  | reg_id | column_id | start | end   | course_type |
   |-----|--------|-----------|-------|-------|-------------|
   | 1  | 1      | 0         | 08:00 | 08:50 | ETH         |
   | 2  | 1      | 1         | 09:00 | 09:50 | ETH         |
   | 3  | 1      | 2         | 10:00 | 10:50 | ETH         |
   | 4 | 1      | 3         | 11:00 | 11:50 | ETH         |
   | 5 | 1      | 4         | 12:00 | 12:50 | ETH         |
   | 6 | 1      | 5         | 14:00 | 14:50 | ETH         |
   | 7 | 1      | 6         | 15:00 | 15:50 | ETH         |
   | 8 | 1      | 7         | 16:00 | 16:50 | ETH         |
   | 9 | 1      | 8         | 17:00 | 17:50 | ETH         |
   | 10 | 1      | 9         | 18:00 | 18:50 | ETH         |
   | 11 | 1      | 10        | 18:51 | 19:00 | ETH         |
   | 12 | 1      | 11        | 19:01 | 19:50 | ETH         |
   | 13 | 1      | 0         | 08:00 | 08:50 | ELA         |
   | 14 | 1      | 1         | 08:51 | 09:40 | ELA         |
   | 15 | 1      | 2         | 09:51 | 10:40 | ELA         |
   | 16 | 1      | 3         | 10:41 | 11:30 | ELA         |
   | 17 | 1      | 4         | 11:40 | 12:30 | ELA         |
   | 18 | 1      | 5         | 12:31 | 13:20 | ELA         |
   | 19 | 1      | 6         | 14:00 | 14:50 | ELA         |
   | 20 | 1      | 7         | 14:51 | 15:40 | ELA         |
   | 21 | 1      | 8         | 15:51 | 16:40 | ELA         |
   | 22 | 1      | 9         | 16:41 | 17:30 | ELA         |
   | 23 | 1      | 10        | 17:40 | 18:30 | ELA         |
   | 24 | 1      | 11        | 18:31 | 19:20 | ELA         |
---
- Classes
  
  Classes shows the different classes of the user. This column matches the timing of the classes using the column_id which is just the index of the time slot so from 0-11 which when            matched with the time database table gives the proper time.
  
   | id  | reg_id | course_id | course_type | day  | column_id |
   |-----|--------|-----------|-------------|------|-----------|
   | 1   | 1      | BAEEE101  | ETH         | MON  | 6         |
   | 2   | 1      | BACSE103  | ETH         | MON  | 8         |
   | 3   | 1      | BAMAT101  | ETH         | MON  | 9         |
   | 4   | 1      | BACHY105  | ETH         | MON  | 10        |
   | 5   | 1      | BAMAT101  | ETH         | TUE  | 6         |
   | 6   | 1      | BACHY105  | ETH         | TUE  | 7         |
   | 7   | 1      | BAEEE101  | ETH         | WED  | 7         |
   | 8   | 1      | BACSE103  | ETH         | WED  | 9         |
   | 9   | 1      | BACSE103  | ETH         | THU  | 6         |
   | 10  | 1      | BAMAT101  | ETH         | THU  | 7         |
   | 11  | 1      | BACHY105  | ETH         | THU  | 8         |
   | 12  | 1      | BAEEE101  | ETH         | FRI  | 8         |
   | 13  | 1      | BAMAT101  | ELA         | MON  | 2         |
   | 14  | 1      | BAMAT101  | ELA         | MON  | 3         |
   | 15  | 1      | BACSE101  | ELA         | TUE  | 0         |
   | 16  | 1      | BACSE101  | ELA         | TUE  | 1         |
   | 17  | 1      | BACHY105  | ELA         | WED  | 0         |
   | 18  | 1      | BACHY105  | ELA         | WED  | 1         |
   | 19  | 1      | BACSE103  | ELA         | WED  | 2         |
   | 20  | 1      | BACSE103  | ELA         | WED  | 3         |
   | 21  | 1      | BAEEE101  | ELA         | FRI  | 0         |
   | 22  | 1      | BAEEE101  | ELA         | FRI  | 1         |
   | 23  | 1      | BACSE101  | ELA         | FRI  | 2         |
   | 24  | 1      | BACSE101  | ELA         | FRI  | 3         |
