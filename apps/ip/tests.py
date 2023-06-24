from django.test import TestCase
from apps.ip.models import Pais


class YourTestClass(TestCase):

    def setUp(self):
        pais1 = Pais.objects.create(nombre='Cuba')
        pais2 = Pais.objects.create(nombre='Venezuela')
        pais3 = Pais.objects.create(nombre='Francia')
        pais4 = Pais.objects.create(nombre='Colombia')
        pais5 = Pais.objects.create(nombre='Rusia')
        pais1.save()
        pais2.save()
        pais3.save()
        pais4.save()
        pais5.save()
        pass

    def tearDown(self):
        # Limpia la ejecución después de cada método de prueba.
        pass

    def test_something_that_will_pass(self):
        #self.assertFalse(True)
        pass

    def test_something_that_will_fail(self):
        #self.assertTrue(True)
        pass
