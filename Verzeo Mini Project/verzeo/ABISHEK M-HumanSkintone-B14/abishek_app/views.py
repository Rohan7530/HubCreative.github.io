from django.shortcuts import render


from subprocess import run,PIPE

import sys
import string


def button(request):
    return render(request,'final_test.html')


def home_view(request):
    return render(request,'final_test.html')

def external(request):
    encoding = 'utf-8'
    inp=request.POST.get('link')
    out=run([sys.executable,"C:\\Users\\feroz\\Desktop\\abishek_project\\ml.py",inp],shell=False,stdout=PIPE)
    #put ml.py path from your computer
    byte= out.stdout
    value=str(byte, encoding)
    print(value)
    return render(request,'final_test.html',{'data':value})

def check(request):
   return render(request,'1.html')
