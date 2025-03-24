SENTENCE_START: str = "Learning new skills is exciting. I explored a new topic and " # adjective noun verb

def main():
    # Get the three inputs from the user to make the ad-lib sentence
    adjective: str = input("Please type an adjective and press enter: ")
    noun: str = input("Please type a noun and press enter: ")
    verb: str = input("Please type a verb and press enter: ")

    # Join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
