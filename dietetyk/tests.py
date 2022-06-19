from django.test import TestCase, Client
from django.urls import reverse, resolve

from dietetyk.views import MealsView, NoteView, Element_of_mealsView, UserView, DietaView

class MyTests(TestCase):

    def test_view_main(self):
        client = Client()
        response = client.get(reverse('main'))
        self.assertEquals(response.status_code, 200)

    # test url
    def test_url_MealsView(self):
        url = reverse(MealsView)
        self.assertEquals(resolve(url).func, MealsView)

    def test_url_NoteView(self):
        url = reverse(NoteView)
        self.assertEquals(resolve(url).func, NoteView)

    def test_url_Element_of_mealsView(self):
        url = reverse(Element_of_mealsView)
        self.assertEquals(resolve(url).func, Element_of_mealsView)

    def test_url_UserView(self):
        url = reverse(UserView)
        self.assertEquals(resolve(url).func, UserView)

    def test_url_DietaView(self):
        url = reverse(DietaView)
        self.assertEquals(resolve(url).func, DietaView)







