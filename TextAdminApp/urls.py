from django.urls import path
from TextAdminApp import views

urlpatterns =[
    path('index/',views.index,name="index"),
    path('demo/',views.demo,name="demo"),
    path('category/',views.category,name="category"),
    path('cdetails/',views.cdetails,name="cdetails"),
    path('save_category/',views.save_category,name="save_category"),
    path('editcat/<int:c_id>/',views.editcat,name="editcat"),
    path('updatecat/<int:ca_id>/',views.updatecat,name="updatecat"),
    path('delete_category/<int:c_id>/',views.delete_category,name="delete_category"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('save_product/',views.save_product,name="save_product"),
    path('pr_display/',views.pr_display,name="pr_display"),
    path('editproduct/<int:p_id>/',views.editproduct,name="editproduct"),
    path('delete_product/<int:pr_id>/',views.delete_product,name="delete_product"),
    path('update_product/<int:pr_id>/',views.update_product,name="update_product"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogin_save/',views.adminlogin_save,name="adminlogin_save"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('contact_details/',views.contact_details,name="contact_details"),
    path('delete_contact/<int:con_id>/',views.delete_contact,name="delete_contact"),
    path('User_details/',views.user_details,name="User_details"),
    path('delete_user/<int:user_id>/',views.delete_user,name="delete_user"),
]