---
description: 这里我构建的是一个二叉排序树
---

# 构建二叉树

```python

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # 生成二叉排序树
    def insert(self, value):
        # 将新值与父节点进行比较
        if self.value:  # 非空
            if value < self.value:  # 新值较小，放左边
                if self.left is None:  # 若空，则新建插入节点
                    self.left = TreeNode(value)
                else:  # 否则，递归往下查找
                    self.left.insert(value)
            elif value > self.value:  # 新值较大，放右边
                if self.right is None:  # 若空，则新建插入节点
                    self.right = TreeNode(value)
                else:  # 否则，递归往下查找
                    self.right.insert(value)
        else:
            self.value = value

```
