

#=============================Leetcode question=======================

#===Q:Given an array nums of unique elements  , return all posiible subsets(the power set).

# def solve(nums , index , output , ans):
#   #Base case
#   if index >= len(nums):
#     ans.append(output[:])
#     return
  
#   solve(nums , index + 1 , output , ans)

#   element = nums[index]
#   output.append(element)
#   solve(nums,index + 1,output,ans)
#   output.pop()

# def powerSet(nums):
#   ans = []
#   output = []
#   index = 0
#   solve(nums , index , output , ans)
#   return ans

# array_set = [1,2,3]
# print(powerSet(array_set))


#=============================Leetcode question=======================

#===Q:You are given a string str containing lowercase english letters from a to z inclusive.Your task is to find all non-empty possible subsequences of str

# def solve(string , output , ans , index):
#   if (index >= len(string)):
#     if(len(output) > 0):
#       ans.append(output)
#     return    
    
#  #Call for excluding case
#   solve(string , output , ans , index + 1)
  
#   #Call for including case
#   element = string[index]
#   output+=element
#   solve(string , output , ans , index + 1)

# def possibleSubsequences(string):
#   ans = []
#   output = ""
#   index = 0
#   solve(string , output , ans , index)
#   return ans


# string = "abc"
# print(possibleSubsequences(string))

