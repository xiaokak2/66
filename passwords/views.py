# Create your views here.
from django.contrib import messages

from .forms import PasswordForm
from .forms import ZhangDnaForm
from .models import PasswordEntry
from .models import TheUserEntry
from .models import ZhangDna


def validate_username(username):
    if len(username) < 6 or len(username) > 20:
        return False
    return True


def validate_password(password):
    if len(password) < 6 or len(password) > 20:
        return False
    return True


# home
def home(request):
    passwords = PasswordEntry.objects.all()
    return render(request, 'passwords111/home.html', {'passwords': passwords})


# 登录页面
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 检查用户是否存在
        if TheUserEntry.objects.filter(theusername=username).exists():
            user = TheUserEntry.objects.get(theusername=username)
            if user.thepassword == password:
                return redirect('index')
            else:
                return render(request, 'passwords111/login.html', {'error': '密码错误'})
        else:
            return render(request, 'passwords111/login.html', {'error': '用户不存在'})

    else:
        return render(request, 'passwords111/login.html')


# 注册页面
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if not validate_username(username):
                return render(request, 'passwords111/register.html', {'error': '用户名不符合，请输入6-20个字符。'})

            if not validate_password(password1):
                return render(request, 'passwords111/register.html', {'error': '密码不符合，请输入6-20个字符。'})

            # 检查用户名是否已存在
            if TheUserEntry.objects.filter(theusername=username).exists():
                return render(request, 'passwords111/register.html', {'error': '该用户名已经被注册。'})

            # 保存用户到数据库
            TheUserEntry.objects.create(theusername=username, thepassword=password1)
            return redirect('home')
        else:
            return render(request, 'passwords111/register.html', {'error': '两次输入的密码不一致。'})
    else:
        return render(request, 'passwords111/register.html')


# 首页
def index(request):
    return render(request, 'passwords111/index.html')


# 密码本
# 1.密码显示页面
def mimabook(request):
    passwords = PasswordEntry.objects.all()
    return render(request, 'passwords111/mimabook.html', {'passwords': passwords})


# 密码添加页面
def add_password(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mimabook')
    else:
        form = PasswordForm()
    return render(request, 'passwords111/add_password.html', {'form': form})


# 密码删除
def delete_password(request, id):
    password = get_object_or_404(PasswordEntry, id=id)
    if request.method == 'POST':
        # 确认用户确实想要删除密码记录
        if 'confirm' in request.POST:
            password.delete()
            messages.success(request, '密码记录已成功删除。')
        else:
            messages.error(request, '删除操作已取消。')
        # 重定向到密码列表页面
        return redirect('mimabook')
    # 如果不是POST请求，则显示确认对话框
    else:
        # 可以在这里创建一个表单或者直接使用一个确认页面
        return render(request, 'passwords111/delete_password.html', {'password': password})


# 密码修改
def rect_password(request, id):
    if request.method == 'POST':
        password = PasswordEntry.objects.get(id=id)
        form = PasswordForm(request.POST, instance=password)
        if form.is_valid():
            form.save()
            return redirect('mimabook')
    else:
        password = PasswordEntry.objects.get(id=id)
        form = PasswordForm(instance=password)
    return render(request, 'passwords111/rect_password.html', {'form': form})


# 记事本
# def notbook(request):
#     return render(request, 'passwords111/notbook.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Notebook
from .forms import NotebookForm


def notebook_list(request):
    notebooks = Notebook.objects.all()

    return render(request, 'notbook/notbook_list.html', {'notebooks': notebooks})


def notebook_detail(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    return render(request, 'notbook/notbook_detail.html', {'notebook': notebook})


def notebook_new(request):
    if request.method == 'POST':
        form = NotebookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notbook_list')
    else:
        form = NotebookForm()
    return render(request, 'notbook/notbook_form.html', {'form': form})


def notebook_edit(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    if request.method == 'POST':
        form = NotebookForm(request.POST, instance=notebook)
        if form.is_valid():
            form.save()
            return redirect('notbook_detail', pk=notebook.pk)
    else:
        form = NotebookForm(instance=notebook)
    return render(request, 'notbook/notbook_form.html', {'form': form})


def notebook_delete(request, pk):
    notebook = get_object_or_404(Notebook, pk=pk)
    if request.method == 'POST':
        notebook.delete()
        return redirect('notbook_list')
    return render(request, 'notbook/notbook_confirm_delete.html', {'notebook': notebook})


# 记账本

def zhang(request):
    all_zhangs = ZhangDna.objects.all()
    shouru = '支出'
    zhangs = []
    zhangz = []
    into = 0
    spand = 0

    for item in all_zhangs:
        if item.Shouzhi == shouru:
            zhangz.append(item)
            spand += float(item.Jiage)
        else:
            zhangs.append(item)
            into += float(item.Jiage)

    context = {
        'income_list': zhangs,
        'expense_list': zhangz,
        'total_income': into,
        'total_expense': spand,
        'total_assets': into - spand,
    }
    return render(request, 'bill/zhang.html', context)


def add_jizhang(request):
    if request.method == 'POST':
        form = ZhangDnaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('zhang')
    else:
        form = ZhangDnaForm()
    return render(request, 'bill/add_jizhang.html', {'form': form})


def delete_zhang(request, id):
    zhang = get_object_or_404(ZhangDna, id=id)
    if request.method == 'POST':
        # 确认用户确实想要删除账单记录
        if 'confirm' in request.POST:
            zhang.delete()
            messages.success(request, '账单记录已成功删除。')
        else:
            messages.error(request, '删除操作已取消。')
        # 重定向到账单列表页面
        return redirect('zhang')
    # 如果不是POST请求，则显示确认对话框
    else:
        # 可以在这里创建一个表单或者直接使用一个确认页面
        return render(request, 'bill/delete_zhang.html', {'zhang': zhang})


# 联系人
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from .forms import ContactForm


# 显示所有联系人的列表
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact/contact_list.html', {'contacts': contacts})


# 显示单个联系人的详细信息
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact/contact_detail.html', {'contact': contact})


# 创建新的联系人
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})


# 更新现有联系人
def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact/contact_form.html', {'form': form})


# 删除联系人
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contact/contact_confirm_delete.html', {'contact': contact})


# 地址管理
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Addresss
from .forms import AddressForm


def address_list(request):
    addresses = Addresss.objects.all()
    return render(request, 'addresses/address_list.html', {'addresses': addresses})


def address_create(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address_list')
    else:
        form = AddressForm()
    return render(request, 'addresses/address_form.html', {'form': form})


def address_update(request, pk):
    address = Addresss.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address_list')
    else:
        form = AddressForm(instance=address)
    return render(request, 'addresses/address_form.html', {'form': form})


def address_delete(request, pk):
    address = Addresss.objects.get(pk=pk)
    if request.method == 'POST':
        address.delete()
        return redirect('address_list')
    return render(request, 'addresses/address_confirm_delete.html', {'address': address})
