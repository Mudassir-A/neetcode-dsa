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

    int hashset(vector<int>& nums) { 
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        for(int num: numSet){
            if(numSet.find(num - 1) == numSet.end()) {
                int length = 1;
                while(numSet.find(num + length) != numSet.end())
                    length++;
                longest = max(longest, length);
            }
        }
        return longest;
    }

    int longestConsecutive(vector<int>& nums) { 
        // return bruteforce(nums); 
        // return sorting(nums); 
        return hashset(nums); 
    }
};
