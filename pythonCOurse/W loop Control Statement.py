# Loop control statement = Change a loops execution from its normal sequence

# break = terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

# Break
while True:
    name = input("Enter your name: ")
    if name != "":
        break

# Continue
phone_number = "889-296-8648"

for i in phone_number:
    if i == ("-"):
        continue
    print(i, end = "")

# Pass

for i in range(0,21):

    if i == 13:
        pass
    else:
        print(i)