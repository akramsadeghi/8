import random

option = ['rock','paper','scissor']
scores = {'user':0 ,'computer':0}
n = int(input('chand dast bazi mikonid?'))
print(option)
for i in range(n):
    computer_choice = random . choice(option)
    user_choice = input('play the game:  ')
    print(user_choice , computer_choice )

    if (user_choice == 'paper' and computer_choice == 'rock' or user_choice == 'cissor' and computer_choice == 'paper' or user_choice == 'rock' and computer_choice == 'cissor') :
        print('user wins')
        scores['user']+=1
    if (computer_choice == 'paper' and user_choice == 'rock' or computer_choice == 'cissor' and user_choice == 'paper' or computer_choice == 'rock' and user_choice == 'cissor') :
        print('computer wins')
        scores['computer']+=1 
    if  computer_choice == user_choice:
        print("shoma barabar shodin.")  

print("emtiyaz user:  ", scores['user'])
print("emtiyaz computer:  ", scores['computer'])             


