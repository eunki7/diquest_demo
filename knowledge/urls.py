from django.urls import path

from .views import *

app_name = 'knowledge'
urlpatterns = [

    # Example: /
    path('', KnowledgeLV.as_view(), name='index'),

    # Example: /support/viewer/1
    path('knowledge/pdf_viewer/<int:pk>', KnowledgePV.as_view(), name='knowledge_pdf_viewer'),

    # Example: /support/ (same as /)
    path('knowledge/', KnowledgeLV.as_view(), name='knowledge_list'),

    # Example: /support/django-example/
    path('knowledge/<slug>/', KnowledgeDV.as_view(), name='knowledge_detail'),

    # Example: /add/
    path('add/',
         KnowledgeCreateView.as_view(), name="add",
         ),

    # Example: /change/
    path('change/',
         KnowledgeChangeLV.as_view(), name="change",
         ),

    # Example: /99/update/
    path('<int:pk>/update/',
         KnowledgeUpdateView.as_view(), name="update",
         ),

    # Example: /99/delete/
    path('<int:pk>/delete/',
         KnowledgeDeleteView.as_view(), name="delete",
         ),
]
