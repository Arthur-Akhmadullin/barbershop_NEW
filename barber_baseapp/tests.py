from django.test import TestCase
from django.urls import reverse

import datetime

from .models import News
from .forms import RecordForm


class NewsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        News.objects.create(title='Новость дня', slug='novost-dnya', date='2020-07-07')

    def test_title_label(self):
        news = News.objects.get(id=1)
        title_label = news._meta.get_field('title').verbose_name
        self.assertEquals(title_label,'title')

    def test_slug_label(self):
        news = News.objects.get(id=1)
        slug_label = news._meta.get_field('slug').verbose_name
        self.assertEquals(slug_label,'slug')

    def test_title_max_length(self):
        news = News.objects.get(id=1)
        max_length = news._meta.get_field('title').max_length
        self.assertEquals(max_length, 250)

    def test_object_name_is_title(self):
        news = News.objects.get(id=1)
        expected_object_name = '%s' % (news.title)
        self.assertEquals(expected_object_name, str(news))

    def test_get_absolute_url(self):
        news = News.objects.get(id=1)
        self.assertIn('/news/novost-dnya-', news.get_absolute_url())


class RecordFormTest(TestCase):

    def test_recordform_name_field_label(self):
        form = RecordForm()
        self.assertTrue(form.fields['name'].label == '')

    def test_recordform_phone_field_label(self):
        form = RecordForm()
        self.assertTrue(form.fields['phone'].label == '')

    def test_recordform_date_field_label(self):
        form = RecordForm()
        self.assertTrue(form.fields['date'].label == '')

    def test_recordform_time_field_label(self):
        form = RecordForm()
        self.assertTrue(form.fields['time'].label == '')

    def test_recordform_date_format_is_false(self):
        date = '10.10.2022'
        form_data = {'date': date}
        form = RecordForm(data=form_data)
        self.assertNotEqual(form.data['date'], '2022-10-09')

    def test_recordform_date_format_is_true(self):
        date = '10.10.2022'
        form_data = {'date': date}
        form = RecordForm(data=form_data)
        self.assertEqual(form.data['date'], '10.10.2022')


class NewsListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_news = 13
        for news_num in range(number_of_news):
            News.objects.create(title='News # %s' % news_num,
                                slug='news-%s' % news_num,
                                date=datetime.date.today(),
                                )

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/news/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('news_page'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('news_page'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'barber_baseapp/news.html')

    def test_pagination_is_four(self):
        resp = self.client.get(reverse('news_page'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['news']) == 4)

    def test_pagination_is_four_for_page2(self):
        resp = self.client.get(reverse('news_page'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['news']) == 4)

    def test_context_first_elem_is_instanse_of_news(self):
        resp = self.client.get(reverse('news_page')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertIsInstance(resp.context['last_news'], News)