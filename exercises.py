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