# 문제 : sort-colors
# 결과 : Accepted / 속도: 38ms / 메모리 : 17.46MB
# 제출시각 : 24-01-17  15:54:14
def sortColors(self, nums):

    nums[:] = [0]*nums.count(0) + [1]*nums.count(1) + [2]*nums.count(2)
