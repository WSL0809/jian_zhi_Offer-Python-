---
description: 难度：简单
---

# 剑指 Offer 39. 数组中出现次数超过一半的数字

### 题目

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

`示例 1:输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]`&#x20;

`输出: 2`

### 题解

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

```

### 小技巧

[Python max()方法扩展：求字典中值最大的键](https://www.cnblogs.com/QianyuQian/p/13667965.html)
