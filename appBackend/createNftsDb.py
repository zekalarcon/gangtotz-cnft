import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from api.models import Nft

with open('GangTotz.csv') as file:
    reader = csv.reader(file)
    next(reader)  # Advance past the header

    for row in reader:

        Nft.objects.create(
            ipfs_CID = 'CID CODE HERE',
            name='GangTotz ' + row[0],
            background = row[1],
            head = row[2],
            tone = row[3],
            gang = row[4],
            expression = row[5],
            hair = row[6],
            hair_color = row[7],
            shoes = row[8],
            right_hand = row[9],
            left_hand = row[10],
            ear_style = row[11],
            neck_style = row[12],
            chest_style = row[13],
            face_style = row[14],
            mark = row[15],
            total_features = row[16]
        )