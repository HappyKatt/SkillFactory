while True:
    try:
        userInput = [int(i) for i in input("Введите последовательность чисел через пробел: ").split()]
        userInput_2 = int(input("Введите любое число: "))
    except ValueError:
        print("Введены невалидные значения!")
        continue
    else:
        break
def sort():
    for i in range(1, len(userInput)):
        x = userInput[i]
        idx = i
        while idx > 0 and userInput[idx - 1] > x:
            userInput[idx] = userInput[idx - 1]
            idx -= 1
        userInput[idx] = x
    return userInput

def binary_search(userInput, userInput_2, left, right):
    middle = (left + right) // 2
    if userInput[0] >= userInput_2 or userInput_2 > userInput[-1]:
        return f"Введенное число не удовлетворяет условию"
    else:
        if left > right:
            return f"Номер позиции элемента, который меньше введенного числа: {middle}\n"
        elif userInput[middle] == userInput_2:
            return f"Номер позиции элемента, который меньше введенного числа: {middle - 1}\n"
        elif userInput_2 < userInput[middle]:
            return binary_search(userInput, userInput_2, left, middle - 1)
        else:
            return binary_search(userInput, userInput_2, middle + 1, right)

print(f"Отсортированный список: {sort()}")
print(binary_search(userInput, userInput_2, 0, len(userInput)))