# 1: define a set with the following values

s = {1, 2, 3, 'a', 'b', 'c'}

# 2; define a function called global_set

def global_set(set_param): #takes 1 parameter, set_param

    # 3: remove all numbers from the set
    set_param.remove(1)
    set_param.remove(2)
    set_param.remove(3)

    # 4: add a three new letters to the set
    set_param.add('d')
    set_param.add('e')
    set_param.add('f')

    # 5: return the new set inside the function
    return set_param

# 6: call the global_set function and pass the set defined in #1
global_set(s)
print(s)

# 7: Print the set variable underneath the function call (should print the updated set)
