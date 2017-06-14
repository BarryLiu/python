print("练习python 基础");

#list   : list[-1] 取最后一个 -2倒数第二...
names = ["Tom","Jim","Bob"]
print(names);
print(names[0]+" "+names[1]+" "+names[2]+" "+names[-1]);

names.append('Lina');
print(names);
names.insert(1,'Jack');
print(names);
names.pop();
print(names);
print(len(names))


#t uple另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

age=(11,12,13);
print(age);

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)


#条件判断
age = 10
if age>10:
	print("年龄大于10")

age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


#多重if
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

    