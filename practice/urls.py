
from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/",include("django.contrib.auth.urls")),
    path('', include("dashboard.urls"))

]
# path('', include("dashboard.urls"))　ボード以外を選んだら、dashboardに行く




# ラーメンの注文を受けたら、厨房に指示をするが、その指示書みたいなもの
# 前がリクエスト、後ろが指示
# path("accounts/",include("django.contrib.auth.urls")), が標準で備わっているログインの処理
