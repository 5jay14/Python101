import random

MyList = ['Rock', 'Paper', 'Scissors']
a = random.choice(MyList)
print(a)

b = random.randint(1, 6)
print(b)
# random whole numbers between 1 to 6

c = random.random()
print(c)
# random floating numbers

cards = [1,2,3,4,5,6,7,8,9,10,"J","K","Q","A"]
random.shuffle(cards)
print(cards)
