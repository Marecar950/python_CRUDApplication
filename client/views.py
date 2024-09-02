from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer
from django.shortcuts import get_object_or_404 

@api_view(['GET'])
def get_all_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_client_details_by_id(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    serializer = ClientSerializer(client)
    return Response(serializer.data, status=status.HTTP_200_OK)    

@api_view(['POST'])
def create_client(request):
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            client = serializer.save()
            return Response(
                {
                    'message': 'Client créé avec succès',
                    'client': ClientSerializer(client).data 
                },
                 status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    serializer = ClientSerializer(client, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                'message': 'Client modifié avec succès',
                'client': serializer.data
            },
            status=status.HTTP_200_OK
        )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()

    return Response(
        {
            'message': 'Client supprimé avec succès'
        },
        status=status.HTTP_204_NO_CONTENT
    )        
