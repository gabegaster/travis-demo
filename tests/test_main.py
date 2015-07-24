import unittest
import gabe_travis_demo

class MainTest(unittest.TestCase):
    def test_main(self):
        things = list(main.main())
        self.assertTrue(set(i[0] for i in things) < set((1,2)))
