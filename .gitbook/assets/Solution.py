# 二叉树节点定义
import queue
from collections import deque


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


class Solution:
    @staticmethod
    def doInsert(root: TreeNode):
        node_val = [14, -1, 10, 19, 31, 42]
        for i in node_val:
            root.insert(i)

    def preOrderTraversal(root: TreeNode) -> list[int]:
        res = []

        def traversal(root: TreeNode):
            if root is None:
                return
            res.append(root.value)
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return res

    def inOrderTraversal(root: TreeNode) -> list[int]:
        res = []

        def traversal(root: TreeNode):
            if root is None:
                return

            traversal(root.left)
            res.append(root.value)
            traversal(root.right)

        traversal(root)
        return res

    def postOrderTraversal(root: TreeNode) -> list[int]:
        res = []

        def traversal(root: TreeNode):
            if root is None:
                return

            traversal(root.left)
            traversal(root.right)
            res.append(root.value)

        traversal(root)
        return res

    '''
Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False，Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]])获取队列，timeout等待时间
Queue.get_nowait() 相当于Queue.get(False)，非阻塞方法
Queue.put(item) 写入队列，timeout等待时间
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号。每个get()调用得到一个任务，接下来task_done()调用告诉队列该任务已经处理完毕。
Queue.join() 实际上意味着等到队列为空，再执行别的操作
    '''

    @staticmethod
    def bfs(root: TreeNode):
        q = deque()
        ress = []
        if root is not None:
            q.append(root)
        else:
            return ress
        while q:
            res = []
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                res.append(cur.value)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ress.append(res)
        return ress

    @staticmethod
    def invertTree(root: TreeNode) -> TreeNode:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        Solution.invertTree(root.left)
        Solution.invertTree(root.right)
        return root

    @staticmethod
    def levelOrderBottom(root: TreeNode):
        stack = deque()
        q = deque()
        results = []
        if root:
            q.append(root)
        else:
            return results
        while q:
            res = []
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                res.append(cur.value)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            stack.appendleft(res)
        while stack:
            tmp = stack.popleft()
            results.append(tmp)
        return results
