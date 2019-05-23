from rest_framework import serializers


class Love_serializer(serializers.Serializer):
  id = serializers.IntegerField()
  first_name = serializers.CharField(max_length=64)
  second_name = serializers.CharField(max_length=64)
  percentage = serializers.FloatField()
  result = serializers.CharField()
  message = serializers.CharField()

class Love_serializer_comment(serializers.Serializer):
  id = serializers.IntegerField()
  author = serializers.CharField(max_length=64)
  text = serializers.CharField()
  date = serializers.DateField()  