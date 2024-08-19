from django.shortcuts import render

from rest_framework.response import Response
import requests
from rest_framework import viewsets
import os
from django.conf import settings

class CheckStatus(viewsets.ViewSet):
    def list(self, request):
        try:
            response = requests.get('http://scrapy_spider:6800/listjobs.json?project=crawler_app')
            job_id = request.query_params.get('jobid')
            response.raise_for_status()
            data = response.json()

            finished = next((element for element in data.get('finished', []) if job_id == element.get('id')), None)

            if finished:
                return Response({"status": True})

            return Response({"status": False})

        except requests.RequestException as e:
            return Response({"status": False})
