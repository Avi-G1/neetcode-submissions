class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        seenWords = {}
        for word in strs:


            pushed = False
            for key in seenWords:
                if Counter(key) == Counter(word):
                    seenWords[key].append(word)
                    pushed = True
                    
            if not pushed:
                seenWords[word] = [word]

        

        for key in seenWords:
            output.append(seenWords[key])

        return output