"""
Python version 3.7.0
1.7 - Rotate Matrix
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate
the image by 90 degrees.  Can you do this in place?
"""
import unittest
from typing import List


def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Rotate matrix will rotate the given matrix by 90 degrees.
    Runtime: O(N^2), asymptotic runtime depends on N
    Space Complexity: O(N^2), creating a new matrix of NxN called 'rotated'
    :param matrix: an NxN matrix
    :param N: the size of the matrix (NxN)
    :return: a newly rotated matrix
    """
    N = len(matrix)
    rotated = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            rotated[j][(N-1)-i] = matrix[i][j]
    return rotated


def _perform_full_rotation(matrix: List[List[int]], row: int, col: int, M: int):
    """
    Helper function that performs four 90 degree rotations starting at row, col.
    at a particular row and column from the matrix, there will be 4 rotations.
    visually, the algorithm looks like this:
    [start] (4th swap with original 3rd) - - - - - - - - - - - - - - - - - - -> (1st gets swapped with start)
                |                                                                       |
                |                                                                       |
                |                                                                       |
                |                                                                       |
    (3rd swap with original 2nd) < - - - - - - - - - - - - - - - - - - - - - -  (2nd gets swapped with original 1st)
    this results in a full rotation in-place of a particular row and col coordinate.
    :param matrix: an MxM sub-matrix out of an NxN matrix
    :param row: starting row
    :param col: starting column
    :param M: size of sub-matrix
    :return:
    """
    num_rotations = 4
    start_row = row
    rotated_row = row
    rotated_col = col
    temp_new = matrix[row][col]
    for _ in range(0, num_rotations):
        # compute new rotated indices
        # (start_row * 2) is an offset to account for reduced M into sub-matrices of matrix
        rotated_col, rotated_row = M - 1 - rotated_row + (start_row * 2), rotated_col
        # store value at newly computed indices
        temp_new, matrix[rotated_row][rotated_col] = matrix[rotated_row][rotated_col], temp_new


def rotate_matrix_in_place(matrix: List[List[int]]) -> List[List[int]]:
    """
    Does the same as rotate_matrix, but in place.
    Runtime: O(N^2), asymptotic runtime depends on N. We make N^2 swaps.
    Space Complexity: O(1), constant amount of temp variables that does not depend on N.
    :param matrix: an NxN matrix
    :return: the input matrix, but rotated
    """
    N = len(matrix)
    # outer loop will keep reducing the matrix size 'n' by 2.
    # For example, a 6x6 matrix contains a 4x4 sub-matrix, we reduce
    # because at first, the values on the perimeter of the matrix will
    # be rotated after the inner for-loop, and we want to start rotating
    # the next sub-matrix perimeter.
    for start_row, n in enumerate(range(N, 1, -2)):
        # rotate along the current row's columns of the current sub-matrix perimeter
        for col in range(start_row, n - 1 + start_row):
            # performs 4 rotations for the current sub-matrix coordinate
            _perform_full_rotation(matrix, start_row, col, n)
    return matrix


class TestRotateMatrixFunction(unittest.TestCase):

    def setUp(self):
        self.cases = [
            (
                [
                    [1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12],
                    [13, 14, 15, 16]
                ],
                [
                    [13, 9, 5, 1],
                    [14, 10, 6, 2],
                    [15, 11, 7, 3],
                    [16, 12, 8, 4]
                ]
            ),
            (
                [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ],
                [
                    [7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]
                ]
            ),
            (
                [
                    [1]
                ],
                [
                    [1]
                ]
            ),
            (
                [
                    [1, 2, 3, 4, 5, 6],
                    [7, 8, 9, 10, 11, 12],
                    [13, 14, 15, 16, 17, 18],
                    [19, 20, 21, 22, 23, 24],
                    [25, 26, 27, 28, 29, 30],
                    [31, 32, 33, 34, 35, 36]
                ],
                [
                    [31, 25, 19, 13, 7, 1],
                    [32, 26, 20, 14, 8, 2],
                    [33, 27, 21, 15, 9, 3],
                    [34, 28, 22, 16, 10, 4],
                    [35, 29, 23, 17, 11, 5],
                    [36, 30, 24, 18, 12, 6]
                ]
            ),
            (
                [
                    [1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25]
                ],
                [
                    [21, 16, 11, 6, 1],
                    [22, 17, 12, 7, 2],
                    [23, 18, 13, 8, 3],
                    [24, 19, 14, 9, 4],
                    [25, 20, 15, 10, 5]
                ]
            ),
            (
                [
                    [1, 2, 3, 4, 5, 6, 7],
                    [8, 9, 10, 11, 12, 13, 14],
                    [15, 16, 17, 18, 19, 20, 21],
                    [22, 23, 24, 25, 26, 27, 28],
                    [29, 30, 31, 32, 33, 34, 35],
                    [36, 37, 38, 39, 40, 41, 42],
                    [43, 44, 45, 46, 47, 48, 49]
                ],
                [
                    [43, 36, 29, 22, 15, 8, 1],
                    [44, 37, 30, 23, 16, 9, 2],
                    [45, 38, 31, 24, 17, 10, 3],
                    [46, 39, 32, 25, 18, 11, 4],
                    [47, 40, 33, 26, 19, 12, 5],
                    [48, 41, 34, 27, 20, 13, 6],
                    [49, 42, 35, 28, 21, 14, 7]
                ]
            )
        ]

    def test_rotate_matrix(self):
        for matrix, expected in self.cases:
            self.assertEqual(rotate_matrix(matrix), expected, msg=(matrix, expected))

    def test_rotate_matrix_in_place(self):
        for matrix, expected in self.cases:
            self.assertEqual(rotate_matrix_in_place(matrix), expected, msg=(matrix, expected))


if __name__ == '__main__':
    unittest.main()
