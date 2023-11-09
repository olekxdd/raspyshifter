s = "abcabcbb"
# s = "bbbbb"
list = []
list_buffer = []

for i in range(len(s)):
    list.append(s[i])
print(list)

for j in list:
    letter = list[list.index(j)]
    list_buffer.append(letter)
    print(list_buffer)
    list.pop(list.index(letter))
    print(list)
    # list.pop(list.index(j))

    # list_buffer.append(poped)
    # print(list)
    # print(list_buffer)
    # for k in list_buffer:
    #     if k in list and list_buffer:
    #         print(len(list_buffer))









# for i in range(len(s)):
#     list.append(s[i])
#     for j in list:
#         poped = list.pop(list.index(j))
#         list_buffer.append(poped)
#         print(list_buffer)
#         print(list)
#         for k in list_buffer:
#             if k in list and list_buffer:
#                 print(len(list_buffer))