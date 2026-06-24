class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        begind=0
        lastind=n-1
        while begind<n:
            sum=numbers[begind]+numbers[lastind]
            if sum==target:
                return[begind+1,lastind+1]
            elif sum<target:
                begind+=1
            else:
                lastind-=1