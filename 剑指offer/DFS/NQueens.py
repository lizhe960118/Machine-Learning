class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        result = []
        if n <= 0:
            return result
            
        path = []
        self.dfsHelper(n, path, result)
        # print(result)
        res = self.draw_board(n, result)
        return res
        
    def dfsHelper(self, n, path, result):
        # 出口
        if len(path) == n:
            result.append(path.copy())
            return
        
        #当前path有多少行
        row = len(path)
        
        # 递归
        for col in range(n):
            # 先判断能不能放进去，再递归
            if not self.is_valid(row, col, path):
                continue
            path.append(col)
            self.dfsHelper(n, path, result)
            path.pop()
        return 
            
    def is_valid(self, row, col, path):
        # 之前放的是(r,c)，现在要放（row,col）
        for r, c in enumerate(path):
            # 放在同一列上
            if c == col:
                return False
            # 对角线上
            if (r - c == row - col) or (r + c == row + col):
                return False
        return True
        
    def draw_board(self, n, result):
        res = []
        for path in result:
            new_path = []
            for col in path:
                tmp = ["Q" if j == col else "." for j in range(n)]
                # print(tmp)
                str_tmp = "".join(tmp)
                new_path.append(str_tmp)
            res.append(new_path)
        return res