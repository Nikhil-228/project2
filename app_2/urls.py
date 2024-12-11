from django.urls import path
from . import views
urlpatterns=[path("path1",views.myform,name="myform"),
             path("path2",views.mydata,name="mydata"),
             path("path7/<id1>",views.delete,name="delete"),
             path("path3",views.display_firstnames,name="display_firstnames"),
             path("path4/<id2>",views.update,name="update"),
             path("path5",views.search,name="search"),
             path("path6",views.send_email,name="send_email"),
             path("path8", views.card, name="card"),
             path("path9/<str:id3>", views.productinfo, name="productinfo"),
             path("",views.home,name="home")
             ]