# Dictionary = A changeable(because we can change the elements after it is declared), unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}


capitals.update({'Germany': 'Berlin'})
print(capitals.values())
print(capitals.keys())
print(capitals.items())
capitals.pop('China')
# capitals.clear

# print(capitals['France']) # this will disrupt the flow of the program if the key is not defined, use the below method
print(capitals.get('France'))  # safe way to print the value of a key

for key, value in capitals.items():
    print(key, value)
