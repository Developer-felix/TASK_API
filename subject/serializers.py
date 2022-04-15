#create subject serializer
from rest_framework import serializers
from subject.models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ("id", "name", "description", "subject", "added_by", "created_at", "updated_at")
        read_only_fields = ("id",)

        def save(self, **kwargs):
            subject = Subject(
                name=self.validated_data['name'],
                description=self.validated_data['description'],
                subject=self.validated_data['subject'],
                added_by=self.validated_data['added_by'],
            )
            subject.save
            return subject
