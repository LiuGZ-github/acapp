from django.http import HttpResponse

def index(request):
    return HttpResponse("我的第一个页面！！！")

def play(request):
    return HttpResponse("游戏界面")
