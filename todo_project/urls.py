"""
URL configuration for todo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
# from django.urls import path
# from graphene_django.views import GraphQLView

# urlpatterns = [
#     path("graphql", GraphQLView.as_view(graphiql=True)),
# ]
# from django.contrib import admin
# from django.urls import path, include
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Welcome to the Todo App!")

# urlpatterns = [
#     path('', include('graphene_django.urls')),  # Add this line for the root URL
#     path('graphql/', include('graphene_django.urls')),  # Assuming you're using graphene-django
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    # path('graphql/', GraphQLView.as_view(graphiql=True)),  # Enable the GraphiQL interface
    path('admin/', admin.site.urls),
   
]

