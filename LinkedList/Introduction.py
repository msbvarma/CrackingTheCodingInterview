class Node:
    #constructor
    def __init__(self,info,link=None):
        self.info = info
        self.link = link

first = Node(13)
print("First=",first)
print("First info=",first.info)
print("First Link=",first.link)

second = Node(51)
first.link = second

print("Second=",second)
print("Second info=",second.info)
