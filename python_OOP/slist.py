#Part 1 - recreate SList and Node.  Recreate addNode and printAllValues methods.
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SList:
    def __init__(self,value):
        self.value = value
        node = Node(value)
        self.head = node
    def addNode(self,value):
        runner = self.head
        while runner.next != None:
            runner = runner.next
        node = Node(value)
        runner.next = node
        return self
    def printAllValues(self):
        runner = self.head
        print("Starting to print slist...")
        while runner.next != None:
            print(f"Node stored in {runner}  ||  Node's value is {runner.value}  ||  Next node is at {runner.next}/n")
            runner = runner.next
        print(f"Node stored in {runner}  ||  Node's value is {runner.value}  || This is the end of your SList")
        return self

slist1 = SList(5)
slist1.addNode(2).addNode(7).printAllValues()
