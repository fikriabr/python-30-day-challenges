class ElectricVehicle:
  def __init__(self, battery_capacity):
    self.battery_capacity = battery_capacity

  @property
  def battery_capacity(self):
    return self._battery_capacity

  @battery_capacity.setter
  def battery_capacity(self, value):
    if value < 0:
      raise ValueError("Battery capacity cannot be negative.")
    self._battery_capacity = value

  def charge(self):
    return f"Charging the electric vehicle with {self.battery_capacity} kWh battery."
  
class ElectricCar(ElectricVehicle):
  def __init__(self, battery_capacity, model):
    super().__init__(battery_capacity)
    self.model = model

  def drive(self):
    return f"Driving the electric car {self.model} with {self.battery_capacity} kWh battery." 
  
class ElectricBike(ElectricVehicle):
  def __init__(self, battery_capacity, brand):
    super().__init__(battery_capacity)
    self.brand = brand

  def ride(self):
    return f"Riding the electric bike {self.brand} with {self.battery_capacity} kWh battery."
  
def main():
  # Create an instance of ElectricCar
  tesla = ElectricCar(75, "Tesla Model 3")
  print(tesla.drive())  # Output: Driving the electric car Tesla Model 3 with 75 kWh battery.
  print(tesla.charge())  # Output: Charging the electric vehicle with 75 kWh battery.

  # Create an instance of ElectricBike
  yamaha = ElectricBike(500, "Yamaha E-Bike")
  print(yamaha.ride())  # Output: Riding the electric bike Yamaha E-Bike with 500 kWh battery.
  print(yamaha.charge())  # Output: Charging the electric vehicle with 500 kWh battery.

if __name__ == "__main__":
  main()
