fruits = ['cherry', 'kiwi', 'apple', 'strawberry']
for fruit in fruits:
    # print(fruit)
    if fruit == 'kiwi':
        print('kiwi')
    else:
        print('not kiwi')

# for x in range(0, 4):
for x in range(len(fruits)):
    if fruits[x] == 'kiwi':
        print(fruits[x])
    else:
        print('not kiwi')


