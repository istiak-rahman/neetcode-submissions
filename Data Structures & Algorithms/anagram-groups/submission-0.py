class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}

        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in hashmap:
                hashmap[sorted_str].append(string)
            else:
                hashmap[sorted_str] = [string]

        for key in hashmap:
            result.append(hashmap[key])

        return result 