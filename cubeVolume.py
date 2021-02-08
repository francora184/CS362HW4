import unittest

def volume(a):
  if(a > 0):
    return a ** 3
  else:
    return -1

class TestVolume(unittest.TestCase):
  def test_volume(self):
    self.assertEqual(volume(2), 8)
    self.assertEqual(volume(3), 27)
    self.assertEqual(volume(-2), -1)

if __name__ == '__main__':
  unittest.main()
