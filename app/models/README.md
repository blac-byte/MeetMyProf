1. User
   User is where all the users(teacher, student) are stored initailly along with their emails and hashed passwords.
<br>
   | id | email                                   | hashed_password | role    | is_active |
   |----|-----------------------------------------|-----------------------|---------|-----------|
   | 1  | blac.byte2025@vitstudent.ac.in | pbk                   | student | 1         |
   - id - auto incremented primary key
   - email - only accepts vit domain email
   - hashed_password - stored only hashed+salted password. This is only a VIEW
   - role - ENUM of student, teacher
   - is_active - boolean value
<br>
3. Student 

| reg_id | user_id | batch | email                                   |
|--------|---------|-------|-----------------------------------------|
| 1      | 1       | NULL  | blac.byte@vit.ac.in |


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


| id  | reg_id | course_id | course_type | day  | column_id |
|-----|--------|-----------|-------------|------|-----------|
| 97  | 1      | BAEEE101  | ETH         | MON  | 6         |
| 98  | 1      | BACSE103  | ETH         | MON  | 8         |
| 99  | 1      | BAMAT101  | ETH         | MON  | 9         |
| 100 | 1      | BACHY105  | ETH         | MON  | 10        |
| 101 | 1      | BAMAT101  | ETH         | TUE  | 6         |
| 102 | 1      | BACHY105  | ETH         | TUE  | 7         |
| 103 | 1      | BAEEE101  | ETH         | WED  | 7         |
| 104 | 1      | BACSE103  | ETH         | WED  | 9         |
| 105 | 1      | BACSE103  | ETH         | THU  | 6         |
| 106 | 1      | BAMAT101  | ETH         | THU  | 7         |
| 107 | 1      | BACHY105  | ETH         | THU  | 8         |
| 108 | 1      | BAEEE101  | ETH         | FRI  | 8         |
| 109 | 1      | BAMAT101  | ELA         | MON  | 2         |
| 110 | 1      | BAMAT101  | ELA         | MON  | 3         |
| 111 | 1      | BACSE101  | ELA         | TUE  | 0         |
| 112 | 1      | BACSE101  | ELA         | TUE  | 1         |
| 113 | 1      | BACHY105  | ELA         | WED  | 0         |
| 114 | 1      | BACHY105  | ELA         | WED  | 1         |
| 115 | 1      | BACSE103  | ELA         | WED  | 2         |
| 116 | 1      | BACSE103  | ELA         | WED  | 3         |
| 117 | 1      | BAEEE101  | ELA         | FRI  | 0         |
| 118 | 1      | BAEEE101  | ELA         | FRI  | 1         |
| 119 | 1      | BACSE101  | ELA         | FRI  | 2         |
| 120 | 1      | BACSE101  | ELA         | FRI  | 3         |



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

