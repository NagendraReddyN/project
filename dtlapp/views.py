from django.shortcuts import render


def dtlfun(request):
    
    return render(request,'home1main.html')

def processingdata(request):
    context = {}
    if request.method == 'POST':
        data = request.POST['t1']
        vowels = 'aeiou'
        output = []
        count = 0
        for ch in data:
            if ch in vowels:
                output.append(ch)
                count = count + 1
                
                
        if len(output)>0:
            dataFound  = 'Yes'
        else:
            dataFound = 'No'
        
        context['output'] = output
        context['dataFound'] = dataFound
        context['count'] = count
        
        return render (request, 'result.html',context)
    
def templateFun(request):
    return render(request,'home2.html')

def thirdFun(request):
    return render(request,'thirdpage.html')