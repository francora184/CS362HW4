import unittest

def avgList(listA):
  total = 0
  items = 0
  for x in range(0, len(listA)):
    total = total + listA[x]
    items += 1

  if(items == 0):
    return -1

  return total / items

class TestList(unittest.TestCase):
  def test_list(self):
    listA = [1, 2, 3]
    self.assertEqual(avgList(listA), 2)

    listB = [3, 3, 3]
    self.assertEqual(avgList(listB), 3)

    listC = []
    self.assertEqual(avgList(listC), -1)

    listC = [-1, -1 ,-1]
    self.assertEqual(avgList(listC), -1)

if __name__ == '__main__':
  unittest.main()
