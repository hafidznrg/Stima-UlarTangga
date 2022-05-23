import os

from Node import Node
from QueueNode import QueueNode


class UlarTangga:
    
    def __init__(self):
        self.playerPos = 0
        self.turn = 0
        self.config = {}
        self.result = []
        self.maximum = 0
        self.readConfig()

    def solve(self):
        start = Node(0, [], self.x*self.y)
        queue = QueueNode()
        queue.push(start)

        while (not queue.isEmpty()):
            current = queue.pop()
            if current.isGoal():
                self.result.append(current)
                self.maximum = len(current.getRoute())
                queue.kill(current.getCost(), self.maximum)
                break
            else:
                # Generate children
                for i in range(1, 7):
                    temp = current.getValue() + i
                    if temp > self.x*self.y:
                        temp = 2*self.x*self.y - temp
                    
                    if temp in self.config:
                        temp = self.config[temp]

                    newNode = Node(temp, current.getRoute() + [i], self.x*self.y)
                    if self.result == [] or len(newNode.getRoute()) <= self.maximum:
                        queue.push(newNode)

    def readConfig(self):
        # input config file from user
        filename = input("Masukkan nama file konfigurasi: ")
        while (not os.path.isfile(filename)):
            print("File tidak ditemukan!")
            filename = input("Masukkan nama file konfigurasi: ")

        # read config file 
        file = open(filename, 'r')
        self.x, self.y = [int(x) for x in file.readline().split()]
        for line in file:
            temp = line.replace("\n", "").split(",")
            self.config[int(temp[0])] = int(temp[1])
        file.close()

    def move(self, n):
        self.turn += 1
        self.playerPos += n
        if self.playerPos > self.x*self.y:
            self.playerPos = 2*self.x*self.y - self.playerPos

        if self.playerPos in self.config:
            self.playerPos = self.config[self.playerPos]

    def printPlayerPos(self):
        print("Player pos: ", self.playerPos)
    
    def printConfig(self):
        print("x: ", self.x, "y: ", self.y)
        for key, value in self.config.items():
            print(key, ":", value)


if __name__ == "__main__":
    game = UlarTangga()
    game.solve()

    result = game.result[0]
    for i in range(len(result.getRoute())):
        print("Turn ke-", i+1, ":", result.getRoute()[i])
        game.move(result.getRoute()[i])
        game.printPlayerPos()
        print()

