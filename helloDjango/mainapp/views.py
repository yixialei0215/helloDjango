from django.http import HttpResponse
from django.shortcuts import render, redirect

from mainapp.models import UserEntity, FruitEntity, StoreEntity


# Create your views here.

def user_list(request):
    datas = [
        {'id': 101, 'name': '王杰超'},
        {'id': 102, 'name': '王宇辰'},
        {'id': 103, 'name': '王栋平'}
    ]
    return render(request, 'user/list.html', {'datas': datas,
                                              'msg': '姓王的成员'})


def user_list2(request):
    datas = [
        {'id': 101, 'name': '王杰超'},
        {'id': 102, 'name': '王宇辰'},
        {'id': 103, 'name': '王栋平'}
    ]
    msg = '姓王的成员'
    return render(request, 'user/list.html', locals())


# 增加
def add_user(request):
    # 从GET请求中读取数据
    # request.GET.get('name')
    # request.GET 是一个dict字典类型，保存的是查询参数
    name = request.GET.get('name', None)
    age = request.GET.get('age', None)
    phone = request.GET.get('phone', None)

    if all((name, age, phone)):
        UserEntity(name=name, age=age, phone=phone).save()
    else:
        return HttpResponse("<h3 style='color:red'>请求参数不完整</h3>", status=400)

    return redirect('/user/list')


# 变更
def update_user(request):
    # 查询参数有id,name,phone
    # 通过模型查询id的用户是否存在
    # Model.objects.get()可能会出现异常-- 尝试捕获
    id = request.GET.get('id', None)
    name = request.GET.get('name', None)
    age = request.GET.get('age', None)
    phone = request.GET.get('phone', None)
    if not id:
        return HttpResponse("<h3 style='color:red'>请输入要更改的人的id</h3>", status=400)
    try:
        u = UserEntity.objects.get(pk=int(id))

        if any((name, age, phone)):
            if name:
                u.name = name
            if age:
                u.age = age
            if phone:
                u.phone = phone
        u.save()
        return redirect('/user/list')
    except:
        return HttpResponse("<h3 style='color:red'>查无此人</h3>", status=404)


# 删除
def delete_user(request):
    id = request.GET.get('id', None)
    if not id:
        return HttpResponse("<h3 style='color:red'>请传入正确的参数</h3>", status=400)
    try:
        u = UserEntity.objects.get(pk=int(id))
    except:
        return HttpResponse("<h3 style='color:red'>查无此人</h3>", status=404)
    u.delete()
    html = """
    <p>%s 删除成功! 三秒后自动跳转<a href='/user/list'>列表</a>
    </p>
    <script>
        setTimeout(function(){
            open('/user/list',target='_self')
        },3000)
    </script>
    """ % id
    return HttpResponse(html)


def user_list3(request):
    datas = UserEntity.objects.all()
    msg = '会员'
    return render(request, 'user/list.html', locals())


def find_fruit(request):
    # 从查询参数中获取价格区间[price1,price2]
    price1 = request.GET.get('price1', 0)
    price2 = request.GET.get('price2', 1000)
    # 根据价格区间查询满足条件所有水果信息
    fruits = FruitEntity.objects.filter(price__gte=price1,
                                        price__lte=price2) \
        .exclude(price=250) \
        .filter(name__contains='果') \
        .all()
    # 将查询到的数据渲染到html模板中
    return render(request, 'fruit/list.html', locals())


def find_store(request):
    # 查询2019年开业的水果店
    # 查询参数：year
    stores = StoreEntity.objects.filter(create_time__month__gt=6).all()

    return render(request, 'store/list.html', locals())
