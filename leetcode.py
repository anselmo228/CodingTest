class Solution(object):
    def nthUglyNumber(self, n):
        i = 0
        ugly_count = 0
        ugly_num = 0
        isUgly = True

        def findUglyNumber(i):
            if i % 2 == 0:
                i = i//2
                if i == 1 or i == 2 or i == 3 or i == 5:
                    return True
                else:
                    findUglyNumber(i)

            elif i % 3 == 0:
                i = i //3
                if i == 1 or i == 2 or i == 3 or i == 5:
                    return True
                else:
                    findUglyNumber(i)

            elif i % 5 == 0:
                i = i //5
                if i == 1 or i == 2 or i == 3 or i == 5:
                    return True
                else:
                    findUglyNumber(i)
            
            else:
                return False


        while(ugly_count < n ):
            if i == 1 or i == 2 or i == 3 or i == 5:
                ugly_num = i
                ugly_count += 1
                i +=1

            else:
                isUgly == findUglyNumber(i)
                if isUgly == True:
                    ugly_num = i
                    ugly_count += 1
                    i += 1


        return ugly_num

                
                
                