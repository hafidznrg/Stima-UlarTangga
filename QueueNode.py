import heapq as hq


class QueueNode:
    def __init__(self):
        self.queue = []

    def push(self, node):
        hq.heappush(self.queue, node)
    
    def pop(self):
        return hq.heappop(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def getSize(self):
        return len(self.queue)

    def kill(self, cost, length):
        i = 0
        while i < len(self.queue):
            if len(self.queue[i].getRoute()) > length:
                self.queue.pop(i)
            elif self.queue[i].getCost() > 2*cost:
                self.queue.pop(i)
            else:
                i += 1
        hq.heapify(self.queue)
    
    def printQueue(self):
        if self.isEmpty():
            print("Queue kosong")
        else:
            for i in range(len(self.queue)):
                self.queue[i].print()
