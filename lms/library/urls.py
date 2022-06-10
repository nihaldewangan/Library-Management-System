from django.urls import path
from .views import list_books, book_detail, add_book, update_book, delete_book, signup, login

urlpatterns = [
    path("admin_signup/", signup, name="admin-signup"),
    path("login/", login, name="signin"),
    path('books/', list_books, name="book-list"),
    path('book-add/', add_book, name="create-book"),
    path('book-detail/<int:pk>', book_detail, name="book-detail"),
    path('book-update/<int:pk>', update_book, name="book-update"),
    path('book-delete/<int:pk>', delete_book, name="book-delete")
]