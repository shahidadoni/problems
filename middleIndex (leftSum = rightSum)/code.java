class Solution {
    public int findMiddleIndex(int[] nums) {
        int[] prefixSum = new int[nums.length];
        
        prefixSum[0] = nums[0];
        
        for(int i=1;i<nums.length;i++){
            prefixSum[i] = prefixSum[i-1] + nums[i];
        }
        
        int left,right;
        
        for(int i=0;i<nums.length;i++){
            if(i==0){
                left = 0;
            }else{
                left = prefixSum[i-1];
            }
            
            if(i==nums.length-1){
                right = 0;
            }else{
                right = prefixSum[nums.length-1] - prefixSum[i];
            }
            
            if(right == left){
                return i;
            }
        }
        
        return -1;
    }
}