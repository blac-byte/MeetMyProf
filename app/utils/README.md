## Utils
Takes care of error handling and user type check.

### User check

```
def is_student_email(email):
    pattern = r'^[a-zA-Z]+(\.[a-zA-Z]+)?\d{4}@vitstudent\.ac\.in$'
    return bool(re.match(pattern, email))

def is_teacher_email(email):
    pattern = r'^[a-zA-Z]+(\.[a-zA-Z]+)?@vit\.ac\.in$'
    return bool(re.match(pattern, email))
```
