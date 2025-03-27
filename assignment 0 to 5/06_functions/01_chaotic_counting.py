import random

# Probability of stopping (e.g., 30% chance to stop)
DONE_LIKELIHOOD = 0.3  

def chaotic_counting():
    for i in range(10):  # Loop 10 times (from 0 to 9)
        curr_num = i + 1  # Convert range to 1-10
        if done():
            return  # Stops counting early if done() returns True
        print(curr_num)

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD  # 30% chance to stop

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done.")

if __name__ == "__main__":
    main()
