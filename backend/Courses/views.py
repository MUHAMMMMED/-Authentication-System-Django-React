from rest_framework import generics
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

 


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer

class CourseDetailView(APIView):
    def get(self, request, course_uuid):
        try:
            course = Course.objects.get(course_uuid=course_uuid)
            serializer = CourseSerializer(course)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'detail': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)









from rest_framework.generics import RetrieveAPIView
from rest_framework import permissions
from .models import Episode
from .serializers import EpisodeSerializer

class EpisodeDetailView(RetrieveAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    permission_classes = [permissions.AllowAny]  # Adjust the permissions as needed

    lookup_field = 'episode_uuid'  # Set the lookup field to 'episode_uuid'

    def get_object(self):
        # Use the lookup field to filter the queryset based on the URL parameter
        queryset = self.get_queryset()
        filter_kwargs = {self.lookup_field: self.kwargs[self.lookup_field]}
        return queryset.get(**filter_kwargs)

 

 

 
 

from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Episode
from .serializers import CourseSerializer, EpisodeSerializer

 

class EpisodeDetailView(RetrieveAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    lookup_field = 'episode_uuid'
    def get_object(self):
        episode_uuid = self.kwargs['episode_uuid']
        return get_object_or_404(Episode, episode_uuid=episode_uuid)
 


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class NextEpisode(APIView):
    def get(self, request, episode_uuid):
        try:
            current_episode = Episode.objects.get(episode_uuid=episode_uuid)
            serial_number = current_episode.serial_number
            next_episode = Episode.objects.filter(serial_number__gt=serial_number).order_by('serial_number').first()
            if next_episode:
                data = {'episode_uuid': next_episode.episode_uuid}
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'No next episode found'}, status=status.HTTP_404_NOT_FOUND)
        except Episode.DoesNotExist:
            return Response({'detail': 'Episode not found'}, status=status.HTTP_404_NOT_FOUND)

 
 
















# from django.shortcuts import render , redirect
# from OnlineCourse.models import Course,Video,UserCourse
# from django.shortcuts import HttpResponse
# # Create your views here.
# from django.contrib.auth.decorators import login_required
# from django.views.generic import ListView
# from django.utils.decorators import method_decorator

# @method_decorator(login_required(login_url='login') , name='dispatch')
    

# class MyCoursesList(ListView):
#     template_name = 'my_courses.html'
#     context_object_name = 'user_courses'
#     def get_queryset(self):
#         return UserCourse.objects.filter(user = self.request.user)


# def coursePage(request , slug):
#     course = Course.objects.get(slug  = slug)

#     serial_number  = request.GET.get('lecture')

#     videos = course.video_set.all().order_by("serial_number")


#     next_lectuer = 2
#     prev_lectuer= None;
#     if serial_number is None:
#         serial_number = 1 
#     else:
#         next_lectuer=int(serial_number)+1 
#         if len(videos)<next_lectuer:
#             next_lectuer =None 
          
          
#         prev_lectuer=int(serial_number)-1 

          
          
#     video = Video.objects.get(serial_number = serial_number , course = course)

#     if (video.is_preview is False):

#         if request.user.is_authenticated is False:
#             return redirect("login_attempt")
#         else:
#             user = request.user
#             try:
#                 user_course = UserCourse.objects.get(user = user , course = course)
#             except:
#                 return redirect("OnlineCourse:check_out" , slug=course.slug)
        
#     context = {
#         "course" : course , 
#         "video" : video , 
#         'videos':videos,
#         'prev_lectuer':prev_lectuer,
#         'next_lectuer':next_lectuer,
#     }
#     return  render(request , template_name="course_page.html" , context=context )    

# from django.shortcuts import render
# from Promo_course.models import *
# # Create your views here.
# from OnlineCourse.models import Course
# def OnlineCourseView(request):
#     Promo_Course =Course.objects.filter(active=True)
#     OnlineCourse = Promo_Course.all()
#     Promo_course =PromoCourse.objects.filter(active=True)
#     Promo_CoursE = Promo_course.all()
#     context = {'Online_Course':OnlineCourse,'Promo_Course':Promo_CoursE}
#     return render(request , 'OnlineCourse.html' , context)




# from django.shortcuts import render , redirect
# from OnlineCourse.models  import Course , Video , Payment , UserCourse ,CouponCode
# from django.shortcuts import HttpResponse
# # Create your views here.
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# # from codewithvirendra.settings import *
# from time import time

# # import razorpay
# client ={'receipt' 
#                 'notes'  
#                 'amount'  
#                 'currency'  
#                 }


# @login_required(login_url='/login')
# def checkout(request , slug):
#     course = Course.objects.get(slug  = slug)
#     user = request.user
#     action = request.GET.get('action')
#     couponcode = request.GET.get('couponcode')
 
