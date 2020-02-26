def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]> nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp



nums=[2,7,21,75,1]
print("unsorted list:\n",nums)
sort(nums)
print("sorted list using Bubble sort\n",nums)