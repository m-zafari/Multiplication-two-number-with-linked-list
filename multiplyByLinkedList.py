# Mohammad Zafari
# mhdzafari80@gmail.com

from typing import final


class Node: 
       
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
class CircularLinkedList: 
      
    def __init__(self): 
        self.head = None 
    
    def push(self, data): 
        given_node = Node(data) 
        temp = self.head 
          
        given_node.next = self.head 
   
        if self.head is not None: 
            while(temp.next != self.head): 
                temp = temp.next 
            temp.next = given_node 
  
        else: 
            given_node.next = given_node 
  
        self.head = given_node 
    
def multiply(p,q): 
    
    first  = [int(d) for d in p]
    second = [int(d) for d in q]
        
    list1 = CircularLinkedList()
    i = len(first) - 1
    while i > -1:  
        list1.push(first[i])
        i -= 1

    list2 = CircularLinkedList()
    j = len(second) - 1
    while j > -1:  
        list2.push(second[j])
        j -= 1
    data1 = list1.head
    data2 = list2.head
    power1 = len(first)  - 1
    power2 = len(second) - 1
    sum = 0
    for l1 in range(len(first)):
        power2 = len(second) - 1
        for l2 in range(len(second)):
            sum += (data1.data)*(10**power1) * (data2.data)*(10**power2)
            data2 = data2.next
            power2 -= 1
        data1 = data1.next
        power1 -= 1
    return sum

num1 = input("Enter the first  number:")
num2 = input("Enter the second number:")
print(f"{num1} * {num2} = {multiply(num1,num2)}")
