import random

value = random.random()
print(value)

#uniform
value = random.uniform(1, 10)
print(value)

#rad int
#simulate coin toss
value = random.randint(0, 1)
print(value)

#get random value from a list
#choice
greeting = ['hello', 'hi', 'hola', 'hey']
value = random.choice(greeting)
print(value + ', prathyusha!')

colors = ['red', 'pink','yellow']
result = random.choices(colors, weights=[18, 18, 2], k=10)
print(result)

deck = list(range(1, 52))
random.shuffle(deck)
print(deck)


#we get only 5 cards
#sample method

hand = random.sample(deck, k=5)
print(hand)

