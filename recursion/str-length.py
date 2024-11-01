def str_len(s, index = 0):
   try:
       s[index]
       return 1 + str_len(s, index+1)
   except:
       return 0


print(str_len('Hello'))


