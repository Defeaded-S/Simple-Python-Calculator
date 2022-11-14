print('Введите первое число:')
a = int(input())
print('Введите второе число:')
b = int(input())
print('Введите действие: +, -, *, /')
c = 0
action = str(input())
if action == "+":
    c = a + b
    print("Результат:", c)
elif action == "-":
    c = a - b
    print("Результат:", c)
elif action == "*":
    c = a * b
    print("Результат:", c)
elif action == "/":
    c = a / b
    print("Результат:", c)
else:
    print("Неверное действие")
