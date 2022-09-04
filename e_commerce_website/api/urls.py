from django.urls import path, include

urlpatterns = [
    path('manageapi/', include('manage_store.api.urls'), name='manage-api')
]
