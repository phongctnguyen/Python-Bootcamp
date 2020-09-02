def greet():
  name = input('Enter your name? ')
  print(f'Hello {name}')

# greet()

def calculate_mpg(car_to_calculate):
  mpg = car_to_calculate["mileage"] / car_to_calculate["fuel_consumed"]
  name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
  print(f"{name} does {mpg} miles per gallon")


car = {
  "make": "Ford",
  "model": "Fiesta",
  "mileage": 23000,
  "fuel_consumed": 460
}

calculate_mpg(car)

def add(a, b):
  return a + b

print(add(4, 5))

def student(firstname, lastname ='Mark', standard ='Fifth'): 
	print(firstname, lastname, 'studies in', standard, 'Standard') 

# 1 positional argument 
student('John') 

# 3 positional arguments						 
student('John', 'Gates', 'Seventh')	 

# 2 positional arguments 
student('John', 'Gates')				 
student('John', 'Seventh') 
