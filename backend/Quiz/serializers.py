from rest_framework import serializers
from .models import Exam, Question

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'







from rest_framework import serializers
from .models import Exam, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

# class ExamDetailSerializer(serializers.ModelSerializer):
#     # creator_username = serializers.CharField(source='creator.username', read_only=True)'creator_username',
#     questions = QuestionSerializer(many=True, read_only=True)

#     class Meta:
#         model = Exam
#         fields = '__all__'
#         read_only_fields = ( 'questions')


class ExamDetailSerializer(serializers.ModelSerializer):
    # creator_username = serializers.CharField(source='creator.username', read_only=True)'creator_username',, read_only=True
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Exam
        fields = '__all__'
        read_only_fields = ('questions',)



