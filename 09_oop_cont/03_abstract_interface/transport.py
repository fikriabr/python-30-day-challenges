from abc import ABC, abstractmethod

class Transport(ABC):
  @abstractmethod
  def move(self):
    pass

class Bike(Transport):
  def move(self):
    return "The bike is pedaling forward."
  
class Car(Transport):
  def move(self):
    return "The car is driving on the road."
  
class Bus(Transport):
  def move(self):
    return "The bus is transporting passengers."
  
# Example usage
def main():
  bike = Bike()
  car = Car()
  bus = Bus()

  print(bike.move())  # Output: The bike is pedaling forward.
  print(car.move())   # Output: The car is driving on the road.
  print(bus.move())   # Output: The bus is transporting passengers.

if __name__ == "__main__":
  main()
