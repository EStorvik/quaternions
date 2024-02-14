import numpy as np


from multiply_and_rotate_quaternions import multiply_quaternion, normalize, conjugate, rotation_quaternion, rotate

from multiply_and_rotate_complex import from_polar, multiply_complex, rotate as rotate_complex



def quaternion_to_mat(q):
    a, b, c, d = q
    return np.array([[a+ b*1j, c+ d*1j], [-c +d*1j, a -b*1j]])

def mat_to_quaternion(A):
    a = A[0, 0].real
    b = A[0, 0].imag
    c = A[0, 1].real
    d = A[0, 1].imag
    return np.array([a, b, c, d])

q1 = np.array([3, 2.5, 8, 4])
q2 = np.array([5, 6, 100, 8])

a = quaternion_to_mat(multiply_quaternion(q1, q2))
b = np.matmul(quaternion_to_mat(q1),quaternion_to_mat(q2))

print(a-b)
