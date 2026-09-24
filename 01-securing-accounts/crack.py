#numbers
#from string import digits

#for i in digits:
#    for j in digits:
#        for k in digits:
#            for l in digits:
#                print(i, j, k, l)


#from string import ascii_letters
#for i in ascii_letters:
#    for j in ascii_letters:
#       for k in ascii_letters:
#            for l in ascii_letters:
#                print(i, j, k, l)


from string import ascii_letters, digits, puntuation
for i in ascii_letters + digits + puntuation:
    for j in ascii_letters + digits + puntuation:
        for k in ascii_letters + digits + puntuation:
            for l in ascii_letters + digits + puntuation:
                print(i, j, k, l)