
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
            self.ringAge = "old"
            if self.length >= 0.6 and self.weight >= 0.5:
                self.physicalAge = "old"
        elif self.rings >= 6:
            self.ringAge = "adult"
            if self.length >= 0.4 and self.weight >= 0.3:
                self.physicalAge = "adult"
        elif self.rings < 6:
            self.ringAge = "young"
            if self.length < 0.4 and self.weight < 0.3:
             self.physicalAge = "young"
        else:
            print("err")
            self.combinedAge = "unknown"

        if self.ringAge != self.physicalAge:
            self.combinedAge = "unknown"


    def predict(self):
        self.rules()
        return self.combinedAge

    def getRing(self):
        return self.ringAge

    def getPhysical(self):
        return self.physicalAge


abalone1 = agePrediction(0.5, 0.3, 10)
prediction = abalone1.predict()
if prediction == "unknown":
    print("physical and ring age classifications do not match\n")
    print(f"ring predictions have the age at: {abalone1.getRing()}\n")
    print(f"while physical attributes show it to be: {abalone1.getPhysical}\n")
    print("true age is uncertain")
else:
    print(f"age of abalone is: {prediction}")