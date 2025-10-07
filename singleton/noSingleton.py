class RegularClass:
    def __init__(self):
        self.value = None

regular1 = RegularClass()
regular2 = RegularClass()

regular1.value = "Sou independente!"

print(regular1.value)
print(regular2.value)
print(regular1 is regular2)