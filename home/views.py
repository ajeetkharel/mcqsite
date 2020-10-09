from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Exam

@login_required(login_url='/')
def online_exam(request):
    questions = Exam.objects.all()
    messages = []
    if request.method == "POST":
        for i in range(questions.count()):
            message = {}
            user_answer = request.POST['question'+str(questions[i].pk)]
            correct_answer = questions[i].CorrectOption
            if user_answer == correct_answer:
                message =  "Correct!"
            else:
                message =  f"Wrong! The answer is option {questions[i].CorrectOption}"
            messages.append(message)
    return render(request, 'home/index.html', {'Exam':questions, 'messages':messages})
