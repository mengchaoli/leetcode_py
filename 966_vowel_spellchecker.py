class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        lowers = {}
        wildcards = {}
        vowels = "aeiouAEIOU"

        for word in wordlist:
            if word.lower() not in lowers:
                lowers[word.lower()] = word
            
            wildcard = "".join(char.lower() if char not in vowels else "*" for char in word)
            if wildcard not in wildcards:
                wildcards[wildcard] = word
            
        res = []
        for q in queries:
            if q in wordlist:
                res.append(q)
            elif q.lower() in lowers:
                res.append(lowers[q.lower()])
            elif "".join(char.lower() if char not in vowels else "*" for char in q) in wildcards:
                res.append(wildcards["".join(char.lower() if char not in vowels else "*" for char in q)])
            else:
                res.append("")

        return res
            