# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print(1)
print(2)
print (0.1+0.1*5-0.3*4)
print ((3.14+0.3)/2+0.15)
print (31 % 2 + 31 % 2)
print (13 % 3 * 3 - 3**2)
print(round(11*2.5/3, 2))
print(round(3.14159 **2/2))
print('1 2 3 4 5 6 7')
pi = 31.4159265
print ("%.4e" % (pi))

d = {'day' : 22, 'month' : 6, 'year' : 2015}
print("||".join(d.keys()))
print(1)
L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

money = int(input("Enter sum: 100000"))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [5600, 5900, 4280, 4000]
for value in per_cent.values():
   result = int(money / 100 * value)
   deposit.append(result)
print(deposit)
print(max(deposit))

colors = 'red blue green'

print(colors.split('red blue green'))







