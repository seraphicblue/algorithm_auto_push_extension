# 문제 : range-sum-of-bst
# 결과 : Accepted / 속도: 115ms / 메모리 : 24.51MB
# 제출시각 : 24-01-13  17:25:43
# Definition for a binary tree node.

# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right

        

class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:

            return 0 #회귀를 멈출 전제 조건

        sum = 0

        if low <= root.val <= high:  # 현재 노드 값이 범위 내에 있으면 합에 추가

            sum += root.val    



        if low<root.val : #low보다 왼쪽을 탐색

            sum += self.rangeSumBST(root.left, low ,high) #root의 왼쪽 검사 low과 root val이 같아질때까지

        

        if root.val<high: #high보다  오른쪽을 탐색 

            sum += self.rangeSumBST(root.right, low ,high) 

            #root의 오른쪽 검사 high과 root val이 같아질때까지



        return sum



                      
