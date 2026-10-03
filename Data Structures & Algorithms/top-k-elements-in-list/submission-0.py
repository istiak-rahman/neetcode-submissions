class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        result = []
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        
        sorted_dict = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)
        # my_dict.items() returns list of tuples (k-v pairs)
        for i in range(k):
            result.append(sorted_dict[i][0])
        return result
