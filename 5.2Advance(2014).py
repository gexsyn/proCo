print " This compares the letters in two words and deletes the same letters in both words and them combines them"
n = int(raw_input(" enter number of words "))
y = []
for x in range(0,n):
    a = raw_input("word 1: ")
    b = raw_input("word 2: ")


    for char in a:
        if char in b:
            y.append(char)
#
 #   print y
  #  for item in y:
   #     print "item :", item
    #    if item in a and item in b:
     #       print "a:",a
      #      print "b:",b
       #     
        #   z = Set(a).intersection(b)
    
z = Set(a).intersection(b)
print z

