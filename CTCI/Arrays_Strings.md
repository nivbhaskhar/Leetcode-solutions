# Arrays and strings




## 1. Does a string have all unique char ?

Method 1 : Store characters seen in dictionary with their frequency. If freq >1, non-unique characters seen. Space complexity - O(|set of possible characters|), Time complexity - O(|string|)

Method 2 : Sort in place. Then scan through to see if any repeats.

```python
def all_unique(s):
    if not s:
       return True

    #Oops. Cannot sort string in place!
    s = sorted(s)
    n = len(s)
    for i in range(n-1):
        if s[i]==s[i+1]:
           return False
    return True

```

_ If len(s) > |set of possible characters|, return False


## 2. Is one string a permutation of the other ?

Method 1: Unequal lengths - return False. Equal lengths - compute freq dict of the two strings. If equal, yes.

Better : Instead of storing 2 dicts, store 1 freq dict and subtract from it for the second string. At the end, check if all values of dict are 0

Method 2 : Sort. Then check if strings are the same.


## 3. Replace white space with %20

def replace_white_space(s):
    return s.replace(" ", '%20')

## 4. Is a string a permutation of a palindrome ?

String is palindrome frequencies are all even or frequencies are all even except for one of them, whose freq is odd.

Method 1 : Use Counter. 

Method 1 variant: Keep track of odd freq characters in a set. As soon as you see a pair, delete it.

Method 2 : Maintain a 26 bit string. If you see character, flip the bit at the character's alphabetical index (a=0, b=1, c=2,...). At the end, you want a bit string with at most one 1.

x = bit string
for valid x, x & (x-1) = 0000..
for invalid x, x & (x-1) != 0

## 5. Is string s <= one edit away from string t ?

edits : insert, delete, replace 1 character 

Let len(s) <= len(t). If len(s) < len(t)-1, return False
Make queues of s, t
Set edit distance = 0
If tops of both queues match, pop both queues
If they don't and len(s)==len(t), increment edit distance and pop both queues
If they don't and len(s) < len(t), increment edit distance and pop t
Keep doing this till s is empty
If edit distance > 1, return False in between

```python
def one_edit_away(s,t):
    len_s = len(s)
    len_t = len(t)
    unequal_lengths = False

    diff = abs(len_s-len_t)
    if diff > 1:
        return False
    elif diff == 1:
        #switch to make s the shorter string
        unequal_lengths = True
        if len_s > len_t:
            temp = s
            s = t
            t = temp
            len_s = len(s)
            len_t = len(t)

    queue_s = deque(s)
    queue_t = deque(t)
    edit_distance = 0
    while(queue_s):
        if  queue_s[0] != queue_t[0]:
            if edit_distance < 1:
                edit_distance += 1        
                if unequal_lengths:
                    queue_t.popleft()
                    continue
            else:
                return False
        queue_s.popleft()
        queue_t.popleft()
    return True


```

## 6. Compress strings (aabcccaa -> a2b1c3a2. If not strictly shorter, return original string)


Keep track of current_char and current_char_count.
scan each character of string
If it differs from current_char, then append current_char and current_char_count into a list and change the current_char to new_character and reset current_char_count = 1.
Otherwise increment current_char_count

return join of the list if length of list is strictly < original string


```python
def compress_string(s):
    current_char = None
    current_char_count = 0
    compressed_string_list = []
    for pos,char_from_s in enumerate(s):
        if current_char == char_from_s:
            current_char_count += 1
        else:
            if current_char:
                compressed_string_list.append(current_char)
                for digit in str(current_char_count):
                    compressed_string_list.append(digit)
            current_char = char_from_s
            current_char_count = 1

    if current_char:
        compressed_string_list.append(current_char)
        for digit in str(current_char_count):
            compressed_string_list.append(digit) 
    if len(compressed_string_list) < len(s):
        return ''.join(compressed_string_list)
    else:
        return s
```







