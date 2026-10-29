fruits = {
    "Grapes": 1000,
    "apple": 200,
    "banana": 100,
    'orange': 150
    }
 
# 1. get the price of banana
print(fruits['banana'])

# 2. add mango costing 300 to collection
fruits['mango'] = 300

# 3. change the price of apple to 250
fruits['apple'] = 250
print(fruits)

print('OR')
for keys, values in fruits.items():
    print(keys, values)
    
    
    """other operations 
    on
    Dictionaries """
    
other_fruits = {
    "avocado:": 250,
    "passion:": 500,
    'pinaple:': 700
    }

## merging the two Dictionaries....
fruits |= other_fruits

print( "========New merged collection=============")
for keys, values in fruits.items():
    print(keys, values)

####If you want to add a key-value pair only if the key doesn’t exist yet......

fruits.setdefault('avocado', 350)
fruits.setdefault('banana',300)
print("========= Added missing key value to collection ===========")
print(fruits)

