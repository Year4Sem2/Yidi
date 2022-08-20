class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        #print("dp:{}".format(dp))
        dp.add(0)
        #print("dp after add: {}".format(dp))
        target = sum(nums) // 2
        #print("target: {}".format(target))

        for i in range(len(nums) - 1, -1, -1):
            #print("i:{}".format(i))
            nextDP = set()
            for t in dp:
                #print("t: {}".format(t))
                if (t + nums[i]) == target:
                    #print("yoyoyo")
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
                #print("nextDP: {}".format(nextDP))
            dp = nextDP
        return False
        