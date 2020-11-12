from rest_framework import serializers 
from apikafka.models import *
 

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ['uuid', 'name', 'color']

 
class MessagesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Messages
        fields = ('id',
                  'title',
                  'description',
                  'published')
