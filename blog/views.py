from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin #as we cant use @login_required decorator in class based views so we import this class
from django.contrib.auth.mixins import UserPassesTestMixin #so only the author of the post can update or delete it
from django.contrib.auth.models import User
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Post


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)


class PostListView(ListView): #in class based view we are just setting some variables
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts' #to tell list view the variable which to be name in the template which we will be looping over
	ordering = ['-date_posted']
	paginate_by = 4


class UserPostListView(ListView): 
	model = Post
	template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
	context_object_name = 'posts' 
	paginate_by = 4

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView): #in class based view we are just setting some variables
	model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','content']
	
	def form_valid(self,form):
		form.instance.author = self.request.user #telling that before we submit the form take that instance and set the author = the current logged in user
		return super().form_valid(form) #running form_valid method on parent class using super()



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title','content']
	
	def form_valid(self,form):
		form.instance.author = self.request.user #telling that before we submit the form take that instance and set the author = the current logged in user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView): 
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	return render(request, 'blog/about.html')

