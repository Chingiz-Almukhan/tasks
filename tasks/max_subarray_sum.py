def max_subarray_sum(numbers: list) -> int:
    max_ending_here = max_so_far = numbers[0]

    for i in range(1, len(numbers)):
        max_ending_here = max(numbers[i], max_ending_here + numbers[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


number_list = [1, -2, 3, 4, -5, 6]
print("Max subarray sum:", max_subarray_sum(number_list))
