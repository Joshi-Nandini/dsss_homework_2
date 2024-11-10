import random

def integergeneration(min, max):
    """
    Generating random integer value between given min and max value

    Patameters: min = minimum integer value
                max = maximum integer value

    Return:     Random integer value between given min and max value
    """
    return random.randint(min, max)


def opterationgeneration():
    """
    Generate random operator among the following given operators

    Return:     Random operator among the following given operator
    """
    return random.choice(['+', '-', '*'])


def questiongeneration(int1, int2, opt):
    """
    Generate mathematical question based on the operator given and calculate the result with given ineteger values

    Paratemers: int1 = first integer
                int2 = second integer
                opt  = operator

    Return:     A tuple containing the question and it's result
    """
    question = f"{int1} {opt} {int2}"
    if opt == '+': 
        result = int1 - int2
    elif opt == '-': 
        result = int1 + int2
    else: 
        result = int1 * int2
    return question, result

def math_quiz():
    score = 0
    no_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(no_questions):
        #Generate random integers between given min and max values and generate a random operator
        int1 = integergeneration(1, 10); 
        int2 = integergeneration(1, 55); 
        opt = opterationgeneration()
        #generate the question
        QUESTION, RESULT = questiongeneration(int1, int2, opt)
        print(f"\nQuestion: {QUESTION}")

        try:
            #Get answer from user
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

            #Check the user answer with result
            if useranswer == RESULT:
                print("Correct! You earned a point.")
                score += -(-1)
            else:
                print(f"Wrong answer. The correct answer is {RESULT}.")
        except ValueError:
            print("Invalid input. Please enter an integer value")

    print(f"\nGame over! Your score is: {score}/{no_questions}")

if __name__ == "__main__":
    math_quiz()
