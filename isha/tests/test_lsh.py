from isha.backend.lsh import LocalitySentitiveHashing


def test_lsh():
    lsh = LocalitySentitiveHashing([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 3)
    assert lsh.query([1, 2, 3]) == {0}
    assert lsh.query([4, 5, 6]) == {1}
    assert lsh.query([7, 8, 9]) == {2}
    assert lsh.query([1, 2, 3, 4]) == set()
    assert lsh.query([1, 2, 3]) == {0}
    assert lsh.query([4, 5, 6]) == {1}
    assert lsh.query([7, 8, 9]) == {2}
