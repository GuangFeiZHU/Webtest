from django.shortcuts import render, Http404

# Create your views here.


def index(request):
    """
    首页展示
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request,'index.html')
    else:
        return Http404()
