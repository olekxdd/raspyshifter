import math

nums = [3, 4, 9, 1, 3, 9, 5]
key = 9
k = 1


# print(list(enumerate(nums)))


def func_k_distances(nums):
    list = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if j == key:
                distance = abs(i - j)
                if 1 <= distance <= len(nums) and nums[j] == key:
                    list.append(distance)
    print(sorted(list))


func_k_distances(nums)

# def func_k_distances(nums):
#     list = []
#     for i, (j, e) in range(len(nums)), enumerate(nums):
#         if e == key:
#             index = j
#             distance = abs(i - index)
#             if 1 <= distance <= len(nums):
#                 list.append(distance)
#     print(sorted(list))
#
# func_k_distances(nums)

# def func_k_distances(nums):
#     list = []
#     for i in range(len(nums)):
#         for j, e in enumerate(nums):
#             if e == key:
#                 index = j
#                 distance = abs(i - index)
#                 if 1 <= distance <= len(nums):
#                     list.append(distance)
#     print(sorted(list))
#
#
# func_k_distances(nums)
