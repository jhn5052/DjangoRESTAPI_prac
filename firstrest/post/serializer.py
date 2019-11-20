from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['id', 'title', 'body']
        #id는 객체의 pk값
        #read_only_fields = ('title',) #어떤 필드를 readonly로 바꾸고 싶은지
        #write_only_fields = ('title',)
