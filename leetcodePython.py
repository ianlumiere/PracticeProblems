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


class SolutionRemoveElement:
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

class SolutionMaxArea:
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

class SolutionMergeTwoLists:
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

class SolutionMaxIncreaseKeepingSkyline:
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

class SolutionToLowerCase:
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

class SolutionNumJewelsInStones:
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

class SolutionCountBits:
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

class SolutionFizzBuzz:
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

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# Example:

# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

class SolutionAddDigits:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # One liner:
        # return (num if num == 0 else (9 if num % 9 == 0 else num % 9))
        
        while(len(str(num)) > 1):
            # This takes a number, converts it into a string
            # then iterates through the characters in the 
            # string converting them to numbers and stores
            # each number in the digits array
            digits = [int(d) for d in str(num)]
            
            # This sums all the numbers in the array
            num = sum(digits)
        
        return num

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 231.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.

class SolutionHammingDistance:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        # Convert the numbers into binary and then a string
        xBin = str(bin(x))
        yBin = str(bin(y))
        
        # Get the shorter number and call the helper
        if len(xBin) < len(yBin):
            answer = hammingHelper(xBin, yBin)
        else:
            answer = hammingHelper(yBin, xBin)
            
        return answer # O(n) where n is the larger binary number
            
def hammingHelper(shorter, longer):
    differentBits = 0

    shortTracker = len(shorter)-1
    longTracker = len(longer)-1
    
    while(longTracker > 1):
        if shortTracker > 1:
            if shorter[shortTracker] != longer[longTracker]:
                differentBits += 1
        elif longer[longTracker] == '1':
            differentBits += 1

        shortTracker -= 1
        longTracker -= 1

    return differentBits

# Write a loop that returns all of the pairs of numbers that equal the sum argument. Do it in O(n)

# data = [1,2,3,4,5,7,10]
# num = 8

# print(sumPairs(num, data))
# outputs [[3,5], [1,7]]

def sumPairs(num, data):
    # num is the sum you are looking for
    # data is the list of numbers that you are comparing
    
    checked = {}
    answers = []
    
    for i in data:
        # if the difference is in the hash, then you can make the sum, so add it to the answer pairs
        if (num - i) in checked:
            answers.append([checked[num-i], i])
        
        # Add the number to the hash if it is not already in there
        if i not in checked:
            checked[i] = i
            
    return answers

# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the transformation of a word.

# Return the number of different transformations among all words we have.

# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation: 
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."

# There are 2 different transformations, "--...-." and "--...--.".

class SolutionUniqueMorseRepresentations:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                     "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
                     "...-",".--","-..-","-.--","--.."]

        
        # create a hash for the words to store the count that they appear in
        transformations = {} # use a hash because has lookup is O(1) vs checking a whole array which is O(n)
        
        for i in words:
            # translate i to morse code
            translatedWord = ""
            
            for letter in i:
                # get the ASCII, then subtract to correspond it to the index of the array
                letterFixed = letter.upper()
                translatedWord += morseCode[ord(letterFixed)-65]
                
            # Add the word to the keys in transformations
            if translatedWord not in transformations:
                transformations[translatedWord] = 1
            else:
                transformations[translatedWord] += 1
        
        # You can also return the number of times a transformation appears
        return len(transformations) # O(nm)

    
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class SolutionReverse:
    def reverse(self, x: int) -> int:
        if x > (2**31 - 1):
            return 0
        elif x < -2**31:
            return 0
                
        # check if negative
        negative = False
        if x < 0:
            numString = str(x * -1)
            negative = True
        else:
            numString = str(x)
        
        answerString = ""
        
        # Reverse each num by iterating through once
        for i in range(0, len(numString)):
            answerString = numString[i] + answerString
        
        answer = int(answerString)
        
        # check if negative
        if negative is True:
            answer = answer * -1
        
        if answer > (2**31 - 1):
            return 0
        elif answer < -2**31:
            return 0
            
        return answer # O(n)
 
# Num Chimes

# 24 element array
def numChimes(hour1, hour2):
    # 24 element array with 0 in each slot
    hourStruck = []
    
    for i in range(0, 25):
        hourStruck.append(0)
    
    if hour2 < hour1:
        hour2 = hour2 + 24
    
    # hour1 = 23
    # hour2 = 1 + 24 = 25
    
    for i in range(hour1, hour2+1):
        if i > 24:
            hourStruck[i-24] = i-24
        else:
            if i > 12:
                hourStruck[i] = i-12
            else:
                hourStruck[i] = i        
        
    # sum hourStruck and return it
    # hoursStruck = [1:1, 23:11, 24:12] = 24
    print(hourStruck)
    return sum(hourStruck)

