from rest_framework import serializers

from .models import Course
from django.utils import timezone

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' 


class CourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['published_by']

    def update(self, instance, validated_data):
        instance.published_at = timezone.now()
        return super().update(instance, validated_data)