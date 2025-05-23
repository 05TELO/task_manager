from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    page_query_param = "page"
    page_size = 10
    page_size_query_param = "size"
    max_page_size = 100
