class User:
  def __init__(self, name, address):
    self.name = name
    self.address = address

  def __str__(self):
    return f"User(name={self.name}, address={self.address})"
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, value):
    self._name = value
  
  @property
  def address(self):
    return self._address
  
  @address.setter
  def address(self, value):
    self._address = value


class Admin(User):
  def __init__(self, name, address, admin_level):
    super().__init__(name, address)
    self.admin_level = admin_level

  @property
  def admin_level(self):
    return self._admin_level
  
  @admin_level.setter
  def admin_level(self, value):
    self._admin_level = value
  
  def __str__(self):
    return f"Admin(name={self.name}, address={self.address}, admin_level={self.admin_level})"


def main():
    # Example usage of the User class
    user = User("Andi", "123 Main St")
    print(user)  # Output: User(name=Andi, address=123 Main St)
    print(f"Name: {user.name}, Address: {user.address}")
    user.name = "Andi Updated"
    user.address = "456 Main St"
    print(user)  # Output: User(name=Andi Updated, address=456 Main St)
    print(f"Name: {user.name}, Address: {user.address}")

    # Example usage of the Admin class
    admin = Admin("Budi", "456 Elm St", "SuperAdmin")
    print(admin)  # Output: Admin(name=Budi, address=456 Elm St, admin_level=SuperAdmin)
    print(f"Name: {admin.name}, Address: {admin.address}, Admin Level: {admin.admin_level}")
    admin.name = "Budi Updated"
    admin.address = "789 Elm St"
    admin.admin_level = "Admin"
    print(admin)  # Output: Admin(name=Budi Updated, address=789 Elm St, admin_level=Admin)
    print(f"Name: {admin.name}, Address: {admin.address}, Admin Level: {admin.admin_level}")

if __name__ == "__main__":
    main()
