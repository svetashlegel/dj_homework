from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from blog.models import Article
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify


class ArticleCreateView(PermissionRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'content', 'preview', 'creation_date')
    permission_required = 'blog.add_article'
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()

        return super().form_valid(form)


class ArticleUpdateView(PermissionRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'content', 'preview', 'creation_date')
    permission_required = 'blog.change_article'

    def form_valid(self, form):
        if form.is_valid():
            new_art = form.save()
            new_art.slug = slugify(new_art.title)
            new_art.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class ArticleDeleteView(PermissionRequiredMixin, DeleteView):
    model = Article
    permission_required = 'blog.delete_article'
    success_url = reverse_lazy('blog:list')
