# String First occurence

s = "vpxowgsdgirfyaevnijubuuqevlrpeysxjfmesyjeg"

pat = "jfmesyjeg"
def occ(s, pat):
    if pat in s:
        for i in range(len(s)):
            if s[i]==pat[0]:
                if s[i:i+len(pat)]==pat[0:]:
                    return i
    else:
        return -1   
print(occ(s,pat))