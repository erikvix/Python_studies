questions = (("Which planet in the solar system is the coldest? "),
("What is Germany's capital? "),
("Which language has the most native speakers?"),
("What is the most common surname in the Brazil?"),
("What country drinks the most coffee per capita?"))



options = (("A. Venus", "B. Earth", "C. Uranus", "D. Saturn", "E. Neptune"),
("A. Frankfurt am Main", "B. Heidenberg", "C. Colônia", "D. Berlim", "E. Mainz"),
("A. Portuguese", "B. Spanish", "C. English", "D. Mandarim", "E. Arabic"),
("A. Fernandes", "B. Oliveira", "C. Santos", "D. Andrade", "E. Silva"),
("A. Finland", "B. Sweden", "C. Brazil", "D. Canada", "E. Portugal"))


answers = ("E", "E", "D", "D", "E", "A")
guesses = []
score = 0
questions_num = 0


for questions in questions:
    print("-=-" * 15)
    print(questions)
    for option in options[questions_num]:
        print(option)
    questions_num += 1
    guess = input("Enter (A), (B), (C), (D), (E): ")
    guesses.append(guess)
    if guess not in ["A", "B", "C", "D", "E"]:
        exit()
    if guess == answers[questions_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"The correct answer is {answers[questions_num]}")

score = int(score / len(options) * 100)

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("             RESULTS           ")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"YOU SCORED {score}%")
if score == 5:
    print("YOU SCORED THE MAXIMUM!!!")