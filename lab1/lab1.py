import math
import sys


def argumentsInput():
    answer = []
    for i in range(1, 4):
        try:
            answer.append(float(sys.argv[i]))
        except:
            return []
    return answer


def consoleInput():
    a, b, c = 0, 0, 0
    while True:
        try:
            a, b, c = map(float, input().split(' '))
        except:
            print('Invalid input, try again.')
            continue
        break
    return a, b, c


def solveRoots(a, b, c):
    ans = b * b - 4 * a * c
    if a == 0:
        if b == 0:
            return []
        else:
            return [-math.sqrt(math.abs(-c / b)), math.sqrt(math.abs(-c / b))]
    if ans < 0:
        return []
    elif ans == 0:
        try:
            x1 = -math.sqrt((-b) / (2 * a))
            x2 = math.sqrt((-b) / (2 * a))
        except:
            return []
        return list(set([x1, x2]))
    else:
        answer = []
        first = True
        second = True
        try:
            x1 = -math.sqrt((-b + math.sqrt(ans)) / (2 * a))
            x2 = math.sqrt((-b + math.sqrt(ans)) / (2 * a))
        except:
            first = False
        try:
            x3 = -math.sqrt((-b - math.sqrt(ans)) / (2 * a))
            x4 = math.sqrt((-b - math.sqrt(ans)) / (2 * a))
        except:
            second = False

        if first:
            answer.append(x1)
            answer.append(x2)
        if second:
            answer.append(x3)
            answer.append(x4)
        return list(set(answer))


def main():
    coefficients = argumentsInput()
    if len(coefficients) == 0:
        print('No arguments, input coefficients:')
        coefficients = consoleInput()
    roots = solveRoots(coefficients[0], coefficients[1], coefficients[2])
    rootsamount = len(roots)
    if rootsamount == 0:
        print('No solutions.')
    elif rootsamount == 1:
        print('Solution #1: ' + str(roots[0]))
    else:
        print('Solutions:')
        for i in range(len(roots)):
            print('x' + str(i + 1) + ' = ' + str(roots[i]))


if __name__ == "__main__":
    main()
