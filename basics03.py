class Tiger:
    __tiger_counter = 0

    def __init__(self, name):
        Tiger.__tiger_counter += 1
        self.Tiger = name
        self.handle_birth()

#nie moge zrobic tej metody statycznej bo wypisuje self.Tiger imie tygrysa
    def handle_birth(self):
        print("Hi everyone. I'm ", self.Tiger, ", I am alive, and I'm born. Roar.")
        return

    @classmethod
    def get_tiger_count(cls):
        return cls.__tiger_counter

print("Execution started")
print("")
Tiger1 = Tiger("John")
Tiger2 = Tiger("Bob")
print("We now have",Tiger.get_tiger_count(),"tigers.")