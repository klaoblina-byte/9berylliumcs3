# POLYMORPHISM
## ACTIVITY 2
**Name:** Karmela Liane A. Oblina
**Section:** 9 - Beryllium
**Last Name:** Oblina
**Date:** 10/11/2026

### Instruction: Do what is asked in each item below:

### 1. Answer the following questions:

#### a. What is duck typing, as explained in the video?

Duck typing, as explained in the video, focuses on what the object can do, and not what it is. To elaborate, it is a programming concept in Python where the suitability of an object for a task is determined by the presence of methods and attributes, rather than its class type. Its name came from the saying: "If it walks like a duck and quacks like a duck, it must be a duck." Lastly, duck typing is another way of achieving polymorphism besides inheritance.

#### b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

The Car class needed to have the same method name as the Dog and Cat classes in oredr for it to work  inside the same loop. In this case, the supposedly name of the Car class method is horn; it was then changed to speak so that it could work inside the same loop as the other classes. Lastly, an alive attribute was also added into this class, indicating whether it is alive (True) or not (False).

### 2. How does the code in 2.2 demonstrate polymorphism?

The code in 2.2 demonstrates a type of polymorphism called duck typing. Each class there involve classes that are independent from each other. The core of this code is the start_trip(vehicle) function, showing that it doesn't care what specific class type they are, but rather if it possesses the move() function. If a class does not possess the function move(), the code will run fine until it tries to call the missing method in a class. 