from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

class authMiddleware(MiddlewareMixin): 
    def process_response(self, request, response):
        '''
        認証系処理
        '''
        # トップ画面、ログイン処理画面はスルー
        if request.path == "/" or request.path.find("/login") >= 1:
            return response
        
        # ログインしていない場合はトップページにリダイレクト
        if not request.user.is_authenticated: 
            return HttpResponseRedirect('accounts/login') 
        
        return response

# Middleware→サイト全体にかかるため、otherwise全てのveiwで確認することがある。
# →ログインしているかチェクする
# →していなかったら、指定したpageに戻す。

# request.path.find("/login") >= 1:　→pathの中に、"/login" を含むかどうが、　>= 1: ①番め（文字の数）
# is_authenticated　→ログインしているかどうか確認する。