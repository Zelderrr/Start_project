import random
turns = ['rock', 'paper', 'scissors']

human_turns = []
computer_turns = []

while(True):
    human_turn = input("Enter your turn, or type exit: ")
    computer_turn = random.choice(turns)

    human_turns.append(human_turn)
    computer_turns.append(computer_turn)

    if human_turn == 'exit':
        print('Thank you for playing! Bye bye')
        break

    print(f'Human:{human_turn} vs. Computer:{computer_turn}')
    if human_turn == computer_turn:
        print('Draw!')
    elif human_turn == 'rock' and computer_turn == 'scissors':
        print('Human wins!')
    elif human_turn == 'paper' and computer_turn == 'rock':
        print('Human wins!')
    elif human_turn == 'scissors' and computer_turn == 'paper':
        print('Human wins!')
    else:
        print('Computer wins!')


print(f'You have played {len(human_turns)} times')
print(human_turns)
print(computer_turns)
