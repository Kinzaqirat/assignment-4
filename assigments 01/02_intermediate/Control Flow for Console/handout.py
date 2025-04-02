import random
num_round=5
def main():
    print("Welcome to high low game")
    print("----------------------------------")
    score=0

    for round_num in range(1,num_round+1):
        print(f"Round {round_num}")
        player_num=random.randint(1,100)
        computer_num=random.randint(1,100)
        print(f"Your number is {player_num}")

        while True:
            guess= input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
            if guess in ["higher", "lower"]:
                break
            print("Invalid input. Please enter either 'higher' or 'lower'.")
            if (guess == "higher" and player_num > computer_num) or (guess == "lower" and player_num < computer_num):
             
             print("You were right!")
            score += 1
        else:

            print("Aww, that's incorrect.")
        
        print(f"The computer's number was {computer_num}")
        print(f"Your score is now {score}\n")
    
    # Final message based on score
    print("Thanks for playing!")
    if score == num_round:
        print("Wow! You played perfectly!")
    elif score >= num_round// 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")


if __name__=="__main__":
    main()