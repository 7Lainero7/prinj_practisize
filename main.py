

def count_and_sum(list_int:list[int]) -> object:
    count = 0
    summary = 0

    for integer in list_int:
        if integer > 0 and integer % 2 == 0:
            count += 1
            summary += integer

    obj_wit_sum_count = {
        "count": count,
        "summary": summary
    }
    return obj_wit_sum_count
