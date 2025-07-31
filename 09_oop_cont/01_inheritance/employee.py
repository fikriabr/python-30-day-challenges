class Employee:
  def __init__(self, name, experience, salary):
    self.name = name
    self.experience = experience
    self.salary = salary

class Manager(Employee):
  def __init__(self, name, experience, salary, department):
    super().__init__(name, experience, salary)
    self.department = department

  def get_salary(self):
    return self.salary * 1.2  # Managers get a 20% bonus on their salary
  
class Developer(Employee):
  def __init__(self, name, experience, salary, programming_language):
    super().__init__(name, experience, salary)
    self.programming_language = programming_language

  def get_salary(self):
    return self.salary * 1.1  # Developers get a 10% bonus on their salary
  
def main():
  # Create an instance of Manager
  alice = Manager("Alice", 10, 80000, "IT")
  print(f"Manager {alice.name} from {alice.department} department earns: ${alice.get_salary()}")

  # Create an instance of Developer
  bob = Developer("Bob", 5, 60000, "Python")
  print(f"Developer {bob.name} who codes in {bob.programming_language} earns: ${bob.get_salary()}")

if __name__ == "__main__":
  main()
