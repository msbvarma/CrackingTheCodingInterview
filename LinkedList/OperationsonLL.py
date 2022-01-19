class Node:
    def __init__(self,info,link=None):
        self.info = info
        self.link = link

class LinkedList:
    def __init__(self):
        self.head =None

    def insert_at_begining(self,info):
        new_node = Node(info)
        if self.head != None:
            new_node.link = self.head
            self.head = new_node
        else:
            self.head = new_node

    def insert_at_end(self,info):
        new_node = Node(info)
        if(self.head!=None):
            current = self.head
            while(current.link!= None):
                current = current.link
            current.link =new_node
        else:
            self.head = new_node

    def insert_at_position(self,info,pos):
        newNode = Node(info)
        if(self.head!=None):
            current = self.head
            temp_pos = 0
            while(temp_pos<pos and current!=None):
                current = current.link
                temp_pos +=1
            newNode.link = current.link
            current.link = newNode
        else:
            self.head = newNode

    def display(self):
        current = self.head
        while(current !=None):
            print(current.info)
            current = current.link

llist = LinkedList()
llist.insert_at_begining(11)
llist.insert_at_begining(8)

llist.insert_at_end(99)
llist.insert_at_end(666)
llist.insert_at_end(777)
llist.display()
llist.insert_at_position(55,1)
print("Test=",llist.head)
llist.display()