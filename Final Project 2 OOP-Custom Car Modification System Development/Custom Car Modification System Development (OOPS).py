#!/usr/bin/env python
# coding: utf-8

# In[4]:


import enum

_totalPrice = 0

class Hood:

    class HoodType(enum.Enum):
        Regular = 1
        Sports = 2
        Lifted = 3
        none = 4

    class HoodColor(enum.Enum):
        Red = 1
        Blue = 2
        Black = 3
        Silver = 4
        Green = 5
        Yellow = 6
        NoColorOption = 7

    class HoodTypePrice(enum.Enum):
        Regular = 499
        Sports = 599
        Lifted = 699
        none = 0

    def __init__(self, _type, _color, _price):
        self.TypeName = _type
        self.TypeColor = _color
        self.TypePrice = _price

# -------------------------------------------

class Fender:
    class FenderType(enum.Enum):
        Regular = 1
        Sports = 2
        CarbonFiber = 3
        none = 4
    
    class FenderColor(enum.Enum):
        Red = 1
        Blue = 2
        Black = 3
        Silver = 4
        Green = 5
        Yellow = 6
        NoColorOption = 7
    
    class FenderPrice(enum.Enum):
        Regular = 100
        Sports = 200
        CarbonFiber = 1000
        none = 0

    def __init__(self, _type, _color, _price):
        self.TypeName = _type
        self.TypeColor = _color
        self.TypePrice = _price

# -------------------------------------------

class Doors:
    class DoorColor(enum.Enum):
        Red = 1
        Blue = 2
        Black = 3
        Silver = 4
        Green = 5
        Yellow = 6
        none = 7
    
    class DoorPrice(enum.Enum):
        Price = 599
        none = 0

    def __init__(self, _color, _price):
        self.Color = _color
        self.Price = _price

# ------------------------------------------

class Wheelset:
    class WheelType(enum.Enum):
        Powder_Coated = 1
        Paint_Coated = 2
        Clear_Coated = 3
        Chrome_Coated = 4
        Bare_Polished = 5
        none = 6

    class WheelPrice(enum.Enum):
        Coated = 1299
        none = 0

    def __init__(self, _type, _price):
        self.WheelType = _type
        self.Price = _price
    


class Address:

    def __init__(self, addressLine1, addressLine2, city, state, zip):        
        self.addressLine1 = addressLine1
        self.addressLine2 = addressLine2
        self.city = city
        self.state = state
        self.zip = zip

class Vehicle:

    def __init__(self, make, model, year, hood, fender, doors, wheelset):
        self.make = make
        self.model = model
        self.year = year
        self.hood = hood
        self.fender = fender
        self.doors = doors
        self.wheelset = wheelset

class Customer:
    
    def __init__(self, firstName, middleName, lastName, address, vehicle):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.address = address
        self.vehicle = vehicle

def SetCustomer1():

  
    objAddress = Address(addressLine1='12345 Good Ave,', addressLine2='Number 1', city='Hastings,', state='MN', zip='55022')

    objhood = Hood(_type=Hood.HoodType.Lifted, _color=Hood.HoodColor.Silver, _price=Hood.HoodTypePrice.Lifted)

    objfender = Fender(_type=Fender.FenderType.CarbonFiber, _color=Fender.FenderColor.Black, _price=Fender.FenderPrice.CarbonFiber)

    objdoor = Doors(_color=Doors.DoorColor.Black,_price=Doors.DoorPrice.Price)
  
    objwheels = Wheelset(_type=Wheelset.WheelType.Paint_Coated,_price=Wheelset.WheelPrice.Coated)

    objVehicle = Vehicle(make='Tesla', model='Model 3', year='2019', hood=objhood, fender=objfender, doors=objdoor, wheelset=objwheels)
 
    objCustomer = Customer(firstName='Syed', middleName='Ali', lastName='Naqvi', address=objAddress, vehicle=objVehicle)

    # Print Customer Details
    print('-----------------------------------------------------\n' + objCustomer.firstName + ' ' + objCustomer.middleName + ' ' + objCustomer.lastName)
    print(objCustomer.address.addressLine1 + ' ' + objCustomer.address.addressLine2)
    print(objCustomer.address.city + ' ' + objCustomer.address.state + ' ' + objCustomer.address.zip)
 
    # # Print Vehicle Details
    print('\nMake: ' + objCustomer.vehicle.make)
    print('Model: ' + objCustomer.vehicle.model)
    print('Year: ' + objCustomer.vehicle.year)

    # # Print Customer selected option
    print('\n'+ 'Customer selected the following options')
    print('\nHood: ' + str(objCustomer.vehicle.hood.TypeName.name) + ' in ' + str(objCustomer.vehicle.hood.TypeColor.name) + ' color, Price: $' + str(float(objCustomer.vehicle.hood.TypePrice.value)))
    print('Fender: ' + str(objCustomer.vehicle.fender.TypeName.name) + ' in ' + str(objCustomer.vehicle.fender.TypeColor.name) + ' color, Price: $' + str(float(objCustomer.vehicle.fender.TypePrice.value)))
    print('Door Color: ' + str(objCustomer.vehicle.doors.Color.name) + ' color, Price: $' + str(float(objCustomer.vehicle.doors.Price.value)))
    print('Wheelset: ' + str(objCustomer.vehicle.wheelset.WheelType.name) + ', Price: $' + str(float(objCustomer.vehicle.wheelset.Price.value)) + '\n' )

    _totalPrice = float(objCustomer.vehicle.hood.TypePrice.value) + float(objCustomer.vehicle.fender.TypePrice.value) + float(objCustomer.vehicle.doors.Price.value) + float(objCustomer.vehicle.wheelset.Price.value)
    print('Total Price: $' + str(_totalPrice)) 


