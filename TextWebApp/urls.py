from django.urls import path
from TextWebApp import views

urlpatterns = [
    path('Home/',views.home,name="Home"),
    path('About/',views.about,name="About"),
    path('Contact/',views.contact,name="Contact"),
    path('Save_Contact/',views.save_contact,name="Save_Contact"),
    path('Products/',views.products,name="Products"),
    path('Single_product/<int:pr_id>/',views.single_product,name="Single_product"),
    path('Filter_products/<cat_name>/',views.filter_products,name="Filter_products"),
    path('',views.signin,name="Signin"),
    path('Create_Account/',views.create_account,name="Create_Account"),
    path('save_createaccount/',views.save_createaccount,name="save_createaccount"),
    path('save_signin/',views.save_signin,name="save_signin"),
    path('Logout_user/',views.logout_user,name="Logout_user"),
    path('Save_Cart/',views.save_cart,name="Save_Cart"),
    path('Cart/',views.cart,name="Cart"),
    path('Delete_item/<int:ca_id>/',views.delete_item,name="Delete_item"),
    path('Checkout/',views.checkout,name="Checkout"),
    path('Payment/',views.payment,name="Payment"),
    path('Save_order/',views.save_order,name="Save_order"),
]