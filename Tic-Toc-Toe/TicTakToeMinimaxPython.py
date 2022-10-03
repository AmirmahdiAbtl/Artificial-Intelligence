environment = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}
def printEnvironment(environment):
    for i in range(1, len(environment)+1):
        if i % 3 == 0:
            print(environment[i])
            print("--------")
        else :
            print(environment[i] + "|", end="")
def emptySpot(x):
    if environment[x] == " ":
        return True
    else:
        return False
def drawChecker():
    for i in range(1, len(environment) + 1):
        if environment[i] == " ":
            return False
    return True
def winChecker():
    if environment[1] != ' ' and environment[1] == environment[2] and environment[1] == environment[3]:
        return True
    elif environment[4] != ' ' and environment[4] == environment[5] and environment[4] == environment[6]:
        return True
    elif environment[7] != ' ' and environment[7] == environment[8] and environment[7] == environment[9]:
        return True
    elif environment[1] != ' ' and environment[1] == environment[5] and environment[1] == environment[9]:
        return True
    elif environment[7] != ' ' and environment[7] == environment[5] and environment[7] == environment[3]:
        return True
    elif environment[1] != ' ' and environment[1] == environment[4] and environment[1] == environment[7]:
        return True
    elif environment[2] != ' ' and environment[2] == environment[5] and environment[2] == environment[8]:
        return True
    elif environment[3] != ' ' and environment[3] == environment[6] and environment[3] == environment[9]:
        return True
    else:
        return False
def minimaxChecher(x):
    if environment[1] == x and environment[1] == environment[2] and environment[1] == environment[3]:
        return True
    elif environment[4] == x and environment[4] == environment[5] and environment[4] == environment[6]:
        return True
    elif environment[7] == x and environment[7] == environment[8] and environment[7] == environment[9]:
        return True
    elif environment[1] == x and environment[1] == environment[5] and environment[1] == environment[9]:
        return True
    elif environment[7] == x and environment[7] == environment[5] and environment[7] == environment[3]:
        return True
    elif environment[1] == x and environment[1] == environment[4] and environment[1] == environment[7]:
        return True
    elif environment[2] == x and environment[2] == environment[5] and environment[2] == environment[8]:
        return True
    elif environment[3] == x and environment[3] == environment[6] and environment[3] == environment[9]:
        return True
    else:
        return False
def insertMovement(n, x):
    if emptySpot(x):
        environment[x] = n
        printEnvironment(environment)
        if winChecker():
            if n == "o":
                print("you win the game")
                exit()
            else :
                print("your rival win the game")
                exit()
        if drawChecker():
            print("The game went to Draw!")
            exit()
    else:
        print("Something wrong was happen please enter another spot for continues this match")
        x = int(input("Enter Your new spot : "))
        insertMovement(n, x)
        return
def minimax(env, ismax, dpt):
    if minimaxChecher("o"):
        return -1
    elif minimaxChecher("x"):
        return 1
    elif drawChecker():
        return 0
    if ismax:
        bestScore = -500
        for i in range(1, len(env) + 1):
            if env[i] == ' ':
                env[i] = "x"
                score = minimax(env , False, dpt+1)
                env[i] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 500
        for i in range(1, len(env) + 1):
            if env[i] == ' ':
                env[i] = "o"
                score = minimax(env, True, dpt + 1)
                env[i] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore
def player():
    x = int(input("Enter spot : "))
    insertMovement("o", x)
    return
def enemy():
    bestScore = -500
    bestSpot = 0
    for i in range(1, len(environment) + 1):
        if environment[i] == ' ':
            environment[i] = "x"
            score = minimax(environment, False, 0)
            environment[i] = ' '
            if score > bestScore:
                bestScore = score
                bestSpot = i
    insertMovement("x", bestSpot)
    return
def printing():
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("You'll play with x and your rival will play with o letter")
def main():
    printing()
    while True:
        player()
        enemy()
        if winChecker() or drawChecker():
            exit()
main()