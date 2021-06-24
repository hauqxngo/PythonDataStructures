def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = 0
    num = nums[0]

    for n in nums:
        most_common_num = nums.count(n)
        if (most_common_num > counter):
            counter = most_common_num
            num = n 
    return num
