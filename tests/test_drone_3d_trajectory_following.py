import conftest
from AerialNavigation.drone_3d_trajectory_following \
    import drone_3d_trajectory_following as m
import numpy as np


def test1():
    m.show_animation = False
    m.main()


def test_zyx_rotation_matrix():
    x_rot = m.rotation_matrix(np.pi, 0, 0)
    x_rot_truth = np.array([[1,  0, 0],
                            [0, -1, 0],
                            [0, 0, -1]])
    assert np.allclose(x_rot, x_rot_truth)

    y_rot = m.rotation_matrix(0, np.pi, 0)
    y_rot_truth = np.array([[-1,  0, 0],
                            [0, 1, 0],
                            [0, 0, -1]])
    assert np.allclose(y_rot, y_rot_truth)

    z_rot = m.rotation_matrix(0, 0, np.pi)
    z_rot_truth = np.array([[-1,  0, 0],
                            [0, -1, 0],
                            [0, 0, 1]])
    assert np.allclose(z_rot, z_rot_truth)


if __name__ == '__main__':
    conftest.run_this_test(__file__)
