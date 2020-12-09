import re

inputstring = "Our meeting will be at 5pm tomorrow."
# inputstring = "Our meeting will be schedule at 11am tomorrow."

findpattern_am = re.search(r'\b([1-9]|0[1-9]|1[0-2]{1,2})(am)\b',
                           inputstring, re.M | re.I)
findpattern_pm = re.search(r'\b([1-9]|0[1-9]|1[0-2]{1,2})(pm)\b',
                           inputstring, re.M | re.I)

if findpattern_am:
    #print findpattern_am.group()
    print(re.sub(r'\b([1-9]|0[1-9]|1[0-2]{1,2})(am)\b', r'\1 a.m.', inputstring))
elif findpattern_pm:
    #print findpattern_pm.group()
    print(re.sub(r'\b([1-9]|0[1-9]|1[0-2]{1,2})(pm)\b', r'\1 p.m.', inputstring))
else:
    print("Not matched...!")
