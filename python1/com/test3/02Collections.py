import collections

# ['deque', 'defaultdict', 'namedtuple', 'UserDict', 'UserList','UserString', 'Counter', 'OrderedDict', 'ChainMap']

# tuple
print("tuple ----------------------------------------------------")
# 不可变元组
name_tuple = ('tom1','tom2','tom3')
# name_tuple[1] = 'tom3' #报错
for name in name_tuple:
    print(name)
##元祖拆包
n1,*n2 = name_tuple;
print('print:  ',n1,n2)
# name_tuple[1].append(32)

print(name_tuple)

# namedtuple
print('namedtuple -----------------------------------------------')
from collections import namedtuple
User = namedtuple("User",['name',"age","height"]) # 相比Class少了很多参数或初始化 eg: __init__
u = User(name='tom',age=33,height='55kg')
print(u)
## methodName(*args,**kwargs)   *args：没有参数名传递的,eg: User('tom',33), **kwargs:有参数名: User(name='Tom',age='33')
t = ('bob',22);
u1=User(*t,height='22kg');
print('tuple u1:',u1)
t2 = {"name":'tina',"age":12,"height":"12kg"}
u1=User(**t2)
print('dict u1:',u1)
u1 = User._make(t2)
print('_make  u1:',u1)



# defaultdict





