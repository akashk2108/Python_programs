computer_parts =["monitor",
                 "keyboard",
                 "mouse"
                 ]
valid_option=[]
for i in range(1,len(computer_parts)+1):
    valid_option.append(str(i))
print(valid_option)
current_choice="-"
selected_parts=[]

while current_choice != '0':
     if current_choice in valid_option:
         print("{0} adding".format(current_choice))
         index=int(current_choice)-1
         selected_parts.append(computer_parts[index])
     else:
         for number,parts in enumerate(computer_parts):
            print("{0}:{1}".format((number+1),parts))
     current_choice=input()
print(selected_parts)