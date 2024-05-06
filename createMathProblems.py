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
    numberSet.append(str(random.randint(0, 10)))
    numberSet.append(str(random.randint(0, 10)))
    numberSet.sort()
    randomOperation = operations[random.randint(0, difficulty)]
    problemSet.append(numberSet[1] + " " + randomOperation + " " + numberSet[0])
    numberSet = []
    numberSet.append(str(random.randint(0, 10)))
    numberSet.append(str(random.randint(0, 10)))
    numberSet.sort()
    randomOperation = operations[random.randint(0, difficulty)]
    problemSet.append(numberSet[1] + " " + randomOperation + " " + numberSet[0])
  else:
    problemSet.append(str(random.randint(0, 10)))
    problemSet.append(str(random.randint(0, 10)))
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

# playerAnswer must be bool of 0 or 1, depending on which gate is taken
# left = 0, right = 1
def createAnswerSet(problemSet):
  # will return if player picked correct answer along with the answers for the two problems
  # correct = 0, incorrect = 1
  answerOne = eval(problemSet[0])
  answerTwo = eval(problemSet[1])
  answerSet = [answerOne, answerTwo]
  return answerSet

# takes the questions and gates, returns the value of the gate chosen
def checkAnswer(problemSet, gates):
  # create line to check player answer
  global streak
  global difficulty
  # if right gate is collided, returns 1, and if left gate is collided, returns 0
  playerAnswer = gates[1]['collided']
  answerSet = createAnswerSet(problemSet)
  # evaluates which is bigger, if left, 0, if right, 1, then checks against player answer
  isCorrect = playerAnswer == (answerSet[0] <= answerSet[1])
  playerGate = answerSet[playerAnswer]
  if isCorrect:
    streak += 1
  elif not isCorrect and streak != 0:
    streak = 0
  elif not isCorrect and streak == 0 and difficulty != 0:
    difficulty -= 1
  else:
    print("This should never happen")
  if streak == 5 and difficulty != 2:
    difficulty += 1
    streak = 0
  return playerGate
