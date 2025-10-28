from rest_framework import serializers
from base.models import StudentsModel

class StudentSerializer(serializers.Serializer):
    s_name=serializers.CharField()
    s_rollno=serializers.IntegerField()
    s_course=serializers.CharField()

    def create(self, validated_data):
        return StudentsModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.s_name=validated_data.get('s_name',instance.s_name)
        instance.s_rollno=validated_data.get('s_rollno',instance.s_rollno)
        instance.s_course=validated_data.get('s_course',instance.s_course)
        instance.save()
        return instance