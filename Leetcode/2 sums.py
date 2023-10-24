# nums_array = [2, 7, 11, 15]
# target = 9

nums = [3, 2, 4]
target = 6

# nums_array = [3, 3]
# target = 6

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target and i != j:

            print(f"[{i},{j}]")


# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if (i != j and nums[i] + nums[j] == target):
#             print(i,j)

# for i in nums_array:
#     n = 0
#     for b in nums_array[n:]:
#         n += 1
#         if i + b == target:
#             print(f"[{nums_array.index(i)},{nums_array.index(b)}]")
#     nums_array[nums_array.index(i)] = 0


# for i, b in nums_array, nums_array[1:]:
#     if i + b == target and nums_array.index(i) != nums_array.index(b):
#         print(f"[{nums_array.index(i)},{nums_array.index(b)}]")

















# for i in nums_array:
#     for b in nums_array:
#         if b + i == target and nums_array[nums_array.index(i)] is not nums_array[nums_array.index(b)]:
#             print(f"[{nums_array.index(i)},{nums_array.index(b)}]")
#     nums_array[nums_array.index(i)] = 0
