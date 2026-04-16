class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputDict = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for character in word:
                count[ord(character) - ord('a')] += 1
            
            outputDict[tuple(count)].append(word)
            
        
        return list(outputDict.values())
        
