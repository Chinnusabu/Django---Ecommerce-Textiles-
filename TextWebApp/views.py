from django.shortcuts import render,redirect
from TextWebApp.models import ContactDB,CreateAccountDB,CartDB,OrderDB
from TextAdminApp.models import addcat
from TextAdminApp.models import ProductDB
from django.contrib import messages
import razorpay



# Create your views here.
def home(request):
    cate = addcat.objects.all()
    product = ProductDB.objects.all()
    return render(request,"Home.html",{'cate':cate,'product':product})
def about(request):
    cate = addcat.objects.all()
    return render(request,"About.html",{'cate':cate})
def contact(request):
    cate = addcat.objects.all()
    return render(request,"Contact.html",{'cate':cate})
def save_contact(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        ms = request.POST.get('msg')
        obj = ContactDB(Name=na, Email=em, Message=ms)
        obj.save()
        return redirect(contact)

def products(request):
    cate = addcat.objects.all()
    product = ProductDB.objects.all()
    return render (request,"Products.html",{'product':product,'cate':cate})
def single_product(request,pr_id):
    cate = addcat.objects.all()
    pr_details = ProductDB.objects.get(id=pr_id)
    return render(request,"Single_Product.html",{'pr_details':pr_details,'cate':cate})
def filter_products(request,cat_name):
    cate = addcat.objects.all()
    cat_datas = ProductDB.objects.filter (Category_Name=cat_name)
    return render(request,"Filter_Products.html",{'cat_datas':cat_datas,'cate':cate})

def signin(request):

    return render(request,"Signin.html")
def create_account(request):
    return render(request,"Create_Account.html")
def save_createaccount(request):
    if request.method=="POST":
        fn = request.POST.get('user1')
        ln = request.POST.get('user2')
        us = request.POST.get('user')
        em = request.POST.get('email')
        pa = request.POST.get('pass1')

        obj = CreateAccountDB(First_Name=fn, Last_Name=ln,Username= us, Email_Id=em,Password=pa)
        obj.save()
        return redirect(signin)
def save_signin(request):
    if request.method=="POST":
        use = request.POST.get('username')
        pas = request.POST.get('password')
        if CreateAccountDB.objects.filter(Username=use,Password=pas).exists():
            request.session['Username'] = use
            request.session['Password'] = pas
            return redirect(home)
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect(signin)
    else:
        messages.error(request, "Invalid Username or Password")
        return redirect(signin)
def logout_user(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(home)

def save_cart(request):
    if request.method == "POST":
        un = request.POST.get('user')
        pr = request.POST.get('prname')
        qu = request.POST.get('quantity')
        pri = request.POST.get('price')
        tot = request.POST.get('total')
        obj = CartDB(User_Name=un, Product_Name=pr, Quantity=qu,  Price=pri, Total_Price=tot)
        obj.save()
        messages.success(request,"Added to Cart")
        return redirect(home)
def cart(request):
    cart_datas = CartDB.objects.filter(User_Name=request.session['Username'])
    cate = addcat.objects.all()
    sub_total = 0
    shipping = 0
    total = 0
    for i in cart_datas:
        sub_total += i.Total_Price
        if sub_total>3000:
            shipping = 00
        elif sub_total>2000:
            shipping = 50
        else :
            shipping =100
        total = sub_total+shipping
    return render(request,"Cart.html",{'cart_datas':cart_datas,'cate':cate,'sub_total':sub_total,'shipping':shipping,'total':total})
def delete_item(request,ca_id):
    x = CartDB.objects.filter(id=ca_id)
    x.delete()
    messages.warning(request, "Product Removed from Cart")
    return redirect(cart)
def checkout(request):
    cate = addcat.objects.all()
    cart_datas = CartDB.objects.filter(User_Name=request.session['Username'])
    sub_total = 0
    shipping = 0
    total = 0
    for i in cart_datas:
        sub_total += i.Total_Price
        if sub_total > 3000:
            shipping = 00
        elif sub_total > 2000:
            shipping = 50
        else:
            shipping = 100
        total = sub_total + shipping
    return render(request,"Checkout.html",{'cart_datas': cart_datas,'cate':cate,'sub_total':sub_total,'shipping':shipping,'total':total})

def payment(request):
    customer = OrderDB.objects.order_by('-id').first()

    pay = customer.Total_Amount

    amount = int(pay*100)

    pay_str = str(amount)

    for i in pay_str:
        print(i)

    if request.method == "POST":
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_JvlnDxuSOwluJp', '58RFuAHoBlTlUeH6DJYL1tJo'))
        payment = client.order.create({'amount':amount,'currency': order_currency})
    return render (request,"Payment.html",{'customer':customer, 'pay_str':pay_str})
def save_order(request):
    if request.method == "POST":
        na = request.POST.get('name')
        em = request.POST.get('mail')
        mo = request.POST.get('mobile')
        ad = request.POST.get('address')
        co = request.POST.get('country')
        ci = request.POST.get('city')
        me = request.POST.get('message')
        to = request.POST.get('total')
        obj = OrderDB(Name=na, Email=em, Mobile=mo, Address=ad, Country=co, City=ci, Message=me, Total_Amount=to)
        obj.save()
        return redirect(payment)