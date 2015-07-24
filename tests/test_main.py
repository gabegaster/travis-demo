import unittest
from gabe_travis_demo import main

class MainTest(unittest.TestCase):
    def test_main(self):
        things = list(main.main())
        self.assertTrue(set(i[0] for i in things) == set((1,2)), things)
