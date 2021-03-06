from decimal import Decimal
from importlib import import_module
from django.test import TestCase
from products.models import Product, Variant
from ..utils import SessionCart

# Create your tests here.
class SessionCartTest(TestCase):

    def setUp(self):
        product = Product.objects.create(name='foo', sku='123')
        variant = product.variant_set.first()
        variant.price = Decimal(12.34)
        variant.sub_sku = '456'
        variant.save()

        self.variant2 = Variant.objects.create(
            product=product, name='bar', price=Decimal(43.21), sub_sku='789'
        )

        self.variant = variant


    def test_session_cart_module_has_uuid(self):
        '''
        Test that SessionCart uses a universally unique identifier (UUID).
        '''
        module = import_module('carts.utils')
        uuid = getattr(module, 'UUID', None)
        self.assertIsNotNone(uuid)


    def test_session_cart_can_have_an_item_added_to_it(self):
        '''
        Test that items can be added to a SessionCart.
        '''
        session = self.client.session
        cart = SessionCart(session)

        cart.add(self.variant)

        self.assertIn(self.variant, cart)


    def test_session_cart_can_be_emptied(self):
        '''
        Test that SessionCart can be emptied.
        '''
        session = self.client.session
        cart = SessionCart(session)

        cart.add(self.variant)
        cart.empty()

        self.assertEquals(cart, [])


    def test_session_cart_can_calculate_total_price_when_empty(self):
        '''
        Test that SessionCart can calculate the total price when it is empty.
        '''
        session = self.client.session
        cart = SessionCart(session)

        self.assertEquals(cart.total, Decimal(0.00))


    def test_session_cart_can_calculate_total_price_with_one_item(self):
        '''
        Test that SessionCart can calculate the total price when it contains one
        item.
        '''
        session = self.client.session
        cart = SessionCart(session)

        cart.add(self.variant)

        self.assertAlmostEqual(cart.total, Decimal(12.34), places=2)


    def test_session_cart_can_calculate_total_price_of_contents(self):
        '''
        Test that SessionCart can calculate the total price of its contents.
        '''
        session = self.client.session
        cart = SessionCart(session)

        cart.add(self.variant)
        cart.add(self.variant2)

        self.assertAlmostEqual(cart.total, Decimal(55.55), places=2)


    def test_session_cart_preserves_contents_between_instantiations(self):
        '''
        Test that SessionCart preserves its contents between sessions.
        '''
        session = self.client.session
        cart = SessionCart(session)

        cart.add(self.variant)
        cart2 = SessionCart(session)

        self.assertIn(self.variant, cart2)


    def test_session_cart_can_remove_items(self):
        '''
        Test that items can be removed to a SessionCart.
        '''
        session = self.client.session
        cart = SessionCart(session)

        cart.add(self.variant)
        cart.add(self.variant2)
        cart.remove(self.variant2)

        self.assertEqual(cart, [self.variant])


    def test_session_cart_removes_items_that_become_unsalable(self):
        '''
        Test that SessionCart removes items that become unsalable between
        instantiations.
        '''
        session = self.client.session
        cart = SessionCart(session)

        cart.add(self.variant)
        self.variant.enabled = False
        self.variant.save()

        cart2 = SessionCart(session)

        self.assertEqual(cart2, [])


    def test_session_cart_removes_items_that_are_deleted(self):
        '''
        Test that SessionCart removes items that are deleted between
        instantiations.
        '''
        session = self.client.session
        cart = SessionCart(session)

        cart.add(self.variant)
        self.variant.delete()

        cart2 = SessionCart(session)

        self.assertEqual(cart2, [])
