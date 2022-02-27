from vectors import Vector
from unittest import TestCase
from io import StringIO
from unittest.mock import patch


class PrintingTest(TestCase):

    def test_no_vector(self):
        self.assertRaises(ValueError, Vector, [[1, 2], [3, 4]])

    def test_sum_error_vector_row(self):
        self.assertRaises(ValueError, Vector.__add__, Vector([1,2,3]), Vector([2,3]))

    def test_sum_error_vector_row_column(self):
        self.assertRaises(ValueError, Vector.__add__, Vector([1,2,3]), Vector([[2],[3],[4]]))

    def test_sum_error_vector_column(self):
        self.assertRaises(ValueError, Vector.__add__, Vector([[1],[3]]), Vector([[2],[3],[4]]))

    def test_sum_vector_row(self):
        v1 = Vector([1, 2, 3, 4])
        v2 = Vector([5, 6, 7, 8])
        expected_output = Vector([6, 8, 10, 12])
        self.assertEqual(v1 + v2, expected_output)

    def test_sum_vector_row_len1(self):
        v1 = Vector([1])
        v2 = Vector([5])
        expected_output = Vector([6])
        self.assertEqual(v1 + v2, expected_output)

    def test_sum_vector_len0(self):
        v1 = Vector([])
        v2 = Vector([])
        expected_output = Vector([])
        self.assertEqual(v1 + v2, expected_output)

    def test_sum_vector_column(self):
        v1 = Vector([[1], [2], [3], [4]])
        v2 = Vector([[5], [6], [7], [8]])
        expected_output = Vector([[6], [8], [10], [12]])
        self.assertEqual(v1 + v2, expected_output)

    def test_sum_vector_column_len1(self):
        v1 = Vector([[1]])
        v2 = Vector([[5]])
        expected_output = Vector([[6]])
        self.assertEqual(v1 + v2, expected_output)

    def test_sum_vector_row_int(self):
        v1 = Vector([1, 2, 3, 4])
        v2 = 1
        expected_output = Vector([2, 3, 4, 5])
        self.assertEqual(v1 + v2, expected_output)

    def test_sum_vector_row_len1_int(self):
        v1 = Vector([1])
        v2 = 1
        expected_output = Vector([2])
        self.assertEqual(v1 + v2, expected_output)

    def test_sum_vector_len0_int(self):
        v1 = Vector([])
        v2 = 1
        expected_output = Vector([])
        self.assertEqual(v1 + v2, expected_output)

    def test_sum_vector_column_int(self):
        v1 = Vector([[1], [2], [3], [4]])
        v2 = 2
        expected_output = Vector([[3], [4], [5], [6]])
        self.assertEqual(v1 + v2, expected_output)

    def test_sum_vector_column_len1_int(self):
        v1 = Vector([[1]])
        v2 = 2
        expected_output = Vector([[3]])
        self.assertEqual(v1 + v2, expected_output)

    def test_sub_error_vector_row(self):
        self.assertRaises(ValueError, Vector.__sub__, Vector([1,2,3]), Vector([2,3]))

    def test_sub_error_vector_row_column(self):
        self.assertRaises(ValueError, Vector.__sub__, Vector([1,2,3]), Vector([[2],[3],[4]]))

    def test_sub_error_vector_column(self):
        self.assertRaises(ValueError, Vector.__sub__, Vector([[1],[3]]), Vector([[2],[3],[4]]))

    def test_sub_vector_row(self):
        v1 = Vector([1, 2, 3, 4])
        v2 = Vector([5, 6, 7, 8])
        expected_output = Vector([4, 4, 4, 4])
        self.assertEqual(v2 - v1, expected_output)

    def test_sub_vector_row_len1(self):
        v1 = Vector([1])
        v2 = Vector([5])
        expected_output = Vector([4])
        self.assertEqual(v2 - v1, expected_output)

    def test_sub_vector_len0(self):
        v1 = Vector([])
        v2 = Vector([])
        expected_output = Vector([])
        self.assertEqual(v2 - v1, expected_output)

    def test_sub_vector_column(self):
        v1 = Vector([[1], [2], [3], [4]])
        v2 = Vector([[5], [6], [7], [8]])
        expected_output = Vector([[4], [4], [4], [4]])
        self.assertEqual(v2 - v1, expected_output)

    def test_sub_vector_column_len1(self):
        v1 = Vector([[1]])
        v2 = Vector([[5]])
        expected_output = Vector([[4]])
        self.assertEqual(v2 - v1, expected_output)

    def test_sub_vector_row_int(self):
        v1 = Vector([1, 2, 3, 4])
        v2 = 1
        expected_output = Vector([0, 1, 2, 3])
        self.assertEqual(v1 - v2, expected_output)

    def test_sub_vector_row_len1_int(self):
        v1 = Vector([1])
        v2 = 1
        expected_output = Vector([0])
        self.assertEqual(v1 - v2, expected_output)

    def test_sub_vector_len0_int(self):
        v1 = Vector([])
        v2 = 1
        expected_output = Vector([])
        self.assertEqual(v1 - v2, expected_output)

    def test_sub_vector_column_int(self):
        v1 = Vector([[1], [2], [3], [4]])
        v2 = 2
        expected_output = Vector([[-1], [0], [1], [2]])
        self.assertEqual(v1 - v2, expected_output)

    def test_sub_vector_column_len1_int(self):
        v1 = Vector([[1]])
        v2 = 2
        expected_output = Vector([[-1]])
        self.assertEqual(v1 - v2, expected_output)

    def test_dot_error_vector_row(self):
        self.assertRaises(ValueError, Vector.__mod__, Vector([1,2,3]), Vector([2,3]))

    def test_dot_error_vector_row_column(self):
        self.assertRaises(ValueError, Vector.__mod__, Vector([1,2,3]), Vector([[2],[3],[4]]))

    def test_dot_error_vector_column(self):
        self.assertRaises(ValueError, Vector.__mod__, Vector([[1],[3]]), Vector([[2],[3],[4]]))

    def test_dot_vector_row(self):
        v1 = Vector([1, 2, 3, 4])
        v2 = Vector([5, 6, 7, 8])
        result = v1 % v2
        expected_output = 70
        self.assertEqual(result, expected_output)

    def test_dot_vector_row_len1(self):
        v1 = Vector([1])
        v2 = Vector([5])
        result = v1 % v2
        expected_output = 5
        self.assertEqual(result, expected_output)

    def test_dot_vector_len0(self):
        v1 = Vector([])
        v2 = Vector([])
        result = v1 % v2
        expected_output = 0
        self.assertEqual(result, expected_output)

    def test_dot_vector_column(self):
        v1 = Vector([[1], [2], [3], [4]])
        v2 = Vector([[5], [6], [7], [8]])
        result = v1 % v2
        expected_output = 70
        self.assertEqual(result, expected_output)

    def test_dot_vector_column_len1(self):
        v1 = Vector([[1]])
        v2 = Vector([[5]])
        result = v1 % v2
        expected_output = 5
        self.assertEqual(result, expected_output)

    def test_dot_vector_row_int(self):
        v1 = Vector([1, 2, 3, 4])
        v2 = 2
        result = v1 % v2
        expected_output = 20
        self.assertEqual(result, expected_output)

    def test_dot_vector_row_len1_int(self):
        v1 = Vector([1])
        v2 = 2
        result = v1 % v2
        expected_output = 2
        self.assertEqual(result, expected_output)

    def test_dot_vector_len0_int(self):
        v1 = Vector([])
        v2 = 1
        result = v1 % v2
        expected_output = 0
        self.assertEqual(result, expected_output)

    def test_dot_vector_column_int(self):
        v1 = Vector([[1], [2], [3], [4]])
        v2 = 2
        result = v1 % v2
        expected_output = 20
        self.assertEqual(result, expected_output)

    def test_dot_vector_column_len1_int(self):
        v1 = Vector([[1]])
        v2 = 2
        result = v1 % v2
        expected_output = 2
        self.assertEqual(result, expected_output)

    def test_cross_error_vector_row(self):
        self.assertRaises(ValueError, Vector.__mul__, Vector([1,2,3]), Vector([2,3]))

    def test_cross_error_vector_row_column(self):
        self.assertRaises(ValueError, Vector.__mul__, Vector([1,2,3]), Vector([[2],[3],[4]]))

    def test_cross_error_vector_column(self):
        self.assertRaises(ValueError, Vector.__mul__, Vector([[1],[3]]), Vector([[2],[3],[4]]))

    def test_cross_error_vector_column_row_not3(self):
        self.assertRaises(ValueError, Vector.__mul__, Vector([[1],[3]]), Vector([[2],[3]]))

    def test_cross_vector_row(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([5, 6, 7])
        expected_output = Vector([-4, 8, -4])
        self.assertEqual(v1 * v2, expected_output)

    def test_cross_vector_column(self):
        v1 = Vector([[1], [2], [3]])
        v2 = Vector([[5], [6], [7]])
        expected_output = Vector([[-4], [8], [-4]])
        self.assertEqual(v1 * v2, expected_output)

    def test_cross_vector_row_int(self):
        v1 = Vector([1, 2, 3])
        v2 = 3
        expected_output = Vector([-3, 6, -3])
        self.assertEqual(v1 * v2, expected_output)

    def test_cross_vector_row_int(self):
        v1 = Vector([[1], [2], [3]])
        v2 = 3
        expected_output = Vector([[-3], [6], [-3]])
        self.assertEqual(v1 * v2, expected_output)
