#Using while loop
class_no=1
while class_no<11:
    if class_no & 1==0:
        class_no+=1
        continue
    roll_no=1
    while roll_no<31:
        if class_no%3==0 and roll_no<15:
            roll_no+=1
            continue
        print('class: ',class_no,'roll_no',roll_no)
        roll_no+=1
    class_no+=1
    