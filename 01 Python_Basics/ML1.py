from operator import index


name = "John"
age = 30
present = True
valueofpie =3.14

print(name, type(name))
print(age, type(age))
print(present, type(present))
print(valueofpie, type(valueofpie))

a=[1,2,3,4,5,6,7,8,9,10,"zeelu"]

print(a[3])
print(a, type(a))

personal_details = [ ['name' , 'vineet soni'], ['age' , 20], ['address' , 'Ahemdabad'] ]
print(personal_details [2][1])

a = {0,1,2,99,3,6,85,4,5,75,6,7,6,88,8,9,6,65}
print(a)

tup = (1,2,3,4,5,6,7,8,9,10)
print(tup)

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year
print(f"Hello {name}, you are {age} years old.")

a = (1,2,3)
b = 4
c = a + (b,)
print(c)

a = {"name": "Prince", "age": 30, "country": "India"}
a["City"] = "ahemdabad"
print(a["age"])

b = {
    "user": {
        "name": "kavya",
        "age": 25,
        "city": "ahmedabad"
    },
    "qualification": {
        "degree": "BCA",
        "year": 2020,
        "university": "GLS"
    }
}

print(b["user"]["name"],b["qualification"]["degree"])


doctor_detail = {
  "count": 14,
  "doctors": [
    {
      "doctor_id": "1",
      "email": "john.smith@hospital.com",
      "name": "Dr. John Smith",
      "phone": "1234567890",
      "specialization": "Cardiologist"
    },
    {
      "doctor_id": "2",
      "email": "anmol.smith@hospital.com",
      "name": "Dr. Anmol Smith",
      "phone": "1234563890",
      "specialization": "Cardiologist"
    },
    {
      "doctor_id": "3",
      "email": "john.smith@hospital.com",
      "name": "Dr. John Smith",
      "phone": "1234567890",
      "specialization": "Cardiologist"
    },
    {
      "doctor_id": "4",
      "email": "sarah.lee@hospital.com",
      "name": "Dr. Sarah Lee",
      "phone": "9876543210",
      "specialization": "Neurologist"
    },
    {
      "doctor_id": "5",
      "email": "john.sad@hospital.com",
      "name": "test 1",
      "phone": "123421",
      "specialization": "Cardiologist"
    },
    {
      "doctor_id": "6",
      "email": "john.sad@hospital.com",
      "name": "test 1",
      "phone": "123421",
      "specialization": "Cardiologist"
    },
    {
      "doctor_id": "7",
      "email": "darjijay017@gmail.com",
      "name": "hello",
      "phone": "23234324",
      "specialization": "fdssdfdsf"
    },
    {
      "doctor_id": "8",
      "email": "darjijay017@gmail.com",
      "name": "jayhd",
      "phone": "1235678",
      "specialization": "mind"
    },
    {
      "doctor_id": "9",
      "email": "darjijay017@gmail.com",
      "name": "jay darji",
      "phone": "23456",
      "specialization": "degree"
    },
    {
      "doctor_id": "10",
      "email": "darjijay017@gmail.com",
      "name": "jay darji",
      "phone": "23456",
      "specialization": "degree"
    },
    {
      "doctor_id": "11",
      "email": "darjijay017@gmail.com",
      "name": "anmol sir",
      "phone": "243246",
      "specialization": "dfgdfg"
    },
    {
      "doctor_id": "12",
      "email": "dgdgdgdfg",
      "name": "jay",
      "phone": "SGADH",
      "specialization": "sfnrry"
    },
    {
      "doctor_id": "13",
      "email": "rajdarji@gmail.cpm",
      "name": "shah",
      "phone": "2345678",
      "specialization": "deh"
    },
    {
      "doctor_id": "14",
      "email": "sdsgs@sgsd.sdf",
      "name": "test",
      "phone": "2342",
      "specialization": "fsdf"
    }
  ]
}

print(doctor_detail["doctors"][2]["doctor_id"])

# smarthome structure (dictionary)

