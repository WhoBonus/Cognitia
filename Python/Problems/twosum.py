#Give an an array of numbers and a target sum, check if that array has any 2 indices that add up to to the target sum
#if it exists, return those 2 indices

class TwoSum:
    def findIndices(self, nums: list[int], target: int):
        #Iterate in double for loop
        for i in range(len(nums)):
            currNum = nums[i]
            remainder = target - currNum
            #2nd loop look for matching value
            for j in range(i + 1, len(nums)):
                if nums[j] == remainder:
                    #if found return pair
                    #print(f"The indices are: {i} and {j}")
                    return [i, j]
        
        return [-1, -1] # Return -1, -1 if no pair
    
    def findIndicesWithMap(self, nums: list[int], target: int):
        #create dictionary to store numbers passed
        map = {}

        #Loop through the numbers and see if a matching number exists in dictionary
        #if it doesnt exist add it to the map with the cuurentInex
        #if it exists, return the position of the index with map[remainder], and currIndex for found pair
        currIndex = 0
        for currNumber in nums:
            remainder = target - currNumber
            if remainder in map:
                return [map[remainder], currIndex]
            map[currNumber] = currIndex
            currIndex+=1
        
        """
        #enumerate tracks the index 
        #i is the iterator index, n is number
        for index, currNumber in enumerate(nums):
            remainder = target - currNumber
            if remainder in map:
                #return as list format [index of stored num, index of current num]
                return [map[remainder], index]
            else: 
                #Save number n at position i
                #map[key] = value, looks for a label n, if it doesnt exist creates it and sticks i inside the label
                #java map.put(n, i)
                map[currNumber] = index # n is number key and i is the value which is the index 
        """
        

        return [-1, -1]

    def findIndicesIfSorted(self, nums: list[int], target: int):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            currSum= nums[left] + nums[right]
            
            #Check first pair
            if currSum == target:
                return [left, right]
            elif currSum < target:
                #Need a larger sum
                left += 1
            else:
                #Need a smaller sum
                right -= 1
                
        return [-1, -1] #No pair found
        
#test the methods
if __name__ == "__main__":
    solver = TwoSum()
    
    #sample
    my_numbers = [1, 2, 3, 4]
    my_target = 100
    
    #brute force
    result = solver.findIndices(my_numbers, my_target)
    if result == [-1, -1]:
        print("No pair adds up to the target.")
    else:
        print(f"The Brute Force indices are: {result}")

    #map impl
    result = solver.findIndicesWithMap(my_numbers, my_target)
    if result == [-1, -1]:
        print("No pair adds up to the target.")
    else:
        print(f"The MAP indices are: {result}")

    #if sorted
    result = solver.findIndicesIfSorted(my_numbers, my_target)
    if result == [-1, -1]:
        print("No pair adds up to the target.")
    else:
        print(f"The ifSorted indices are: {result}")
    
    
    