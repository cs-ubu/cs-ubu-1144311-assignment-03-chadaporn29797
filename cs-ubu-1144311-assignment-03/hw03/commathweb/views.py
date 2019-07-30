from django.shortcuts import render
from django.http import HttpResponse
import csv

def index(req):
    return render(req,'commathweb/index.html')

def IEEE32(req):
    try:
        r = ''
        d = req.GET.get('num')
        d = float(d)
        print(d, type(d))
        
        nb = bin(int(d))
        nb = nb[2:]
        print(nb)
        lung = d-int(d)   
        while lung>0 and len(nb) + len(r) < 31:
            lung = lung*2
            r += str(int(lung))
            lung -= int(lung) 
        print("r=",r)
        
        e = len(nb)-1
        s = '0' if d >= 0 else '1'
        
        e += 127
        bie = bin(e)
        bie = bie[2:]
        nbbilung = nb+r
        nbbilung = nbbilung[1:]
        b = s+bie+nbbilung
        b = b + '0'*(32-len(b))
        print(b)
        result = {'answer':b, 'd':d}
    except :
        result = {'answer':"กรุณากรอกค่าใหม่"}
    return render(req,'commathweb/IEEE32.html',result)

def IEEE64(req):
    try:
        # r = ''
        x = req.GET.get('num')
        x = float(x)
        print(type(x))
        w = int(x)
        d = x - w
        bw = bin(w)[2:]
        bd = ''
        while d != 0:
            d  *= 2
            bd += str(int(d))
            d  -= int(d)
        bwbd = bw+bd
        t = len(bw) - 1
        m = bwbd[1:]
        s = 0 if d >= 0 else 1
        e = 1023 + t
        be = bin(e)[2:]
        b = str(s) + be + m
        b += '0'*(64-len(b))
        l = '0'*32
        print(len(b))
        result = {'answer':b, 'x':x, 'l':l}
    except :
        result = {'answer':"กรุณากรอกค่าใหม่"}
    return render(req,'commathweb/IEEE64.html',result)

def AB(req):
    name1 = req.GET.get('name1')
    # o = float(name1)
    # o = int(o)
    # print(o, type(o))
    a = []
    for i in range(int(name1)-1):
        a.append('[input id="name" class="input300" type="text" name="equation" placeholder="กรุณาใส่สมการ"]') 

    print('a=',a)
    print('i=',i)

    m = {
        'y' : a,
        'x' : name1
    }

    # A = []
    # b = []
    eqA = req.GET.get('eq')
    eqb = req.GET.get('eqb')
    # A.append(eqA)
    # b.append(eqb)
    print(eqA)
    print("=======================")
    print(eqb)
    # a = ['input id="name" class="input300" type="text" name="name" placeholder="Full name"']
    # for i in range()
    
    # p = {'name1':name1}
    # print(m)
    return render(req,'commathweb/AB.html',m)