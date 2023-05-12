from messenger.views import CreateMessageView
from django.urls import path

urlpatterns = [
    path('', CreateMessageView.as_view(), name = 'create_message'),
]