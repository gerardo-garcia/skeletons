#!/usr/bin/env python
import unittest

def setUpModule():
    return

def tearDownModule():
    return

class TestStringMethods(unittest.TestCase):

    upper_string = 'FOO'
    split_string = 'hello world'

    def test_upper(self):
        self.assertEqual('foo'.upper(), self.upper_string)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        self.assertEqual(self.split_string.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            self.split_string.split(2)

#The class Widget to be tested should be in a different module.
#It is possible to place definitions of test cases and test suites in the same modules as the code they are to test,
# but there are several advantages to placing the test code in a separate module
class Widget:
    def __init__(self, title):
        self.title = title
        self.x = 50
        self.y = 50

    def size(self):
        return (self.x, self.y)

    def resize(self, x, y):
        self.x = x
        self.y = y

    def dispose(self):
        return

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()
        self.widget = None

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

class ListTestCase(unittest.TestCase):
    _myClassList = []

    @classmethod
    def setUpClass(cls):
        cls._myClassList = []
    
    @classmethod
    def tearDownClass(cls):
        del cls._myClassList
    
    def setUp(self):
        self.mylist = []
    
    def tearDown(self):
        del self.mylist
    
    def test_add_one_element(self):
        self._myClassList.append(1)
        self.mylist.append(1)
        self.assertEqual(len(self.mylist), 1, 'incorrect length')
    
    def test_add_two_elements(self):
        self._myClassList.append(1)
        self._myClassList.append(2)
        self.mylist.append(1)
        self.mylist.append(2)
        self.assertEqual(len(self.mylist), 2, 'incorrect length')
    
    def test_check_lengths(self):
        self.assertEqual(len(self.mylist), 0, 'incorrect length')
        #print self.mylist
        #print self._myClassList
        self.assertEqual(len(self._myClassList), 3, 'incorrect length')

class NumbersTestCase(unittest.TestCase):
    def test_equal(self):
        n = 2
        self.assertEqual(n, 2)
        self.assertNotEqual(n, 3)

    def test_boolean(self):
        b = True
        self.assertTrue(b)

    def test_division(self):
        self.assertEqual(4/2, 2)
        with self.assertRaises(ZeroDivisionError):
            a = 1/0

if __name__ == '__main__':
    #unittest.main(verbosity=2)
    
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(WidgetTestCase)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(ListTestCase)
    suite4 = unittest.TestLoader().loadTestsFromTestCase(NumbersTestCase)
    #suite = unittest.TestSuite([suite1, suite2, suite3, suite3, suite4])
    # suite3 will call the methods setUpClass and tearDownClass only if there is a different TestCase being called
    suite = unittest.TestSuite([suite1, suite2, suite3, suite4, suite3])
    unittest.TextTestRunner(verbosity=2).run(suite)

