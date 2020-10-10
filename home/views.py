from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Exam, Question, Result
from user.models import User
from datetime import datetime, timedelta
import pytz
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

@login_required(login_url='/')
def online_exam(request):
    current_exam = None
    questions = None
    messages = None
    if request.user.is_student:
        exams = Exam.objects.all()
        today_date = datetime.now().replace(tzinfo=pytz.UTC) + timedelta(hours=5, minutes=45) 
        for exam in exams:
            if exam.start_date <= today_date <= exam.end_date:
                current_exam = exam
        questions = Question.objects.filter(exam=current_exam)
        messages = []
        if request.method == "POST":
            correct = 0
            wrong = 0
            for i in range(questions.count()):
                message = {}
                user_answer = request.POST['question'+str(questions[i].pk)]
                correct_answer = questions[i].CorrectOption
                if user_answer == correct_answer:
                    message =  "Correct!"
                    correct+=1
                else:
                    wrong+=1
                    message =  f"Wrong! The answer is option {questions[i].CorrectOption}"
                messages.append(message)
            result = Result(idt=int(request.user.pk), exam=current_exam, right=correct, wrong=wrong)
            result.save()
        return render(request, 'home/index.html', {'Exam':current_exam, 'Questions':questions, 'messages':messages})
    else:
        students = User.objects.filter(is_student=True)
        page = request.GET.get('page', 1)
        paginator = Paginator(students, 10)
        try:
            fstudents = paginator.page(page)
        except PageNotAnInteger:
            fstudents = paginator.page(1)
        except EmptyPage:
            fstudents = paginator.page(paginator.num_pages)

        return render(request, 'home/index.html', {'Students':fstudents, 'Exam':current_exam, 'Questions':questions, 'messages':messages})