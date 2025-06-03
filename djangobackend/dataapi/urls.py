from django.urls import path
from .views import DataListView
from .streaming.views import stream_logs

urlpatterns = [
    path('data', DataListView.as_view(), name="data-list"),
    path('streaming/data', stream_logs, name="data-sse-stream")
]
