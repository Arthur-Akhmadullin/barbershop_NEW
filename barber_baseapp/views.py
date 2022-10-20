from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView

from .models import News, Price, Record
from .forms import RecordForm


class MainPage(View):
	def get(self, request):
		last_news = News.objects.all()[:2]
		recordform = RecordForm()
		context = {'last_news': last_news, 'recordform': recordform}
		return render(request, 'barber_baseapp/index.html', context)


class RecordCreate(View):
	form_class = RecordForm

	def post(self, request):
		recordform = self.form_class(request.POST)
		if recordform.is_valid():
			cd = recordform.cleaned_data
			record = Record(name=cd['name'], phone=cd['phone'], date=cd['date'], time=cd['time'])
			record.save()
			return render(request, 'barber_baseapp/record_created.html', {'record': record})
		return redirect('main_page')


class NewsListView(ListView):
	template_name = 'barber_baseapp/news.html'
	context_object_name = 'news'
	paginate_by = 4

	def get_context_data(self, **kwargs):
		context = super(NewsListView, self).get_context_data(**kwargs)
		context['last_news'] = News.objects.all().first()
		return context

	def get_queryset(self):
		return News.objects.all()[1:]


class NewsDetailView(DetailView):
	model = News
	template_name = 'barber_baseapp/news_detail.html'
	slug_url_kwarg = 'slug'
	context_object_name = 'news'


class PriceListView(ListView):
	model = Price
	template_name = 'barber_baseapp/price.html'
	context_object_name = 'price'