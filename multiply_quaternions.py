import numpy as np

def multiply(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2
    z = w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2
    return np.array([w, x, y, z])

def normalize(q):
    magnitude = np.linalg.norm(q)
    return q / magnitude

def conjugate(q):
    q_conj = q.copy()
    q_conj[1:] = -q_conj[1:]
    return q_conj

def magnitude(q):
    return np.linalg.norm(q)

q = np.array([1, 2, 3, 4])
p = normalize(q)

q_bar = conjugate(q)


v = np.array([0, 1, 0, 1])

rotate_angle = np.pi/2
rotate_vector = np.array([1, 0, 0])

def rotation_quaternion(angle, vector):
    return np.array([np.cos(angle/2), np.sin(angle/2)*vector[0], np.sin(angle/2)*vector[1], np.sin(angle/2)*vector[2]])

def rotate(v, q):
    return multiply(multiply(q, v), conjugate(q))

q_rotate = rotation_quaternion(rotate_angle, rotate_vector)

v_rotated = rotate(v, q_rotate)

print(v_rotated)