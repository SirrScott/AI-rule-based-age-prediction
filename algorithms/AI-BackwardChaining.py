
class agePrediction:
    def __init__(self,length,weight,rings):
        self.weight = weight
        self.length = length
        self.rings = rings

    def old(self):
        if self.rings >= 16 and self.length >=0.6 and self.weight >= 1.5:
            return True
        else:
            return False

    def adult(self):
        if self.rings >= 9 and self.length >= 0.35 and self.weight >= 0.5:
            return True
        else:
            return False

    def young(self):
        if self.rings < 9 and self.length < 0.35 and self.weight < 0.5:
            return True
        else:
            return False

    def getAge(self):
        if self.old() == True:
            return "old"
        elif self.adult() == True:
            return "adult"
        elif self.young() == True:
            return "young"
        else:
            return "unknown"


abalone1 = agePrediction(length = 0.5, weight = 0.8, rings = 10)
age = abalone1.getAge()
print(f"age is classified as: {age}")