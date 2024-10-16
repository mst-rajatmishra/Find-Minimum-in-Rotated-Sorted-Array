class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Check which part is unsorted
            if nums[mid] > nums[right]:
                left = mid + 1  # Minimum is in the right part
            else:
                right = mid  # Minimum is in the left part (including mid)
        
        return nums[left]  # At the end of loop, left == right

# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMin([3, 4, 5, 1, 2]))  # Output: 1
    print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
    print(solution.findMin([11, 13, 15, 17]))  # Output: 11

