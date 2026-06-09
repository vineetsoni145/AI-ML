#Task 1

a = "42"
b = 42
c = 42.0
d = True
e = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("a==b",a==b)
print("b==c",b==c)
print("c==d",c==d)
print("d==e",d==e)
print("a==e",a==b)

#Task 2

text =  "Python is really fun to learn"
print(text[::-1])
print(text[0::2])
print(text[10:16:1])
print(text[-10:])

#Task 3

    #removing duplicate values from score list

scorenew = []

scores = [45, 82, 91, 38, 76, 55, 91, 60, 82, 100]

for score in scores:
    if score not in scorenew:
        scorenew.append(score)

print(scorenew)

    #second highest score from the list

def secondhighest():
    s1h = max(scorenew)
    scorenew.remove(s1h)
    s2h = max(scorenew)
    print("Second highest score:", s2h)

secondhighest()

    #inserting no 70 at third position 

scorenew = scorenew[:2] + [70] + scorenew[2:]
print(scorenew)

    #reversed version of final list 

rev_score = scorenew[::-1]
print(rev_score)

    #original list 
print(scorenew)

#Task 4

students = [
    ("Aryan", 21, "Computer Science"),
    ("Meera", 22, "Mathematics"),
    ("Rohan", 20, "Physics"),
    ("Sneha", 23, "Computer Science"),
]

    #unpacking tuple and printing the values

for name, age, department in students:
    print(f"{name} ({age}) - {department}")

    #total computer science students

totalcs = 0

for student in students:
    if student[2] == "Computer Science":
        totalcs = totalcs + 1

print("Total CS student:", totalcs)

    #oldest student 

def oldest_student():
    
    oldest = students[0]

    for student in students:
        if student[1] > oldest[1]:
            oldest = student

    print(oldest)

    return oldest 

oldest_student()

    #names only tuple

names = ()

for name, age, department in students:
    names = names + (name,)

print(names)

#Task 5

workshop_a = ["Aryan", "Meera", "Rohan", "Fatima", "Karan"]
workshop_b = ["Meera", "Karan", "Priya", "Sneha", "Aryan"]

set_1 = set(workshop_a)
set_2 = set(workshop_b)

print(type(set_1))
print(type(set_2))

    #finding out student who attended both workshop

both_workshop = set_1.intersection(set_2)
print(both_workshop)

    #students who only attended workshop_a

a_only = set_1.difference(set_2)
print(a_only)

    #students who attended at least one workshop

atl_one = set_1.union(set_2)
print(atl_one)

    #students who attended only one workshop either a or b

only_one = set_1.symmetric_difference(set_2)
print(only_one)

#Task 6

inventory = {
    "apples": 50,
    "bananas": 30,
    "mangoes": 0,
    "oranges": 120,
    "grapes": 0,
    "watermelon": 8
}

    #item in stock

inventory_copy = inventory.copy()

for fruits, quantity in inventory_copy.items() :
    if quantity > 0 :
        print(fruits, quantity)

    #adding new item to inventory

inventory["pineapple"] = 15
print(inventory)

    #updating banana quatity

inventory["bananas"] = 45
print(inventory)

    #removing all the items with zero quantity

inventory_copy = inventory.copy()

for fruits, quantity in inventory_copy.items() :
    if quantity == 0 :
        inventory.pop(fruits)

print(inventory)

    #item with highest quantity

name = ""
highest_quantity = 0

for fruits, quantity in inventory_copy.items() :
    if quantity > highest_quantity:
        highest_quantity = quantity
        name = fruits

print(f"{name} has the highest quantity {highest_quantity}")  

#Task 7

    #sum of all even number from 1 to 100
total = 0

for evnum in range(2,101,2):  
    total = total + evnum

print(total)
    
    #Multiplication Table for 7 (7*1 to 7*12)

no1 = 7
no2 = 0

for i in range(12):    
    no2 = no2 + 1
    total = no1 * no2
    print(f"{no1} * {no2} = {total}"  )

    #print only words longer than 3 characters

words = ["sky", "blue", "deep", "ocean", "wide"]

for word in words:
    letter = 0

    for char in word:
        letter = letter + 1
    
    if letter > 3:
        print(word)
    
    #count how many times does "a" appear accross all words in the list 

total_a = 0

for word in words:
    for char in word:
        if char == "a":
            total_a = total_a + 1 
            print(f"times a appears : {total_a} in {word}")

#Task 8 

    #Build a number guessing game

secret_value = 47
useratmp = 0

while True:
    userinp = input("Guess a number OR type quit : ")

    if userinp == "quit":
        print("Game over")
        break

    userinp = int(userinp)
    useratmp = useratmp + 1

    if userinp == secret_value :
        print("Win")
        print("Attempts :",useratmp)
        break
        
    elif userinp > 50:
        print("Guess Too High")
        print("Attempts :",useratmp)
    
    else:
        print("Guess Too Low")
        print("Attempts :",useratmp)

#Task 9

products = [
    {"name": "Mechanical Keyboard", "price": 3499.00, "stock": 12},
    {"name": "USB Hub", "price": 899.50, "stock": 0},
    {"name": "Monitor Stand", "price": 1250.75, "stock": 5},
    {"name": "Webcam", "price": 2199.00, "stock": 3},
]

    #Print a formatted table 

print(f"{'Product':<20} {'Price (₹)':<15} {'Stock':<10} Status")

print("-" * 55)

for product in products:
    if product["stock"] > 0:
        Status = "Available"
    else :
        Status = "Out Of Stock"

    print(f"{product['name']:<20}" 
      f"{product['price']:<15}"
      f"{product['stock']:<10}"
      f"{Status}"
      )

#Task 10

raw_data = [
    "Alice,28,Engineer,75000",
    "Bob,34,Designer,62000",
    "Charlie,28,Engineer,80000",
    "Diana,31,Manager,95000",
    "Eve,34,Designer,58000",
    "Frank,28,Engineer,72000",
]


employees = []

for data in raw_data:

    name, age, role, salary = data.split(",")

    employee = {
        "name": name,
        "age": int(age),
        "role": role,
        "salary": int(salary)
    }

    employees.append(employee)

print(f"{employees}")

#remaining 

# Store all parsed records in a list
# Use a set to find all unique roles
# Use a dictionary to group employees by role (role → list of names)
# Find the average salary per role
# Print a summary using formatted strings