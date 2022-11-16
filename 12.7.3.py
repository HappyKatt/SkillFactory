per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
money = 100000
deposit = [5600, 5900, 4280, 4000]
VTB = per_cent['VTB']*(money/100)
print(VTB)
TKB = per_cent['TKB']*(money/100)
print(TKB)
SKB = per_cent['SKB']*(money/100)
print(SKB)
SBER = per_cent['SBER']*(money/100)
print(SBER)
values = {key: value*(money/100) for key, value in per_cent.items()}
print(values)
print(max(deposit))




