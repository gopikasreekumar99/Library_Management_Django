from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # URLs for Book
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('book_list/', views.book_list, name='book_list'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    # URLs for Member
    path('add_member/', views.add_member, name='add_member'),
    path('edit_member/<int:pk>/', views.edit_member, name='edit_member'),
    path('member_list/', views.member_list, name='member_list'),
    path('delete_member/<int:member_id>/', views.delete_member, name='delete_member'),

    # URLs for Borrow
    path('add_borrow/', views.add_borrow, name='add_borrow'),
    path('edit_borrow/<int:pk>/', views.edit_borrow, name='edit_borrow'),
    path('borrow_list/', views.borrow_list, name='borrow_list'),

    # URLs for Reservation
    path('add_reservation/', views.add_reservation, name='add_reservation'),
    path('edit_reservation/<int:pk>/', views.edit_reservation, name='edit_reservation'),
    path('reservation_list/', views.reservation_list, name='reservation_list'),

    # URLs for Fine
    path('add_fine/', views.add_fine, name='add_fine'),
    path('edit_fine/<int:pk>/', views.edit_fine, name='edit_fine'),
    path('fine_list/', views.fine_list, name='fine_list'),
]
