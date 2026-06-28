class Solution {
    public boolean hasDuplicate(int[] nums) {
        Object[] found = new Object[nums.length];
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j <= i; j++) {
                if (found[j] != null && (int) found[j] == nums[i]) {
                    return true;
                } else if (j == i) {
                    found[j] = nums[i];
                }
            }
        }        
        return false;
    }
}
