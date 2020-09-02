ages = [24, 54, 23, 54, 44, 66, 25, 67]

odds = [age for age in ages if age % 2 == 1]
print(odds)

friends = {'Rolf', 'Ruth', 'Charlie', 'Jen'}
guests = {'Jose', 'Bob', 'Charlie', 'Rolf', 'Michael'}


present_friends = friends.intersection(guests)
present_friends = {name for name in present_friends}

print(present_friends)

my_friends = ['Rolf', 'Ruth', 'Charlie', 'Jen']
time_since_seen = [3, 7, 15, 11]

long_timers = {
  my_friends[i]: time_since_seen[i]
  for i in range(len(my_friends))
  if time_since_seen[i] > 5
}

print(long_timers)