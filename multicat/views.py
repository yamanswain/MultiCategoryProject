from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import Category, Product
from rest_framework.response import Response
# Create your views here


class ProductViewAPI(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class CategoryViewAPI(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def create(self, request, *args, **kwargs):
        data = request.data.get('categories')
        for cat in data:
            c_name = cat.get('c_name')
            parent = cat.get('parent')
            if parent is None:
                if Category.objects.filter(c_name=c_name).exists():
                    print(f'{c_name} - category already exists')
                    continue
                c = create_category(c_name)
                print("CREATING CATEGORY...")
                print(" ")
                print(c)
                continue
            elif not isinstance(parent, str):
                return Response("Parent not in correct format. Please specify parent name")
            parent_object = Category.objects.filter(c_name=parent)
            if not parent_object.exists():
                return Response("Parent specified does not exists. Category/Sub-Category not found")
            if Category.objects.filter(c_name=c_name, parent=parent_object[0]).exists():
                print(f'{c_name} - Sub-category already exists')
                continue
            c = create_category(c_name, parent_object[0])
            print("CREATING SUB CATEGORY...")
            print(" ")
            print(c)
        return Response("Data created successfully")

    def partial_update(self, request, *args, **kwargs):
        category_id = kwargs.get('pk')
        c_name = request.data.get("c_name")
        parent = request.data.get("parent")
        # find category using pk
        category = Category.objects.filter(id=category_id)
        if category.exists():
            if isinstance(parent, str):
               parent_object = Category.objects.filter(c_name=parent)
               category.update(c_name=c_name, parent=parent_object[0])
            elif isinstance(parent, int):
               parent_object = Category.objects.filter(id=parent)
               category.update(c_name=c_name, parent=parent_object[0])
            else:
                # parent is null. update it as it is
                category.update(c_name=c_name, parent=parent)
        # if parent is None:
        #     if Category.objects.filter(c_name=c_name).exists():
        #         Category.objects.update(c_name=c_name,parent=parent)
        #         print(f'{c_name} - category already exists')
        #         continue
        return Response("Data Updated Successfully")


def create_category(cat_name, parent_name=None):
    return Category.objects.create(c_name=cat_name, parent=parent_name)



