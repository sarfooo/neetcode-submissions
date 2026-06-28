class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matrix = []

        while (len(strs) > 0):
            strings = []

            for potential_string in strs:
                if len(potential_string) == len(strs[0]):
                    strings.append(potential_string)
            
            chars = []
            occurences = {}

            for string in strings:
                occurences[string] = {}
                string_chars = occurences[string]

                for char in string:
                    if char not in string_chars:
                        string_chars[char] = 1
                        chars.append(char)
                    else:
                        string_chars[char] += 1

                occurences[string] = string_chars

            done = []
            for i in range(len(strings)):
                anagrams = []
                if strings[i] not in done:
                    done.append(strings[i])
                    anagrams.append(strings[i])

                    for j in range(len(strings)):
                        if i != j and occurences[strings[i]] == occurences[strings[j]]:
                            anagrams.append(strings[j])
                            done.append(strings[j])

                    if len(anagrams) > 0:
                        matrix.append(anagrams)
                    else:
                        matrix.append([strings[i]])

            for string in strings:
                strs.remove(string)

        return matrix