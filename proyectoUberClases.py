class Account:
    def __init__(self, id, name, document, email, password):
        self.id = id
        self.name = name
        self.document = document
        self.email = email
        self.password = password

class Payment:
    def __init__(self, id):
        self.id = id

class Car:
    def __init__(self, id, license, driver, passengers):
        self.id = id
        self.license = license
        self.driver = driver
        self.passengers = passengers

