cars = ["ok", "ok", "faulty", "ok"]

for status in cars:
  if status == "faulty":
    print('Stopping the production line!')
    break
  print(f"This car is {status}")

for status in cars:
  if status == "faulty":
    print('Stopping the production line!')
    continue
  print(f"This car is {status}")