from rss_parse.utils.collection_utils import group_by, merge_by_key


def test_group_by_no_key():
    actual = group_by([1, 1, 2, 3, 2])
    assert actual == dict([(1, [1] * 2), (2, [2] * 2), (3, [3])]).items()


def test_group_by_modifying_key():
    actual = group_by([1, 1, 2, 3, 2], key=lambda x: x // 2)
    assert actual == dict([(0, [1, 1]), (1, [2, 3, 2])]).items()


def test_group_by_field():
    def a_b(a, b):
        return {"a": a, "b": b}

    actual = group_by([a_b(1, 2), a_b(2, 3), a_b(2, "a"), a_b("c", 3)], key=lambda x: x["a"])
    assert actual == dict([(1, [a_b(1, 2)]), (2, [a_b(2, 3), a_b(2, "a")]), ("c", [a_b("c", 3)])]).items()


def test_merge_by_key_distinct():
    actual = merge_by_key([1, 1, 1, 2, 3, 2])
    assert actual == [1, 2, 3]


def test_merge_by_key_modifying_key():
    actual = merge_by_key([1, 1, 1, 2, 3, 2, 3, 4], lambda x: x // 2)
    assert actual == [1, 3, 4]


def test_merge_by_key_field():
    def a_b(a, b):
        return {"a": a, "b": b}

    actual = merge_by_key([a_b(1, 2), a_b(1, 3), a_b(1, 4), a_b(2, 3), a_b(3, 2)], key=lambda x: x["a"])
    assert actual == [a_b(1, 4), a_b(2, 3), a_b(3, 2)]
