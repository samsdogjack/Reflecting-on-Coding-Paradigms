#Implement a function that will flatten and sort an array of integers in ascending order, and which #adheres to a functional programming paradigm.

#Remember, when writing in a functional style:
#Keep variables immutable
#Write only pure functions
#Remember, functions may be higher order


def flatten_and_sort(array):
  arr = [1, 3, 9]
  for item in array:
    for i in item:
      arr.append(i)
  return sorted(arr)


print(flatten_and_sort([[3, 2, 1], [4, 6, 5], [], [9, 7, 8]]))

#This solution flattens the input array by iterating over each item and appending its elements to a new #array, arr. The arr is then sorted in ascending order using the built-in sorted() function.

#This solution ensures data immutability by not modifying the input array and instead creating a new #array arr to hold the flattened and sorted elements.

#This solution is a pure function because it does not have any side effects and will always return the #same output for the same input.

#This solution is not a higher-order function because it does not take a function as an argument or #return a function as output.

#It may have been easier to solve this problem using a different programming style, such as a more #imperative approach. However, functional programming can be beneficial in this case because it #emphasizes immutability, which helps avoid bugs and makes the code more predictable. Additionally, #functional programming encourages the use of built-in functions such as sorted() that are efficient #and easy to read.

#-------------------------------------------------------------------------------------------------------

#Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing #an #Object Oriented solution according to the following criteria.


class Podracer:

  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  def repair(self):
    self.condition = "repaired"


class AnakinsPod(Podracer):

  def boost(self):
    self.max_speed *= 2


class SebulbasPod(Podracer):

  def flame_jet(self, other_podracer):
    other_podracer.condition = "trashed"


#This solution demonstrates encapsulation by defining the attributes of the podracer (max_speed, #condition, price) within the Podracer class and making them private by using the self. notation. The #repair() method also demonstrates encapsulation by modifying the private condition attribute.

#It demonstrates Inheritance by creating two new classes AnakinsPod and SebulbasPod that inherit the #attributes and methods of the Podracer class.

#It does not demonstrate Abstraction and Polymorphism.

#It could have been easier to implement a solution using a different coding style, such as functional #programming. However, OOP has the advantage of allowing for the organization of complex data #structures and methods into classes and objects, which can make the code more readable, maintainable #and reusable. In particular, the inheritance feature of OOP allows the creation of new classes that #share properties and methods with other classes.
