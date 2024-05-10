class Stack:

    def __init__(self,max_length) -> None:
        self.__max_length = max_length
        self.__first = None
        self.__nodes = []

    def push(self,data):
        if len(self.__nodes) < self.__max_length:
            new_item = node(data)
            self.__nodes.append(new_item)
            item,blank = self.find_end()
            if item != None:
                item.set_pointer(new_item)
            else:
                self.__first = new_item

    def peek(self):
        item, blank = self.find_end()
        if item != None:
            #print(item.get_data())
            return item.get_data()
        else:
            #print("stack is empty")
            return None

    def pop(self):
        end, item = self.find_end()
        try:
            item.set_pointer(None)
        except:
            pass
        try:
            self.__nodes.remove(end)
        except:
            pass
    
    def is_empty(self):
        if len(self.__nodes) == 0:
            return True
        return False
    
    def is_full(self):
        if len(self.__nodes) == self.__max_length:
            return True
        return False


    def find_end(self):
        item = self.__first
        old_item = None
        if item != None:
            while item.get_pointer() != None:
                old_item = item
                item = item.get_pointer()
        return item, old_item

class node:
    
    def __init__(self, data, pointer = None) -> None:
        self.__data = data
        self.__pointer = pointer

    def get_data(self):
        return self.__data
    
    def get_pointer(self):
        return self.__pointer
    
    def set_pointer(self,pointer):
        self.__pointer = pointer

#s = Stack(20)
#s.push("Dave")
#s.push("Jim")
#s.push("Bob")
#s.pop()
#s.peek()