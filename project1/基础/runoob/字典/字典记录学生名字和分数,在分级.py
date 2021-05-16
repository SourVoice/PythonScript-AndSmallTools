students = {}
write = 1
while write:
    name = str(input('input a name:'))
    grade = int(input('input his or her grade:'))
    students[str(name)] = grade  # 向字典中添加key
    write = int(input('go on?\n 1/for continue 0/for exit'))
print('name rate'.center(20, '-'))
for key, value in students.items():
    if value >= 90:
        print((key + ' ' + str(value) + ' ' + 'A').center(20, '-'))
    elif 89 > value >= 60:
        print((key + ' ' + str(value) + ' ' + 'B').center(20, '-'))
    else:
        print((key + " " + str(value) + ' ' + 'C').center(20, '-'))
