class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        def getBulls(secret, guess):
            result = 0
            i = 0
            while i < (len(secret)):
                ## if there is a correct gues
                if secret[i] == guess[i]:
                    ## add one to bulls
                    result += 1
                    ## remove the character 
                    secret = secret[0:i] + secret[i+1:]
                    guess = guess[0:i] + guess[i+1:]
                ## in case of a wrong guess, just update the counter
                else:
                    i += 1

            return result, secret, guess

        def getCows(modified_s, modified_g):
            result = 0
            ## create a dictionary for both s and g
            s_map = Counter(modified_s)
            g_map = Counter(modified_g)

            for key in g_map:
                ## add the minimum count found in whether secret or guess
                result += min(s_map.get(key, 0), g_map[key])
            return result

        bull, modified_s, modified_g = getBulls(secret, guess)
        cow = getCows(modified_s, modified_g)
        return f"{bull}A{cow}B"