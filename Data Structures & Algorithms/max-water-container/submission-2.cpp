class Solution {
public:
    int bruteforce(vector<int>& height) {
        int maxAmount = INT_MIN;
        for (int i = 0; i < height.size() - 1; i++) {
            for (int j = i + 1; j < height.size(); j++) {
                maxAmount = max(maxAmount, min(height[i], height[j]) * (j - i));
            }
        }
        return maxAmount;
    }

    int optimal(vector<int>& height) {
        int l = 0, r = height.size() - 1;
        int res = INT_MIN;

        while (l < r) {
            int area = (r - l) * min(height[l], height[r]);
            res = max(area, res);
            if (height[l] <= height[r])
                l++;
            else
                r--;
        }

        return res;
    }

    int maxArea(vector<int>& height) {
        // return bruteforce(height);
        return optimal(height);
    }
};