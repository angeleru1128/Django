from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewCreateForm


# Create your views here.

def review_list(request):

    context = {
        'review_list': Review.objects.all().order_by('-created_at'),
    }
    return render(request, 'reviews/reviews_list.html', context)
def review_detail(request, pk):
    context = {
       'review': get_object_or_404(Review, pk=pk)
    }
    return render(request, 'reviews/review_detail.html', context)

#口コミ作成ページが表示される
def review_create(request):
    form = ReviewCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('reviews:review_list')

    context = {
        'form': form
    }
    return render(request, 'reviews/review_form.html', context)

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    form = ReviewCreateForm(request.POST or None, instance=review)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('reviews:review_list')

    context = {
        'form': form
    }
    return render(request, 'reviews/review_form.html', context)

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
       review.delete()
       return redirect('reviews:review_list')

    context = {
        'review': review
    }
    return render(request, 'reviews/review_confirm_delete.html', context)