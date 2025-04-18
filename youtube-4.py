password = "@me_//123ABC"

word_list = ["123456", "admin", "letmein", "python123", "bin002"]

for word in word_list:
    
    if word == password:
        
        print(f"Password found: {word}")
        
        break
else:
    print("Password not found!")