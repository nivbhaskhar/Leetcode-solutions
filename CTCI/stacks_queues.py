from collections import deque
import math
# 1

class ThreeStacks:

    def __init__(self, N):
        self.N = N
        i = (N % 3)
        self.x = int((N-i)/3) if i!=2 else int((N-i)/3)+1
        self.arr = [None]*N
        self.stack_lengths = [self.x,self.x,N-2*self.x]
        self.stack_top_positions = [-1,-1,-1]
        

    def is_empty(self, i):
        '''Checks if the i-th stack is empty for i=0,1,2'''
        return (self.stack_top_positions[i]==-1)

    def push(self,i,val):
        '''Pushes value i into the i-th stack for i=0,1,2. 
           If stack is full, prints Error and does nothing'''

        #Check if stack has space
        if self.stack_top_positions[i]+1 < self.stack_lengths[i]:
            #Push val and update top position of stack 
            self.stack_top_positions[i] += 1
            self.arr[i*self.x+ self.stack_top_positions[i]] = val
        else:
            print(f"Error: Stack {i} full. Can't push elements")

    def peek(self,i):
        ''' Returns value of the top of stack i for i=0,1,2.
            If stack is empty, returns None'''
        if self.is_empty(i):
            return None
        else:
            top_pos = i*self.x + self.stack_top_positions[i]
            return self.arr[top_pos]

    def pop(self,i):
        '''Pops the i-th stack for i=0,1,2 and returns the value of the element.
           If stack is empty, prints Error and returns None'''
        
        #Check if stack is empty
        if self.is_empty(i):
            print(f"Error: Stack {i} empty. Can't pop elements")
            return None
        else:
            #Pop val and update top position of stack 
            top_pos = i*self.x + self.stack_top_positions[i]
            popped_value = self.arr[top_pos]
            self.arr[top_pos]=None
            self.stack_top_positions[i] -=1
            return popped_value

    def print(self):
        print(f"Stack 0 - {self.arr[:self.stack_top_positions[0]+1]}")
        print(f"Stack 1 - {self.arr[self.x:self.stack_top_positions[1]+self.x+1]}")
        print(f"Stack 2 - {self.arr[2*self.x:self.stack_top_positions[2]+2*self.x+1]}")


stacks = ThreeStacks(5)
stacks.push(1,3)
stacks.print()
stacks.push(2,5)
stacks.print()
stacks.push(1,4)
stacks.print()
stacks.pop(0)
stacks.print()
stacks.pop(1)
stacks.print()
print(f"Pop {stacks.pop(2)}")
stacks.print()
print(f"Peek {stacks.peek(1)}")
stacks.print()
stacks.push(0,8)
stacks.print()
stacks.peek(0)
stacks.print()


#2

class min_stack():
    def __init__(self):
        self.stack = []

    def is_empty(self):
        '''Checks if the  stack is empty'''
        if self.stack:
            return False
        else:
            return True

    def push(self,val):
        '''Pushes value into stack'''
        if self.is_empty():
            self.stack.append((val,math.inf))
        else:
            prev_top, prev_min = self.stack[-1]
            min_of_substack = min(prev_top, prev_min)
            self.stack.append((val, min_of_substack))
    
    def peek(self):
        ''' Returns value of the top of stack.
            If stack is empty, returns None'''
        if self.is_empty():
            return None
        else:
            print(f"peek is {self.stack[-1][0]}")
            return self.stack[-1][0]

    def find_min(self):
        '''Returns min of stack. 
           If stack is empty, returns None'''
        if self.is_empty():
            return None
        else:
            print(f"min is {min(self.stack[-1][0], self.stack[-1][1])}")
            return min(self.stack[-1][0], self.stack[-1][1])
          

    def pop(self):
        '''Pops the stack and returns the value of the element.
           If stack is empty, prints Error and returns None'''
        
        #Check if stack is empty
        if self.is_empty():
            print(f"Error: Stack {i} empty. Can't pop elements")
            return None
        else:
            val,prev_min = self.stack.pop()
            print(f"pop is {val}")
            return val
            

    def print(self):
        print(f"Stack  - {self.stack}")
        

print("*************")
stack = min_stack()
stack.push(3)
stack.push(5)
stack.push(1)
stack.push(2)
stack.print()
stack.pop()
stack.print()
stack.find_min()
stack.push(10)
stack.push(4)
stack.print()
stack.find_min()


#3

class stack_of_stacks():
    def __init__(self, threshold):
        self.outer_stack = []
        self.t = threshold
        

    def is_empty(self):
        '''Checks if the  stack is empty'''
        if self.outer_stack:
            return False
        else:
            return True

    def push(self,val):
        '''Pushes value into stack'''
        if self.is_empty() or (len(self.outer_stack[-1])>=self.t):
            self.outer_stack.append([val])
        else:
            self.outer_stack[-1].append(val)

        print(f"after pushing : {self.outer_stack}")
    
    def peek(self):
        ''' Returns value of the top of stack.
            If stack is empty, returns None'''
        if self.is_empty():
            return None
        else:
            print(f"peek is {self.outer_stack[-1][-1]}")
            return self.outer_stack[-1][-1]
          

    def pop(self):
        '''Pops the stack and returns the value of the element.
           If stack is empty, prints Error and returns None'''
        
        #Check if stack is empty
        if self.is_empty():
            print(f"Error: Stack  empty. Can't pop elements")
            return None
        else:
            val = self.outer_stack[-1].pop()
            if not self.outer_stack[-1]:
                self.outer_stack.pop()
            print(f"after popping {val} : {self.outer_stack}")
            return val
            

    def print(self):
        print(f"Stack  - {self.outer_stack}")


print("*************")
stack = stack_of_stacks(3)
stack.push(3)
stack.push(5)
stack.push(1)
stack.push(2)
print(stack.peek())
stack.pop()
stack.push(10)
stack.push(4)
stack.push(18)
stack.push(20)
stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack.peek())
stack.pop()
stack.pop()
stack.pop()
stack.pop()


#4
