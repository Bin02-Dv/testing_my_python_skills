from string import digits, ascii_letters, punctuation

real_password = "@saa"

passwords = []

# for first_set in digits:
#     for second_set in digits:
#         for third_set in digits:
#             for fourth_set in digits:
#                 password  = first_set + second_set + third_set + fourth_set
#                 passwords.append(password)
#                 print(first_set, second_set, third_set, fourth_set)
                
# for first_set in ascii_letters:
#     for second_set in ascii_letters:
#         for third_set in ascii_letters:
#             for fourth_set in ascii_letters:
#                 password  = first_set + second_set + third_set + fourth_set
#                 passwords.append(password)
                
for first_set in ascii_letters + digits + punctuation:
    for second_set in ascii_letters + digits + punctuation:
        for third_set in ascii_letters + digits + punctuation:
            for fourth_set in ascii_letters + digits + punctuation:
                print(first_set, second_set, third_set, fourth_set)
                
                password  = first_set + second_set + third_set + fourth_set
                passwords.append(password)


for password in passwords:
            
    if password == real_password:
        print("BINGO... Your password is:", password)