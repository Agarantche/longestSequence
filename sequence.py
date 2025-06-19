class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)  # Store all numbers in a set for O(1) lookups
        longest_sequence = 0

        for num in nums:
            # Check if 'num' is the start of a sequence
            # A number is the start of a sequence if num-1 is NOT in the set
            if (num - 1) not in numSet:
                current_num = num
                current_sequence = 1

                # Keep extending the sequence as long as the next number exists in the set
                while (current_num + 1) in numSet:
                    current_num += 1
                    current_sequence += 1

                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence
