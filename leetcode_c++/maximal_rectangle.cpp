#include<iostream> 
#include<vector> 
#include<stack>

class Solution{
public: 
    int maximalRectangle(vector<vector<char> > &matrix){
        if (matrix.size() == 0 || matrix[0].size() == 0){
            return 0;
        }

        int ans = 0;
        vector<int> heights(matrix[0].size(), 0);
        for(int i = 0; i < matrix.size(); i++){
            for(int j = 0; j < matrix[0].size(); j++){
                heights[j] = ((matrix[i][j] == '0') ?  0:heights[j] + 1);
            }
            ans = max(ans, largestRectangleArea(heights));
        }
        return ans;
    }

private: 
    int largestRectangleArea(vector<int> &heights){
        stack<int> s;
        int ans = 0;
        heights.push_back(0); // 在最后加入0，保证都出栈
        for (int i =0; i < heights.size(); i++){
            while(!s.empty() and heights[s.top()] > heights[i]){ // 如果当前比较高，则一直要出栈到比他小
                int h_left = heights[s.top()]; // 得到对应位置
                s.pop(); 
                int area = h_left * (s.empty()? i : (i - s.top() - 1));
                ans = max(ans, area);
            }
            s.push(i); //压入的是height对应的位置
        }
        return ans;
    }
};


class Solution2 {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0){
            return 0;
        }

        int ans = 0;
        int m = matrix[0].size();
        int n = matrix.size();
        vector<int> height(m, 0); //保存当前行对应列能到达的最大高度
        vector<int> left(m, 0);
        vector<int> right(m, m);

        for(int i = 0; i < n; i++){
            int cur_left = 0;
            int cur_right = m; //最后计算是[left, right)
            for(int j = 0; j < m; j ++){
                height[j] = (matrix[i][j] == '0' ? 0 : height[j] + 1);
            }
            for(int j = 0; j < m; j ++){
            //     left[j] = (matrix[i][j] == '1'? max(left[j], cur_left):0); // 考虑left[j-1]>cur_left的情况
            //     cur_left = (matrix[i][j] == '1'? cur_left: j+ 1); // 如果等于0，则cur_left = j+1
            // }
                if (matrix[i][j] == '1'){
                    left[j] = max(left[j], cur_left);
                } else {
                    left[j] = 0;
                    cur_left = j+1; // 如果当前位置是'0'，则cur_left就为当前位置的右侧，cur_right就为当前位置（因为左闭右开）
                }
            }
            for(int j = m-1; j >= 0; j--){
                if (matrix[i][j] == '1'){
                    right[j] = min(right[j], cur_right);
                } else {
                    right[j] = m;
                    cur_right = j;
                }
            }

            for(int j=0; j < m; j++){
                ans = max(ans, (right[j] - left[j]) * height[j]);
            }
        }
        return ans;
    }
};