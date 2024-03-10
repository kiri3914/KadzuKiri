from apps.products.models import Category


class CategoryService:
    @staticmethod
    def get_categories():
        return Category.objects.all()

    @staticmethod
    def get_category_by_id(category_id):
        return Category.objects.get(id=category_id)


category_service = CategoryService()