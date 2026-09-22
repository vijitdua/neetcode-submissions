class Solution:
    
    def build_frequency_maps(self, word) -> dict[str,int]:
        frequency_map: dict[str,int] = {}
        for letter in word:
            frequency_map[letter] = frequency_map.get(letter, 0) + 1
        return frequency_map

    def isAnagram(self, s: str, t: str) -> bool:
        return self.build_frequency_maps(s) == self.build_frequency_maps(t)
