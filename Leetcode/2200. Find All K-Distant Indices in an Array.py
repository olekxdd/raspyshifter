import math

nums = [3, 4, 9, 1, 3, 9, 5]
key = 9
k = 1


# print(list(enumerate(nums)))
# for every index of the key nums[j]
# you have to check if the distance abs(i - j) is in the constraints 1 <= distance <= len(nums) and nums[j] == key
list = []
for j, e in enumerate(nums):
    if e == key:
        for i in range(len(nums)):
            distance = abs(i - j)
            if 1 <= k <= len(nums) and nums[j] == key:
                list.append(distance)

print(sorted(list))

# distance = abs(i - j)
# if 1 <= distance <= len(nums) and nums[j] == key:




















# def func_k_distances(nums):
#     list = []
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if j == key:
#                 distance = abs(i - j)
#                 if 1 <= distance <= len(nums) and nums[j] == key:
#                     list.append(distance)
#     print(sorted(list))




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
