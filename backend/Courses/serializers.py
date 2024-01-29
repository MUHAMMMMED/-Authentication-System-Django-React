from rest_framework import serializers
from .models import CategoryCourse, Course, Rate, CourseSection, EpisodeQuiz, Episode, Comment, CouponCode
from Quiz.serializers  import  QuestionSerializer

class CategoryCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryCourse
        fields = '__all__'

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'

class EpisodeQuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = EpisodeQuiz
        fields = '__all__'


class EpisodeSerializer(serializers.ModelSerializer):
    exam = EpisodeQuizSerializer()

    class Meta:
        model = Episode
        fields = '__all__'






class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CouponCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponCode
        fields = '__all__'


class CourseSectionSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = CourseSection
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    category = CategoryCourseSerializer()
    rating = RateSerializer(many=True, read_only=True)
    course_sections = CourseSectionSerializer(many=True, read_only=True)
    comment = CommentSerializer(many=True, read_only=True)
    exam = EpisodeQuizSerializer()

    class Meta:
        model = Course
        fields = '__all__'
        # exclude=[
        #    'id'
        # ]
