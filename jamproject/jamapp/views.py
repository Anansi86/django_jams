from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import Http404
from .models import song
from rest_framework.response import Response







# class Jamapp(APIView):
#     def get_object(self, pk):
        
#         try:
#             return jamapp.objects.get(pk=pk)
#         except jamapp.DoesNotExist:
#             raise Http404

#     def get(self, request, format=None, pk=None):
#         if pk:
#             data = self.get_object(pk)
#             serializer = JamappSeriallizer(data)

#         else:
#             data = jamapp.objects.all()
#             serializer = JamappSeriallizer(data, many=True)

#             return Response(serializer.data)
