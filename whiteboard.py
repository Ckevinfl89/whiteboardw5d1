# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example Input: [0,0,11,2,3,4]					
# Example Output: [11,2,3,4,0,0]


# def solution(lst):
#     empty_list = []
#     while 0 in lst:
#         empty_list.append(0)
#         lst.remove(0)
#     for num in empty_list:
#         if num == 0:
#             lst.append(num)
#     return lst


def solution(nums):
   return [x for x in nums if x != 0] + [0] * nums.count(0)



def move_zeros(nums):
    if len(nums) <= 1:
        return nums
    p1, p2, = 0, 1
    while p2 < len(nums):
        if nums[p1] == 0 and nums[p2] == 0:
            p2 += 1
        elif nums[p1] == 0 and nums[p2] != 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 += 1
        elif nums[p1] != 0 and nums[p2] == 0:
            p1 += 1
            p2 += 1
        elif nums[p1] != 0 and nums[p2] != 0:
            p1 += 1
            p2 += 1
    return nums