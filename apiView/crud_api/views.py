from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from .models import Students
from .serializers import StudentSerializer

# Create your views here.

# API View
class StudentView(APIView):
    def post(self, request, format=None):
        print("Student1", request)
        print("Student2", request.method)
        print("Student3", request.data)

        # serializer = StudentSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()

        return Response(
            {"success": "Student uploaded successfully"}, status=status.HTTP_200_OK
        )

    def get(self, request, id=None, format=None):
        if id is None:
            student = Students.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data)
        else:
            student = Students.objects.get(id=id)
            # print(student)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

    # def get(self, request, format=None):
    #

    def put(self, request, id=None, format=None):  # Update
        student = Students.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"success": "Student updated successfully"}, status=status.HTTP_200_OK
        )

    def delete(self, request, id=None, format=None):
        student = Students.objects.get(id=id)
        print("Student", student)
        student.delete()
        return Response(
            {"success": "Student deleted successfully"}, status=status.HTTP_200_OK
        )


# While getting a data:
# database -> Views -> user   ?? serializer where


# while posting a data to the database:
# user -> Views -> database ?? serializer where


# Mixins Views


class StudentMixinView(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentRetrieveMixinView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




# Generic Views 

# class StudentGenericView(generics.ListAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer


# class StudentGenericView(generics.CreateAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer

class StudentGenericView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

# class StudentDataGenericsView(generics.RetrieveAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer

# class StudentDataGenericsView(generics.UpdateAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer


# class StudentDataGenericsView(generics.DestroyAPIView): 
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer


# class StudentDataGenericsView(generics.RetrieveUpdateAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer 



# class StudentDataGenericsView(generics.RetrieveDestroyAPIView):  
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer


class StudentDataGenericsView(generics.RetrieveUpdateDestroyAPIView): 
    queryset = Students.objects.all()
    serializer_class = StudentSerializer

