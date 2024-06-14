nums: list[float | int] = []


def enter_results(*args):
    nums.extend(args)


def get_sum():
    return round(sum(nums[0::2]), 2), round(sum(nums[1::2]), 2)


def get_average():
    key_sum, val_sum = get_sum()
    n = len(nums) // 2
    return round(key_sum / n, 2), round(val_sum / n, 2)


if __name__ == "__main__":
    enter_results(3.5, 2.14, 45.2, 37.99)
    print(get_sum(), get_average())
    enter_results(5.2, 7.3)
    print(get_sum(), get_average())
    enter_results(1.23, 4.56, 3.14, 2.71, 0, 0)
    print(get_sum(), get_average())
