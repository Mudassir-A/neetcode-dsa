class Solution {
   public:
    int bruteforce(vector<int>& nums) {
        int res = 0;
        unordered_set<int> store(nums.begin(), nums.end());

        for (int num : nums) {
            int streak = 0, curr = num;
            while (store.find(curr) != store.end()) {
                streak++;
                curr++;
            }
            res = max(res, streak);
        }
        return res;
    }

    int sorting(vector<int>& nums) { 
        if(nums.empty()) return 0;
        sort(nums.begin(), nums.end());

        int res = 0, curr = nums[0], streak = 0, i = 0;

        while(i < nums.size()) {
            if(curr != nums[i]){
                curr = nums[i];
                streak = 0;
            }
            while(i < nums.size() && nums[i] == curr) {
                i++;
            }
            streak++;
            curr++;
            res = max(res, streak);
        }
        return res;
    }

    int longestConsecutive(vector<int>& nums) { 
        // return bruteforce(nums); 
        return sorting(nums); 
    }
};
