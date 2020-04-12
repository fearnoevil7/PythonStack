class Toy:
    def __init__(self, name, catchphrase, material):
        #TOY ATTRIBUTES GO HERE
        self.name = name
        self.catchphrase = catchphrase
        self.material = material
        self.eyes = 2
        self.lover = None
        pass
#TOY METHODS GO HERE
    def speak(self):
        print(self.catchphrase)
        return self

    def say_info(self):
        print("I have " + str(self.eyes) + "eyes")
        return self



woody = Toy("Woody", "Howdy partner!", "fabric")
buzz = Toy("Buzz", "To infinity and beyond", "plastic")
jessie = Toy("Jessie", "Yee_haw", "fabric")
# print(buzz['name'])
woody.lover = jessie
jessie.lover = buzz
buzz.lover = jessie
print(woody.lover.lover.lover.lover.name)



# ["Green", "skinny"] <- arr[0]
# {'color': "green"} <- obj["color"]