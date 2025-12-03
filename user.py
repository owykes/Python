class Users:
    def __init__(self, first_name, last_name, email):
          self.first_name = first_name
          self.last_name = last_name
          self.email = email

    def describe_user(self):
        print(self.first_name, self.last_name, self.email)

    def greet_user(self):
         print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

owen = Users('owen', 'wykes', 'hello@gmail.com')

owen.greet_user()
owen.describe_user()