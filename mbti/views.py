from django.shortcuts import render
from django.http import HttpResponse

from .predict import predict_mbti
from .predict import mbtiDescription

def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        if description:
            predictedType = predict_mbti(description)
            desc = mbtiDescription(predictedType)
            print(desc)
            return render(request, 'mbti/result.html', {'result': predictedType,'mbtiDesc' : desc})
    return render(request, 'mbti/index.html')
