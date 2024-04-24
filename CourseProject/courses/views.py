from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course
from .serializers import CourseSerializer
from .serializers import CourseUpdateSerializer


class CourseListView(APIView):
    def get(self, reequest, *args, **kwargs):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)
    

class CourseUpdatePublishView(APIView):
    def put(self, request, pk, *args, **kwargs):
        course = Course.objects.get(pk=pk)
        
        if not course:
            return Response({'error': 'Course not found'}, status=404)
        
        serializer = CourseUpdateSerializer(course, data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        
        serializer.save()
        return Response(CourseSerializer(course).data, status=200)