import os

listTotal = []

for i in enumerate(os.listdir('./imgs/')):
    totImgs = len(os.listdir(f'./imgs/{i[1]}'))
    listTotal.append(totImgs)
    print((f'number of {i[0]} is  {totImgs}'))

print(listTotal)
print(max(listTotal))
print(min(listTotal))

maximum = max(listTotal)

for i in enumerate(listTotal):
    print(f'{i[0]} needs to be increamented by {maximum - i[1]}')