import random

def presentProblem():
  streak = 0
  difficulty = 0
  optionSet = createProblem(difficulty)
  print(optionSet)
  
def createProblem(difficulty):
  optionSet = []
  numberSet = []
  randomOperation = ""
  operations = difficultyCheck(difficulty)
  if difficulty != 0:
    numberSet.append(random.randint(0, 10))
    numberSet.append(random.randint(0, 10))
    numberSet.sort()
    randomOperation = operations[random.randint(0, difficulty)]
    optionSet.append(numberSet[1] + " " + randomOperation + " " + numberSet[0])
    numberSet = []
    numberSet.append(random.randint(0, 10))
    numberSet.append(random.randint(0, 10))
    numberSet.sort()
    randomOperation = operations[random.randint(0, difficulty)]
    optionSet.append(numberSet[1] + " " + randomOperation + " " + numberSet[0])
  else:
    optionSet.append(random.randint(0, 10))
    optionSet.append(random.randint(0, 10))
  return optionSet
  
def difficultyCheck(difficulty):
  match difficulty:
    case 0:
      return []
    case 1:
      return ["+", "-"]
    case 2:
      return ["+", "-", "*"]

# still needs something to get player answer
# then use eval()

presentProblem()
