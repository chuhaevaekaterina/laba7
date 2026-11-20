def two_sum_sorted(lst, target):
    left = 0
    right = len(lst) - 1

    while left < right:
        total = lst[left] + lst[right]

        if total == target:
            return (left, right)
        elif total < target:
            left += 1
        else:
            right -= 1

    return None
print(two_sum_sorted([1, 2, 3, 4, 6], 6))