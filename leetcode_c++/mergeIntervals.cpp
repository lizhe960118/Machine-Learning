#include<iostream>
#include<vector>
#include<deque>

using namespace std;

struct Interval {
    int start;
    int end;
    Interval():start(0), end(0){}
    Interval(int s, int e):start(s), end(e){}
};

class Solution{
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval){
        auto it = intervals.begin();
        while(it != intervals.end() && newInterval.start > it->start) ++it;
        intervals.insert(it, newInterval); // 在合适位置插入newInterval， 方便后面排序

        // Merge intervals without sorting
        vector<Interval> ans;
        for (const auto& interval: intervals){
            if (ans.empty() || ans.back().end < interval.start){
                ans.push_back(interval);
            } else { // 当interval.start < ans.back().end, 说明有交集 (3,5)(4,6)
                ans.back().end = max(ans.back().end, interval.end);
                // ans.back().start = min(ans.back().start, interval.start); //不需要，前面按照规则插入
            }
        }

        return ans;
    }
};

class Solution2{
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval){
        int new_start = newInterval.start;
        int new_end = newInterval.end;

        deque<Interval> left;
        deque<Interval> right;

        for(const auto& interval:intervals){
            if (interval->end < new_start){
                left.push_back(interval);
            } else if (interval->start > new_end){
                right.push_front(interval);
            } else {
                new_start = min(interval.start, new_start);
                new_end = max(interval.end, new_end);
            }
        }
        
        // concat the intervals
        vector<Interval> ans;
        for(const auto& interval: left){
            ans.push_back(interval);
        }
        ans.push_back(Inteval(new_start, new_end));
        for(const auto& interval: right){
            ans.push_back(interval);
        }
        return ans;
    }
};

class Solution{
public:
    vector<vector<int> > merge(vector<vector<int>>& intervals){
        vector<vector<int> > ans;
        sort(intervals.begin(), intervals.end(), [](const vector<int> &a, const vector<int> &b){return a[0] < b[0];});

        for(const auto& interval:intervals){
            if ( ans.empty() || ans.back().back() < interval.front()) {
                ans.push_back(interval);
            } else {
                ans.back().back() = max(ans.back().back(), interval.back());
                // ans.back().front() = min(ans.back().front(), interval.front());
            }
        }
        
        return ans;

    }
};