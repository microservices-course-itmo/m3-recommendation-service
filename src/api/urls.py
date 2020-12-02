from django.conf.urls import url, include
from api.views import PredictView

urlpatterns = [
    url(r"^api/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"),
]