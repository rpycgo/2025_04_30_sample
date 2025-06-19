import unittest


class TestExample(unittest.TestCase):
    def test_fail(self):
        self.assertEqual(1, 2, "This test is expected to fail for demonstration purposes.")


if __name__ == '__main__':
    unittest.main()
