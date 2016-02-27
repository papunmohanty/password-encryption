def encryption():
    count = 0
    print "========================================================="
    password = raw_input("Enter your Password between 6 to 8 Characters: ")
    tempPassword = []
    if len(password) < 7 or len(password) > 8:
        print "Your Password Must be 7 - 8 Characters Long --- Try Again"
        encryption()
    for e in password:
        if e == 'a':
            temp = '@'
            count += 1
            if count <=2:
                tempPassword.append(temp)
            else:
                tempPassword.append('a')
        elif e == 'e':
            temp = '3'
            count += 1
            if count <=2:
                tempPassword.append(temp)
            else:
                tempPassword.append('e')
        elif e == 'i':
            temp = '1'
            count += 1
            if count <=2:
                tempPassword.append(temp)
            else:
                tempPassword.append('i')
        elif e == 'o':
            temp = '0'
            count += 1
            if count <=2:
                tempPassword.append(temp)
            else:
                tempPassword.append('o')
        elif e == 'r':
            temp = '4'
            count += 1
            if count <=2:
                tempPassword.append(temp)
            else:
                tempPassword.append('r')
        elif e == 's':
            temp = '5'
            count += 1
            if count <=2:
                tempPassword.append(temp)
            else:
                tempPassword.append('s')
        else:
            tempPassword.append(e)

    temp = ''
    for i in tempPassword:
        temp += i
       
    print "=====================================", password, ":", temp

    press =  raw_input("\nDo You Need More? Y or N? ")
    if press == 'y':
        encryption()
        print "========================================================="
       

encryption()
