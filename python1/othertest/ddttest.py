import unittest
from ddt import ddt,data,unpack

"""
setUp tearDown 分别每个单元测试方法执行前后执行


"""
@ddt
class MyTestCase2(unittest.TestCase):
    #在一个测试类中在所有test开始之前
    @classmethod
    def setUpClass(selv):
        print('setUpClass---------------')

    def setUp(self):
        print('setUp MyTestCase2')

    @data(1,2,3)
    def test_normal(self,value):
        print('test_normal',value)
        self.assertEqual(value,value)
    @data((1,2),(2,3))#下面的(1,2)(2,3)代表我们传入的参数,每次传入两个值
    @unpack#告诉我们的测试用例传入的是两个以上的值
    def test_tuple(self,value1,value2):
        print('test_tuple',value1,value2)
        self.assertEqual(value2,value1+1)
    @data([1,2],[2,3])
    @unpack
    def test_list(self,value1,value2):
        print('test_list',value1,value2)
        self.assertEqual(value2,value1+1)
    @data({'value1':1,'value2':2},{'value1':1,'value2':2})
    @unpack
    def test_dict(self,value1,value2):
        print('test_dict',value1,value2)
        self.assertEqual(value2,value1+1)

    def tearDown(self):
        print('tearDown tearDown')

    #在一个测试类中在所有test结束之后
    @classmethod
    def tearDownClass(self):
        print('tearDownClass------------')
if __name__=='__main__':
    unittest.main()
