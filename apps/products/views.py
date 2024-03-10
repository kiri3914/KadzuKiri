from django_filters.rest_framework import FilterSet, DjangoFilterBackend, DateFilter
from rest_framework import viewsets, filters, pagination

from .models import Product, Category, ProductImage
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer 
    # ModelViewSet - обеспечивает все операции CRUD для модели Category.
    # queryset - модель для работы с данными.
    # serializer_class - класс для сериализации данных.
    

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint для работы с категориями новостей.

    list:
    Получение списка всех категорий.

    create:
    Создание новой категории.

    retrieve:
    Получение информации о конкретной категории.

    update:
    Обновление информации о конкретной категории.

    partial_update:
    Частичное обновление информации о конкретной категории.

    destroy:
    Удаление конкретной категории.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductPagination(pagination.PageNumberPagination):
    """
    PageNumberPagination - обеспечивает пагинацию для модели News.
    page_size - количество элементов на странице.
    page_size_query_param - параметр для указания количества элементов на странице.
    max_page_size - максимальное количество элементов на странице.
    """
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProductFilter(FilterSet):
    """
    FilterSet - обеспечивает фильтрацию данных для модели News.
    category - фильтр по категории.
    is_published - фильтр по статусу публикации.
    start_date - фильтр по дате создания (больше или равно).
    end_date - фильтр по дате создания (меньше или равно).
    filters.DateFilter - обеспечивает фильтрацию по дате.
    """
    start_date = DateFilter(field_name="created_at", lookup_expr='gte')
    end_date = DateFilter(field_name="created_at", lookup_expr='lte')
    start_price = DateFilter(field_name="price", lookup_expr='gte')
    end_price = DateFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'start_date', 'end_date', 'start_price', 'end_price', 'is_available']


class ProductViewSet(viewsets.ModelViewSet):
    """
    filter_backends - обеспечивает фильтрацию данных для модели News.
    filterset_class - класс для фильтрации данных.
    search_fields - поля для поиска.
    pagination_class - класс для пагинации данных.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'category', 'description', 'price']
    pagination_class = ProductPagination

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


