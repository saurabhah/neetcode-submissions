class Solution {

    hasDuplicate(nums) {
    const numset = new Set();
    let len = nums.length
   
    for (let i = 0; i < len; i++){
        
        if(numset.has(nums[i])){
            return true
        }
        numset.add(nums[i])
    }
    return false
    }
}
