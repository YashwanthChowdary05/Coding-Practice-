def find_subarray(arr, target):
    left = 0
    current_sum = 0
    n = len(arr)

    for right in range(n):
        current_sum += arr[right]

        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1

        if current_sum == target:
            return [left + 1, right + 1]

    return [-1]

arr = [1, 2, 3, 7, 5]
target = 12
result = find_subarray(arr, target)
print(result)
