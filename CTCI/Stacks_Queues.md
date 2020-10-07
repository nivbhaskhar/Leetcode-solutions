# Stacks and Queues



## 1. Use a single array to implement 3 stacks

Method 1 : Allocate 1/3 space to each stack. Maintain indices of tops of stacks

N=combined length of stacks

Deciding lengths of each stack

01|23|456  7=3(2)+1
--------------
012|345|67|  8 = 3(3)-1
012|345|678| 9 =3(3)
012|345|6789| 10 = 3(3)+1
--------------
0123|4567|8910 11=3(4)-1

N=3x or 3x+1 or 3x-1

3x-1=n x+x+(x-1) = 3y+2. x= y+1
3x=n x+x+x
3x+1=n x+x+(x+1)

stack 1 - [0,1...., x-1]
stack 2 - [x, ... 2x-1]
stack 3 = [2x,...,N-1]

```python

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


```


Method 2: 





```python


```



## 2. Design a stack with push, pop, peek and also find_min function (O(1))

Method : When pushing in a new element, also push with it the min of the stack below.
When popping, just pop normally
When finding min, return min of (top value, min of stack below)
For initial value, push (initial val, math.inf)

```python


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


```



## 3. Design a set of stacks with push, pop, peek functionality which should behave just like one stack but each stack should have len <= given threshold. Once one stack exceeds threshold, the other should start filling in

Method: Have a stack of stacks

```python

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

```


## 4. Implement a queue with two stacks

Have two stacks - Stack and ReverseStack

Keep pushing to Stack.
If a pop/peek request, pop/peek from Reverse Stack if non-empty.
If Reverse stack is empty, pop all elements of Stack and push into Reverse Stack


## 5. Sort a stack so that smaller elements on top. Can use another temp stack but cannot use other data structures to copy elements


Old stack = s (unsorted)
Temp stack = t (empty)

make t sorted in ascending order as follows:
pop element in s (*)
insert into t if maintains sorted order
If not, hold it in temp variable, pop elements from t and insert into s
insert the (*) in t

..once s is empty, pop elements from t to s

O(n^2)



## 6. Design a queue which has two kinds of elements (category A, category B). Want operations : = enqueue, dequeueAny, dequeueA, dequeueB (dequeue A dequeues the first A in etc..)

Maintain 2 queues, one for Category A and one for Category B. When inserting, also insert time-stamp.

For dequeueAny, pop the oldest one amongst heads of Queue A, B.






## 7. Implement a stack


## 8. Implement a queue


## 9. Implement a recursion problem using stacks



