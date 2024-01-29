# exams/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Exam, Question,UserExam
from .serializers import ExamSerializer, QuestionSerializer,ExamDetailSerializer 
from Users.models import CustomUser
from django.contrib.auth.decorators import login_required
@login_required
@api_view(['GET'])
def available_exams(request):
    exams = Exam.objects.all()
    serializer = ExamSerializer(exams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def exam_detail(request, exam_id):
    exam = Exam.objects.get(pk=exam_id)
    serializer = ExamSerializer(exam)

    # questions = exam.questions.all()
    # serializer = QuestionSerializer(questions, many=True)
    print('serializer',serializer.data)

    return Response(serializer.data)


# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from .models import Exam
 

# @api_view(['GET'])
# def exam_quiz(request, exam_id):
#     print('exam_id',exam_id)
#     exam = Exam.objects.get(pk=exam_id)
#     print('exam',exam)
#     serializerexam = ExamSerializer(exam)
#     questions = exam.questions.all().order_by('?') 
#     serializerquestion = QuestionSerializer(questions, many=True)
#     print('serializer',serializerquestion.data)
#     return Response(serializerexam.data,serializerquestion.data,)

from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET'])
# def exam_quiz(request, exam_id):
#     print('exam_id', exam_id)
#     exam = Exam.objects.get(pk=exam_id)
#     print('exam', exam)

#     # Serialize exam data
#     serializer_exam = ExamSerializer(exam)

#     # Get and serialize randomized questions
#     questions = exam.questions.all().order_by('?')
#     serializer_questions = QuestionSerializer(questions, many=True)

#     # Combine exam and question data into a dictionary
#     response_data = {
#         'exam': serializer_exam.data,
#         'questions': serializer_questions.data,
#     }

#     print('serializer', response_data)
#     return Response(response_data)


from rest_framework.decorators import api_view
from rest_framework.response import Response

# @api_view(['GET'])
# def exam_quiz(request, exam_id):

#     exam = Exam.objects.get(pk=exam_id)
#     # Serialize exam data
#     serializer_exam = ExamSerializer(exam)

#     # Get and serialize randomized questions with index
#     questions = exam.questions.all().order_by('?')
#     serialized_questions = []
#     for index, question in enumerate(questions, start=1):
#         serialized_question = QuestionSerializer(question).data
#         serialized_question['index'] = index
#         serialized_questions.append(serialized_question)

#     # Combine exam and question data into a dictionary
#     response_data = {
#         'exam': serializer_exam.data,
#         'questions': serialized_questions,
#     }

#     print('serializer', response_data)
#     return Response(response_data)

from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response


  



# @api_view(['GET'])
# def exam_quiz(request, exam_id):

#     user = request.CustomUser
#     print(user)
#     userexam = UserExam.objects.filter(student=user).first()
#     triesuser=userexam.tries
#     print(triesuser)

#     try:
#         # Assuming your Exam model has a UUIDField named 'id'
#         exam = Exam.objects.get(id=exam_id)
#     except Exam.DoesNotExist:
#         raise Http404("Exam does not exist")

#     # Serialize exam data
#     serializer_exam = ExamSerializer(exam)

#     # Get and serialize randomized questions with index
#     questions = exam.questions.all().order_by('?')
#     serialized_questions = []
#     for index, question in enumerate(questions, start=1):
#         serialized_question = QuestionSerializer(question).data
#         serialized_question['index'] = index
#         serialized_questions.append(serialized_question)

#     # Combine exam and question data into a dictionary
#     response_data = {
#         'exam': serializer_exam.data,
#         'questions': serialized_questions,
#     }

#     return Response(response_data)
# @login_required
@api_view(['GET'])
def exam_quiz(request, exam_id):
    # user = request.user.CustomUser
    # print('user',user)
    # if request.user.is_authenticated:
    #     user_id = request.user.id
    #     print('user', user_id)
    # else:
    #       print('User is not authenticated')

    # userexam = UserExam.objects.filter(student=user.id ).first()
    # print(userexam)
    # triesuser = userexam.tries
    # print(triesuser)

    try:
        # Assuming your Exam model has a UUIDField named 'id'
        exam = Exam.objects.get(id=exam_id)
    except Exam.DoesNotExist:
        raise Http404("Exam does not exist")

    # Serialize exam data
    serializer_exam = ExamSerializer(exam)

    # Get and serialize randomized questions with index
    questions = exam.questions.all().order_by('?')
    serialized_questions = []
    for index, question in enumerate(questions, start=1):
        serialized_question = QuestionSerializer(question).data
        serialized_question['index'] = index
        serialized_questions.append(serialized_question)

    # Combine exam and question data into a dictionary
    response_data = {
        'exam': serializer_exam.data,
        'questions': serialized_questions,
    }

    return Response(response_data)
