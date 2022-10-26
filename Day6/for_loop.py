#basic syntax
for x in range(0, 10, 3): #start, stop, step
    print(x)
    
fruits = ['apple','banana','cherry','kiwi','guva']
for fruits in fruits:
    print(fruits)

integers = [1, 2, 3, 4, 5]
for num in integers:
    print(num)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count_even = 0
count_odd = 0
for num in numbers:
    if(num%2 == 0):
        count_even += 1
    if(num%2 == 1):
        count_odd += 1
print(f'no.of even numbers are:', count_even)
print(f'no.of odd numbers are:', count_odd)

