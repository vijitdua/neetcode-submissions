class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_frequency_map: Dict[int, int] = dict()
        for num in nums:
            if not num in number_frequency_map:
                number_frequency_map[num] = 0
            number_frequency_map[num] += 1
        sorted_frequency_maps = sorted(number_frequency_map, key=number_frequency_map.get, reverse=True)
        result: List[int] = []
        for i in range(k):
            result.append(sorted_frequency_maps[i])
        return result
        