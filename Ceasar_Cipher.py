#!/usr/bin/env python
# coding: utf-8

# ## Ceasar Cipher



def index_return(i_num, incr):
    count = i_num
    if (incr >= 0):
        for i in range(incr):
            count += 1
            if (count == 26):
                count = 0
    if (incr < 0):
        for i in range(abs(incr)):
            count -= 1
            if (count == -1):
                count = 25
    return count

    


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




alpha_index = list()

for i in range(0,26):
    alpha_index.append(i)




alpha_dict = dict(zip(alphabet,alpha_index))



def encrypt_decrypt(text, val):
    text1 = text.lower()
    enc_text = ''
    for char in text1:
        enc_text += alphabet[index_return(alpha_dict[char],val)]
    return enc_text

x = encrypt_decrypt('durlabh', 2)
print(x)





