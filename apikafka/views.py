from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import *
from .serializers import *
from .producer import kafka_send


class PersonAPIView(generics.ListCreateAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

	def post(self, request, *args, **kwargs):
		topic = 'colortrends'
		name = request.data.get("name")
		color = request.data.get("color")

		kafka_send(topic,name,color)

		colors = kafka_synchronous_colors()

		self.create(request, *args, **kwargs)
		return Response({"success": True, "name" : name, "colors" : colors}, status=status.HTTP_201_CREATED)

class ColortrendsAPIView(generics.ListCreateAPIView):
	queryset = Colortrends.objects.all()
	serializer_class = ColortrendsSerializer

	def list(self, request):
		colors = kafka_consumercolor_last()

		return Response({"colors": colors}, status=status.HTTP_201_CREATED)


def kafka_synchronous_colors():
	collection = Person.objects.order_by('-id')[:2]
	lista = []
	for col in collection:
		lista.append({
			'name' : col.name,
			'color': col.color
			})
	return lista


def kafka_consumercolor_last():
	raw = Colortrends.objects.all()
	collection = raw[(len(raw)-2):(len(raw))]
	lista = []
	for col in collection:
		lista.append({
			'name' : col.name,
			'color': col.color
			})
	return lista


class MessagesList(generics.ListCreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


class MessagesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer


# from logpipe import Producer
# from apikafka.models import *
# from apikafka.serializers import *
# person = Person.objects.create(name='Joe', color='#d66851')
# producer = Producer('color', PersonSerializer)
# producer.send(person)

# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser 
# from rest_framework import status
 
# from apikafka.models import Messages
# from apikafka.serializers import MessagesSerializer
# from rest_framework.decorators import api_view


# @api_view(['GET', 'POST', 'DELETE'])
# def messages_list(request):

# 	if request.method == 'GET':
# 		messages = Messages.objects.all()

# 		title = request.GET.get('title', None)

# 		if title is not None:
# 			messages = messages.filter(title__icontains=title)

# 		messages_serializer = MessagesSerializer(messages, many=True)
# 		return JsonResponse(messages_serializer.data, safe=False)
#         # 'safe=False' for objects serialization

# 	elif request.method == 'POST':
# 		messages_data = JSONParser().parse(request)
# 		messages_serializer = MessagesSerializer(data=messages_data)

# 		if messages_serializer.is_valid():
# 			messages_serializer.save()
# 			return JsonResponse(messages_serializer.data, status=status.HTTP_201_CREATED)
# 		return JsonResponse(messages_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
# @api_view(['GET', 'PUT', 'DELETE'])
# def messages_detail(request, pk):
# 	    # find tutorial by pk (id)
# 	try: 
# 		message = Messages.objects.get(pk=pk) 
# 	except Messages.DoesNotExist: 
# 		return JsonResponse({'message': 'The message does not exist'}, status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		messages_serializer = TutorialSerializer(message)
# 		return JsonResponse(messages_serializer.data)

# 	elif request.method == 'PUT':
# 		message_data = JSONParser().parse(request)
# 		message_serializer = TutorialSerializer(message, data=message_data)

# 		if message_serializer.is_valid():
# 			message_serializer.save()
# 			return JsonResponse(message_serializer.data)

# 		return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		message.delete()
# 		return JsonResponse({'message': 'Message was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
#     # GET / PUT / DELETE tutorial
    
        
# @api_view(['GET'])
# def messages_list_published(request):

# 	messages = Messages.objects.filter(published=True)
        
# 	if request.method == 'GET': 
# 		messages_serializer = MessagesSerializer(messages, many=True)
# 		return JsonResponse(messages_serializer.data, safe=False)