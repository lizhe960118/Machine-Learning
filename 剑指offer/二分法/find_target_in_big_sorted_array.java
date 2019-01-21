public class Solution{
    public int searchBigSortedArray(ArrayReader reader, int target){
        int index = 1;
        
        // 使用自定义的index来判断二分结束的位置
        while(reader.get(index - 1) < target){
            index *= 2
        }

        int start = 0, end = index - 1;
        while(start + 1 < end){
            int mid = start + (end - start) / 2
            if(reader.get(mid) < target){
                start = mid;
            } else {
                end = mid;
            }
        }

        if (reader.get(start) == target){
            return start;
        }

        if (reader.get(end) == target){
            return end;
        }

        return -1;
    }
}