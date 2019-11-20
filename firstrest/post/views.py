#데이터 처리 대상
from post.models import Post
from post.serializer import PostSerializer

#1. <APIView>를 사용할때 import
#status에 따라 직접 Response를 처리할 것
#from django.http import Http404 #Get Object or 404 직접 구현
#from rest_framework.response import Response
#from rest_framework import status
#APIView를 상속받은 CBV
#from rest_framework.views import APIView
#from rest_framework import viewsets

#PostDetail 클래스의 get_object 메소드 대신 이거 써도 된다
#from django.shortcuts import get_object_or_404

#2. APIView말고 이제 Mixins적용
#from rest_framework import generics
#from rest_framework import mixins


#3. ViewSet사용
from rest_framework import viewsets
# @action처리 -> decorator, default GET방식으로 처리됨 -> CRUD말고 다른 로직들 
# Custom해서 view만듦
from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse


#CBV
#class PostViewSet(viewsets.ModelViewSet):
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer

'''
class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all() #객체를 가져와야해서 쿼리셋
        serializer = PostSerializer(posts, many=True) #쿼리셋 넘기기, (many=True인자) -> 다수를 serializing시킨 것
        return Response(serializer.data) #직접 Response 리턴해주기 : serializer.data (여러개를 serializing 시킨 것)

    def post(self, request):
        serializer = PostSerializer(data = request.data) #보내는 데이터 당연히 직렬화
        if serializer.is_valid(): #직접 유효성 검사
            serializer.save()   #저장
            return Response(serializer.data, status=status.HTTP_201_CREATED) #유효성 검사 성공하면 상태화, 데이터를 보냄
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#PostList 클래스와는 달리 pk값을 받음(메소드에 pk인자)
class PostDetail(APIView):
    def get_object(self, pk): #get_object_404직접 구현한 것
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post = self.get_object(pk) #pk맞는 객체를 갖고와라
        # post = get_object_or_404(Post, pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    #위 post 메소드와 비슷비슷한 논리
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(resializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, pk, format = None):
        post = sele.get_object(pk)
        post.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


#위는 전부 API View , 아래는 mixins

class PostList(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    #get은 list메소드를 내보내는 메소드
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    #post는 create메소드를 내보내는 메소드
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # DetailView의 get은 retrieve를 내보내는 메소드
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # put은 update을 내보내는 메소드
    def put(self, request, *ars, **kwargs):
        return self.update(request, *args, **kwargs)

    #delete는 destroy를 내보내는 메소드
    def delete(self, request, *ars, **kwargs):
        return self.destroy(request, *args, **kwargs)

#여기까지 mixins
'''

#여기서부터 Viewset

#ReadOnlyModelViewSet은 말 그대로 ListView, DetailView의 조회만 가능
#class PostViewSet(viewsets.ReadOnlyModelViewSet):
#    queryset = Post.objects.all()
#    serializer_class = PostSerializer

#ModelViewSet은 ListView와DetailView에 대한 CRUD가 모두 가능
class PostViewSet(viewsets.ModelViewSet):  
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # @action(method = ['post'])
    @action(detail=True, renderer_classes = [renderers.StaticHTMLRenderer])
    #그냥 얍을 띄우는 custom api
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍!")