from rest_framework import serializers
from .models import Nft

class NftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nft
        fields = (
            'id', 
            'ipfs_CID',
            'name', 
            'background', 
            'head',
            'tone',
            'gang',
            'expression',
            'hair',
            'hair_color',
            'shoes',
            'right_hand',
            'left_hand',
            'ear_style',
            'neck_style',
            'chest_style',
            'face_style',
            'mark',
            'total_features',
            'description', 
            'thumbnail',
            'get_absolute_url',
            'get_image',
            'get_thumbnail'
            )