def SetCustomer2():

  
    objAddress = Address(addressLine1='499 Apple Street', addressLine2='', city='Eagan', state='MN', zip='55123')

    objhood = Hood(_type=Hood.HoodType.none, _color=Hood.HoodColor.NoColorOption, _price=Hood.HoodTypePrice.none)

    objfender = Fender(_type=Fender.FenderType.CarbonFiber, _color=Fender.FenderColor.Black, _price=Fender.FenderPrice.CarbonFiber)

    objdoor = Doors(_color=Doors.DoorColor.Yellow,_price=Doors.DoorPrice.Price)

    objwheels = Wheelset(_type=Wheelset.WheelType.Powder_Coated,_price=Wheelset.WheelPrice.Coated)

    objVehicle = Vehicle(make='Ford', model='F150', year='2016', hood=objhood, fender=objfender, doors=objdoor, wheelset=objwheels)

    objCustomer = Customer(firstName='Gloria', middleName='J', lastName='Redford', address=objAddress, vehicle=objVehicle)

    # Print Customer Details
    
    print('-----------------------------------------------------\n' + objCustomer.firstName + ' ' + objCustomer.middleName + ' ' + objCustomer.lastName)
    print(objCustomer.address.addressLine1 + ' ' + objCustomer.address.addressLine2)
    print(objCustomer.address.city + ' ' + objCustomer.address.state + ' ' + objCustomer.address.zip)
 
    # # Print Vehicle Details
    
    print('\nMake: ' + objCustomer.vehicle.make)
    print('Model: ' + objCustomer.vehicle.model)
    print('Year: ' + objCustomer.vehicle.year)

    # # Print Customer selected option
    
    print('\n'+ 'Customer selected the following options')
    print('\nHood: ' + str(objCustomer.vehicle.hood.TypeName.name) + ' in ' + str(objCustomer.vehicle.hood.TypeColor.name) + ' color, Price: $' + str(float(objCustomer.vehicle.hood.TypePrice.value)))
    print('Fender: ' + str(objCustomer.vehicle.fender.TypeName.name) + ' in ' + str(objCustomer.vehicle.fender.TypeColor.name) + ' color, Price: $' + str(float(objCustomer.vehicle.fender.TypePrice.value)))
    print('Door Color: ' + str(objCustomer.vehicle.doors.Color.name) + ' color, Price: $' + str(float(objCustomer.vehicle.doors.Price.value)))
    print('Wheelset: ' + str(objCustomer.vehicle.wheelset.WheelType.name) + ', Price: $' + str(float(objCustomer.vehicle.wheelset.Price.value)) + '\n' )

    _totalPrice = float(objCustomer.vehicle.hood.TypePrice.value) + float(objCustomer.vehicle.fender.TypePrice.value) + float(objCustomer.vehicle.doors.Price.value) + float(objCustomer.vehicle.wheelset.Price.value)
    print('Total Price: $' + str(_totalPrice) + '\n') 


# ---------------------- Code Execution ----------------------

SetCustomer1()
SetCustomer2()


# In[ ]:




