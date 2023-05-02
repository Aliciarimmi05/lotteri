import random

class lotteri:
    def __init__(self):
        self.list_vinster = [
        "solstol",
        "röd porche",
        "handuk",
        "10 liter tvål"
        ]

    def get_vinst(self):
        slumptal = random.randint(0, 3)
        return self.list_vinster [slumptal]