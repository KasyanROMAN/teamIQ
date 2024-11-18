class person:
    name='Kiril'
    age=12
    
    def get(self):
        print(self.name,self.age)
    def ret_name(self):
        return self.name
    def ret_age(self):
        return self.age
    def typ(self):
        print(type(self.age),type(self.name))
        