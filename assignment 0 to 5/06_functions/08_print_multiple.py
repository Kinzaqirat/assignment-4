def multiple_message(message,repeats):
    for i in range(repeats):
        print(message)


def main():
    message=input("Enter a message: ")
    repeats=int(input("Enter a number of times to repaet the message: "))
    multiple_message(message,repeats)


if __name__ == "__main__":
    main()
