from main import count_and_sum


def test_sum_and_count():
    list_int = [-1, -5, 2, 4]

    obj_sum_and_count = count_and_sum(list_int)

    assert (obj_sum_and_count['count'] == 2
            and obj_sum_and_count['summary'] == 6)
