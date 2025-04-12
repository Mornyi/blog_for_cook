from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import CommentForm


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = "blog/home.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    slug_url_kwarg = 'post_slug'

    def get_object(self, queryset=None):
        return Post.objects.get(
            category__slug=self.kwargs['slug'],
            slug=self.kwargs['post_slug']
        )


class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/post_detail.html'  # Укажите ваш шаблон

    def form_valid(self, form):
        form.instance.author = self.request.user  # Автор = текущий пользователь
        form.instance.post_id = self.kwargs.get('pk')  # Привязка к посту
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_single', kwargs={
            'slug': self.object.post.category.slug,
            'post_slug': self.object.post.slug
        })
