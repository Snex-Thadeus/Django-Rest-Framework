from api.serializers import UserPublicSerializer
from rest_framework.reverse import reverse
from rest_framework import serializers
from .models import Product
from .validators import validate_title_no_hello, unique_product_title

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    # edit_url = serializers.SerializerMethodField(read_only=True)
    # url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    # email = serializers.EmailField(source='user.email', read_only=True)
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    # name = serializers.CharField(source='title', read_only=True)
    body = serializers.CharField(source='content')
    class Meta:
        model = Product
        fields = [
            'owner',
            # 'url',
            # 'edit_url',
            'pk',
            'title',
            'body',
            # 'name',
            'content',
            # 'email',
            'price',
            'sale_price',
            'public',
            'path',
            'endpoint',
            # 'my_discount'
        ]

    def validate_title(self, value):
        request = self.context.get('request')
        user = request.user
        qs = Product.objects.filter(user=user, title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name.")
        return value

 #Model serializers Create & Update Methods
    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email') 
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None

        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    # def get_my_discount(self, obj): #obj is the instance being called
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount()