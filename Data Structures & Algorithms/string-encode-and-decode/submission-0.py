class Solution:

    # we want to replace \ with \\
    # but in python \ is an escape character 
    # so \ is written as \\ and \\ is written is \\\\
    # \l is our delim
    def encode(self, strs: List[str]) -> str:
        output = ''
        for i in range(len(strs)):
            s = strs[i]
            output += s.replace("\\", "\\\\") + "\\l"
        return output

    def decode(self, s: str) -> List[str]:
        res = []
        cur = ''
        i = 0
        while i < len(s):
            if s[i] == '\\':
                if s[i + 1] == '\\':
                    cur += '\\'
                else:
                    res.append(cur)
                    cur = ''
                i += 2
            else:
                cur += s[i]
                i += 1
        return res