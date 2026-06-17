class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []

        for i in range(0, len(temperatures)):
            maxi = None
            j = i
            n = 0
            curr = temperatures[i]

            while j in range(len(temperatures)):
                if temperatures[j] > curr:
                    maxi = temperatures[j]
                    break
                
                else:
                    j += 1
                    n += 1
            
            if maxi is None:
                output.append(0)
            
            else:
                output.append(n)

        print(output)
        return output