class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None
        self.prev = None

class Stack:
    def __init__ (self):
        self.head = None
        self.tail = None
    def append(self, data):
        orders = Node(data)

        if self.head is None:
            self.head = orders
            self.tail = orders

        else: 
            self.tail.next = orders
            orders.prev = self.tail
            self.tail = orders 

    def remove (self):
        if not self.tail:
            return "There is nothing to remove from this order. "
        removed = self.tail 

        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.tail = removed.prev
            self.tail.next = None
        return removed.data
    
    def Fullorder (self):
        last = self.tail
        while last: 
            print(last.data)
            last = last.prev
    def peek (self):
      if self.tail is None:
          return "The stack is empty."
      return self.tail.data



   
       
 
    
manageOrder = Stack()
manageOrder.append ("Order 5")
manageOrder.append ("Order 4")
manageOrder.append ("Order 3")
manageOrder.append ("Order 2")
manageOrder.append ("Order 1")

print("Original Order")
manageOrder.Fullorder()

print("Remove Order")
print (manageOrder.remove())

print ("==============")
manageOrder.Fullorder()

print ("Top Order")
print(manageOrder.peek())

class QueuesNode:
    def __init__ (self, data):
        self.data = data
        self.next = None
        self.prev = None

class orderQue:
    def __init__ (self):
        self.head = None
        self.tail = None
    
    def waiting_time (self):
        if self.head is None:
            return "No one is waiting"
        
        current = self.head
        while current.next:
            current = current.next
        return f"{current.data} you are next in line."

    def append (self,data):
        add_order = QueuesNode(data)
        if self.head is None:
            self.head = add_order
            self.tail = add_order
        else:
            self.tail.next = add_order
            add_order.prev = self.tail
            self.tail = add_order

    def process (self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    
    def order_ready (self,data):
      
        if data == 'ready':
            return "Your order is ready."
        else:
            return "Your order is not ready."

            

queue = orderQue()
queue.append("Order A")
queue.append("Order B")
queue.append("Order C")
queue.append("Order D")
queue.append("Order E")

print("Processing orders in the queue:")
queue.process()


print("\nChecking waiting time:")
print(queue.waiting_time())


print("\nChecking order readiness:")
print(queue.order_ready("ready"))  
print(queue.order_ready("not ready")) 

                

