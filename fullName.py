import unittest

def fullName(a, b):
  return a + " " +  b

first = input("Enter first name: ")
last = input("Enter last name: ")

class TestName(unittest.TestCase):
  def test_fullname(self):
    self.assertEqual(fullName(first, last), first + " " + last)
    self.assertTrue(fullName(first, last), first + last)
    self.assertNotEqual(fullName(first, last), last + " " + first)

if __name__ == '__main__':
  unittest.main()
