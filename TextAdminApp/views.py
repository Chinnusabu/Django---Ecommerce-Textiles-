from django.shortcuts import render,redirect
from TextAdminApp.models import addcat,ProductDB
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from TextWebApp.models import ContactDB,CreateAccountDB
from django.contrib import messages

# Create your views here.
def index(page):
    return render(page,"index.html")
def demo(page):
    return render(page,"DEMO.html")
def category(page):
    return render(page,"Addcategory.html")
def cdetails(page):
    data = addcat.objects.all()
    return render(page,"Category_Details.html",{'data':data})
def save_category(request):
    if request.method == "POST":
        ca =request.POST.get('cate')
        de =request.POST.get('cdesc')
        im = request.FILES['cimage']
        obj = addcat(Category =ca, Description=de,Image=im)
        obj.save()
        messages.success(request,"Category Added Successfully")
        return redirect(category)

def editcat(page,c_id):
    data = addcat.objects.get(id=c_id)
    return render(page,"Edit_category.html",{'data':data})
def updatecat(request,ca_id):
    if request.method == "POST":
        ca = request.POST.get('cate')
        de = request.POST.get('cdesc')
        try :
            im = request.FILES['cimage']
            fs = FileSystemStorage()
            file = fs.save(im.name,im)
        except MultiValueDictKeyError :
            file =addcat.objects.get(id=ca_id).Image
        addcat.objects.filter(id=ca_id).update(Category =ca, Description=de,Image=file)
        messages.success(request, "Category Updated Successfully")
        return redirect(cdetails)
def delete_category(request,c_id):
    x = addcat.objects.filter(id=c_id)
    x.delete()
    messages.warning(request,"Category Deleted...!")
    return redirect(cdetails)
def addproduct(page):
    category = addcat.objects.all()
    return render(page,"Add_Product.html",{'category':category})
def save_product(request):
    if request.method=="POST":
        ca = request.POST.get('pcate')
        pro = request.POST.get('prname')
        de = request.POST.get('pdesc')
        pri = request.POST.get('price')
        br = request.POST.get('pbrand')
        im1 = request.FILES['pimg1']
        im2 = request.FILES['pimg2']
        im3 = request.FILES['pimg3']
        obj = ProductDB(Category_Name=ca, Product=pro, Pr_Description=de, Price=pri, Brand=br, Pr_Image1=im1, Pr_Image2=im2, Pr_Image3=im3)
        obj.save()
        messages.success(request, "Product Added Successfully")
        return redirect(addproduct)
def pr_display(page):
    products = ProductDB.objects.all()
    return render(page,"Product_Display.html",{'products':products})
def editproduct(request,p_id):
    data = ProductDB.objects.get(id=p_id)
    cat = addcat.objects.all()
    return render(request,"Edit_Product.html",{'data':data,'cat':cat})
def delete_product(page,pr_id):
    y = ProductDB.objects.filter(id=pr_id)
    y.delete()
    messages.error(page, "Product Deleted...!")
    return redirect(pr_display)
def update_product(request,pr_id):
    if request.method=="POST":
        ca = request.POST.get('pcate')
        pro = request.POST.get('prname')
        de = request.POST.get('pdesc')
        pri = request.POST.get('price')
        br = request.POST.get('pbrand')
        try :
            im1 =request.FILES['pimg1']
            fs = FileSystemStorage()
            file1 = fs.save(im1.name, im1)
        except MultiValueDictKeyError:
            file1 = ProductDB.objects.get(id=pr_id).Pr_Image1
        try:
            im2 = request.FILES['pimg2']
            fs = FileSystemStorage()
            file2 = fs.save(im2.name, im2)
        except MultiValueDictKeyError:
            file2 = ProductDB.objects.get(id=pr_id).Pr_Image2
        try:
            im3 = request.FILES['pimg3']
            fs = FileSystemStorage()
            file3 = fs.save(im3.name, im3)
        except MultiValueDictKeyError:
            file3 = ProductDB.objects.get(id=pr_id).Pr_Image3
        ProductDB.objects.filter(id=pr_id).update(Category_Name=ca, Product=pro, Pr_Description=de, Price=pri, Brand=br, Pr_Image1=file1, Pr_Image2=file2, Pr_Image3=file3)
        messages.success(request, "Product Updated Successfully")
        return redirect(pr_display)
def adminlogin(request):
    return render(request,"AdminLogin.html")
def adminlogin_save(request):
    if request.method == "POST":
        un = request.POST.get('user')
        pa = request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pa)
            if x is not None:
                login(request,x)
                request.session['username'] = un
                request.session['password'] = pa
                messages.success(request,"Welcome...!")
                return redirect(index)
            else:
                messages.warning(request,"Invalid Username or Password..!")
                return redirect(adminlogin)
        else:
            messages.warning(request, "User not found..!")
            return redirect(adminlogin)
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)
def contact_details(request):
    details = ContactDB.objects.all()
    return render(request,"Contact_Details.html",{'details':details})
def delete_contact(request,con_id):
    z = ContactDB.objects.filter(id=con_id)
    z.delete()
    return redirect(contact_details)
def user_details(request):
    user_data= CreateAccountDB.objects.all()
    return render(request,"User_Details.html",{'user_data':user_data})
def delete_user(request,user_id):
    z = CreateAccountDB.objects.filter(id=user_id)
    z.delete()
    return redirect(user_details)
