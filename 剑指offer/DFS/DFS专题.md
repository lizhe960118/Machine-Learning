# DFS（Depth First Search)
找到所有的方案的题，排列或者组合  
从某个节点一直往下搜索，直到没有可以搜索的点则返回

## 组合（Combination）
### 子集（递归实现（Recursion））
- subSets.py 
### 给定目标数，求数组和为target的组合
- CombinationSum.py (一个数可以使用多次)
- CombinationSumII.py (每个答案中同一个数只能使用一次)
### 回文串划分（划分某个字符串为回文子串，输出所有答案）
- PalindromePartition.py 

## 排列（Permutation）
### 给定数组，求数组中数的所有排列
- permutations.py
### 给定带有重复元素的数组，求所有不同的排列（去重问题）
- permutationsII.py
### N皇后问题（同一行，同一列，同一对角线不能出现重复）
- NQueens.py

## 图中的搜索
### 单词阶梯(给出两个单词start，end和一个字典，找出start变换到end的最短序列，每次变换只改变一个字母)
- wordLadder.py
- wordLadderII.py (找出所有的最短变换序列）