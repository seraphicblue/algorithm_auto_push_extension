# 문제 : search-in-a-binary-search-tree
# 결과 : Accepted / 속도: 50ms / 메모리 : 19.23MB
# 제출시각 : 24-01-15  9:2:54
class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val

        self.left = left

        self.right = right



class Solution:

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # 현재 노드가 None이면 None 반환

        if not root:

            return None



        # 찾고자 하는 값이 현재 노드의 값과 같으면 현재 노드 반환

        if root.val == val:

            return root



        # 찾고자 하는 값이 현재 노드의 값보다 작으면 왼쪽 서브트리 탐색

        if val < root.val:

            return self.searchBST(root.left, val)



        # 찾고자 하는 값이 현재 노드의 값보다 크면 오른쪽 서브트리 탐색

        if val > root.val:

            return self.searchBST(root.right, val)


