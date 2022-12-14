from urllib import request
from rest_framework import  generics, mixins
from .models import Product
from . serializers import ProductSerializer
from api.mixins import StaffEditorPermissionMixin, UserQuerySetMixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404



class ProductListCreateAPIView(StaffEditorPermissionMixin,UserQuerySetMixins, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication, TokenAuthentication] #We use those in settings
    # permission_classes =[permissions.DjangoModelPermissions] #Works for PUT POST DELETE
    # permission_classes =[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # print(serializer.validated_data)
        # email = serializer.validated_data.pop('email')
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Product.objects.none
    #     # print(request.user)
    #     return qs.filter(user=request.user)

product_list_create_view = ProductListCreateAPIView.as_view()



class ProductDetailAPIView(StaffEditorPermissionMixin,UserQuerySetMixins, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'



class ProductListAPIView(generics.ListAPIView):
    '''
    Not Gonna use it because of ProductListCreateAPIView
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()



class ProductUpdateAPIView(StaffEditorPermissionMixin,UserQuerySetMixins, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title



class ProductDeleteAPIView(StaffEditorPermissionMixin,UserQuerySetMixins, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        #instance
        super().perform_destroy(instance)



#CLASS BASED VIEWS: No conditions
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = "This is a single view doing cool stuffs"
        serializer.save(content=content)


product_mixin_view = ProductMixinView.as_view()





#FUNCTION BASED VIEW: we write conditions

@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            #detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        else:
            #list view
            qs = Product.objects.all() #qs=queryset
            data = ProductSerializer(qs, many=True).data
            return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # instance = serializer.save()
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"Invalid": "Not good data"}, status=400)

