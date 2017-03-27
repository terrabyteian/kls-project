# Simple example of object-oriented programming
# A zoo contains pens (3) and each pen contains one of 3 animals
# Animals: lion, tiger, bear

# When instantiating a zoo, it becomes populated with lions, tigers, and bears
# The zoo can perform an action called "observe", where it looks around each pen and says what the animals in each are doing

class Zoo:

    pens = {"PEN1":[],"PEN2":[],"PEN3":[]}

    def __init__(self):
        self.pens["PEN1"].append(Lion())
        self.pens["PEN2"].append(Tiger())
        self.pens["PEN3"].append(Bear())

    def observe(self):
        for pen in sorted(self.pens.keys()):
            for animal in self.pens[pen]:
                print "In %s, " % pen
                animal.doItsThing()

class Animal:
    name=""
    action=""
    def doItsThing(self):
        print "%s performs action: %s\n" % (self.name,self.action)

class Lion(Animal):
    name="Lion"
    action="Roar!"

class Tiger(Animal):
    name="Tiger"
    action="Jump!"

class Bear(Animal):
    name="Bear"
    action="Sleep!"


# Instantiate zoo
zoo = Zoo()
zoo.observe()
