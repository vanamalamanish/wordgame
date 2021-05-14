import random 
from collections import defaultdict as dd
name = input("What is your name? ") 
print("Good Luck ! ", name) 
print("Guess me who am I??")
dictionary=dd(list)
dictionary["I am a seasonal fruit"].append(["mango","apple"])
dictionary["No one lives without me now a days"].append(["mobile","phone",'mask','sanitizer']) 
dictionary["first program teach in all programming languages"].append("helloworld")
dictionary["I will form when there is heavy rainfall"].append("rainbow")
dictionary["I look beautiful but when you touch me you get pain"].append("rose")
dictionary["I am round but when you lift i will become triangle"].append("pizza")
c='yes'
points=0
while(c=='yes'):
    word = random.choice(list(dictionary.keys())) 
    print(word) 
    turns = 3
    print("You have",turns,"turns")
    flag=0
    while turns > 0:
        guess = input("\nGuess me:")
        for i in dictionary[word]:
            if guess in i:   
                print("\nYou Won")  
                print("The word is:", guess) 
                flag=1
                points+=1
                break
            else: 
                turns-=1
                print("Wrong")  
                if turns == 0: 
                    print("You Loose")  
                    for i in dictionary[word]:
                        print("The correct answer is",i)
                        break
                    break
                print("You have", + turns, 'more guesses')
        if flag==1:
            break
    del dictionary[word]
    print("you got",points,"points")
    print("Do you want to play again(Enter Yes or NO)")
    c=input()
            
        
