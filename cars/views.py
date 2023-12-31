from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.
from django.views.generic import CreateView,UpdateView,DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages

@method_decorator(login_required, name="dispatch")
class AddCarCreateView(CreateView):
    model=models.Car
    form_class=forms.CarForm
    template_name='add_car.html'
    success_url=reverse_lazy('add_car')
    def form_valid(self, form) :
        form.instance.author = self.request.user
        messages.success(self.request, 'Add car successful')
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class EditCarView(UpdateView):
    model=models.Car
    form_class=forms.CarForm
    template_name='add_car.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('profile')
    
@login_required
def delete_car(request, id):
        car=models.Car.objects.get(pk=id)
        car.delete()
        return redirect('homepage')



def add_brand(request):
    if request.method == 'POST': 
        brand_form = forms.BrandForm(request.POST) 
        if brand_form.is_valid():
            brand_form.save()
            return redirect('add_brand') 
    
    else: 
        brand_form = forms.BrandForm()
    return render(request, 'add_brand.html', {'form' : brand_form})


class DetailCarView(DetailView):
    model=models.Car
    pk_url_kwarg='id'
    template_name="car_details.html"
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
