from apps.products.models import Product

class ProductService:
    @staticmethod
    def get_product_by_id(product_id):
        try:
            return Product.objects.get(id=product_id)
        except:
            return None

    @staticmethod
    def get_products():
        return Product.objects.all()
    
    @staticmethod
    def search_product(search_term):
        return Product.objects.filter(name__icontains=search_term)
    
    @staticmethod
    def get_products_by_category(category_id):
        return Product.objects.filter(category__id=category_id)
    

product_service = ProductService()