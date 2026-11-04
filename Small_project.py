import random  # play rock, paper, scissors with computer

emojis = {"r": "🪨", "p": "📄", "s": "✂️"}
 
choices = ["r", "p", "s"]
 
print("Ladies and Gentlemen, Welcome to Rock, Paper, Scissors Game! ")

 
while True:
 
    user_choice = input("rock, paper, or scissors (r/p/s): ").lower().strip()

 
    if user_choice not in choices:
        print("❌ Error: Invalid choice! Please type (r/p/s).")
        continue 
 
    computer_choice = random.choice(choices)

 
    print("\nYou chose:     ", user_choice, emojis[user_choice])

    print("Computer chose:", computer_choice, emojis[computer_choice])
 
    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (
    (user_choice == "r" and computer_choice == "s") or 
         (user_choice == "p" and computer_choice == "r") or 
         (user_choice == "s" and computer_choice == "p")):
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")
 
    again = input("\nDo you want to play again? (y/n): ").lower().strip()
 
    if again == "n":
        print("\n👋 Thanks for playing. Goodbye!")
        break