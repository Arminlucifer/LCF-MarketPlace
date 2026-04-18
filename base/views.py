from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from . models import Category, Product, Comment, CommentLike
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from . forms import ProductForm








def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    input = request.GET.get('q')

    products = Product.objects.filter(
        Q(category__name__icontains=q) |
        Q(name__icontains=q) |
        Q(seller__name__icontains=q)
    )
    product_count = products.count()



    now = timezone.now()
    products_data = []

    for product in products:
        time_diff = now - product.added
        upload_time_str = ''
        if time_diff < timedelta(minutes=1):
            upload_time_str = 'just now!'
        elif time_diff < timedelta(hours=1):
            minutes = int(time_diff.total_seconds() // 60)
            upload_time_str = f'{minutes} minutes ago!'
        elif time_diff < timedelta(days=1):
            hours = int(time_diff.total_seconds() // 3600)
            upload_time_str = f'{hours} hours ago!'
        elif time_diff < timedelta(days=7):
            days = int(time_diff.total_seconds() // 86400)
            upload_time_str = f'{days} days ago!'
        elif time_diff < timedelta(days=30):
            weeks = int(time_diff.total_seconds() // (7 * 86400))
            upload_time_str = f'{weeks} weeks ago!'
        elif time_diff < timedelta(days=365):
            months = int(time_diff.total_seconds() // (30 * 86400))
            upload_time_str = f'{months} months ago!'
        else:
            upload_time_str = f'{product.added}'

        products_data.append({'product': product, 'upload_time': upload_time_str})

    context = {'products_data': products_data, 'product_count': product_count, "input": input}




    return render(request, 'base/home.html', context)



@login_required(login_url='login')
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    main_comments = Comment.objects.filter(
        parent__isnull=True
    ).annotate(
        like_count=Count('likes', distinct=True),

        reply_count=Count('replies')
    ).order_by('-reply_count', '-like_count',)


    comments_data = []
    for comment in main_comments:

        is_liked = False
        if request.user.is_authenticated:

            is_liked = comment.likes.filter(user=request.user).exists()

        comments_data.append({
            'comment': comment,
            'like_count': comment.like_count,
            'is_liked': is_liked,
            'reply_count': comment.reply_count,
        })


    context = {'product': product, 'comments_data': comments_data}




    return render(request, 'base/product_detail.html', context)


def comment_replies(request, id):
    page = 'comment_replies'
    parent_comment = get_object_or_404(Comment, id=id)


    replies = Comment.objects.filter(parent = parent_comment).annotate(
        like_count=Count('likes'),
        reply_count=Count('replies')
    ).order_by('-reply_count', '-like_count')

    replies_data = []
    if request.user.is_authenticated:
        for reply in replies:
            is_liked = reply.likes.filter(user=request.user).exists()
            replies_data.append({
                'reply': reply,
                'like_count': reply.like_count,
                'is_liked': is_liked,

            })
    else:

        for reply in replies:
            replies_data.append({
                'reply': reply,
                'like_count': reply.like_count,
                'is_liked': False,
                'reply_count': reply.reply_count,
            })

    context = {
        'replies': replies_data,
        'parent_comment': parent_comment,
        'page': page
    }



    return render(request, 'base/product_detail.html', context)



def toggle_like(request, id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=id)


    like_obj = CommentLike.objects.filter(
        user=request.user,
        comment=comment
    )

    if like_obj.exists():

        like_obj.delete()
    else:

        CommentLike.objects.create(
            user=request.user,
            comment=comment
        )


    return redirect("product_detail", id=comment.product.id)



@login_required
def post_ad(request):
        categories = Category.objects.all()

        if request.method == 'POST':

            form = ProductForm(request.POST, request.FILES)

            if form.is_valid():
                product = form.save(commit=False)
                product.seller = request.user
                product.save()
                return redirect('home')



        else:
            form = ProductForm()

        context = {'form': form, 'categories': categories}
        return render(request, 'base/ad_form.html', context)





