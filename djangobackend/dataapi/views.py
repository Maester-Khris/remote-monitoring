from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from pathlib import Path
import os
import json

# Create your views here.
class DataListView(APIView):
    def get(self, request):
        DATA_DIR = Path(__file__).resolve().parent
        datapath = os.path.join(DATA_DIR, "data", "todos.json")
        with open(datapath, 'r') as file:
            data = json.load(file)

        return Response(data)
    
