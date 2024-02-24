import io
import unittest.mock
import exercise_math


class MyTestCase(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_math(self, mock_stdout):
        exercise_math.math()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "64")  # suma
        self.assertEqual(results[1], "50")  # resta
        self.assertEqual(results[2], "399")  # add assertion here
        self.assertEqual(results[3], "32.0")  # add assertion here
        self.assertEqual(results[4], "8")  # add assertion here
        self.assertEqual(results[5], "1")  # add assertion here
        self.assertEqual(results[6], "8.142857142857142")  # add assertion here


if __name__ == '__main__':
    unittest.main()
