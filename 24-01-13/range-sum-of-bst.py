# 문제 : range-sum-of-bst
# 결과 : Accepted / 속도: 120ms / 메모리 : 24.36MB
# 제출시각 : 24-01-13  16:55:36
class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:

            return 0



        sum = 0

        if low <= root.val <= high:  # 현재 노드 값이 범위 내에 있으면 합에 추가

            sum += root.val



        if root.val > low:  # 왼쪽 자식 노드 탐색

            sum += self.rangeSumBST(root.left, low, high)



        if root.val < high:  # 오른쪽 자식 노드 탐색

            sum += self.rangeSumBST(root.right, low, high)



        return sum