smarthome = {
  "count": 10,
  "smartdevices": [
    {
      "device_id": 1,
      "device_name": "Smart AC",
      "type": "air_conditioner",
      "brand": "Mitsubishi",
      "active_status": "ON",
      "settings": {
        "temperature": 25,
        "unit": "celsius",
        "mode": "dry"
      }
    },
    {
      "device_id": 2,
      "device_name": "Smart Hub",
      "type": "hub",
      "brand": "TP-Link",
      "active_status": "ON",
      "specs": {
        "model": "Tapo H200",
        "storage_type": "micro_sd"
      }
    },
    {
      "device_id": 3,
      "device_name": "Smart Fan",
      "type": "fan",
      "brand": "Havells",
      "active_status": "ON",
      "specs": {
        "fan_type": "ceiling",
        "color": "brown"
      }
    },
    {
      "device_id": 4,
      "device_name": "Smart Lights",
      "type": "lighting",
      "brand": "Philips",
      "active_status": "ON",
      "specs": {
        "light_type": "tubelight",
        "color": "white"
      }
    },
    {
      "device_id": 5,
      "device_name": "Smart TV",
      "type": "television",
      "brand": "Samsung",
      "active_status": "ON",
      "specs": {
        "screen_size_inch": 52,
        "os": "android"
      }
    },
    {
      "device_id": 6,
      "device_name": "Smart CCTV",
      "type": "camera",
      "brand": "CP Plus",
      "active_status": "ON",
      "settings": {
        "recording_status": "ON",
        "connectivity": "wifi"
      }
    },
    {
      "device_id": 7,
      "device_name": "Smart Air Purifier",
      "type": "air_purifier",
      "brand": "Crompton",
      "active_status": "ON",
      "settings": {
        "mode": "hybrid",
        "battery_status": "charging"
      }
    },
    {
      "device_id": 8,
      "device_name": "Smart Refrigerator",
      "type": "refrigerator",
      "brand": "LG",
      "active_status": "ON",
      "settings": {
        "mode": "auto",
        "temperature": 15,
        "unit": "celsius"
      }
    },
    {
      "device_id": 9,
      "device_name": "Smart Lock",
      "type": "security_lock",
      "brand": "Godrej",
      "active_status": "ON",
      "settings": {
        "mode": "auto",
        "battery_status": "charged"
      }
    },
    {
      "device_id": 10,
      "device_name": "Smart Doorbell",
      "type": "doorbell",
      "brand": "Orient",
      "active_status": "ON",
      "settings": {
        "mode": "single_ring",
        "battery_status": "charging"
      }
    }
  ]
}

print(smarthome["smartdevices"][0:5])

def birth_date():
  name = input("Enter your name : ")
  birth_year = int(input("Enter your birth year : "))
  current_year = 2026
  age = current_year - birth_year
  print(name,age)

birth_date()

def avg():
   no1=int(input("Enter number1 : "))
   no2=int(input("Enter number2 : "))
   no3=int(input("Enter number3 : "))
   no4=int(input("Enter number4 : "))
   no5=int(input("Enter number5 : "))
   total = no1 + no2 + no3 + no4 + no5
   avg5 = total / 5  
   print(total,avg5)

avg()



from os import name


def average():
  total = 0

  for i in range(5):
    no = int(input("enter no."))
    total = total + no
    avg5 = total / 5

  print(total,avg5)


average()

#ask user his/her name and print first 2 + last 2 words of their name using while loop



while True:
  name = input("Enter your name ")
  firsttwo = (name[0:2:1])
  lasttwo = (name[-2::1])
  print(f"{firsttwo},{lasttwo}")



# task-1
# ask age and return the category from child, adult, Senior citizen

age = int(input("Enter your age : "))
print(age)

def category(age):

  if age < 15 :
    print("child")
  elif age < 55 : 
    print ("adult")
  else :
    print ("Senior Citizen")
    

category(age)


# ask age name and last four digit of aadhar card and return a unique ID like 
# if name is amol and age is 12 and aadhar card no is 4567
# then id will be an124567



def user():
  name = input("Enter your name : ")
  age = int(input("Enter your age : "))
  aadharL4 = int(input("Enter your last 4 digit of aadhar card : "))
  f2n = (name[0:2:1])
  print(f"your name is {f2n} your age is {age} your aadharL4 is {aadharL4} your unique id is {f2n}{age}{aadharL4}")

user()


#ask user a no and generate a number and check if both are same if  
#both are same then win else loose

import random

while True:
    userno = int(input("Guess a number : "))
    
    random_no = random.randint(1, 10)

    if random_no == userno:
        print("Win")
    else:
        print("Loose")
        print("Correct number is :", random_no)




while True:
    userinp = input("Enter your name : ")

    if userinp == "prince":
        print("NOOB")
    
    elif userinp == "zeelu":
        print("BOT")

    elif userinp == "vineet":
        print("HACKER")

    else :
        print("Hello")


from turtle import update


Task = {
    "tasklist" :[]
}

while True:
    choice = input("press 1 to add, \npress2 to delete, \npress3 to update \npress 4 to view tasks \npress5 to quit\nEnter Choice:")

    if choice == "1":
        name = input("enter name of task:")    
        desc = input("enter description:")
        email = input("enter email:")
        data = {"name":name, "description":desc,"email":email }
        Task["tasklist"].append(data)
        
        print("Task Addedd Successfully")
    
    elif choice == "3":
        update = input("Enter task name to update :")

        for task in Task["tasklist"]:

            if task["name"] == update:

                task["name"] = input("Enter new name : ")
                task["description"] = input("Enter new description : ")
                task["email"] = input("Enter new Email : ")

                print("Task updated Successfully")
            
            else :
                print("task not found")


    elif choice == "4":
        print(Task["tasklist"])

    elif choice == "5":
        print("Task Ended")
        break