from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from users.serializers import UserSerializer, UserDetailSerializer

#권한설정에 사용 permissions
from rest_framework import permissions  
#토큰 정보 커스텀을 위해 사용
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"},status=status.HTTP_400_BAD_REQUEST)         
    
    def put(self, request):
        serializer = UserDetailSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response({"message":"수정완료!"})
        else:
             return Response({"message":f"${serializer.errors}"},status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        request.user.delete()
        return Response({"message": "삭제완료"}, status=status.HTTP_204_NO_CONTENT)            