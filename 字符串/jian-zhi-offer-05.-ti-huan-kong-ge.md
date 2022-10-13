---
description: 难度：简单
---

# 剑指 Offer 05. 替换空格

题目链接：[https://leetcode.cn/problems/ti-huan-kong-ge-lcof/](https://leetcode.cn/problems/ti-huan-kong-ge-lcof/)

### 题目

请实现一个函数，把字符串 `s` 中的每个空格替换成"%20"。

```
// Example
输入：s = "We are happy."
输出："We%20are%20happy
```

### 解答

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []
        for c in s:
            if c == ' ': res.append("%20")
            else: res.append(c)
        return "".join(res)
```
