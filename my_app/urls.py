from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.BookListView.as_view(), name='homepage'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.book_detail, name='book_detail'),
    path('<int:book_id>/share/', views.book_share, name='book_share'),
    path('login/', views.login_view, name='login_page'),
    path('signup/', views.SignUpView.as_view(), name='signup_page'),
    path('logout/', views.logout_view, name='logout_page'),
    path('stats/', views.stats_page, name='stats_page') ,
    path('add_book/', views.crudpageadd , name='add_book_page'),
    path('book_list/', views.book_list_page, name='book_list_page'),
    path('edit_book/<int:book_id>/', views.crudpageedit, name='edit_book_page')
]
