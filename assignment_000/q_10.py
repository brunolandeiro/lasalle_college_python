digits = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
password = input("password (4 digits a to z): ")

flag = False
for a in digits:
    for b in digits:
        for c in digits:
            for d in digits:
                newpass = a+b+c+d
                print(newpass)
                if(newpass == password):
                    flag = True
                    break
            if(flag): break    
        if(flag): break    
    if(flag): break    