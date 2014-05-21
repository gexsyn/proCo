numTaken= raw_input()
listTaken= raw_input().split(" ")
print listTaken
pivot = int(my_list[0])
num_list = []

front = []
back = []

for x in listTaken:

    num_list.append(x)

    
for k in range(len(num_list)):
     if (int(num_list[k]) < pivot):
        current = num_list[k]
        front.append(current)

     if (int(num_list[k]) >= pivot):
        current = num_list[k]
        back.append(current)
   

for y in num_list:
    print y,


