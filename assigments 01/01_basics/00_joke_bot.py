import pyjokes
PROMPT="What do you want?"
JOKE=pyjokes.get_joke()
SORRY="Sorry I tell only jokes!!"
def main():
    user_input = input(PROMPT).strip().lower()
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)


if __name__ == "__main__":
    main()             
