from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from mainapp.models import FruitImage, UserEntity


@csrf_exempt
def find_fruit(request):
    price1 = request.GET.get('price1', 0)
    price2 = request.GET.get('price2', 1000)
    fruits = FruitImage.objects \
        .values('url', 'fruit_id__name', 'fruit_id__price', 'fruit_id__source', 'width', 'height') \
        .filter(fruit_id__price__gte=price1, fruit_id__price__lte=price2).all()
    if request.method == 'GET':
        # 将查询到的数据渲染到html模板中
        # 从查询参数中获取价格区间[price1,price2]

        # 根据价格区间查询满足条件所有水果信息

        login_is = request.COOKIES.get('is_login')
        if login_is:
            name1 = request.COOKIES.get('name')
        return render(request, 'fruit/list.html', locals())

    if request.method == "POST":
        ret = ''
        name = request.POST.get('name')
        pwd = request.POST.get('pwd')
        if not all((name, pwd)):
            ret = '用户名或者密码不能为空'
        else:
            # 验证用户是否存在
            user_: UserEntity = UserEntity.objects.filter(name=name).first()
            if user_:
                if check_password(pwd, encoded=user_.password):
                    obj = redirect('/user/find')
                    obj.set_cookie('is_login', True, max_age=20)
                    obj.set_cookie('name', user_.name, max_age=20)
                    return obj
                else:
                    ret = '用户名或密码错误'
            else:
                ret = '用户名不存在，请先注册'
    return render(request, 'fruit/list.html', locals())


def delete_cookie(request):
    name1 = request.COOKIES.get('name')
    is_login = request.COOKIES.get('is_login')

    if is_login:
        obj = redirect('/user/find')
        obj.delete_cookie('is_login')
        obj.delete_cookie('name')
        return obj
