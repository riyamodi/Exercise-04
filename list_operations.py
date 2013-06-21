
"""
Part 1: Fundamental operations on lists
---------------------------------------

The fundamental operations on lists in Python are those that are part of the
language syntax and/or cannot be implemented in terms of other list operations:
    * List literals ([], ['hello'], [3, 1, 4, 1, 5, 9], etc.)
    * List indexing (some_list[index])
    * List indexing assignment (some_list[index] = value)
    * List slicing (some_list[start:end])
    * List slicing assignment (some_list[start:end] = another_list)
    * List index deletion (del some_list[index])
    * List slicing deletion (del some_list[start:end])

In this section you will implement functions that each use just one of the
operations. The docstring of each function describes what it should do. Consult
test_list_operations.py for concrete examples of the expected function behavior.
"""

def head(input_list):
    """Return the first element of the input list."""
    return input_list[0]

def tail(input_list):
    """Return all elements of the input list except the first."""
    return input_list[1:]

def last(input_list):
    """Return the last element of the input list."""
    return input_list[-1]

def init(input_list):
    """Return all elements of the input list except the last."""
    return input_list[:-1]

def first_three(input_list):
    """Return the first three elements of the input list."""
    return input_list[:3]

def last_five(input_list):
    """Return the last five elements of the input list."""
    return input_list[-5:]

def middle(input_list):
    """Return all elements of the input list except the first two and the last
    two.
    """
    return input_list[2:-2]

def inner_four(input_list):
    """Return the third, fourth, fifth, and sixth elements of the input list."""
    return input_list[2:6]

def inner_four_end(input_list):
    """Return the sixth, fifth, fourth, and third elements from the end of the
    list, in that order.
    """
    return input_list[custom_len(input_list)-6:custom_len(input_list)-2]
    #return input_list[5:1:-1]

def replace_head(input_list):
    """Replace the head of the input list with the value 42."""
    input_list[0] = 42
    return input_list[0]

def replace_third_and_last(input_list):
    """Replace the third and last elements of the input list with the value 37."""
    input_list[2] = 37
    input_list[-1] = 37

def replace_middle(input_list):
    """Replace all elements of the input list with the the values 42 and 37, in
    that order, except for the first two and last two elements.
    """
    input_list[2]=42
    input_list[3] = 37
    del input_list[4:-2]


def delete_third_and_seventh(input_list):
    """Remove the third and seventh elements of the input list."""
    del input_list[6]
    del input_list[2]


def delete_middle(input_list):
    """Remove all elements from the input list except for the first two and the
    last two.
    """
    del input_list[2:-2]

"""
Part 2: Derived operations on lists
-----------------------------------

In this section you will implement your own versions of the standard list methods.
You should use only the primitive operations from Part 1 in your implementations.
For loops are also allowed, such as the following:
    for element in some_list:
        # Do something with element

Each custom method imitates a built-in list method, as described by the docstring
for each function. Play with the built-in methods in the Python REPL to get a feel
for how they work before trying to write your custom version. You may also look at
the test_list_operations.py file for concrete examples of expected behavior.
"""

def custom_len(input_list):
    """custom_len(input_list) imitates len(input_list)"""
    
    counter = 0

    for element in input_list:
        counter += 1
    
    return counter
                         
# For the next four functions, get clever using slice operations described in the first half
def custom_append(input_list, value):
    """custom_append(input_list, value) imitates input_list.append(value)"""
    
    
    #input_list += [value]                                                                                   
    
    input_list[custom_len(input_list):] = [value] 


def custom_extend(input_list, values):
    """custom_extend(input_list, values) imitates input_list.extend(values)"""
                         
    #input_list[0:-1] += [values]

    #input_list[custom_len(input_list):] = [values]

    #custom_append(input_list,values)

    for element in values:
        custom_append(input_list, element)

