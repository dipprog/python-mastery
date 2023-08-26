# testsimple.py

import simple
import unittest

# Must inherit from unittest.TestCase
class TestAdd(unittest.TestCase):
    def test_simple(self):
        # Test with simple integer arguments
        r = simple.add(2,2)
        self.assertEqual(r, 5)

    def test_str(self):
        # Test with strings
        r = simple.add('hello', 'world')
        self.assertEqual(r, 'helloworld')

    # Each method must start with 'test...'

# Running test
if __name__ == '__main__':
    unittest.main()

# Comments on unittest

# Can grow to be quite complicated for large applications
# The unittest module has a huge number of options related to test runners, collection of results, and other aspects of testing
# Look at 'pytest' as an alternative
