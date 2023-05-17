from django.shortcuts import render

def calculator(request):
    if request.method=='POST':
        num1=float(request.POST.get('num1'))
        num2=float(request.POST.get('num2'))
        operation =request.POST.get('operation')
        if operation=='add':
            result=num1+num2
        elif operation=='substract':
            result=num1-num2
        elif operation=='multiply':
            result=num1*num2
        elif operation=='divide':
            if num2==0:
                result='No dividing by 0'
            else:
                result=num1/num2
        
        context={'result': result}

        return render(request, 'calculator/calculator.html', context)
    else:	
    	return render(request, 'calculator/calculator.html')