def custom_insert(input_list, index, value):
    """custom_insert(input_list, index, value) imitates
    input_list.insert(index, value)
    """
    input_list[index:index] = [value]
    
    # print "Index: ", index
    # print "Value : ", value
    # first_half= input_list[0:index+1]
    # print "First Half", first_half
    # second_half= input_list[index:-1]
    # print "Second Half", second_half
    
    # input_list[0:-1] = first_half + [value] + second_half
    # print "Input List", input_list


   # for element in input_list:
   #     if input_list[]== index:
   #         custom_extend(element, value)

    # input_list[custom_extend(input_list):] = [value]

    # input_list.custom_extend(index,value)

    # for element in xrange(index):
    #     custom_extend(input_list,value) 
    #    custom_extend(input_list,value)

    # input_list[index] += 
    
    # THIS MAKES SENSE TO ME!!
    # custom_extend(input_list[index],value)

    # input_list[custom_extend(index,value):] = [value]

    # input_list[index] += custom_extend(input_list,value)

    # custom_append(input_list[index],value)

def custom_remove(input_list, value):
    """custom_remove(input_list, value) imitates input_list.remove(value)"""


    #for element in input_list:
    #    if element == value:
    #        (del input_list[])

    #del input_list[0:0]

    # for element in input_list:
    #    if element == value:
    #        del element

    counter=0
    # print "Value: %r " % value

    for element in input_list:
        # print "COUNTER: %r" % counter
        # print "ELEMENT: %r" % element
        if element == value:
           del input_list[counter]
           return 
        counter += 1

def custom_pop(input_list):
    """custom_pop(input_list) imitates input_list.pop()"""
    
    x = input_list[-1]
    del input_list[-1]

    return x



def custom_index(input_list, value):
    """custom_index(input_list, value) imitates input_list.index(value)"""
    
    counter = 0

    for string in input_list:
        if string == value:
            return counter
        counter += 1


def custom_count(input_list, value):
    """custom_count(input_list, value) imitates input_list.count(value)"""
    
    counter = 0

    for element in input_list:
        if element == value:
            counter += 1 
    return counter

def custom_reverse(input_list):
    """custom_reverse(input_list) imitates input_list.reverse()"""

   # for element in input_list #range(custom_len(input_list)-1,-1,-1):
     #    input_list[element]=temp
      #input_list[::-1]

    # counter = 1
    # temp = " "

    # for index in range(len(input_list)):
    #     input_list[index] = temp
    #     input_list[len(input_list)-counter] = input_list[index]
    #     temp = input_list[len(input_list)-counter]

    # return input_list

    temp=" "
    counter = 1

    for index in range(custom_len(input_list)/2):
    # print "Counter at beginning is: %r" % counter
    # print "Index at beginning is: %r" % index
    # print "temp before the temp line is: %s" % temp
    #give temp the value of the first element
        temp = input_list[index]
        input_list[index] = input_list[custom_len(input_list)-counter]
    #print "TEMP is: %s" % temp
        input_list[custom_len(input_list)-counter] = temp 
    # print "TEMPP: %s" % temp
    # #cat[len(cat)-counter] = cat[index]
    # print "Cat right now is: %r" % cat
    
        counter += 1
    # print "COUNTER at the end of loop is: %r" % counter
    # print "INDEX at the end is: %r" % index
    # print "TEMP the   tat end is: %s" % temp
    #print "Cat right now is: %r" % cat
    return input_list

def custom_contains(input_list, value):
    """custom_contains(input_list, value) imitates (value in input_list)"""
    pass

    for element in input_list:
        if element == value:
            return True
    else:
        return False

def custom_equality(some_list, another_list):
    """custom_equality(some_list, another_list) imitates
    (some_list == another_list)
    """
    counter = 0

    if custom_len(some_list) != custom_len(another_list):
        return False

    # while (counter < custom_len(some_list) and counter < custom_len(another_list)):
    for counter in range(custom_len(some_list)-1): 
        if some_list[counter] == another_list[counter]:
            counter += 1
        else:
            return False
    return True




