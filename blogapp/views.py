from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Post, Category, Comment, About, Privacy, Terms
from .forms import CreateForm, CommentForm, AboutForm, PrivacyForm, TermForm
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger
from django.db.models import Count
from django.contrib import messages


def home_view(request, tag_slug=None):
    # display only published posts
    object_list = Post.objects.filter(status=1).order_by('-date_created')
    categories = Category.objects.all()
    all_tags = Tag.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags=tag)
        
    # pagination
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')
    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        object_list = paginator.page(1)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
    return render(request, 'blogapp/home.html', {'object_list': object_list,
                                                 'page': page, 'all_tags': all_tags,
                                                 'categories': categories,
                                                 'tag': tag})



def category_view(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    object_list = Post.objects.all()
    all_tags = Tag.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        object_list = object_list.filter(category=category)
    return render(request, 'blogapp/category.html', {'category': category,
                                                     'categories': categories
        , 'object_list': object_list,
        'all_tags': all_tags})



def detail_view(request, slug, *args, **kwargs):
    post = get_object_or_404(Post, slug=slug)
    categories = Category.objects.all()
    all_tags = Tag.objects.all()
    comments = post.comments.filter(active=True, parent__isnull=True)
    new_comment = None
    comment_count = post.comments.count()
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = get_object_or_404(Comment, id=parent_id)
                if parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.parent = parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.name = request.user
            new_comment.post = post
            new_comment.save()
            messages.success(request, "your comment was sucessfully uploaded!")
            return redirect('blogapp:detail', slug=post.slug)
    else:
        comment_form = CommentForm()
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids) \
        .exclude(id=post.id)  # related posts
    similar_posts = similar_posts.annotate(same_tags=Count('tags')) \
                        .order_by('-same_tags')[:4]  # related posts

    return render(request, 'blogapp/detail.html', {'post': post, 'all_tags': all_tags,
                                                   'categories': categories,
                                                   'similar_posts': similar_posts,
                                                   'comments': comments,
                                                   'new_comment':new_comment,
                                                   'comment_form': comment_form,
                                                   'comment_count': comment_count,

                                                   })


class CreatePostView(CreateView):
    model = Post
    template_name = 'blogapp/create.html'
    context_object_name = 'blog_list'
    fields = ['title', 'category', 'tags', 'content', 'image', 'image_credit', 'status']
    success_url = reverse_lazy('blogapp:home')
    
    def form_valid(self, form):
        # Setting the author to the current user
        form.instance.author = self.request.user  
        return super().form_valid(form)



class CreateCategoryView(CreateView):
    model = Category
    template_name = 'blogapp/add_category.html'
    fields = ['name',]
    success_url = reverse_lazy('blogapp:home')

class EditView(UpdateView):
    model = Post
    template_name = 'blogapp/edit_post.html'
    fields = ['title', 'category', 'tags', 'content', 'image', 'image_credit', 'author']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blogapp:home')

class Delete(DeleteView):
    model = Post
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blogapp:home')
    template_name = 'blogapp/delete.html'


def about_view(request):
    about = About.objects.all().first()
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AboutForm()
    return render(request, 'blogapp/about.html', {'form': form, 'about': about})

def terms_view(request):
    terms = Terms.objects.all().first()
    if request.method == 'POST':
        form = TermForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TermForm()
    return render(request, 'blogapp/terms.html', {'form': form, 'terms': terms})

def privacy_view(request):
    privacy = Privacy.objects.all().first()
    if request.method == 'POST':
        form = PrivacyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PrivacyForm()
    return render(request, 'blogapp/privacy.html', {'form': form, 'privacy': privacy})

def error_404(request, exception):
    return render(request, '404.html')