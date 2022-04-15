
#create course serializer
from rest_framework import serializers
from course.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "name", "description", "added_by", "created_at", "updated_at")
        read_only_fields = ("id",)

        def save(self, **kwargs):
            course = Course(
                name=self.validated_data['name'],
                description=self.validated_data['description'],
                added_by=self.validated_data['added_by'],
            )
            course.save
            return course