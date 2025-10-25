#Moustapha Bah 09/25/2025
#Lab 6 User Login System with security levels

#dictionary with usernames, passwords, and security levels
dict1 = {
    'guest': {'password': 'guest', 'security_level': 1},
    'user': {'password': 'userpass', 'security_level': 2},
    'admin': {'password': 'adminpass', 'security_level': 3},
    'boss': {'password': 'bossman', 'security_level': 4}
}
wrong_guesses = 0
username = input('Enter your username: ')
while True:
    if username not in dict1:
        #stops program if username not found
        print('Username not found. Access denied.')
        break
    else:
        print(f'Hello {username}! Please enter your password.')
        password = input('Enter your password: ')
        if password != dict1[username]['password']:
            #tries for wrong password
            wrong_guesses += 1
            print()
            print('Incorrect password. Access denied')
            print(f"Tries left: {3 - wrong_guesses}")
            
            if wrong_guesses == 3:
                #too many wrong attempts code block
                print('Too many incorrect attempts. Access denied.')
                break
            continue
        
        else:
            #successful login with greeting and security level
            security_level = dict1[username]['security_level']
            print(f'Greetings {username}! Your security level is {security_level}.')
            break
        
