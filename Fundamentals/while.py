is_learning = True

while is_learning:
  print('I am learning')
  user_input = input('Are you still learning? ')
  is_learning = user_input == 'yes'

print('Bye')