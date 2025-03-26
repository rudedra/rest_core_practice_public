from rest_framework import serializers
from .models import Person, Color




class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()



class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['color_name']






class PeopleSerializer(serializers.ModelSerializer):

    fav_color = ColorSerializer()
    color_info = serializers.SerializerMethodField()


    class Meta:
        model = Person
        fields = '__all__'


    def get_color_info(self, obj):
        color_obj = Color.objects.get(id = obj.fav_color.id)
        
        return ({"color_name" : color_obj.color_name, "color_hex" : "#f00"})

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError('Age should be greater than 18')
        

        return data

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.Charfield()


    def validate(self, request):
        data = request.data

        if(data['username']):
            if (Person.objects.filter(username=data['username']).exists()):
                raise serializers.ValidationError('username is taken')
            
        if(data['email']):
            if (Person.objects.filter(email=data['email']).exists()):
                raise serializers.ValidationError('email is taken')
            
        return data



















