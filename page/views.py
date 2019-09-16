from django.shortcuts import render
from .forms import PageForm
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool


def index_page(request):
	form = PageForm()
	return render(request, 'page/index_page_form.html', context={'form': form})


def kiev_python(request):
	workua_data = []
	rabotaua_data = []

	def get_workua_html(url):
		r = requests.get(url)
		return r.text

	def get_workua_data(html):
		bs = BeautifulSoup(html, 'lxml')

		job_list = bs.find('div', id='pjax-job-list').find_all('div', class_='card card-hover card-visited wordwrap job-link')

		for item in job_list:
			try:
				title = item.find('h2', class_='add-bottom-sm').text
				company = item.find('b').text
				descr = item.find('p', class_='overflow').text
				url = 'https://www.work.ua' + item.find('h2', class_='add-bottom-sm').find('a').get('href')

				workua_data.append({'title': title, 'company': company, 'descr': descr, 'url': url})
			except:
				pass

	def workua_main():
		pattern = 'https://www.work.ua/ru/jobs-kyiv-python/?page={}'

		for i in range(0, 4):
			url = pattern.format(str(i))
			get_workua_data(get_workua_html(url))

	def get_rabotaua_html(url):
		r = requests.get(url)
		if r.ok:
			return r.text
		print(r.status_code)

	def get_rabotaua_data(html):
		bs = BeautifulSoup(html, 'lxml')

		trs = bs.find('section', class_='f-vacancylist-leftwrap fd-f1 f-paper').find('table').find_all('tr')

		for item in trs:
			try:
				title = item.find('td').find('div', class_='fd-f1').find('h3').text.strip()
				company = item.find('td').find('div', class_='fd-f1').find('p').find('a').text.strip()
				descr = item.find('td').find('div', class_='fd-f1').find('p', class_='f-vacancylist-shortdescr f-text-gray fd-craftsmen').text.strip()
				url = 'https://rabota.ua/zapros/python/%d0%ba%d0%b8%d0%b5%d0%b2' + item.find('td').find('div', class_='fd-f1').find('h3').find('a').get('href')

				rabotaua_data.append({'title': title, 'company': company, 'descr': descr, 'url': url})
			except:
				pass

	# def rabotaua_make_all(url):
	# 	html = get_rabotaua_html(url)
	# 	get_rabotaua_data(html)
	#
	# def rabotaua_main():
	# 	url = 'https://rabota.ua/zapros/python/%d0%ba%d0%b8%d0%b5%d0%b2/pg{}'
	# 	urls = [url.format(str(i)) for i in range(0, 10)]
	#
	# 	with Pool(20) as p:
	# 		p.map(rabotaua_make_all, urls)

	def rabotaua_main():
		pattern = 'https://rabota.ua/zapros/python/%d0%ba%d0%b8%d0%b5%d0%b2/pg{}'

		for i in range(0, 10):
			url = pattern.format(str(i))
			get_rabotaua_data(get_rabotaua_html(url))

	def kiev_python_main():
		workua_main()
		rabotaua_main()

	kiev_python_main()

	return render(request, 'page/kiev_python_result.html', context={'workua_data': workua_data, 'rabotaua_data': rabotaua_data})


def kiev_javascript(request):
	workua_data = []
	rabotaua_data = []

	def get_workua_html(url):
		r = requests.get(url)
		return r.text

	def get_workua_data(html):
		bs = BeautifulSoup(html, 'lxml')

		job_list = bs.find('div', id='pjax-job-list').find_all('div', class_='card card-hover card-visited wordwrap job-link')

		for item in job_list:
			try:
				title = item.find('h2', class_='add-bottom-sm').text
				company = item.find('b').text
				descr = item.find('p', class_='overflow').text
				url = 'https://www.work.ua' + item.find('h2', class_='add-bottom-sm').find('a').get('href')

				workua_data.append({'title': title, 'company': company, 'descr': descr, 'url': url})
			except:
				pass

	def workua_main():
		pattern = 'https://www.work.ua/ru/jobs-kyiv-javascript/?page={}'

		for i in range(0, 5):
			url = pattern.format(str(i))
			get_workua_data(get_workua_html(url))

	def get_rabotaua_html(url):
		r = requests.get(url)
		if r.ok:
			return r.text
		print(r.status_code)

	def get_rabotaua_data(html):
		bs = BeautifulSoup(html, 'lxml')

		trs = bs.find('section', class_='f-vacancylist-leftwrap fd-f1 f-paper').find('table').find_all('tr')

		for item in trs:
			try:
				title = item.find('td').find('div', class_='fd-f1').find('h3').text.strip()
				company = item.find('td').find('div', class_='fd-f1').find('p').find('a').text.strip()
				descr = item.find('td').find('div', class_='fd-f1').find('p', class_='f-vacancylist-shortdescr f-text-gray fd-craftsmen').text.strip()
				url = 'https://rabota.ua/zapros/javascript-developer/%d0%ba%d0%b8%d0%b5%d0%b2' + item.find('td').find('div',class_='fd-f1').find('h3').find('a').get('href')

				rabotaua_data.append({'title': title, 'company': company, 'descr': descr, 'url': url})
			except:
				pass

	def rabotaua_main():
		pattern = 'https://rabota.ua/zapros/javascript-developer/%d0%ba%d0%b8%d0%b5%d0%b2/pg{}'

		for i in range(0, 14):
			url = pattern.format(str(i))
			get_rabotaua_data(get_rabotaua_html(url))

	def kiev_javascript_main():
		workua_main()
		rabotaua_main()

	kiev_javascript_main()

	return render(request, 'page/kiev_javascript_result.html', context={'workua_data': workua_data, 'rabotaua_data':rabotaua_data})

