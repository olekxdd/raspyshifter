#height = [1,8,6,2,5,4,8,3,7]
height =[4,3,2,1,4]
#height  = [1, 1]
volume_list = []
# for x, y in enumerate(height):
#     for i in height:
#         volume = ((y - (y % y)) * x-(x % len(height)))
#         volume_list.append(abs(volume))
#
#         print(max(volume_list))

left = 0
right = len(height) - 1
maxArea = 0

while left < right:
    currentArea = min(height[left], height[right]) * (right - left)
    maxArea = max(maxArea, currentArea)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

print(maxArea)



# print(max(list(enumerate(height))))
# print(min(list(enumerate(height))))
# print(list((enumerate(height))))