class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # 异常判断
        if A is None:
            return B 
        if B is None:
            return A 
            
        # 假设 A很大，B很小
        point_a = len(A) - 1
        
        for i in range(len(B)):
            # 先拓展B个数
            A.append(0)
            
        # 小数组插到大数组
        point_b = len(B) - 1 
        cur_point = point_a + point_b + 1 
        
        while(point_b >= 0 and point_a >= 0):
            if B[point_b] > A[point_a]:
                A[cur_point] = B[point_b]
                point_b -= 1 
                cur_point -= 1 
            else:
                A[cur_point] = A[point_a]
                point_a -= 1 
                cur_point -= 1 
        
        while(point_b >= 0):
            A[cur_point] = B[point_b]
            point_b -= 1 
            cur_point -= 1 
        
        return A
                
        
        
