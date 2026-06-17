class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        if len(matrix) == 1 and len(matrix[0]) == 1:
            if len(matrix[0]) == 1 and matrix[0][-1] == target:
                return True
            return False

        print(33333)
        while i < len(matrix):
            if target <= matrix[i][-1]:
                break
            else:
                i += 1

        if i >= len(matrix):
            return False

        bs = matrix[i]
        
        l, r = 0, len(bs) - 1

        while l <= r:
            mid = (l+r) // 2

            if bs[mid] == target:
                return True

            elif bs[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False