# Define the questions as tuples
questions = (("Which planet in the solar system is the coldest? "),
             ("What is Germany's capital? "),
             ("Which language has the most native speakers?"),
             ("What is the most common surname in Brazil?"),
             ("What country drinks the most coffee per capita?"))

# Define the options for each question as tuples
options = (("A. Venus", "B. Earth", "C. Uranus", "D. Saturn", "E. Neptune"),
           ("A. Frankfurt am Main", "B. Heidenberg",
            "C. Colônia", "D. Berlin", "E. Mainz"),
           ("A. Portuguese", "B. Spanish", "C. English", "D. Mandarin", "E. Arabic"),
           ("A. Fernandes", "B. Oliveira", "C. Santos", "D. Andrade", "E. Silva"),
           ("A. Finland", "B. Sweden", "C. Brazil", "D. Canada", "E. Portugal"))

# Define the correct answers for each question
answers = ("E", "E", "D", "D", "E", "A")

# Initialize variables for guesses, score, and question number
guesses = []
score = 0
questions_num = 0

# Loop through each question
for question in questions:
    print("-=-" * 15)
    print(question)  # Display the question
    # Display the options for the current question
    for option in options[questions_num]:
        print(option)
    questions_num += 1  # Move to the next question
    guess = input("Enter (A), (B), (C), (D), (E): ")  # Get user's guess
    guesses.append(guess)  # Add the guess to the guesses list
    if guess not in ["A", "B", "C", "D", "E"]:
        exit()  # Exit the program if an invalid input is given
    if guess == answers[questions_num]:  # Check if the guess is correct
        score += 1  # Increase the score if the guess is correct
        print("CORRECT!")
    else:
        print("INCORRECT!")
        # Display the correct answer
        print(f"The correct answer is {answers[questions_num]}")

score = int(score / len(options) * 100)  # Calculate the final score percentage

# Display the results
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("             RESULTS           ")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"YOU SCORED {score}%")
if score == 5:
    # Display a message if the maximum score is achieved
    print("YOU SCORED THE MAXIMUM!!!")
