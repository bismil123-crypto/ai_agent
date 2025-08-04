from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import FAQ

def home(request):
    return render(request, 'helpdesk/home.html')
def detail(request):
    return render(request, 'helpdesk/detail.html')
def main(request):
    return render(request, 'helpdesk/main.html')
@csrf_exempt
def ask_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        question = data.get('question', '').lower()

        faqs = FAQ.objects.all()
        for faq in faqs:
            if any(word in question for word in faq.question.lower().split()):
                return JsonResponse({'answer': faq.answer})

        return JsonResponse({'answer': "Sorry, I don't have the information on that. Please contact the help desk."})

    return JsonResponse({'answer': 'Send a POST request with a question.'})