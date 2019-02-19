import math


def count_sq(a, b, c, x):
    """
    a == b
    Counts the area of square by triangle ares
    """
    p = (a + b + c) / 2
    s_of_big_tr = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    h = 2 * s_of_big_tr / c
    h_of_top_tr = h - x
    s_of_top_tr = 0.5 * x * h_of_top_tr
    s_of_lower_triangles = 0.5 * x * (c - x)
    res = s_of_big_tr - s_of_top_tr - s_of_lower_triangles
    return res


def bin(a, b, c, acc):
    """
    Binary finds x
    """
    min_val = 0
    max_val = c
    max_iter = int(math.log((c / acc), 2)) + 1
    for i in range(max_iter):
        current_value = (min_val + max_val) / 2
        cur_area = count_sq(a, b, c, current_value)
        if (current_value + acc)**2 < cur_area:
            min_val = current_value
        elif (current_value - acc)**2 > cur_area:
            max_val = current_value
        else:
            return current_value


if __name__ == "__main__":
    nums = input("Enter triangles sides: ").split()
    while len(nums) != 3:
        nums = input("Triangle should have 3 sides").split()
    while True:
        try:
            for i in range(len(nums)):
                nums[i] = int(nums[i])
            break
        except:
            nums = input("Enter sides again!: ").split()

    acc = float(input("Enter accuracy: "))

    while acc != float(acc):
        acc = input("Accuracy should be float")
    nums.append(acc)
    a = nums[0]
    b = nums[1]
    c = nums[2]
    acc = nums[3]
    print("Result is\t", bin(a, b, c, acc))