from collections import deque
# 1
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



print(all_unique('abcdregr'))


# 3
def replace_white_space(s):
    return s.replace(" ", '%20')

#5

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


print(one_edit_away("ttts", "tts"))

print(one_edit_away("tttts", "tts"))

print(one_edit_away("tut", "tts"))


print(one_edit_away("tttts", "ttttsr"))


print(one_edit_away("tttter", "ttttsr"))            
                    
                



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


print(compress_string('aaaaaaaaaaaaaaaaaaaaaaaaaabbccaaar'))
print(compress_string(''))
print(compress_string('aAsswwe'))

    
                
    
            
        