# check intersection 
def func(list1, list2):
    # get what numbers they have in common
    # they are not sorted
    # O(n log n) Merge sort
    # nested for loop is brute, O(n^2)
    
    # declare a new array for the intersection or remove values
        
    # look at the shorter list
    
    # list1 = [7,3,4,5,10348294]
    
    # list2 = [9,5,6,7,8]
    
    # hashA[0,0,0,0,1,2,1,0,10348294] # bad solution because of large numbers
    # hashD{7:2, 3:1, 10348294:1, 9:1} # use a dictionary instead, this is O(n)
    
    # answer[5,]
    # iterate list1 then list2 and identify keys that have value of 2
    pass
    
# Next Prime
def next_prime(n):
    i = n + 1
    prime = False
    
    while(prime is False):
        prime = True
        
        for k in range(2, i): # go to sqrt or check bigger divisors
            if i % k == 0:
                prime = False
                break
                
        if prime is True:
            answer = i
            
        i+=1
    
    return answer # next prime after n

# Output words of change due based on an input like "12.34;100.35"

import sys

def change_due():
    for line in sys.stdin:    
        inputs = line.split(";")
        pp = float(inputs[0])
        ch = float(inputs[1])
        values = [100, 50, 20, 10, 5, 2, 1, .5, .25, .1, .05, .01]
        dollars = ["ONE HUNDRED", "FIFTY", "TWENTY", "TEN", "FIVE", "TWO", "ONE", "HALF DOLLAR", "QUARTER", "DIME", "NICKEL", "PENNY"]
        outputChange = []
            
        if ch < pp:
            print("ERROR")
        
        elif ch == pp:
            print("ZERO")
        
        else:
            change = round(ch - pp, 2)
            
            count = 0
            
            for i in values:
                while (change - i) >= 0:
                    change = change - i
                    outputChange.append(dollars[count]) # Skips PENNY for some reason
                    
                count = count + 1
        
            listWords = sorted(outputChange)
            answer = ','.join(listWords)
        
            print(answer)

# Return the first word in a sentence that is the longest even word. 
# Ex: "The dog ran fast through the park" would return "fast".
# Return "00" if there are no even words

def longestEvenWord(sentence):
    sentenceList = sentence.split(" ")
    longest = 0
    found = False
    
    for i in sentenceList:
        if len(i) > longest and len(i) % 2 == 0:
            answer = i
            found = True
            longest = len(i)
    
    if found is False:
        return "00"
    else:
        return answer
   
# Employees per department

# A company stores EE and Dept info in two tables: employee and department. Write a query to print the respective department name
# and number of employees in each department (even ones with no employees). Sort the results by descending order of the number
# of employees; if two ore more are tied, sort alpgabetically by dept name.
# Each row must have the name of the department and the number of employees in it

# SELECT
#     d.name,
#     COUNT(e.id) AS num_ee
# FROM department d
# LEFT JOIN employee e on d.id = e.dept_id
# GROUP BY d.name
# ORDER BY num_ee DESC, d.name

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class SolutionRemoveDuplicates:
    # nums is a list
    def removeDuplicates(self, nums) -> int:
        lookforward_index = 1
        i = 0
        
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        while i != len(nums)-1:
            if nums[lookforward_index] == nums[i]:
                del nums[lookforward_index]
            else:
                lookforward_index = lookforward_index + 1
                i = i + 1
        
        return len(nums)


#Write a function:

#def solution(A)

#that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

#For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

#Given A = [1, 2, 3], the function should return 4.

#Given A = [−1, −3], the function should return 1.

#Write an efficient algorithm for the following assumptions:

#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [−1,000,000..1,000,000].

class SolutionReturnSmallestPositive:
    def solution(A):
        smallest = 1
        A.sort()
        
        for i in A:
            if i <= 0:
                pass
            elif i <= smallest:
                smallest = i + 1
            else:
                return smallest
        
        return smallest

#The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

# +----+-------+--------+-----------+
# | Id | Name  | Salary | ManagerId |
# +----+-------+--------+-----------+
# | 1  | Joe   | 70000  | 3         |
# | 2  | Henry | 80000  | 4         |
# | 3  | Sam   | 60000  | NULL      |
# | 4  | Max   | 90000  | NULL      |
# +----+-------+--------+-----------+
# Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

# +----------+
# | Employee |
# +----------+
# | Joe      |
# +----------+

# SELECT
#     e.name AS "Employee"  # I added the name to satisfy one of the requirements, but it is not necessary
# FROM employee e
# INNER JOIN employee m on e.managerId = m.id  # join the table on itself for all ees that have managers
# WHERE e.managerId IS NOT NULL
#     and e.salary > m.salary

