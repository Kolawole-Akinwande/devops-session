# # Receive an input of words as a string
# print("Enter a statement: ")
# send = input()


# # Attempting to use dictionary mapping
# xchange = {'a' : 'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r', 'j':'q',
#             'k':'p', 'l':'o', 'm':'n', 'n':'m', 'o':'l', 'p':'k', 'q':'j', 'r':'i', 's':'h', 't':'g',
#             'u':'f', 'v':'e', 'w':'d', 'x':'c', 'y':'b', 'z':'a' }


# for key in xchange.values():
#     send = send.replace(key, xchange[key])

# print(send)

# #my challenge so far has been failing to recognize the use of values early on the the for statement.
# # and also the inbuilt replace function, I had to search online to discover that the way I could introduce the
# the dict in the new parameter field was to enclose in []

#Bolow is The massive list of my try and failed methods.


#eip = xchange.keys()
#vep = xchange.values()

#reip = str(eip)
#veip = str(vep)
#convstring = xchange.items()
#fg = xchange.values()

#for char in send:
 #   for fg in convstring:
  #      sent = send.replace(send.lower(), convstring)

#print(sent)
 #   if char in convstring == xchange.keys():
  #      char = xchange.values()
   #     print(send)
#    reip = xchange.keys()
 #   veip = xchange.values()
   # sent = send.replace(reip, veip)
    #print(sent)
    #if char in send == xchange.keys():
     #   send = send.replace()




    #send = dict.values(xchange)
    #print(send)

        #send = send.values()

        #print(sent)

    #if (char for char in send) == xchange.keys():




#print(send)

# ============================
def decrypter(encrypted_character):
    distance_from_a = ord(encrypted_character) - 97
    decrypted_string = ord('z') - distance_from_a

    return chr(decrypted_string)

def solution(encryted_string):
    # xchange = {'a' : 'z', 'b':'y', 'c':'x', 'd':'w', 'e':'v', 'f':'u', 'g':'t', 'h':'s', 'i':'r', 'j':'q',
    #         'k':'p', 'l':'o', 'm':'n', 'n':'m', 'o':'l', 'p':'k', 'q':'j', 'r':'i', 's':'h', 't':'g',
    #         'u':'f', 'v':'e', 'w':'d', 'x':'c', 'y':'b', 'z':'a' }

    decrypted_string = []

    for every_character in encryted_string:
        if every_character.islower():
           decrypted_string.append(decrypter(every_character))
        else:
            decrypted_string.append(every_character)    
    return "".join(decrypted_string)


if __name__ == "__main__":
   print(solution('"vmxibkgrlm"'))

"""
//Time complexity
//Data structure
//Algoritms
//github
Big O notation  Time complexity O(n) space complexity O(1)
"""