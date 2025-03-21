'''
#1. Write a function called count_vowels(input) that takes a string
    and returns the number of vowels (a, e, i, o, u) in it.
'''

def countVowel(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0

    for letter_in_word in word:
        if letter_in_word.lower() in vowels:
            count += 1
    return count
print(countVowel("Apple"))
print(countVowel("yes"))
print(countVowel("physics"))


'''
#2. Write a function called is_palindrome(s) that checks whether a string is a palindrome
    (reads the same forward and backward, ignoring case). The function should returns
    either True or False.
'''
def is_palindrome(s):
    lowerWord = s.lower()
    flipped = lowerWord[::-1]

    return lowerWord == flipped

print(is_palindrome("OOOpOOO"))



'''
#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
    For example, water is very effective to fight fire.
    Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
    strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
    simple type effectiveness rules. Your solution only needs to work for these three sets of input:
    print(type_advantage("Water", "Fire"))  # "Super Effective"
    print(type_advantage("Fire", "Water"))  # "Not Very Effective"
    print(type_advantage("Electric", "Grass"))  # "Neutral"
'''

def type_advantage(attacker, defender):
    if attacker == "Water" and defender == "Fire":
        return "Supper effective"
    elif attacker == "Fire" and defender == "Water":
        return "Not Very Effective"
    elif attacker == "Electric" and defender == "Grass":
        return "Neutral"
    else:
        return "Neutral"


print(type_advantage("Water", "Fire"))
print(type_advantage("Fire", "Water")) 
print(type_advantage("Electric", "Grass"))
print(type_advantage("Fire", "Electric"))



'''
#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington State Ferry fare
    based on age and whether the person has a vehicle. Assume the following rates:
    * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
    * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
    * Children (0-18): Free.
'''


def ferry_price(age, vehicle):
    if 19 <= age <= 64 and vehicle == "yes":
        price = 20
    elif 19 <= age <= 64 and vehicle == "no":
        price = 10
    elif age >= 65 and vehicle == "yes":
        price = 15

    elif age >=65 and vehicle == "no":
        price = 5

    elif age <=18 and vehicle == "no":
        price = 0
    else:
        price = 0

    return price

print(ferry_price(39,"no"))




'''
#5. Write a function called level_up(experience) that takes a player's experience points
    and returns their new level based on these rules:
    * 0-99 XP → Level 1
    * 100-199 XP → Level 2
    * 200+ XP → Level 3
    
'''
def level_up(exp):
    if 0 < exp <= 99:
        lv = 1
    elif exp >= 200:
        lv = 3
    else:
        lv = 2

    return lv
print("Level:",level_up(89))
print("Level:",level_up(123))
print("Level:",level_up(323))
