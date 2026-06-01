class  car:
    brand = None
    color = None
    HP = None
    
obj1 = car()
obj2 = car()
obj3 = car()

obj1.brand = "BMW"
obj1.color = "Black"
obj1.HP = 200


obj2.brand = "Audi"
obj2.color = "White"

obj3.brand = "Mercedes"
obj3.color = "Grey"
obj3.HP = 250

print(obj1.brand,obj1.color,obj1.HP)
print()
print(obj2.brand, obj2.color, obj2.HP)
print()
print(obj3.brand, obj3.color, obj3.HP)