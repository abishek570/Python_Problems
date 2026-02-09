def uncommonChars(s1, s2):
        #code here
        import re
        s1 = re.findall('[a-z]',s1)
        s2 = re.findall('[a-z]',s2)
        s1 = set(s1)
        s2 = set(s2)
        
        s = s1^s2
        s =sorted(list(s))
        
        
        return ''.join(s)


print(uncommonChars("geeksfor","geaks"))