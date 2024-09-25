from django.shortcuts import render
from django.http import HttpResponse

from .predict import predict_mbti

def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        result = predict_mbti(description)
        return render(request, 'mbti/result.html', {'result': result})
    return render(request, 'mbti/index.html')
