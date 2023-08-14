from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch, Toy
from .forms import BirdseedForm

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', 
  { 
    'finches': finches
    }
)

def toys_index(request):
  toys = Toy.objects.all()
  return render(request, 'toys/index.html', 
  { 
    'toys': toys
    }
)

def finches_detail(request, finch_id):
  finch = Finch.objects.get(id=finch_id)
  id_list = finch.toys.all().values_list('id')
  toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
  birdseed_form = BirdseedForm()
  return render(request, 'finches/detail.html', {
     'finch': finch, 'birdseed_form': birdseed_form,
     'toys': toys_finch_doesnt_have 
     })

def toys_detail(request, toy_id):
  toy = Toy.objects.get(id=toy_id)
  return render(request, 'toys/detail.html', {'toy': toy})

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/finches/{finch_id}'

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'
  success_url = '/toys/{toy_id}'

class FinchUpdate(UpdateView):
  model = Finch
  fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['color', 'price']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def add_birdseed(request, finch_id):
  form = BirdseedForm(request.POST)
  if form.is_valid():
    new_birdseed = form.save(commit=False)
    new_birdseed.finch_id = finch_id
    new_birdseed.save()
  return redirect('detail', finch_id=finch_id)

def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)