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