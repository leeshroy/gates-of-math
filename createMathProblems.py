import random

streak = 0
difficulty = 0

def createProblemSet():
    global difficulty
    problemSet = []
    numberSet = []
    randomOperation = ""
    operations = difficultyCheck()
    if difficulty != 0:
        for _ in range(2):  # Generate two problems
            num1 = random.randint(-10, 10)
            num2 = random.randint(-10, 10)
            randomOperation = operations[random.randint(0, len(operations) - 1)]
            # Ensure that num1 is always greater than or equal to num2 before creating problem
            if num1 < num2:
                num1, num2 = num2, num1
            problemSet.append(f"{num1} {randomOperation} {num2}")
    else:
        problemSet.append(str(random.randint(-10, 10)))
        problemSet.append(str(random.randint(-10, 10)))
    return problemSet

def difficultyCheck():
    global difficulty
    match difficulty:
        case 0:
            return []
        case 1:
            return ["+", "-"]
        case 2:
            return ["+", "-", "*"]

def createAnswerSet(problemSet):
    answerOne = eval(problemSet[0])
    answerTwo = eval(problemSet[1])
    answerSet = [answerOne, answerTwo]
    return answerSet

def checkAnswer(problemSet, gates):
    global streak
    global difficulty
    playerAnswer = gates[1]['collided']  # True if the right gate is collided
    answerSet = createAnswerSet(problemSet)
    # Determine the correct gate based on answers
    correctGate = 0 if answerSet[0] > answerSet[1] else 1
    isCorrect = (playerAnswer == correctGate)
    playerGateValue = answerSet[playerAnswer]

    if isCorrect:
        streak += 1
    else:
        streak = 0
        if difficulty > 0:
            difficulty -= 1

    if streak == 5 and difficulty < 2:
        difficulty += 1
        streak = 0

    return playerGateValue
