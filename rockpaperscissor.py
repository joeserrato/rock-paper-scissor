import random

print('''
      WELCOME TO THE ROCK PAPER SCISSOR GAME
      You are playing against the computer.

      Rock vs Paper -> Paper wins 
      Rock vs Scissors -> Rock wins 
      Paper vs Scissors -> Scissors wins 
''')

options = ['rock','paper','scissor']

computer_score = 0
your_score = 0

while True:
    try:
        user_input = int(input(
            '''
        Enter Your Choice Below:
        1 -> Rock
        2 -> Paper
        3 -> Scissor 
        
        '''))
    except ValueError:
        print("Invalid input! Please enter a valid NUMBER.")
        continue


    if user_input < 1 or user_input > 3:
        print("Invalid input! Please enter a number between 1 and 3.")
        continue
    
    computer_choice = random.randint(1,3)
    
    if user_input == computer_choice:
        print("It's a Tie!")
    elif user_input == 1 and computer_choice == 3:
        print("You Win!")
        your_score += 1
    elif user_input == 2 and computer_choice == 1:
        print("You Win!")
        your_score += 1
    elif user_input == 3 and computer_choice == 2:
        print("You Win!")
        your_score += 1
    else:
        computer_score +=1
        print("Computer Wins!")
    
    print(f'You Choose: {options[user_input-1]}')
    print(f'Computer Choose: {options[computer_choice-1]}')
    
    print(f"Your Score: {your_score}")
    print(f"Computer Score: {computer_score}")


    game_over = ['Y', 'N']    
    while True:
        
        
        play_again = input("Do you want to play again?: (Y/N)").upper()
        
        if play_again not in game_over:
            print("Invalid input! Please enter Y or N.")
            continue

        if play_again == 'N':
            print("Thanks for playing!")
            print(f"Final Score: Your Score: {your_score} Computer Score: {computer_score}")

            if your_score > computer_score:
                print("You Win!")
            elif your_score < computer_score:
                print("Computer Wins!")
            else:
                print("It's a Tie!")
            
            exit()
        elif play_again == 'Y':
            break
        
        
            
        
            

