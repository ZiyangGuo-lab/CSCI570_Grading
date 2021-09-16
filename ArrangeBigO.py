from bisect import bisect_left

def lengthOfLIS(nums):
    sub = []
    for num in nums:
        i = bisect_left(sub, num)

        # If num is greater than any element in sub
        if i == len(sub):
            sub.append(num)

        # Otherwise, replace the first element in sub greater than or equal to num
        else:
            sub[i] = num
    return len(sub)

def mindelete(nums):
    return len(nums)-lengthOfLIS(nums)

def grade(student_input, answers, penalty, maxloss):
    minimum = float('inf')
    for answer in answers:
        dict = {}
        for i,a in enumerate(answer):
            dict[a] = i
        nums = []
        for input in student_input:
            nums.append(dict[input])
        minimum = min(minimum, mindelete(nums))
    return -1*(minimum * penalty if minimum * penalty < maxloss else maxloss)


# Examples: 
# correct answers can be dhifacjbeg or dhfacjibeg

print("Student with answer abcdefhgji loses points:",grade('abcdefhgji', ['dhifacjbeg','dhfacjibeg'], 2, 10))
print("Student with answer dhjfacibeg loses points:",grade('dhjfacibeg', ['dhifacjbeg','dhfacjibeg'], 2, 10))
print("Student with answer dhfacjibeg loses points:",grade('dhfacjibeg', ['dhifacjbeg','dhfacjibeg'], 2, 10))