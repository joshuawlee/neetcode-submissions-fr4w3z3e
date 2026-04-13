class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int, vector<int>> maxHeap;

        for (int stone : stones) {
            maxHeap.push(stone);
        }

        while (maxHeap.size() > 1) {
            int val1 = maxHeap.top();
            maxHeap.pop();
            int val2 = maxHeap.top();
            maxHeap.pop();

            if (val1 > val2) {
                maxHeap.push(val1 - val2);
            }
        }

        maxHeap.push(0);
        return maxHeap.top();
    }
};
