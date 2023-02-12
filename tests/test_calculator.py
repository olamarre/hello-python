from hello.calculator import add, add_lists
import numpy as np

import pytest


def test_add():
    assert add(3, 5) == 8
    with pytest.raises(Exception):
        add([1, 2, 3], 4)


def test_add_lists():
    assert add([1, 1, 1], [2, 2, 2]) == [3, 3, 3]

    # for numpy arrays, need to use:
    np.testing.assert_allclose(add_lists([1, 1, 1], [2, 2, 2]), np.array([3, 3, 3]))

    with pytest.raises(Exception):
        add_lists([1, 2, 3], 4)


if __name__ == "__main__":
    # test_add()
    test_add_lists()
