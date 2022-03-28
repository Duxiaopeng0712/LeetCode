from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])  #分别用来获取矩阵的行数和列数
        i, j = 0, m - 1   #从右上角开始，初始化角标为0, m - 1
        while i < n and j >= 0: #因为是从右上角开始的，所以结束条件就应该是角标移动到了左下角左上角对应的是矩阵[0, m - 1]，左下角对应的是矩阵[n - 1, 0]，结束条件不能超出矩阵的范围
            if matrix[i][j] > target: #说明当前位置的数值比target大，当前位置的右边和下边肯定比target大，上面也不可能，因为如果往上走，是与上一步矛盾的，因为最开始就是从右上角开始的。因此，如果当前位置的数值比target大，则应该往左走，同样道理，如果当前位置的数值比target小，则应该往下走
                j = j - 1 #往左走，列角标-1
            elif matrix[i][j] < target:
                i += 1  #往下走，行角标-1
            else:
                return True  #找到了target，则返回true
        return False #没找到，则返回False
