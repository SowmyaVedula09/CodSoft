import random
while True:
 userinp = input('Choose \nRock , Paper or Scissors\n ')
 actions=["rock","paper","scissors"]
 comp_act=random.choice(actions)
 if userinp==comp_act:
    print('Its a TIE!!')
 elif userinp=="rock":
    if comp_act=="paper":
        print('Rock beats Paper! You Win!!')
    else:
        print('Scissors beat Rock!! ComputerBot Wins!!')
        
 elif userinp=="paper":
    if comp_act=="rock":
        print('Paper beats Rock! You Win!!')
    else:
        print('Scissors beat Paper!! ComputerBot Wins!!')
        
 elif userinp=="scissor":
    if comp_act=="paper":
        print('Scissor beats Paper! You Win!!')
    else:
        print('Rock beat Scissors!! ComputerBot Wins!!')
        
 nextround=input('Ready for another round of Rock-Paper-Scissors? (Yes/No)')
 if nextround.lower()!="yes":
   break