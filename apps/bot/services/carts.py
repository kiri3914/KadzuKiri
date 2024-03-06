from apps.customers.models import Cart, CartItem, Client
from apps.products.models import Product

class CartService:
    @staticmethod
    def get_cart_by_tg_id(tg_id: int) -> Cart:
        """
        Функция которая получает корзину клиента по телеграмм id
        A если не нашлось корзины то создает её и возвращает корзину.
        """
        cart = Cart.objects.filter(customer__user__telegram_id=tg_id).first()
        if cart is None:
            customer = Client.objects.filter(user__telegram_id=tg_id).first()
            cart = Cart.objects.create(customer=customer)
        return cart

    @staticmethod
    def get_cart_item_by_product(cart: Cart, product_id: int) -> CartItem:
        """
        Функция которая получает товар из корзины по его id.
        """
        if cart is None:
            return None
        if product_id is None:
            return None
        if not isinstance(product_id, int):
            return None
        if not isinstance(cart, Cart):
            return None
        cart_item = CartItem.objects.filter(cart=cart, product__id=product_id).first()
        return cart_item

    @staticmethod
    def add_product_to_cart(cart: Cart, product_id: int, quantity: int):
        """
        Функция которая добавляет товар в корзину.
        """
        product = Product.objects.get(id=product_id)
        cart_item = CartService.get_cart_item_by_product(cart, product)
        if cart_item is None:
            cart_item = CartItem.objects.create(cart=cart, product=product, quantity=quantity)
        else:
            cart_item.quantity += quantity
            cart_item.save()
        return cart_item


cart_service = CartService()
