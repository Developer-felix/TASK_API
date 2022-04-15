import email
from rest_framework import serializers

from users.models import Acount


class AcountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acount
        fields = ("id", "first_name", "last_name", "email", "is_staff","is_manager","is_student","is_teacher","is_active","is_superuser","is_admin")
        read_only_fields = ("id",)

        def save(self, **kwargs):
            user = Acount(
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name'],
                email=self.validated_data['email'],
                is_staff=self.validated_data['is_staff'],
                is_manager=self.validated_data['is_manager'],
                is_student=self.validated_data['is_student'],
                is_teacher=self.validated_data['is_teacher'],
            )
            user.save
            return user