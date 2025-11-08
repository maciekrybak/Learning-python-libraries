import re

login_pattern = r'^[a-z0-9]{3,8}$'
email_pattern = r'^[a-z]{3,8}[@]{1}[a-z]{2,5}[.]{1}com$'
password_pattern = r'[\w]{2,12}'

users = [
    ('marc', 'marc@omotillo204.com', 'z5205'),
    ('beren', 'beren123@gmail.com', '5205'),
    ('so_dandy', 'so_dandy@maarine.net', '1234567890'),
    ('omotillo204', 'omotillo204@yahoo.com', 'das5205'),
    ('maarine', 'maarine@bere.com', 'DANDY123'),
    ('dandy52', 'dandy@marc.io', 'omotillo204'),
]
for data in users:
    login = data[0]
    email = data[1]
    password = data[2]
    if re.match(login_pattern,login) and re.match(email_pattern,email) and re.match(password_pattern,password):
        print(f'LOGIN : {login}')
        print(f'EMAIL : {email}')
        print(f'PASSWORD : {password}')


