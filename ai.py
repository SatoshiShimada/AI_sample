﻿#-*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

fp = open("wagahaiwanekodearu.txt", "r")
ustr = fp.readline()

ustr = unicode("""本来プログラム言語といえばはじめに文法が決まっていて、
そこに文法に従った文字列を入れると実行可能な何かができあがるというのが普通の流れです。
これを逆にしたらどうなるかと思ったのが今回の話題です。""", "utf-8")

# ustr = unicode(fp.read(), "utf-8")

def splitChar(str):
    i = 0
    last = 0
    splited = [""]
    
    for ch in str:
        if last != isType(ch):
            i += 1
            splited.append("")
            splited[i] += ch
        else:
            splited[i] += ch
        last = isType(ch)
    return splited

def isType(ch):
    if (ch >= u"A" and ch <= u"Z") or (ch >= u"a" and ch <= u"z"):
        return 0
    elif ch >= u"ぁ" and ch <= u"ん":
        return 1
    elif ch >= u"ァ" and ch <= u"ン":
        return 2
    elif ch >= u"一" and ch <= u"龳":
        return 3
    else:
        return 4

ret = splitChar(ustr)

for ch in ret:
    print ch