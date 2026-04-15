def count_common_elements(*lists):
    sets = [set(lst) for lst in lists ]

    common_elements = set.intersection(*sets)
    return len(common_elements)