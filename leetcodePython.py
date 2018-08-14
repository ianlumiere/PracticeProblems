# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Example 1:

# Given nums = [3,2,2,3], val = 3,

# Your function should return length = 2, with the first two elements of nums being 2.

# It doesn't matter what you leave beyond the returned length.
# Example 2:

# Given nums = [0,1,2,2,3,0,4,2], val = 2,

# Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

# Note that the order of those five elements can be arbitrary.

# It doesn't matter what values are set beyond the returned length.
# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

# Internally you can think of this:

# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);

# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = (value for value in nums if value != val)

        return len(nums)


# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

 



# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maximumWater = 0
        currentWater = 0
        
        for i in range(0, len(height)):
            for k in range(i+1, len(height)):
                if height[i] <= height[k]:
                    currentWater = height[i] * (k-i)
                else:
                    currentWater = height[k] * (k-i)
                if currentWater > maximumWater:
                    maximumWater = currentWater
                        
        return maximumWater #NOTE THIS TAKES TOO LONG IN PYTHON, BUT NOT C++

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """        
        temp = l3 = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            
            l3 = l3.next

        l3.next = l1 or l2
            
        return temp.next


# In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

# At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

# What is the maximum total sum that the height of the buildings can be increased?

# Example:
# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation: 
# The grid is:
# [ [3, 0, 8, 4], 
#   [2, 4, 5, 7],
#   [9, 2, 6, 3],
#   [0, 3, 1, 0] ]

# The skyline viewed from top or bottom is: [9, 4, 8, 7]
# The skyline viewed from left or right is: [8, 7, 9, 3]

# The grid after increasing the height of buildings without affecting skylines is:

# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]

# Notes:

# 1 < grid.length = grid[0].length <= 50.
# All heights grid[i][j] are in the range [0, 100].
# All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        numRow = len(grid)
        numCol = len(grid[0])
        
        verticleView = []
        horizontalView = []
        
        # Initialize the arrays
        for i in range(0, numRow):
            horizontalView.append(0)
            
        for i in range(0, numCol):
            verticleView.append(0)
        
        # Get the view for verticle and horizontal
        for i in range(0, numRow):
            for k in range(0, numCol):
                if grid[i][k] > horizontalView[i]:
                    horizontalView[i] = grid[i][k]
                
                if grid[i][k] > verticleView[k]:
                    verticleView[k] = grid[i][k]
        
        sum = 0
        
        # Sum how much height can be added
        for i in range(0, numRow):
            for k in range(0, numCol):
                # Get the smaller of the two max numbers and sum it if the difference
                # is greater than 0
                if verticleView[k] < horizontalView[i]:
                    if verticleView[k] - grid[i][k] > 0:
                        sum += verticleView[k] - grid[i][k]
                else:
                    if horizontalView[i] - grid[i][k] > 0:
                        sum += horizontalView[i] - grid[i][k]
        
        return sum
                    
# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

class Solution:
    def toLowerCase(self, str):
        """
            :type str: str
            :rtype: str
            """
        # can be done just by doing:
        # return str.lower()
        lowercaseStr = ""
        
        for i in range(0, len(str)):
            if ord(str[i]) > 64 and ord(str[i]) < 91:
                lowercaseStr += chr(ord(str[i]) + 32)
            else:
                lowercaseStr += str[i]
        
        return lowercaseStr


# You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:

# Input: J = "z", S = "ZZ"
# Output: 0
# Note:

# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # One line solution:
        # return sum([S.count(j) for j in J])

        totalFound = 0
        
        for i in range(0, len(J)):
            for k in range(0, len(S)):
                if J[i] == S[k]:
                    totalFound += 1
        
        return totalFound  # O(nm)

# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example 1:

# Input: 2
# Output: [0,1,1]
# Example 2:

# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:

# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # One liner:
        # return [(bin(n).split('0b'))[1].count('1') for n in range(num+1)]

        # Solution using bitwise operators: https://wiki.python.org/moin/BitwiseOperators
        # num+=1
        # bit_counts = [0]*num
        # for i in range(1, num):
        #     bit_counts[i] = bit_counts[i>>1] + (i&1)
        # return bit_counts

        answer = []
        
        # Run the operation on each number up to num (inclusive)
        for i in range(0, num+1):
            # Get the binary of the number as a string
            currentBinary = str(bin(i))
            
            # Add the sum of the 1 count in the binary string to the
            # answer array
            answer.append(sum([currentBinary.count('1')]))
                    
        return answer  # Likely O(n*m)

# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

# Example:

# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []
        
        for i in range (1, n+1):
            if i % 5 == 0 and i % 3 == 0:
                results.append('FizzBuzz')
            elif i % 3 == 0:
                results.append('Fizz')
            elif i % 5 == 0:
                results.append('Buzz')
            else:
                results.append(str(i))
        
        return results


