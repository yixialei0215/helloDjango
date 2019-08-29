from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from mainapp.models import UserEntity, FruitEntity, StoreEntity, FruitImage
from django.db.models import Count, Sum, Min, Max, Avg, F, Q


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
    fruits = FruitImage.objects \
        .values('url', 'fruit_id__name', 'fruit_id__price', 'fruit_id__source', 'width', 'height') \
        .filter(fruit_id__price__gte=price1, fruit_id__price__lte=price2).all()
    # 将查询到的数据渲染到html模板中
    return render(request, 'fruit/list.html', locals())


def find_store(request):
    # 查询2019年开业的水果店
    # 查询参数：year
    queryset = StoreEntity.objects.filter(create_time__year__gt=2010).order_by('id', 'city')

    first_store = queryset.first()  # 模型类的实例对象
    stores = queryset.all().filter(name='西安')  # ?? 返回还是queryset吗?

    return render(request, 'store/list.html', locals())


def all_store(request):
    # 返回所有水果店json 数据
    result = {}
    if StoreEntity.objects.exists():
        datas = StoreEntity.objects.values()
        print(type(datas))  # 是一个QuerySet<{},{}>

        store_list = []
        for store in datas:
            store_list.append(store)

        result['data'] = store_list
        result['total'] = StoreEntity.objects.count()
    else:
        result['msg'] = '数据是空的'

    return JsonResponse(result)


def count_fruit(request):
    # 返回json数据，统计每种分类的水果数量，最高价格，最低价格和总价格
    result = FruitEntity.objects.aggregate(cnt=Count('name'),
                                           max=Max('price'),
                                           min=Min('price'),
                                           avg=Avg('price'),
                                           sum=Sum('price'))
    # 中秋节：全场水果打8.8折扣
    # FruitEntity.objects.update(price=F('price') * 1.88)
    fruits = FruitEntity.objects.values()

    # 查询价格低于1的或高于200的，或原产地是西安且名称中包含“果”
    fruit2 = FruitEntity.objects.filter(
        Q(price__lte=1) | Q(price__gte=200) | Q(Q(source='西安') & Q(name__contains='果'))).values()

    # raw()
    fruit3 = FruitEntity.objects.raw('select * from t_fruit')
    for fruit in fruit3:
        print(fruit.name)
    return JsonResponse({
        'content': result,
        'fruits': [fruit for fruit in fruit2]
    })


def delete_fruit(request):
    result = FruitEntity.objects.filter(name='哈密瓜').delete()
    print(result)

    return render(request, 'fruit/delete.html', locals())
