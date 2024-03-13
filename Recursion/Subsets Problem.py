
#===Q:Given an array nums of unique elements  , return all posiible subsets(the power set).

def solve(nums , index , output , ans):
  #Base case
  if index >= len(nums):
    ans.append(output[:])
    return
  
  solve(nums , index + 1 , output , ans)

  element = nums[index]
  output.append(element)
  solve(nums,index + 1,output,ans)
  output.pop()

def powerSet(nums):
  ans = []
  output = []
  index = 0
  solve(nums , index , output , ans)
  return ans

array_set = [1,2,3]
print(powerSet(array_set))
