from apps.deliveries.models import Delivery
from apps.customers.models import Cart
from apps.customers.models import Adress
from datetime import datetime

class DeliveryService:
    @staticmethod
    def get_delivery(tg_id: int) -> Delivery:
        """
        Функция которая получает Заказ клиента по телеграмм id
        A если не нашлось Заказа то создает её и возвращает корзину.
        """
        delivery = Delivery.objects.filter(cart__customer__user__telegram_id=tg_id).first()
        return delivery
    
    @staticmethod
    def create_delivery(cart: Cart, adress: Adress, delivery_date: datetime) -> Delivery:
        delivery = Delivery.objects.create(
            cart=cart,
            adress=adress,
            delivery_date=delivery_date
        )
        return delivery


delivery_service = DeliveryService()