import random 
name = input("What is your name? ") 
print("Good Luck ! ", name) 
print("Guess me who am I??")
dictionary = {"I am a seasonal fruit":"mango","No one lives without me now a days":"mobile",
"first program teach in all programming languages":"helloworld",
"I will form when there is heavy rainfall":"rainbow",
"I look beautiful but when you touch me you get pain":"rose",
"I am round but when you lift i will become triangle":"pizza",
} 
c='yes'
while(c=='yes'):
    word = random.choice(list(dictionary.keys())) 
    print(word) 
    turns = 3
    print("You have",turns,"turns")
    while turns > 0:
        guess = input("\nGuess me:") 
        if guess==dictionary[word]:   
            print("\nYou Won")  
            print("The word is: ", dictionary[word]) 
            print("Do you want to play again(Enter Yes or NO)")
            c=input()
            break
        else: 
            turns-=1
            print("Wrong")  
            if turns == 0: 
                print("You Loose")     
                print("Do you want to play again(Enter Yes or NO)")
                c=input()
                break
            print("You have", + turns, 'more guesses')
    del dictionary[word]
            
        
