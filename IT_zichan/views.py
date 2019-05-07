from django.shortcuts import render,redirect
from IT_zichan.models import IT_assets_pc,Collect_employee_information_PC

# Create your views here.


def Collect_employee_information(request):
    if request.method == 'POST':
        info = request.POST.get('User_Englishname')
        User_Chinesename = request.POST.get('User_Chinesename')
        Product_Name = request.POST.get('Product_Name')
        Amount = request.POST.get('Amount')
        Attribution_Dept = request.POST.get('Attribution_Dept')
        Number_Pc = request.POST.get('Number_Pc')
        Brand = request.POST.get('Brand')
        xinghao = request.POST.get('xinghao')
        Service_Tag = request.POST.get('Service_Tag')
        E_Service = request.POST.get('E_Service')
        """#将数据添加到数据库中"""
        Collect_employee_information_PC.objects.create(User_Englishname = info,
                                                       User_Chinesename = User_Chinesename,
                                                       Product_Name = Product_Name,
                                                       Amount =Amount,
                                                       Attribution_Dept = Attribution_Dept,
                                                       Number_Pc =Number_Pc,
                                                       Brand =Brand,
                                                       xinghao = xinghao,
                                                       Service_Tag = Service_Tag,
                                                       E_Service =E_Service )
        #跳转到列表总
        return render(request,'index.html')
    else:
        return render(request,'Collect_employee_information.html',)



def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'test.html')