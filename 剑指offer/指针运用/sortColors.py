class Solution:
    def sortColors(self, colors):
        n = len(colors)
        if n <= 1:
            return colors

        left = 0 # 指向左边第一个不为0的位置，方便交换
        right = n - 1 # 指向右边算起第一个不为2的位置

        i = 0

        while i <= right:

            if colors[i] == 0:
                colors[i] = colors[left]
                colors[left] = 0
                left += 1

            if colors[i] == 2:
                colors[i] = colors[right]
                colors[right] = 2
                right -= 1
                i -= 1 #(因为之后会统一i+1，这时不确定colors[right]是否为0，i不移位)

            i += 1

        return colors

if __name__ == '__main__':
    print(Solution().sortColors([2,0,1,1,0,2]))
