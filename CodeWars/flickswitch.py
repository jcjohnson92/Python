# Task
# Create a function that always returns True/true for every item in a given list.
# However, if an element is the word 'flick', switch to always returning the opposite boolean value.
# ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]
# ['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]
# ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]\


# create a variable labled true that switchs when looping through the list to false when 'flick' is shown


def flick_switch(lst):
    empty_lst = []
    answer = True
    for i in lst:
        if i == 'flick':
            answer = not answer    
        empty_lst.append(answer)
    print(empty_lst)




flick_switch(['codewars', 'flick', 'code', 'wars'])
flick_switch(['flick', 'chocolate', 'adventure', 'sunshine'])
flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick'])
flick_switch(['bicycle'])
flick_switch(['john, smith, susan', 'flick'])
flick_switch(['flick', 'flick', 'flick', 'flick', 'flick'])