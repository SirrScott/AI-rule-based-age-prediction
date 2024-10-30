
class agePrediction:
    def __init__(self,length,weight,rings):
        self.length = length  #mm
        self.weight = weight  #g
        self.rings = rings
        self.ringAge = None
        self.physicalAge = None

    def ringRules(self):
        if self.rings >= 16:
            print("1")
            self.ringAge = "old"
        elif self.rings >= 9:
            print("2")
            self.ringAge = "adult"
        elif self.rings < 9:
            print("3")
            self.ringAge = "young"
        else:
            print("err1")
            self.ringAge = "unknown"

    def physRules(self):
        if self.length >= 0.6 and self.weight >= 1.5:
            print("1.1")
            self.physicalAge = "old"
        elif self.length >= 0.35 and self.weight >= 0.5:
            print("2.1")
            self.physicalAge = "adult"
        elif self.length < 0.35 and self.weight < 0.5:
            print("3.1")
            self.physicalAge = "young"
        else:
            print("err2")
            self.physicalAge = "unknown"

    def getRing(self):
        return self.ringAge

    def getPhysical(self):
        return self.physicalAge


abalone1 = agePrediction(length = 0.5, weight = 0.3, rings = 13)
abalone1.ringRules()
abalone1.physRules()

if abalone1.getRing() != abalone1.getPhysical():
    print("predictions with physical attributes dont match true age given by ring age")
    print(f"ring method has the age at: {abalone1.getRing()}")
    print(f"while physical attributes show it to be: {abalone1.getPhysical()}")
elif abalone1.getRing() == abalone1.getPhysical():
    print("physical attribute age prediction match actual age from rings")
    print(f"ring method has the age at: {abalone1.getRing()}")
    print(f"while physical attributes show it to be: {abalone1.getPhysical()}")