class Node:
    def __init__(self, value):
        self.value = value
        self.pointer = None

class SList:
    def __init__(self, value):
        self.value = value
        node = Node(value)
        self.head = node
    def print(self):
        runner = self.head
        while runner.pointer:
            print(f'Node Value: {runner.value}')
            runner = runner.pointer
        print(f'Node Value: {runner.value}\n')
        return self
    def addNode(self, value):
        runner = self.head
        while runner.pointer:
            runner = runner.pointer
        node = Node(value)
        runner.pointer = node
        return self
    def removeNode(self, value):
        runner = self.head
        prevrunner = self.head
        while runner.pointer and runner.value != value:
                prevrunner=runner
                runner = runner.pointer
        if runner == self.head:
            self.head = runner.pointer
            runner = None
        elif runner.value == value:
            if runner.pointer == None:
                prevrunner.pointer = None
            else:
                prevrunner.pointer = runner.pointer
                runner.pointer = None
        return self
    def insertNode(self,value,index):
        runner = self.head
        node = Node(value)
        count = 0
        if count == index:
            node.pointer = self.head
            self.head = node
        while runner:
            count += 1
            if count == index:
                node.pointer = runner.pointer
                runner.pointer = node
            runner = runner.pointer
        return self


            
    


list1 = SList(5)

list1.addNode(7)

list1.addNode(9)
list1.addNode(1)
list1.print()

# list1.removeNode(7)
list1.insertNode(2,4)
list1.print()
 # removes 9, which is one of the middle nodes in the list
list1.removeNode(5) # removes 5, which is the first value in the list
list1.removeNode(1) # removes 1, which is the last node in the list
list1.print()
# list1.printAllValues("Attempt 1")
