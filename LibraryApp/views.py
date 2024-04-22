

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Member, Borrow, Reservation, Fine
from .forms import BookForm, MemberForm, BorrowForm, ReservationForm, FineForm

# Views for Book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book/add_book.html', {'form': form})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/edit_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/book_list.html', {'books': books})

# Views for Member
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'member/add_member.html', {'form': form})

def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'member/edit_member.html', {'form': form})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'member/member_list.html', {'members': members})

# Views for Borrow
def add_borrow(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('borrow_list')
    else:
        form = BorrowForm()
    return render(request, 'borrow/add_borrow.html', {'form': form})

def edit_borrow(request, pk):
    borrow = get_object_or_404(Borrow, pk=pk)
    if request.method == 'POST':
        form = BorrowForm(request.POST, instance=borrow)
        if form.is_valid():
            form.save()
            return redirect('borrow_list')
    else:
        form = BorrowForm(instance=borrow)
    return render(request, 'borrow/edit_borrow.html', {'form': form})

def borrow_list(request):
    borrows = Borrow.objects.all()
    return render(request, 'borrow/borrow_list.html', {'borrows': borrows})

# Views for Reservation
def add_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservation/add_reservation.html', {'form': form})

def edit_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservation/edit_reservation.html', {'form': form})

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation/reservation_list.html', {'reservations': reservations})

# Views for Fine
def add_fine(request):
    if request.method == 'POST':
        form = FineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fine_list')
    else:
        form = FineForm()
    return render(request, 'fine/add_fine.html', {'form': form})

def edit_fine(request, pk):
    fine = get_object_or_404(Fine, pk=pk)
    if request.method == 'POST':
        form = FineForm(request.POST, instance=fine)
        if form.is_valid():
            form.save()
            return redirect('fine_list')
    else:
        form = FineForm(instance=fine)
    return render(request, 'fine/edit_fine.html', {'form': form})

def fine_list(request):
    fines = Fine.objects.all()
    return render(request, 'fine/fine_list.html', {'fines': fines})

def index(request):
    return render(request, 'index.html')

def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_list.html')

def delete_member(request, member_id):
    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'member_list.html')