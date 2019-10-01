##An object is a single software unit that combines data and method.
##Data in an object are known as attributes.
##Procedures/Functions in an object are known as methods.
##
##
##class Car:
##    pass
##
##ford=Car() #ford is the object or instance of class Car
##honda=Car()
##audi=Car()
##
###can add attributes(speed) on the go for empty classes(Car)
##ford.speed=200
##honda.speed=220
##audi.speed=250
##
##ford.color='red'
##honda.color='blue'
##audi.color='black'
##
##print(ford.speed)
##print(ford.color)
##
##ford.speed=300
##ford.color='blue'
##
##print(ford.speed)
##print(ford.color)





class Rectangle:
    pass
rect1=Rectangle()
rect2=Rectangle()

rect1.height=20
rect2.height=30

rect1.width=40
rect2.width=10

print(rect1.height*rect1.width)
print(rect2.height*rect2.width)




##
##class Car:
##    def __init__(self,speed,color):
##        
##        #init behaves as a constructor.
##        #First method called whenever an instance is created
##        #default values for attributes allowed eg. self.speed=100
##        #if multple init methods are used, python takes the last init method by default
##        print('the __init__ is called')
##        print(speed,color)
##        self.speed=speed
##        self.color=color
##        
##
##ford=Car(200,'red')
###ford is the object or instance of class Car
##honda=Car(250,'blue')
##audi=Car(300,'black')
##
##print(ford.speed)
##print(ford.color)
