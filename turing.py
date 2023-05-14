def solution(k: [int]) -> int:

    # Count the frequency of each integer in the array
    freq = {}
    for num in k:
        freq[num] = freq.get(num, 0) + 1
    weight = max(freq.values())

    # Initialize variables
    left = 0
    freq_window = {}
    min_len = len(k) + 1

    # Iterate over the array
    for right in range(len(k)):
        # Increment frequency of current integer in the window
        freq_window[k[right]] = freq_window.get(k[right], 0) + 1

        # Shrink the window if the frequency of the current integer exceeds the weight
        while freq_window[k[right]] > weight:
            freq_window[k[left]] -= 1
            left += 1

        # Update smallest subarray length found so far if the frequency of the current integer is equal to the weight
        if freq_window[k[right]] == weight:
            min_len = min(min_len, right - left + 1)

    return min_len
print(solution([1, 2, 2, 3, 1]))