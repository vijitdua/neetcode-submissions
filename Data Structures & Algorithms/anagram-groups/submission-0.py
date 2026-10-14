class Solution:
    def build_letter_frequency_in_string_map(self, string: str) -> tuple[int]:
        frequency_by_letter_position_array = [0] * 26
        first_char_ascii = ord('a')
        for letter in string:
            frequency_by_letter_position_array[ord(letter) - first_char_ascii] += 1
        return tuple(frequency_by_letter_position_array)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequency_hash_key_to_position_map: dict[tuple, list[int]] = dict()
        for i in range(0, len(strs), 1):
            string_hash_key = self.build_letter_frequency_in_string_map(strs[i])
            if string_hash_key not in frequency_hash_key_to_position_map:
                frequency_hash_key_to_position_map[string_hash_key] = []
            frequency_hash_key_to_position_map[string_hash_key].append(i)
        result: list[list[str]] = []
        for positions in frequency_hash_key_to_position_map.values():
            same_group: list[str] = []
            for position in positions:
                same_group.append(strs[position])
            result.append(same_group)
        return result
        