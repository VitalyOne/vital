from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *
from django.shortcuts import redirect
import re

# Create your views here.
def main_page(request):
	form ={}
	if request.POST:
		form['ser'] = request.POST.get('ser')
		try:
			detal = Detal.objects.get(catalog_number=form['ser'])
			detal.kolvo_zaprosov+=1
			detal.save()
			return redirect('detal_detail', pk = detal.pk)
		except 	Detal.DoesNotExist:
			try:
				detal = Detal.objects.get(alternativ_number=form['ser'])
				return redirect('detal_detail', pk = detal.pk)
			except Detal.DoesNotExist:
				return redirect('search_list')

			

	return render(request, 'ctpBase/main_page.html', {'form':form})

	
def search_list(request):
	detals = Detal.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
	form ={} #добавлено
	if request.POST: #добавлено
		form['ser'] = request.POST.get('ser') #добавлено
		try: #добавлено
			detal = Detal.objects.get(catalog_number=form['ser']) #добавлено
			detal.kolvo_zaprosov+=1 #добавлено
			detal.save() #добавлено
			return redirect('detal_detail', pk = detal.pk) #добавлено
		except 	Detal.DoesNotExist: #добавлено
			try: #добавлено
				detal = Detal.objects.get(alternativ_number=form['ser']) #добавлено
				return redirect('detal_detail', pk = detal.pk) #добавлено
			except Detal.DoesNotExist: #добавлено
				return redirect('search_list') #добавлено
	return render(request, 'ctpBase/search_list.html', {'detals': detals, 'form':form})   #добавлена форм-форм

def detal_detail(request, pk):
	detal = get_object_or_404(Detal, pk=pk)
	form ={} #добавлено
	if request.POST: #добавлено
		form['ser'] = request.POST.get('ser') #добавлено
		try: #добавлено
			detal = Detal.objects.get(catalog_number=form['ser']) #добавлено
			detal.kolvo_zaprosov+=1 #добавлено
			detal.save() #добавлено
			return redirect('detal_detail', pk = detal.pk) #добавлено
		except 	Detal.DoesNotExist: #добавлено
			try: #добавлено
				detal = Detal.objects.get(alternativ_number=form['ser']) #добавлено
				return redirect('detal_detail', pk = detal.pk) #добавлено
			except Detal.DoesNotExist: #добавлено
				return redirect('search_list') #добавлено
	return render(request, 'ctpBase/detal_detail.html', {'detal': detal, 'form':form}) #добавлено


def search(request):
	if request.method == 'POST':
		form=SearchForm(request.POST)
		if form.is_valid():
			search_number = form.cleaned_data['search_number']

			try:
				detal = Detal.objects.get(catalog_number=search_number)
				detal.kolvo_zaprosov+=1
				detal.save()
			#if detal:
				return redirect('detal_detail', pk = detal.pk)
			except 	Detal.DoesNotExist:
				try:
					detal = Detal.objects.get(alternativ_number=search_number)
					return redirect('detal_detail', pk = detal.pk)
				except Detal.DoesNotExist:
			#else:
					return redirect('search_list')

	else:
		form=SearchForm()
	return render(request,'ctpBase/search.html', {'form':form})

def poisk_primenimost(request):
	if request.method == 'POST':
		form = SearchCAT(request.POST)
		if form.is_valid():
			search_category = form.cleaned_data['search_category']
			number = 0
			detals = []
			#try:
			#	detals = Detal.objects.get(opisanie=r'.+(search_category).+')
			for de in Detal.objects.all():
				fl1 = de.opisanie.split(', ')
				for opis in fl1:
					if search_category == opis:
						number +=1
						detals.append(de)
						break
			#if number == 0:
			#	for de in Detal.objects.all():
			#		fl2 = de.opisanie.split(',')
			#		for opis in fl1:
			#			if search_category == opis:
			#				number +=1
			#				detals.append(de)
			#				break



				
				
				#if search_category in de.opisanie:
			

			if number == 1:	
				return redirect('detal_detail', pk = detals[0].pk)
			elif number == 0:	


			#except Detal.DoesNotExist:
			
				return redirect('poisk_primenimost')
			else:
				return	render(request, 'ctpBase/search_category_result.html', {'detals': detals})


	else:
		form = SearchCAT()

	return render (request, 'ctpBase/search_for_category.html', {'form':form})	

def detal_new(request):
	#form ={} #добавлено
	#if request.GET: #добавлено
	#	form['ser'] = request.GET.get('ser') #добавлено
	#	try: #добавлено
	#		detal = Detal.objects.get(catalog_number=form['ser']) #добавлено
	#		detal.kolvo_zaprosov+=1 #добавлено
	#		detal.save() #добавлено
	#		return redirect('detal_detail', pk = detal.pk) #добавлено
	#	except 	Detal.DoesNotExist: #добавлено
	#		try: #добавлено
	#			detal = Detal.objects.get(alternativ_number=form['ser']) #добавлено
	#			return redirect('detal_detail', pk = detal.pk) #добавлено
	#		except Detal.DoesNotExist: #добавлено
	#			return redirect('search_list') #добавлено
	if request.method == "POST":
		form = DetalForm(request.POST)
		if form.is_valid():
			detal = form.save(commit=False)
			detal.author = request.user
			detal.published_date = timezone.now()
			detal.save()
			return redirect('detal_detail', pk = detal.pk)
	else:
		form = DetalForm()
	return render(request, 'ctpBase/detal_edit.html', {'form':form})




def detal_edit(request, pk):
	detal = get_object_or_404(Detal, pk=pk)
	if request.method == "POST":
		form = DetalForm(request.POST, instance=detal)
		if form.is_valid():
			detal = form.save(commit=False)
			detal.author = request.user
			detal.published_date = timezone.now()
			detal.save()
			return redirect('detal_detail', pk=detal.pk)
	else:
		form = DetalForm(instance=detal)
	return render(request, 'ctpBase/detal_edit.html', {'form': form})


def detal_delete(request, pk):
	detal = get_object_or_404(Detal, pk=pk)
	detal.delete()
	return redirect('search_list')
