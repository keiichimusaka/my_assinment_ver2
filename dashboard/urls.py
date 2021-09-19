from django.urls import path
from .views import Helloview,TodoDetail,TodoCreate,TodoDelete,TodoUpdate,LogoutView

urlpatterns = [


    path('text',Helloview.as_view(),name = "text"),
    path('detail/<int:pk>',TodoDetail.as_view(),name = "detail"),
    # path('forms',FormView.as_view(),name = "forms"),
    path('create', TodoCreate.as_view(),name = "create"),
    path('delete/<int:pk>', TodoDelete.as_view(),name = "delete"),
    path('update/<int:pk>', TodoUpdate.as_view(),name = "update"),
    path('logout', LogoutView.as_view(),name = "logout")


    
]

# ラーメンの注文を受けたら、厨房に指示をするが、その指示書みたいなもの
# 前がリクエスト、後ろが指示        
# int:pk で特定のデータを指定する（primal keyを指定してデータをいじる）