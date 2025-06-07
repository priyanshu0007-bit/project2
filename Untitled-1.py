def is_strong(pwd):
    
    if len(pwd) >= 8 and any(c.isupper() for c in pwd) and any(c.islower() for c in pwd) and any(c.isdigit() for c in pwd):
        return True
    return False
password = input("enter password:")
if(is_strong(password)):
    print("your pass is strong", password)  
else:
    print("pass is not strong", password)      
