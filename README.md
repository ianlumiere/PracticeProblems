# PracticeProblems
A repo to hold my answers to practice problems.

# CTCI Notes

# 7 Steps
1. Listen Carefully (use all details, they may be helpful, like if the array is sorted)
2. Example (large enough and avoids special cases)
3. Brute Force (do not need to code it, just figure something that works and then optimize)
4. Optimize (improve your space and time complexity, consider sorting because it is O(n log n))
5. Walk Through Your Algorithm (avoid coding too quickly, make sure you really know what you want)
6. Code (style matters, be consistent, use space wisely, use descriptive names)
7. Test (think about each line, use small test cases first, then think of edge cases, if there's time do big test cases)

# 3 Strategies for Solving Problems

## BUD

- Bottlenecks: eliminate bottlenecks to speed things up by changing your design
- Unnecessary Work: think about the common prefix problem where the longest common prefix can only be as long as the
shortest word, so no need to look at letters beyond that length.
- Duplicated Work: avoid doing the same thing more than once.

## Space Time Tradeoffs

Usually means using a different data structure (typically a dictionary) to save time. So even though it may take up
more space, the time complexity may be much better with a dictionary.

## DIY

Given an actual example, the way your brain will solve it is actually pretty optimal. Think about how you would ideally
do it, like the common prefix problem where you would want to stack all the words and then identify when the letters do
not match and stop.

# Big O
O(1)   O(log n)   O(n)   O(n log n)   O(n^2)   O(2^n)   O(n!)

- If you have multiple steps in your algo, you + those steps
- The fastest sort is merge sort at O(n log n)
- Each nested loop that iterates through the same thing adds to the exponent, so a nested for loop that iterates through the same array is O(n^2)
- You drop constants in big O, so O(2n) is really O(n)
- If you have different inputs, then use different variables to represent them. So if you iterate through array A and have a nested iteration through array B, the complexity is actually O(A*B), NOT O(A^2)
- Drop non dominant terms, so if you have one step that is O(n), and another step that is O(log n), O(n) dominates O(log n), so O(n) + O(log n) gets reduced and the overall complexity is O(n)

# General Tips
Constantly think out loud, including talking about what you are not doing and why.
Be sure to test your code, not just your algorithm (this will help you catch bugs).
When nearing the end of a test, make sure everything compiles and write notes if you
cannot finish in time. Do not let it auto submit!
