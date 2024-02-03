questions = ("How many elements in the periodic table?:",
             "Which animal is largest in world?:",
             "what is the most abundant gas in earth's atmosphere?:",
             "how many bones in the human boby?:")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. whale", "B. tortoise", "C. elephant", "D. ostrich"),
           ("A. Nitrogen", "B. carbonmonoxide", "C. hydrogen", "D. helium"),
           ("A. 206", "B. 207", "C. 208", "D. 209"))

answers = ("C", "A", "A", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input(" Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("TNCORRECT")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("-------RESULT-----")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ",end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")


