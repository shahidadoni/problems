/**
 * @param {number[]} nums
 * @return {number}
 */
 var findMiddleIndex = function(nums) {
    let prefix_sum = [nums]
    prefix_sum[0]= nums[0]
    
    for(let i=1;i<nums.length;i++){
        prefix_sum[i] = prefix_sum[i-1]+nums[i]
    }
    
    let left,right
    
    for(let i=0;i<nums.length;i++){
        if(i===0){
            left = 0
        }else{
            left = prefix_sum[i-1]
        }
        
        if(i===nums.length-1){
            right=0
        }else{
            right=prefix_sum[nums.length-1]-prefix_sum[i]
        }
        
        if (left===right){
            return i
        }
    }
    
    return -1
};