from django.views.generic import CreateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect

from rest_framework import viewsets

from noxtwitter import models, serializers


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

    http_method_names = ['get', 'post']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ToggleLikeView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        post_id = request.POST.get('post_id')
       
        if post_id:
            post = models.Post.objects.get(id=post_id)
            user = request.user

            if post.liked_by.filter(id=user.id).first():
                post.liked_by.remove(user)
            else:
                post.liked_by.add(user)

        return redirect(reverse_lazy('post_list'))


class PostListView(LoginRequiredMixin, ListView):
    model = models.Post
    template_name = 'post_list.html'
    paginate_by = 10


class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    fields = ['content']
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_list')
