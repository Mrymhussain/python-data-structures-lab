# Exercise 0: Example


def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

example_list_function()


# Exercise 1: List and Indexing
def manage_students():
    students = ['Maryam', 'Sara', 'Ali']

    first_student = students[1]
    last_student = students[-1]

    return first_student, last_student


print('Exercise 1:', manage_students())

# Exercise 2: Loop and String Concatenation

def combine_foods():
    foods = ('pizza', 'pasta', 'burger')

    meal = ''

    for food in foods:
        meal += food

    return meal


print('Exercise 2:', combine_foods())

# Exercise 3: Slicing Tuples

def slice_foods():
    foods = ('pizza', 'pasta', 'burger')

    last_two_foods = foods[-2:]

    return last_two_foods


print('Exercise 3:', slice_foods())

# Exercise 4: Dictionaries and String Formatting

def hometown_info():
    home_town = {
        'city': 'Manama',
        'state': 'Bahrain',
        'population': 200000
    }

    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"

    return home_town_message


print('Exercise 4:', hometown_info())

# Exercise 5: Iterating Over Dictionary Items

def list_home_town_items():
    home_town = {
        'city': 'Manama',
        'state': 'Bahrain',
        'population': 200000
    }

    home_town_items = []

    for key, value in home_town.items():
        home_town_items.append(f"{key} = {value}")

    return home_town_items


print('Exercise 5:', list_home_town_items())

# Exercise 6: Celebrate Students

def create_awesome_students():
    students = ['Maryam', 'Sara', 'Ali']

    awesome_students = [f"{student} is awesome!" for student in students]

    return awesome_students


print('Exercise 6:', create_awesome_students())


# Exercise 7: Filter Foods

def filter_foods_with_a():
    foods = ('Taco', 'Burrito', 'Sandwich')

    foods_with_an_a = [food for food in foods if 'a' in food]

    return foods_with_an_a


print('Exercise 7:', filter_foods_with_a())

