import random  #imported random so I can use it to create a random password

used = {}  #empty dictionary to append passwords with their emails later and security answer 

#set security question outside the loop so it doesnt keep repeating
question = "What is your favorite color?"

while True:  #loop until its broken by 'exit'
    choice = input("Type 'own' to create your own password, 'gen' to generate one randomly, 'forgot' if you've forgotten your password, or 'exit' to quit: ")
    
    if choice == "own":  #if user typed 'own'
        print("Your password must consist of a minimum of 6 characters, including uppercase letters, numbers, special characters, and lowercase letters.")  #criteria for password
        email = input("Enter your email address: ")  #asks user for their email to link it with the password
        
        if "@" not in email:  #to make sure its a valid email containing @
            print("please type in a valid email.")
            continue   #skips the rest of the loop if email does not contain a @
        
        if email in used:  #Check if the email already exists
            print("This email is already used. Please use 'forgot' to retrieve your password or choose a different email.")
            continue  #Skip the rest of the loop if email is already used

        own = input("Create your own password that fits the criteria listed above: ")  #user types in their password
        own_b = input("Enter your own password once again to confirm it: ")  #confirmation of password

        if own == own_b:  #checking if the two passwords match
            if len(own) < 6:  #length of password must be at least 6
                print("Password must be at least 6 characters long")
                continue  #skips the rest of the code if length is less than 6
            
            upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #uppercase characters
            lower = "abcdefghijklmnopqrstuvwxyz"  #lowercase characters
            no = "1234567890"  #numbers
            special = "!@#$%^&*():\"~+_=-?/>.<,\\|';{}[]"  #special characters
            
            contain_upper = False  #checks if password contains at least one uppercase letter
            contain_lower = False  #checks if password contains at least one lowercase letter
            contain_no = False  #checks if password contains at least one number
            contain_special = False  #checks if password contains at least one special character

            for i in own:  #to check each character in the password
                if i in upper:
                    contain_upper = True  
                elif i in lower:
                    contain_lower = True
                elif i in no:
                    contain_no = True
                elif i in special:
                    contain_special = True
                    
            if own in [info['password'] for info in used.values()]:   #check if password has already been used by another user 
                print("This password is already used by another user. Please choose a different unique password.")
                continue  # If password is not unique it skips all other loops so user can enter password again
                
                
            if not contain_upper:  #if not valid, display message
                print("Invalid, your password must contain an uppercase letter")
            if not contain_lower:
                print("Invalid, your password must contain a lowercase letter")
            if not contain_no:
                print("Invalid, your password must contain a number")
            if not contain_special:
                print("Invalid, your password must contain a special character")
            else:  #if all criteria are met
                print("Valid, password is accepted")
                if len(own) < 8:  #if password is less than 8 characters, it wont be as strong as a longer password
                    print("I recommend that your password should consist of more uppercase letters, lowercase letters, numbers, or special characters. It's ***/5 stars for how strong the password is. You can keep it or type it again but include more than 8 so it can be strengthened.")
                    
                else:
                    print("I recommend this password as it is *****/5 on our strength test")
                    
                
                answer = input("Answer the security question so if you have to retrieve your password later on: '{}' ".format(question))  #asking for the answer for security question that will be asked if forgot is typed
                used[email] = {'password': own, 'answer': answer}  #store the email and password pair and security answer
        else:
            print("Passwords do not match")  #if passwords don't match
    
    elif choice == "gen":
        email = input("Enter your email address: ")  #ask for user's email

        if "@" not in email:
            print("Please type in a valid email")
            continue 
        
        if email in used:  #Check if the email already exists
            print("This email is already used. Please use 'forgot' to retrieve your password or choose a different email.")
            continue  #Skip the rest of the loop if email is already used

        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        no = "1234567890"
        special = "!@#$%^&*():\"~+_=-?/>.<,\\|';{}[]"
        all_characters = upper + lower + no + special  #all of the characters that can be used so it can be used in the generated password to fulfill the 6 length requirement

        while True:  #loop until password is unique and not in the list used
            password = [random.choice(upper), random.choice(lower), random.choice(no), random.choice(special),
                        random.choice(all_characters), random.choice(all_characters), random.choice(all_characters),
                        random.choice(all_characters), random.choice(all_characters), random.choice(all_characters)]  #random.choice selects any random character from that variable 
            gen_pass = "".join(password)  #combines all the characters from the random.choice to create a generated password

            if gen_pass not in [info['password'] for info in used.values()]:  #check if the generated password is unique
                answer = input("Answer the security question: '{}' ".format(question))  #asking for the answer to the predefined security question
                used[email] = {'password': gen_pass, 'answer': answer}  #store the email-password pair and security answer
                print("Your generated password is: {}".format(gen_pass))  #the generated password goes in that empty dictionary 
                break  #get out of loop because password is made 
            else:
                print("Generated password is not unique, generating a new one...")  #prompt if the password is not unique

    elif choice == "forgot":  #if user forgot their password
        email = input("Enter your email address to recover your password: ")
        if email in used:  #check if email exists from the dictionary 
            answer = input("To verify, answer this: '{}' ".format(question))  #asking the security question again for verification
            if answer == used[email]['answer']:  #check if the answer matches 
                print("Correct! Your password is: {}".format(used[email]['password']))  #display the stored password in used 
            else:
                print("Wrong, I suspect it isn't {}. Access denied.".format(email))
        else:  #if email is not in the dictionary used 
            print("Email not found, please try again.")
    
    elif choice == "exit":  #if user wants to leave program 
        print("Exiting program.")
        break  #exit the loop if 'exit' is chosen
    
    else:  #if the user didn't type own, gen, forgot, exit then this would be displayed 
        print("Invalid option, please choose 'own', 'gen', 'forgot', or 'exit'.")

