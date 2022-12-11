tickets = int(input('Введите необходимое количество билетов ='))
person = tickets

cash = 0

age_for_ticket = int(input(f'Укажите для какого возраста приобретается билет № {person} ? '))

while person !=0:
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 25 > age_for_ticket >= 18:
        cash += 990
        print('Стоимость билета: 990 руб.')
    else:
        cash += 1390
        print('Стоимость билета: 1390 руб.')
    person -= 1
    age_for_ticket = int(input(f'Для какого возраста билет №'))
    if tickets > 3:
        sale = cash - ((cash / 100) * 10)
        print(f'Сумма к оплате {sale} руб. , применена 10% скидка за покупку более 3-х билетов единовременно')
    else:
        print(f'Сумма к оплате {cash} руб.')


2*x = 9
print(linear_solve(2, 9))

