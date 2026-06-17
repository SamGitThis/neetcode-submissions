class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def test(i, l):
            if l[i] == target:
                return True
            elif l[i] > target:
                return 'l'
            else:
                return 'r'

        ma = -1
        for m in range(len(matrix)):
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                ma = m
                li = matrix[m]
                break
        
        if ma == -1:
            return False
        
        l, h = 0, len(li) - 1

        while l <= h:
            mid = (l+h) // 2
            print(l, h, mid)
            t = test(mid, li)

            if t is True:
                return True
            elif t == 'l':
                h = mid-1
            else:
                l = mid+1
        return False
