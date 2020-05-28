from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request):
    context = {}
    c=request.GET.get('name0')+request.GET.get('name1')
    score=0
    for i in c:
        if i in "aeiou":
                score+=5
        if i in "friends":
                score+=10
        if i in "bcdfgjklmnpqrstvwxyz":
                score+=2
    context['result']=score
    print(context)
    return render(request, 'result.html', {'result':context})
