from pydantic import BaseModel

# Creating a class which inherits the pydantic Base class
class Person(BaseModel):
    name:str
    age:int
    city:str

# Instantiating a object of person class
person = Person(name="Manu", age=34, city="Aberdeen")
print("\n")
print(person)

# # Here i have entered the value of city wrong, so the pydantic data validator will throw error
try:
    person1  = Person(name="Manu", age=34, city=12)
except ValueError as e:
    print("\n")
    print(e)


# What if we have optional values to fill
from typing import Optional, List

class Employee(BaseModel):
    id:int
    name:str
    department:str
    salary:Optional[float] = None #This field is optional and can be None.
    is_active:Optional[bool] = None  #This field is optional and can be None.

employee = Employee(id=1, name="Manu", department="Science", salary = 10000, is_active=True)
print("\n")
print(employee)

employee1 = Employee(id=1, name="Manu", department="Science")
print("\n")
print(employee1)

# if need to store list of values then there is a room for that too
from typing import List

class Classroom(BaseModel):
    room_number:int
    student_names:List[str]
    capacity:int

classroom = Classroom(room_number=1, student_names=["Manu","Anju","Ashvi"], capacity=3)
print("\n")
print(classroom)

# What if I entered one value in List as integer
try:
    invalid_entry = Classroom(roon_number=2, student_names = ["Manu", 123, "Ashvi"], capacity=4)
except ValueError as e:
    print("\n")
    print(e)



#Pydantic fields and customizations

from pydantic import BaseModel, Field

class Items(BaseModel):
    name:str=Field(min_length=2) # We are setting condition that it should have 2 char atleast
    price:float=Field(ge=0,le=100)
    quantity:int=Field(ge=0)


item = Items(name="rice", price=5.70, quantity=2)
print("\n")
print(item)

try:
    item1 = Items(name="s", price="2.89", quantity=4)
except ValueError as e:
    print("\n")
    print(e)

