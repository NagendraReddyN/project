from django.shortcuts import render

# Create your views here.
def calfun(request):
    context={}
    if request.method=='POST':
        #print(request.POST)
        n1=int(request.POST['t1'])
        n2=int(request.POST['t2'])
        if 'add' in request.POST:
            res=n1+n2
            #output='Addition of {} and {} is {}'.format(n1,n2,res)
            action='Addition'
        elif 'sub' in request.POST:
            res=n1-n2
            #output='Subtraction of {} and {} is {}'.format(n1,n2,res)
            action='Subtraction'
        elif 'div' in request.POST:
            res=n1//n2
            #output='Division of {} and {} is {}'.format(n1,n2,res)
            action='Division'
        else:
            res=n1*n2
            #output='Multiplication of {} and {} is {}'.format(n1,n2,res)
            action='Multiplication'
        context['input1']=n1
        context['input2']=n2
        context["result"]=res
        context['action']=action
        return render(request,'output.html',context)
    resp= render(request,'calculator.html')
    return resp