def kiev_java(request):
	workua_data = []
	rabotaua_data = []

	def get_workua_html(url):
		r = requests.get(url)
		return r.text

	def get_workua_data(html):
		bs = BeautifulSoup(html, 'lxml')

		job_list = bs.find('div', id='pjax-job-list').find_all('div', class_='card card-hover card-visited wordwrap job-link')

		for item in job_list:
			try:
				title = item.find('h2', class_='add-bottom-sm').text
				company = item.find('b').text
				descr = item.find('p', class_='overflow').text
				url = 'https://www.work.ua' + item.find('h2', class_='add-bottom-sm').find('a').get('href')

				workua_data.append({'title': title, 'company': company, 'descr': descr, 'url': url})
			except:
				pass

	def workua_main():
		pattern = 'https://www.work.ua/ru/jobs-kyiv-java/?page={}'

		for i in range(0, 5):
			url = pattern.format(str(i))
			get_workua_data(get_workua_html(url))

	def get_rabotaua_html(url):
		r = requests.get(url)
		if r.ok:
			return r.text
		print(r.status_code)

	def get_rabotaua_data(html):
		bs = BeautifulSoup(html, 'lxml')

		trs = bs.find('section', class_='f-vacancylist-leftwrap fd-f1 f-paper').find('table').find_all('tr')

		for item in trs:
			try:
				title = item.find('td').find('div', class_='fd-f1').find('h3').text.strip()
				company = item.find('td').find('div', class_='fd-f1').find('p').find('a').text.strip()
				descr = item.find('td').find('div', class_='fd-f1').find('p', class_='f-vacancylist-shortdescr f-text-gray fd-craftsmen').text.strip()
				url = 'https://rabota.ua/zapros/java/%d0%ba%d0%b8%d0%b5%d0%b2' + item.find('td').find('div',class_='fd-f1').find('h3').find('a').get('href')

				rabotaua_data.append({'title': title, 'company': company, 'descr': descr, 'url': url})
			except:
				pass

	def rabotaua_main():
		pattern = 'https://rabota.ua/zapros/java/%d0%ba%d0%b8%d0%b5%d0%b2/pg{}'

		for i in range(0, 8):
			url = pattern.format(str(i))
			get_rabotaua_data(get_rabotaua_html(url))

	def kiev_java_main():
		workua_main()
		rabotaua_main()

	kiev_java_main()

	return render(request, 'page/kiev_java_result.html', context={'workua_data': workua_data, 'rabotaua_data':rabotaua_data})


def kiev_c_sharp(request):
	workua_data = []
	rabotaua_data = []

	def get_workua_html(url):
		r = requests.get(url)
		return r.text

	def get_workua_data(html):
		bs = BeautifulSoup(html, 'lxml')

		job_list = bs.find('div', id='pjax-job-list').find_all('div', class_='card card-hover card-visited wordwrap job-link')

		for item in job_list:
			try:
				title = item.find('h2', class_='add-bottom-sm').text
				company = item.find('b').text
				descr = item.find('p', class_='overflow').text
				url = 'https://www.work.ua' + item.find('h2', class_='add-bottom-sm').find('a').get('href')

				workua_data.append({'title': title, 'company': company, 'descr': descr, 'url': url})
			except:
				pass

	def workua_main():
		pattern = 'https://www.work.ua/ru/jobs-kyiv-c%23/?page={}'

		for i in range(0, 2):
			url = pattern.format(str(i))
			get_workua_data(get_workua_html(url))

	def get_rabotaua_html(url):
		r = requests.get(url)
		if r.ok:
			return r.text
		print(r.status_code)

	def get_rabotaua_data(html):
		bs = BeautifulSoup(html, 'lxml')

		trs = bs.find('section', class_='f-vacancylist-leftwrap fd-f1 f-paper').find('table').find_all('tr')

		for item in trs:
			try:
				title = item.find('td').find('div', class_='fd-f1').find('h3').text.strip()
				company = item.find('td').find('div', class_='fd-f1').find('p').find('a').text.strip()
				descr = item.find('td').find('div', class_='fd-f1').find('p',class_='f-vacancylist-shortdescr f-text-gray fd-craftsmen').text.strip()
				url = 'https://rabota.ua/zapros/c-sharp/%d0%ba%d0%b8%d0%b5%d0%b2' + item.find('td').find('div',class_='fd-f1').find('h3').find('a').get('href')

				rabotaua_data.append({'title': title, 'company': company, 'descr': descr, 'url': url})
			except:
				pass

	def rabotaua_main():
		pattern = 'https://rabota.ua/zapros/c-sharp/%d0%ba%d0%b8%d0%b5%d0%b2/pg{}'

		for i in range(0, 9):
			url = pattern.format(str(i))
			get_rabotaua_data(get_rabotaua_html(url))

	def kiev_c_main():
		workua_main()
		rabotaua_main()

	kiev_c_main()

	return render(request, 'page/kiev_c_result.html', context={'workua_data': workua_data, 'rabotaua_data': rabotaua_data})


# TODO:
#  Основное:
# 1.Вёрстка спаршеной страницы
# 2.Пагинация спаршеной страницы
# 3.Ускорение работы парсера
# 5.Фильтр одинаковых вакансий

#  Дополнительно:
# 1.Парсить картинки
# 3.Парсер djinny
# 4.Парсер dou
