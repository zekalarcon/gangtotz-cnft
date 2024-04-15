from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import NftSerializer
from .models import Nft
import json, os, random, requests
from cardano_tools import NodeCLI
import ipfshttpclient

@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint': 'nfts',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Nfts'
        },
        {
            'Endpoint': 'nfts/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single Nft object'
        },
        {
            'Endpoint': 'build_nft',
            'method': 'POST',
            'body': None,
            'description': 'Mint Nft'
        }
    ]
    return Response(routes)


@api_view(['GET'])
def getNftsInfo(request):
    
    nfts = Nft.objects.all()
    serializer = NftSerializer(nfts, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getNftInfo(request, pk):
    
    nfts = Nft.objects.get(id=pk)
    serializer = NftSerializer(nfts, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def build_nft(request):
    '''
    Private Code
    '''
    pass