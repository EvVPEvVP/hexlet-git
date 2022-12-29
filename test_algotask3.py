import unittest
import Algotask3


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.da = Algotask3.DynArray()

    def test_insert1(self):
        for i in range(1, 4):
            self.da.append(i)
        self.da.insert(2, 10)
        self.assertEqual(self.da.count, 4)
        self.assertTrue(self.da.count < self.da.capacity)
        self.assertTrue(self.da.capacity == 16)

    def test_insert2(self):
        for i in range(1, 17):
            self.da.append(i)
        self.da.insert(16, 10)
        self.assertEqual(self.da.count, 17)
        self.assertTrue(self.da.count < self.da.capacity)
        self.assertTrue(self.da.capacity == (16*2))

    def test_insert3(self):
        for i in range(1, 5):
            self.da.append(i)
        try:
            self.da.insert(6, 10)
        except IndexError:
            print('out of the range')

    def test_delete1(self):
        for i in range(1, 5):
            self.da.append(i)
        self.da.delete(1)
        self.assertEqual(self.da.count, 3)
        self.assertTrue(self.da.capacity == 16)

    def test_delete2(self):
        for i in range(1, 34):
            self.da.append(i)
        self.da.delete(1)
        self.assertEqual(self.da.count, 32)
        self.assertTrue(self.da.capacity == 64)

    def test_delete3(self):
        for i in range(1, 13):
            self.da.append(i)
        self.da.resize(24)
        self.assertTrue(self.da.capacity == 24)
        self.da.delete(1)
        self.assertEqual(self.da.count, 11)
        self.assertTrue(self.da.capacity == int(24/1.5))

    def test_delete4(self):
        for i in range(1, 5):
            self.da.append(i)
        try:
            self.da.delete(-1)
        except IndexError:
            print('out of the range')

    # def test_delete5(self):
    #     for i in range(1, 2):
    #         self.da.append(i)
    #     self.da.resize(32)
    #     self.assertTrue(self.da.capacity == 32)
    #     self.da.delete(0)
    #     self.assertEqual(self.da.count, 0)
    #     self.assertTrue(self.da.capacity == int((32/1.5)))



if __name__ == '__main__':
    unittest.main()
