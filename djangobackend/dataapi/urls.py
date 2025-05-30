from django.urls import path
from .views import DataListView
from .streaming.views import sse_stream

urlpatterns = [
    path('data', DataListView.as_view(), name="data-list"),
    path('streaming/data', sse_stream, name="data-sse-stream")
]
