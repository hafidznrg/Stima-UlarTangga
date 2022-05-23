from math import ceil


class Node:
    def __init__(self, value, route, max):
        self.value = value
        self.route = route
        self.max = max
        self.cost = self.calculateCost()
    
    def isGoal(self):
        return self.value == self.max
    
    def getValue(self):
        return self.value

    def getRoute(self):
        return self.route
    
    def calculateCost(self):
        return len(self.route) + ceil((self.max - self.value)/6)
    
    def getCost(self):
        return self.cost
    
    def print(self):
        print("value:", self.value, "cost:", self.cost, "length:", len(self.route))
    
    def __lt__(self, other):
        if self.cost == other.getCost():
            if len(self.route) == len(other.getRoute()):
                return self.value > other.getValue()
            return len(self.route) > len(other.getRoute())
        return self.cost < other.getCost()
