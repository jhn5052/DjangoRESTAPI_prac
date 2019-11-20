from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
#<APIView일때>
#from rest_framework.urlpatterns import format_suffix_patterns

#django rest framework -> router -> url

#router = DefaultRouter() #라우터 정의
#router.register('post', views.PostViewSet) #라우터 등록
'''
urlpatterns = [ 
    #url등록
    # 127.0.0.1:8000/post = ListView
    path('post/',views.PostList.as_view()),
    #127.0.0.1:8000/post/<pk> == DetailView
    path('post/<int:pk>/', views.PostDetail.as_view()),
]
#
urlpatterns = format_suffix_patterns(urlpatterns)
'''

router = DefaultRouter()
router.register('post', views.PostViewSet)
urlpatterns = [
    path('', include(router.urls)),
]