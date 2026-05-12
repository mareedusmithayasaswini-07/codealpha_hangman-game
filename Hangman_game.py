import random
def choose_word():
    words=["shoe", "door", "table", "pencil", "case", "glasses", "towel","windows","error", "watch", "piano", "pen", "hat", "shoes", "socks", "jeans","trampoline"]
    return random.choice(words)
def get_attempts(level):
    if level=="easy":
        return 8
    elif level=="medium":
        return 6
    else:
        return 4
def show_hint(word):
    print(f"Hint:The word starts with'{word[0]}' and ends with'{word[-1]}'")
def play_game():
    print("Welcome to Hangman Game!")
    level=input("Choose difficulty (easy/medium/hard):").lower()
    attempts_left=get_attempts(level)
    word=choose_word()
    guessed_word=["_"]*len(word)
    guessed_letters=[]
    use_hint=input("Do you want a hint?(yes/no):").lower()
    if use_hint=="yes":
        show_hint(word)
    while attempts_left>0 and "_" in guessed_word:
        print("\n WORD:"," ".join(guessed_word))
        print("Attempts left:",attempts_left)
        print("Guessed letters:",guessed_letters)
        guess=input("Enter a letter:").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print("Correct guess!")
            for i in range(len(word)):
                if word[i]==guess:
                    guessed_word[i]=guess
        else:
            print("Wrong guess!")
            attempts_left-=1
    if "_" not in guessed_word:
        print("\n You Won! The word was:",word)
        return True
    else:
        print("\n Game Over! The word was:",word)
        return False
wins=0
losses=0
while True:
    result=play_game()
    if result:
        wins+=1
    else:
        losses+=1
    print(f"\n Score-->Wins:{wins}|Losses:{losses}")
    choice=input("\n Do you want to play again?(yes/no):").lower()
    if choice!="yes":
        print("\n Final Score:")
        print(f"Wins:{wins}|Losses:{losses}")
        print("Thanks for playing!")
        break