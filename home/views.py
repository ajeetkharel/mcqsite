from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Exam, Question
from datetime import datetime
import pytz

@login_required(login_url='/')
def online_exam(request):
    exams = Exam.objects.all()
    today_date = datetime.now().replace(tzinfo=pytz.UTC)
    for exam in exams:
        if exam.date <= today_date:
            current_exam = exam
            break
    questions = Question.objects.filter(exam=current_exam)
    print(questions)
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
