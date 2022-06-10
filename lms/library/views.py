from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import login, authenticate

from library.serializers import BookSerializer
from .models import Book, User


# View methods
def signup(request):
    context = {}
    if request.method == "POST":
        print (request.POST)
        if not request.POST.get("email", None):
            context["signup_error"] = "Email required!"
        elif not request.POST.get("password", None):
            context["signup_error"] = "Password required!"
        elif not request.POST.get("first_name", None) or not request.POST.get("last_name", None):
            context["signup_error"] = "First and/or last name required!"
        
        if not context.get("signup_error", False): # if form data is validated, proceed with signup
            try:
                user = User.objects.get(email=request.POST.get("email"))
                context["signup_error"] = "Admin with same email address already exists."
            except User.DoesNotExist:
                new_admin = User()
                new_admin.first_name = request.POST.get("first_name", "")
                new_admin.last_name = request.POST.get("last_name", "")
                new_admin.username = f"{request.POST.get('first_name', '').lower()}-{request.POST.get('last_name', '').lower()}"
                new_admin.email = request.POST.get("email")
                new_admin.set_password(request.POST.get("password"))
                new_admin.is_staff = True
                new_admin.save()

                context["signup_success"] = "Admin created successfully."


    return render(request, "admin_signup.html", context)

def login(request):
    context = {}
    if request.method == "POST":
        print (request.POST)
        if not request.POST.get("email", None):
            context["signup_error"] = "Email required!"
        elif not request.POST.get("password", None):
            context["signup_error"] = "Password required!"
        
        try:
            user = authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
            if user:
                return redirect("/books/")
        except User.DoesNotExist:
            context["signin_error"] = f"User with this email address: '{request.POST.get('email')}' does not exists."


    return render(request, "login.html", context)


# APIs

# Create
@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({"msg": "Name and/or price not provided."})
    return Response(serializer.data)

# Retrieve
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_books(request):
    serializer = BookSerializer(Book.objects.all(), many=True)
    data = serializer.data
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def book_detail(request, pk):
    serializer = BookSerializer(get_object_or_404(Book, id=pk))
    data = serializer.data
    return Response(data)

# Update
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({"msg": "Name and/or price not provided."})
    return Response(serializer.data)

# Delete
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_book(request, pk):
    book = get_object_or_404(Book, id=pk)
    book.delete()
    return Response({"msg" : "Book deleted successfully."})
