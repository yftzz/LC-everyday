# This is the folder to keep track of the progress upon leetcode problems.

Ideally, he will do this on a regular basis, and write the programming problems in `python`, `java`, ~~and `c++`(even though he hasn't known anything about `c++` yet.)~~ (I love python).

## Number of questions done in each category.

| Category | Array | String | Tree | DP  | DFS/BFS | Linked List | Binary Search | Sliding Window | Divide and Conquer | Graph | Misc | Design | Backtracking | Union and Find |
| -------- | ----- | ------ | ---- | --- | ------- | ----------- | ------------- | -------------- | ------------------ | ----- | ---- | ------ | ------------ | -------------- |
| Number   | 14    | 20     | 2    | 5   | 11      | 8           | 4             | 1              | 1                  |       | 1    | 2      | 2            | 3              |

| Legend | Description           |
| ------ | --------------------- |
| \*     | Looked up solution    |
| p      | Passed                |
| ?      | Solved with struggles |

### Array

| Name                                                                                                                          | Status | Description                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Two Sum](https://leetcode.com/problems/two-sum/)                                                                             | ??     | a bit memory complexity tradeoff for much more time complexity                                                                                                                  |
| [Remove Duplicates from Sorted Array](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/) | ?pp    | Only make amendment on the referenced data, keep an eye on index when deleting element                                                                                          |
| [Best Time to Buy and Sell Stock](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/)     | ppp    | Focus only on "gradient"                                                                                                                                                        |
| [Rotate Array](https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/)                        | p\*p   | List can be "added up" by sub list with same added up length                                                                                                                    |
| [Merge Sorted Array](https://leetcode.com/explore/featured/card/top-interview-questions-easy/96/sorting-and-searching/587/)   | \*pp   | go backward to avoid losing array values                                                                                                                                        |
| [First Bad Version](https://leetcode.com/explore/featured/card/top-interview-questions-easy/96/sorting-and-searching/774/)    | ?pp    | take care of the returned inx in the end                                                                                                                                        |
| [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)                                     | \*\*   | Binary search on two sorted list, should make your mind clear on the edge of two sublists.                                                                                      |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)                                         | ?p     | silly proof                                                                                                                                                                     |
| [Three Sum](https://leetcode.com/problems/3sum/)                                                                              | \*?    | O(n^2 + nlogn), two pointers on left and right                                                                                                                                  |
| [First Missing Positive](https://leetcode.com/problems/first-missing-positive/)                                               | \*p    | Brilliant idea of using the very same array, adding length to element, and check with mod, to record the state change                                                           |
| [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)                                                     | \*p    | 木桶原理: The amount of water kept always corresponds to the lower side (consider induction: if there is a bar higher than curr, then we always use the height of the curr bar) |
| [Jump Game](https://leetcode.com/problems/jump-game/)                                                                         | pp     | Going forward or backward, keep track of the longest distance you can reach                                                                                                     |
| [Merge Intervals](https://leetcode.com/problems/merge-intervals/)                                                             | pp     | ezpz                                                                                                                                                                            |
| [Campus Bikes](https://leetcode.com/problems/campus-bikes/)                                                                   | \*\*   | No smart solutions, O(n) running time, O(n) space, just traverse and store distance                                                                                             |

### String

| Name                                                                                                                            | Status | Description                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------- |
| [Reverse String](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/)                     | ppp    | ezpz                                                                                                                   |
| [Reverse Integer](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/)                    | pp?    | max(1, x) to avoid zero division, // to avoid float type                                                               |
| [First Unique Character in a String](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/) | ???    | search only lowercase ascii to reduce time and space                                                                   |
| [Valid Anagram](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/)                      | ?pp    | you can compare list by values directly, but make sure their order is matached. Can also compare with ascii lowercase  |
| [Valid Palindrome](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/)                   | \*p    | better to know more about string attributes                                                                            |
| [String to Integer (atoi)](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/)           | ?pp    | RegEx is all you need.                                                                                                 |
| [Implement strStr()](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/)                 | ppp    | be aware of the starting index of string you are comparing                                                             |
| [Count and Say](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/886/)                      | ppp    | Count number of elemenets in a row                                                                                     |
| [Longest Common Prefix](https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/)              | ppp    | haixing                                                                                                                |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | p?     | hai xing                                                                                                               |
| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)                                   | ??     | about O(n^2)                                                                                                           |
| [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)                   | pp     | ezpz silly char stitching                                                                                              |
| [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)                                                     | p\*    | like in 302, recursion with base cases and digit representation of stack                                               |
| [Next Permutation](https://leetcode.com/problems/next-permutation/)                                                             | \*\*   | Traverse in reverse order, since the sequence u r looking for is always at the end, be aware of how next perm comes up |
| [Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)                                           | ?p     | Keep in mind the properties of valid parans: if a pair is matched, then all parens inside are matched.                 |
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/)                                                                 | ?p     | Tuple is hashable for key of dict                                                                                      |
| [License Key Formatting](https://leetcode.com/problems/license-key-formatting/)                                                 | pp     | re zhen kuai                                                                                                           |
| [Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/)                               | pp     | inverted list with indices in dict                                                                                     |
| [Shortest Way to Form String](https://leetcode.com/problems/shortest-way-to-form-string/)                                       | ?p     | inverted list with indices in dict, if not match then u r at end of list                                               |
| [Most Common Word](https://leetcode.com/problems/most-common-word/)                                                             | ?p     | counter and re would help                                                                                              |

### Tree

| Name                                                                                                                                 | Status | Description                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------ | ------ | ----------------------------------------------------------------------------------- |
| [Maximum Depth of Binary Tree](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/)               | pp     | ezpz                                                                                |
| [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)                                                    | \*p    | The largest length always happens in two childs of a node                           |
| [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)                                                              | pp     | No comment                                                                          |
| [Validate Binary Search Tree](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/)                | \*p    | make it clear of the idea about lower bound and upper bound in a binary search tree |
| [Symmetric Tree](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/)                             | \*p    | you can actually use helper function upon recursively iterating over trees          |
| [Binary Tree Level Order Traversal](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/)          | pp     | typycal bfs                                                                         |
| [Convert Sorted Array to Binary Search Tree](https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/) | \*p    | recursive matters. recursively build instances                                      |

### DP

| Name                                                                                                                                   | Status | Description                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------ | ---------------------------------------------------------------------------------- |
| [Climbing Stairs](https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/569/)                 | \*p    | Using array to keep values computed already, or do ti as 'bottom-up'               |
| [Best Time to Buy and Sell Stock](https://leetcode.com/explore/featured/card/top-interview-questions-easy/97/dynamic-programming/572/) | \*p    | Only care about the min value and current                                          |
| [Maximum Subarray](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/)               | \*p    | kanade algo, own:TLE, be aware of edge case                                        |
| [House Robber](https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/)                   | \*p    | Fibonacci sequence                                                                 |
| [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)                                              | \*     | Matching table and forward propagation                                             |
| [Unique Paths](https://leetcode.com/problems/unique-paths/)                                                                            | \*p    | Iteration always faster than recursionn, also we could use 1-D array for this prob |

### DFS/BFS

| Name                                                                    | Status | Description                                                                                   |
| ----------------------------------------------------------------------- | ------ | --------------------------------------------------------------------------------------------- |
| [Evaluate Division](https://leetcode.com/problems/evaluate-division/)   | p?     | Graph building and path checking                                                              |
| [Number of Islands](https://leetcode.com/problems/number-of-islands/)   | ?p     | Best solution is the first one you come up with                                               |
| [The Maze I](https://leetcode.com/problems/the-maze/)                   | p      | both dfs and bfs work, dfs faster. Both recursion and iteration work, with similar complexity |
| [The Maze II](https://leetcode.com/problems/the-maze-ii/)               | p      | uniform cost search, heapq function much faster than queue                                    |
| [The Maze III](https://leetcode.com/problems/the-maze-iii/)             | \*     | use dict to save and compare the lexicalgraphical order                                       |
| [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | ?      | pair of dict and dfs on nodes that have no father node                                        |

### Linked List

| Name                                                                                                                             | Status | Description                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Delete Node](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/)                      | p      | ezpz, but dont get confused with reference and value                                                                                                                                                                                                                                       |
| [Remove Nth Node From End of List](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/) | \*     | Recursion is best for data structure like this where one refs to another, even though we have only the reference to the node, we can modify its inner private var by dot operator. By visiting nodes one by one and reset its reference everytime, we can achieve what we want in between. |
| [Reverse Linked List](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/)              | \*     | use multiple pointer(or reference) upon recursion or iteration                                                                                                                                                                                                                             |
| [Merge Two Sorted Lists](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/)           | \*     | recursion matters in linked list                                                                                                                                                                                                                                                           |
| [Palindrome Linked List](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/)           | \*     | fast and slow pointer, be brave                                                                                                                                                                                                                                                            |
| [Linked List Cycle](https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/)                | p      | fast and slow pointer, you've seen this before and you know it                                                                                                                                                                                                                             |
| [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)                                                                | ?      | Dont be afraid of creating new objects, and in-place modification is not always the best solution.                                                                                                                                                                                         |
| [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)                                                      | \*     | use fancy data structure to save time on lookup                                                                                                                                                                                                                                            |

### Binary Search

| Name                                                                                                                                              | Status | Description                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----------------------------------------------------------------------------------- |
| [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)                                                   | p      | Do one more check on the boundary                                                   |
| [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | p      | boring, not really binary search                                                    |
| [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)                                                                 | \*     | Binary search on allowed largest sum in all subarrays or stupid dp with memoization |
| [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)                                                 | ?      | heap, or quick select                                                               |

### Design

| Name                                                            | Status | Description                                                                                               |
| --------------------------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------- |
| [LRU Cache](https://leetcode.com/problems/lru-cache/)           | \*     | Doubly linked list or ordered dict to track last recent one                                               |
| [My Calendar II](https://leetcode.com/problems/my-calendar-ii/) | \*     | To check interval overlap, one inverval cannot be to to right of both start and end of the other interval |

## Back Tracking

| Name                                                              | Status | Description                                                     |
| ----------------------------------------------------------------- | ------ | --------------------------------------------------------------- |
| [Combination Sum](https://leetcode.com/problems/combination-sum/) | \*     | save progress in recursive function vars as in 302              |
| [Permutations](https://leetcode.com/problems/permutations/)       | p      | Can do either in backtracking or in recursive calls in like 302 |

### Sliding Window

| Name                                                                          | Status | Description                                                                                                                         |
| ----------------------------------------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | \*\*   | Oberserve that subarray of k occurs if the difference between the cum sum at end of the subarray and start of the subarray equals k |

### Union and Find

| Name                                                                                | Status | Description                      |
| ----------------------------------------------------------------------------------- | ------ | -------------------------------- |
| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |        |                                  |
| [Sentense Smilarity I](https://leetcode.com/problems/sentence-similarity/)          | ?      | Use dict as doubly linked list   |
| [Sentense Smilarity II](https://leetcode.com/problems/sentence-similarity-ii/)      | ?      | Standard union and find approach |

### Divide and Conquer

| Name                                                                                  | Status | Description                                                                            |
| ------------------------------------------------------------------------------------- | ------ | -------------------------------------------------------------------------------------- |
| [Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/) | ?      | The property of complete binary tree and "binary": one child is full or both are full. |

### Graph

| Name | Status | Description |
| ---- | ------ | ----------- |
|      |        |             |

### Misc

| Name                                                                            | Status | Description                                                                                                 |
| ------------------------------------------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------- |
| [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/) | \*     | Store the seen indices while only the last vertex of a rect is valid by checking if we have seen the others |

**_Click on the pic to learn more about my life xD_**

<a href="https://www.leetcode.com"><img src="https://github.com/yftzz/LC-everyday/blob/master/my_life.jpeg"/></a>
