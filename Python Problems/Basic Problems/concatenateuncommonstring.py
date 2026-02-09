def concatenatedString(s1,s2):
        #code here
        import re
        s1 = re.findall('[a-z]',s1)
        s2 = re.findall('[a-z]',s2)
        
        for i in range(len(s1)):
            for j in range(i+1,len(s1)):
                if s1[i]!=s1[j]:
                    pass
                elif s1[i]==s1[j]:
                    s1[j] = 0
        if 0 in s1:
            s1.remove(0)
        
        for i in range(len(s2)):
            for j in range(i+1,len(s2)):
                if s2[i]!=s2[j]:
                    pass
                elif s2[i]==s2[j]:
                    s2[j] = 0
        if 0 in s2:
            s2.remove(0)
        
        for i in s1:
            for j in s2:
                if i==j:
                    s1.remove(i)
                    s2.remove(j)
        return "".join(s1+s2)