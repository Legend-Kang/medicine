import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pill.settings")
django.setup()

from collections import Counter
from pill_detection.models import Photo, pillinformation
from operator import itemgetter

from django.http import HttpResponse



# def ch():






a = ['e', '2¢"', '~*', '_R®°', 'RNC', '', 'cS', '2¢"', '~*', '', '_ RNC', '', 'D', 'Bp', '~*', 'KM', 'RNP']

b = "".join(a)

# sample_string = "1234567890abcdefgABCDEFG!@#$%^&*()_{}[]<>"
result_string = ""
for c in b:
    if c.isalnum():
        result_string +=c
print(result_string)

b = result_string


cnt = Counter(b)
c = cnt.most_common(2)
c1 = c[0][0]
c2 = c[1][0]
print(a)
print(cnt)
print(cnt.most_common(2))
print(c1 + c2)
print(c2)

for i in a:
    maching = pillinformation.objects.values('char').filter(char=i, shape='circle', color='orange')
    if(maching.count()==1):
        chart = maching[0].get('char')
        print(chart)
        print(maching.filter(shape='circle', color='orange'))
        print(maching)


d = pillinformation.objects.values('char').filter(char__contains=c1)
if(d.count()==1):
    e = d.filter(char__contains=c1)
    chart = e[0].get('char')
elif(d.count()!=1):
    if(d.filter(shape='circle', color='orange').count()==1):
        e = d.filter(shape='circle', color='orange')
        chart = e[0].get('char')
    else:
        f = d.filter(char__contains=c2)
        chart = f[0].get('char')

print(chart)