#     coupon = None
#     coupon_code_message= None;
#     order = None
#     payment = None
#     error = None
#     try:
#         user_course = UserCourse.objects.get(user = user  , course = course)
#         error = "You are Already Enrolled in this Course"
#     except:
#         pass
#     amount=None
#     if error is None : 
#         amount =  int((course.price - ( course.price * course.discount * 0.01 )) * 100)
# #    if ammount is zero dont create paymenty , only save emrollment obbect 

#     if couponcode :
#          print('Couponcode',couponcode)
#          try:
#              coupon= CouponCode.objects.get(course=course,code=couponcode) 
#              amount1=course.price-(course.price*course.discount*0.01)
#              amount=amount1-(amount1*coupon.discount*0.01)
#              amount=int(amount) 
#              print(amount)
#          except:
#              coupon_code_message='Invalid Coupon Code'
#             # messages.success(request, 'invalid Coupon code')
            
#     if amount==0:
#         userCourse = UserCourse(user = user , course = course)
#         userCourse.save()
#         return redirect('OnlineCourse:my-courses')   
 
    

    
#     context = {
#         "course" : course , 
#         "order" : order, 
#         "payment" : payment, 
#         "user" : user , 
#         "error" : error,
#         "coupon":coupon,
#         "coupon_code_message":coupon_code_message,
#         'amount':amount
       
#     }
#     return  render(request , template_name="check_out.html" , context=context )    

# @login_required(login_url='/login')
# @csrf_exempt
# def verifyPayment(request):
#     if request.method == "POST":
#         data = request.POST
#         context = {}
#         print(data)
#         try:
#             # client.utility.verify_payment_signature(data)
#             # razorpay_order_id = data['razorpay_order_id']
#             # razorpay_payment_id = data['razorpay_payment_id']

#             # payment = Payment.objects.get(order_id = razorpay_order_id)
#             # payment.payment_id  = razorpay_payment_id
#             # payment.status =  True
            
#             userCourse = UserCourse(user = payment.user , course = payment.course)
#             userCourse.save()

#             print("UserCourse" ,  userCourse.id)

#             payment.user_course = userCourse
#             payment.save()

#             return redirect('OnlineCourse:my-courses')   

#         except:
#             return HttpResponse("Invalid Payment Details")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#  from django.shortcuts import render , redirect
# from courses.models import Course , Video , Payment , UserCourse
# from django.shortcuts import HttpResponse
# # Create your views here.
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
# from codewithvirendra.settings import *
# from time import time

# import razorpay
# client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))


# @login_required(login_url='/login')
# def checkout(request , slug):
#     course = Course.objects.get(slug  = slug)
#     user = request.user
#     action = request.GET.get('action')
#     order = None
#     payment = None
#     error = None
#     try:
#         user_course = UserCourse.objects.get(user = user  , course = course)
#         error = "You are Already Enrolled in this Course"
#     except:
#         pass
#     amount=None
#     if error is None : 
#         amount =  int((course.price - ( course.price * course.discount * 0.01 )) * 100)
#    # if ammount is zero dont create paymenty , only save emrollment obbect 
    
#     if amount==0:
#         userCourse = UserCourse(user = user , course = course)
#         userCourse.save()
#         return redirect('my-courses')   
#                 # enroll direct
#     if action == 'create_payment':

#             currency = "INR"
#             notes = {
#                 "email" : user.email, 
#                 "name" : f'{user.first_name} {user.last_name}'
#             }
#             reciept = f"codewithvirendra-{int(time())}"
#             order = client.order.create(
#                 {'receipt' :reciept , 
#                 'notes' : notes , 
#                 'amount' : amount ,
#                 'currency' : currency
#                 }
#             )

#             payment = Payment()
#             payment.user  = user
#             payment.course = course
#             payment.order_id = order.get('id')
#             payment.save()


    
#     context = {
#         "course" : course , 
#         "order" : order, 
#         "payment" : payment, 
#         "user" : user , 
#         "error" : error
#     }
#     return  render(request , template_name="courses/check_out.html" , context=context )    

# @login_required(login_url='/login')
# @csrf_exempt
# def verifyPayment(request):
#     if request.method == "POST":
#         data = request.POST
#         context = {}
#         print(data)
#         try:
#             client.utility.verify_payment_signature(data)
#             razorpay_order_id = data['razorpay_order_id']
#             razorpay_payment_id = data['razorpay_payment_id']

#             payment = Payment.objects.get(order_id = razorpay_order_id)
#             payment.payment_id  = razorpay_payment_id
#             payment.status =  True
            
#             userCourse = UserCourse(user = payment.user , course = payment.course)
#             userCourse.save()

#             print("UserCourse" ,  userCourse.id)

#             payment.user_course = userCourse
#             payment.save()

#             return redirect('my-courses')   

#         except:
#             return HttpResponse("Invalid Payment Details")
        
        
 