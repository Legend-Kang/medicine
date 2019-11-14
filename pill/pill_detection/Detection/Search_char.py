import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pill.settings")
django.setup()

from collections import Counter
from pill_detection.models import pillinformation
from operator import itemgetter


class Search_char:
    def __init__(self):
        pass

    def searh_c(self, col, ch):
        a = ch
        b = "".join(a)
        result_string = ""
        for c in b:
            if c.isalnum():
                result_string += c

        b = result_string

        cnt = Counter(b)
        c = cnt.most_common(2)
        c1 = c[0][0]
        c2 = c[1][0]
        # c2 = 'n'
        print(a)
        print(b)
        print(cnt)
        print(cnt.most_common(2))

        for i in a:
            maching = pillinformation.objects.values('char').filter(char=i, shape='circle', color=col)
            if (maching.count() == 1):
                chart = maching[0].get('char')
                # print('outt')
                return chart

        d = pillinformation.objects.values('char').filter(char__contains=c1)
        d2 = pillinformation.objects.values('char').filter(char__contains=c2)
        print(d.count())
        if(d.count()==1):
            print(c1)
            print(d)
            chart = d[0].get('char')
            return chart
        elif(d.count()!=1):
            if(d.filter(shape='circle', color=col).count()==1):
                e = d.filter(shape='circle', color=col)
                chart = e[0].get('char')
                return chart
            else:
                f = d.filter(char__contains=c2)
                chart = f[0].get('char')
                return chart
        elif(d2.count()==1):
            chart = d2[0].get('char')
            return chart

        chart = 'NULL'
        print(chart)

        return chart
