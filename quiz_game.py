print("Welcome to my computer quiz")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    quit()
    
print("OKAY! Let's play : ")


score = 0
answer = input("What does CPU stands for? ")
if answer.lower() == 'central processing unit':
    print("Correct")
    score += 2
else:
    print("Incorrect")
    
    
answer = input("What does GPU stands for? ")   
if answer.lower() == 'grapics processing unit':
    print("Correct")
    score += 2
else:
    print("Incorrect")
    
answer = input("What does API stands for? ")   
if answer.lower() == 'application programming interface':
    print("Correct")
    score += 2
else:
    print("Incorrect")
    
answer = input("What does AP stands for? ")   
if answer.lower() == 'andhra pradesh':
    print("Correct")
    score += 2
else:
    print("Incorrect")
    
answer = input("What does RAM stands for? ")   
if answer.lower() == 'random access memory':
    print("Correct")
    score += 2
else:
    print("Incorrect")
    
    
answer = input("What does JSON stands for? ")   
if answer.lower() == 'javascript object notation':
    print("Correct")
    score += 2
else:
    print("Incorrect")
    
    
answer = input("What does ROM stands for? ")   
if answer.lower() == 'random order memory':
    print("Correct")
    score += 2
else:
    print("Incorrect")
    
    
answer = input("What does ILY stands for? ")   
if answer.lower() == 'i lovd you':
    print("Correct")
    score += 2
else:
    print("Incorrect")
    
     
    
print(f'your total score is {score}')
    
    
    
    

    
