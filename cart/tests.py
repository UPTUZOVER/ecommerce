# from django.test import TestCase
# from django.contrib.auth.models import User
# from store.models import Product
# from .models import Cart, CartItem


# class CartTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.product = Product.objects.create(name='Test Product', price=10, stock=5)
#         self.cart = Cart.objects.create()

#     def test_is_empty(self):
#         self.assertTrue(self.cart.is_empty())

#         # Add an item to the cart
#         CartItem.objects.create(product=self.product, cart=self.cart)
#         self.assertFalse(self.cart.is_empty())

#     def test_clear_cart(self):
#         # Add some items to the cart
#         CartItem.objects.create(product=self.product, cart=self.cart)
#         CartItem.objects.create(product=self.product, cart=self.cart)
#         CartItem.objects.create(product=self.product, cart=self.cart)

#         self.cart.clear_cart()
#         self.assertTrue(self.cart.is_empty())

#     def test_get_item_count(self):
#         # Add some items to the cart
#         CartItem.objects.create(product=self.product, cart=self.cart)
#         CartItem.objects.create(product=self.product, cart=self.cart)

#         self.assertEqual(self.cart.get_item_count(), 2)

#     def test_remove_item(self):
#         # Add an item to the cart
#         cart_item = CartItem.objects.create(product=self.product, cart=self.cart)

#         self.cart.remove_item(cart_item.id)
#         self.assertTrue(self.cart.is_empty())

#     def test_update_item_quantity(self):
#         # Add an item to the cart
#         cart_item = CartItem.objects.create(product=self.product, cart=self.cart)

#         self.cart.update_item_quantity(cart_item.id, 3)
#         self.assertEqual(cart_item.quantity, 3)

#         self.cart.update_item_quantity(cart_item.id, 0)
#         self.assertTrue(self.cart.is_empty())


# class CartItemTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.product = Product.objects.create(name='Test Product', price=10, stock=5)
#         self.cart = Cart.objects.create()

#     def test_toggle_active(self):
#         cart_item = CartItem.objects.create(product=self.product, cart=self.cart)
#         cart_item.toggle_active()
#         self.assertFalse(cart_item.is_active)

#         cart_item.toggle_active()
#         self.assertTrue(cart_item.is_active)

#     def test_increment_quantity(self):
#         cart_item = CartItem.objects.create(product=self.product, cart=self.cart)
#         cart_item.increment_quantity()
#         self.assertEqual(cart_item.quantity, 2)

#     def test_decrement_quantity(self):
#         cart_item = CartItem.objects.create(product=self.product, cart=self.cart)
#         cart_item.decrement_quantity()
#         self.assertEqual(cart_item.quantity, 1)

#         cart_item.decrement_quantity()
#         self.assertEqual(cart_item.quantity, 1)

#     def test_get_subtotal_price(self):
#         cart_item = CartItem.objects.create(product=self.product, cart=self.cart, quantity=3)
#         expected_subtotal_price = self.product.price * 3
#         self.assertEqual(cart_item.get_subtotal_price(), expected_subtotal_price)

#     def test_is_in_stock(self):
#         cart_item = CartItem.objects.create(product=self.product, cart=self.cart, quantity=3)
#         self.assertTrue(cart_item.is_in_stock())

#         cart_item.quantity = 10
#         self.assertFalse(cart_item.is_in_stock())