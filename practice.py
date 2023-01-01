# -*- coding: utf-8 -*-
"""Practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lhm5RYBcvk6SMK6at79usDiZ68TQL-Wk
"""

class Multiset:
    def __init__(self):
        self.items=[]

    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.items.append(val)
    

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if len(self.items):
            if val in self.items:
                self.items.remove(val)

    def __contains__(self, val):
        if val in self.items:
            return True
        return False
        
    
    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.items)

class Car:
    def __init__(self, max_speed, unit):
        self.max_speed = max_speed
        self.unit = unit

    def __str__(self):
        return 'Car with the maximum speed of ' + str(self.max_speed) + ' ' + str(self.unit)


class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def __str__(self):
        return 'Boat with the maximum speed of ' + str(self.max_speed) + ' knots'


car = Car(120, 'km/h')
print(car)

for i in range(1,15):
 
    # Number divisible by 15,(divisible
    # by both 3 & 5), print 'FizzBuzz'
    # in place of the number
    if i % 15 == 0:
        print("FizzBuzz")                                        
        continue
 
    # Number divisible by 3, print 'Fizz'
    # in place of the number
    elif i % 3 == 0:    
        print("Fizz")                                        
        continue
 
    # Number divisible by 5,
    # print 'Buzz' in
    # place of the number
    elif i % 5 == 0:        
        print("Buzz")                                    
        continue
 
    # Print numbers
    print(i)