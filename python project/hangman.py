# make hangman  game

import random
words=["cat","dog","sun""hat","car","tree","fish","ball","apple","moon","star"]
word= random.choice(words)
guess_letters=[]
attmepts=5

print("Welcome to Hangman Game 🎩😀")
print("_" * len(word))

while attmepts >0:

  guess=input("Guess a letter: ").lower()

  if len(guess) != 1 or not guess.isalpha():
    print("Write only one letter")
    continue
  if guess in  guess_letters:
    print("This letter is already guess🤷‍♀️")
    continue
  guess_letters.append(guess)
  if guess in word:
    print("You guess right ✅😊 ")
  else:
    attmepts -=1
    print(f"Wrong ❌ {attmepts} only")

  show_words=" ".join([letter if letter in guess_letters else "_" for letter in word])
  print(show_words)

  if "_" not in show_words:
    print(f"You win!🏆 the correct word is {word}")
    break
else:
  print(f"Game over ....⏳ The correct word is {word}")