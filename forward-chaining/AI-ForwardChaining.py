
class agePrediction:
    def __init__(self,length,weight,rings):
        self.length = length
        self.weight = weight
        self.rings = rings
        self.ringAge = None
        self.physicalAge = None
        self.combinedAge = None

    #less than 6 rings (<7.5 years old),  young
    #from 6 to 13 rings (7.5 to 14.5 years old),  adult
    #and more than 13 rings (>14.5 years old),  old

    def rules(self):
        if self.rings >= 13:
            print("1")
            self.ringAge = "old"
            self.physRules()
        elif self.rings >= 6:
            print("2")
            self.ringAge = "adult"
            self.physRules()
        elif self.rings < 6:
            print("3")
            self.ringAge = "young"
            self.physRules()
        else:
            print("err")
            self.combinedAge = "unknown"

        if self.ringAge != self.physicalAge:
            self.combinedAge = "unknown"

    def physRules(self):
        if self.length >= 0.6 and self.weight >= 0.5:
            print("1.1")
            self.physicalAge = "old"
            self.combinedAge = "old"
        elif self.length >= 0.4 and self.weight >= 0.3:
            print("2.1")
            self.physicalAge = "adult"
            self.combinedAge = "adult"
        elif self.length < 0.4 and self.weight < 0.3:
            print("3.1")
            self.physicalAge = "young"
            self.combinedAge = "young"
        else:
            print("err")

    def predict(self):
        self.rules()
        return self.combinedAge

    def getRing(self):
        return self.ringAge

    def getPhysical(self):
        return self.physicalAge


abalone1 = agePrediction(length = 0.5, weight = 0.3, rings = 13)
prediction = abalone1.predict()
if prediction == "unknown":
    print("physical and ring age classifications do not match")
    print(f"ring predictions have the age at: {abalone1.getRing()}")
    print(f"while physical attributes show it to be: {abalone1.getPhysical()}")
    print("true age is uncertain")
else:
    print(f"age of abalone is: {prediction}")