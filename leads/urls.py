
from unicodedata import name
from django.urls import path
from . import views

app_name = "leads"
urlpatterns = [
    # path('', views.landing_page, name="landing-page"),
    path('list/', views.LeadListView.as_view(), name="lead-list"),
    path('<int:pk>', views.LeadDetailView.as_view(), name="lead-detail"),
    path('lead_create/', views.LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/update', views.LeadUpdateView.as_view(), name="lead-update"),
    path('<int:pk>/delete', views.lead_delete, name="lead-delete")
]
