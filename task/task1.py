# Rotate a list to the right by k steps.

# Input: [1, 2, 3, 4, 5], k=2
# Output: [4, 5, 1, 2, 3]

k=3
data = [1,2,3,4,5]

length = len(data)
k = k % length # k =2 2 % 5  k =2 k>len
x = data[-k:] + data[:-k] # -k: 4,5 :-k 1,2,3

print(x)
