#!/usr/bin/env python
# coding: utf-8

# In[107]:


def validate_input(list_bracket):
    bracks = ["[", "]", "{", "}", "(", ")"]
    for bracket in list_bracket:
        if (bracket not in bracks):
            return False
    return True
        
# n= "{{[]/}}"
# validate_input(n)


# In[108]:


def rev_string(string):
    rev_str = ''
    for i in range(len(string)-1,-1, -1):
        rev_str += string[i]
    return rev_str

# print(rev_string("RANA"))


# In[109]:


brackets_correct = "{([[{}]])}"
brackets_wrong = "{[{}{})]}"



# In[117]:


'''Function to check Bracket Symmetry'''
def bracket_symmetry_checker(bracks):
    brack_dict = {'{':'}', '[':']', '(':')'}
    brack_close_stack = []
    brack_open_stack = []
    brack = bracks

    '''Create Stack of Open and Close Brackets'''
    for br in brack:
        if (br in brack_dict.keys()):
            brack_open_stack.append(brack_dict[br])
        if (br in brack_dict.values()):
            if (br == brack_open_stack.pop()):
                continue
            else:
                return False
    return True
            


# In[119]:


print(bracket_symmetry_checker(brackets_wrong))

