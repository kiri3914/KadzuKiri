from apps.customers.models import Cart, CartItem, Client
from apps.products.models import Product


class CartService:
    @staticmethod
    def get_cart(tg_id: int) -> Cart:
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
    def get_cart_item_by_product(cart: Cart, product: int) -> CartItem:
        """
        Функция которая получает товар из корзины по product
        """
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        return cart_item


    @staticmethod
    def get_cart_item(cartitem_id) -> CartItem:
        """
        Функция которая получает один товар из корзины по его id.
        """
        cart_item = CartItem.objects.filter(id=cartitem_id).first()
        return cart_item



    @staticmethod
    def add_product(cart: Cart, product_id: int, count: int):
        """
        Функция которая добавляет товар в корзину.
        """
        product = Product.objects.get(id=product_id)
        cart_item = CartService.get_cart_item_by_product(cart, product)
        if cart_item is None:
            cart_item = CartItem.objects.create(cart=cart, product=product, count=count)
        else:
            cart_item.count += count
            cart_item.save()
        return cart_item


    @staticmethod
    def get_cart_items(cart: Cart) -> list[CartItem]:
        """
        Функция которая получает все товары из корзины.
        """
        cart_items = CartItem.objects.filter(cart=cart)
        return cart_items.all()
    
    
    @staticmethod
    def delete_cart_item(cart_item: CartItem):
        """
        Функция которая удаляет товар из корзины.
        """
        cart_item.delete()
        return True
    
    
    @staticmethod
    def increment(cart_item: CartItem):
        """
        Функция которая добавляет количество товара в корзине.
        """
        cart_item.count += 1
        cart_item.save()
        return cart_item
    
    
    @staticmethod
    def decrement(cart_item: CartItem):
        """
        Функция которая уменьшает количество товара в корзине.
        """
        cart_item.count -= 1
        cart_item.save()
        return cart_item
        

    

cart_service = CartService()