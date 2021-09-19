from django.http.response import HttpResponse
from django.views.generic import DetailView,CreateView,ListView,DeleteView,UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from dashboard.models import ProfileModel
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views import generic


class Helloview(ListView):
    template_name = "text.html"
    model = ProfileModel

class TodoDetail(DetailView):
        template_name = "detail.html"   
        model = ProfileModel

# class FormView(TemplateView):
#     template_name = "forms.html"
    
#     def get(self,request):    
#         # selfはクラスの中の関数であれば、引数として必要：そのクラス内WEBページをひらいた時の処理
#         form = FormAspp()
#         # →インスタンス化（実体化をしている）
#         return self.render_to_response({"form":form})
#         # →HTMLを生成する処理

class TodoCreate(CreateView):
    template_name = "create.html"
    model = ProfileModel
    fields = ("name","age","avalability","description","birhday")
    success_url = reverse_lazy("text")


# Create your views here.
# HTMLの表示を制御
    # template_name = "text.html" →templateの中にある、textを呼びだす

    
        # return self.render_to_response({"form":form})
        # 文字列がKEYで、変数がvalue
# reverse_lazy はDjaogo.urlsの中に入っている。フォーム作成後の遷移先のURL

class TodoDelete(DeleteView):
    template_name = "delete.html"
    model = ProfileModel
    success_url = reverse_lazy("text")

class TodoUpdate(UpdateView):
    template_name = "update.html"
    model = ProfileModel
    fields = ("name","age","avalability","description","birhday")
    success_url = reverse_lazy("text")

class LogoutView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        logout(request)

    
# Template_name は表示したいHTMLファイルがある場合のみ必要
# ログアウトviewについては決まり文句