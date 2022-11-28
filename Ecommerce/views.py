from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.filters import SearchFilter,OrderingFilter
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# Create your views here.

class UserRegistrationView(generics.ListAPIView, generics.CreateAPIView):

    serializer_class = UserRegistrationSerializer
    # queryset = User.objects.all()
    

    def get(self, request, *args, **kwargs):
        try:
            response={"status":status.HTTP_400_BAD_REQUEST,"message":"Fetching Users Details are  Failed"}
            all_user = User.objects.all()
            serializer = self.serializer_class(all_user, many=True)
            response["status"] = status.HTTP_200_OK
            response["message"] = " Users Details fetched successfully"
            response["data"] = serializer.data
            return Response(response, status=status.HTTP_200_OK)
        except Exception:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
            

    def post(self, request, *args, **kwargs):
            response = {'status':status.HTTP_400_BAD_REQUEST, "message": "User Creation failed"}
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response["status"] = status.HTTP_200_OK
                response["data"] = serializer.data
                response["message"] = 'message: User created successfully.'
                return Response(response, status=status.HTTP_201_CREATED)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)





class ProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['product_name','id']
    # 
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    
    def get(self, request, *args, **kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Products Fetching failed"}
        product_list =Product.objects.all()
        serializer = self.serializer_class(product_list, many=True)
        response["status"] = status.HTTP_200_OK
        response["data"] = serializer.data
        response["message"] = 'Products Fetched Successfully'
        return Response(response, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
            response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Product Creation failed"}
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                response["status"] = status.HTTP_200_OK
                response["data"] = serializer.data
                response["message"] = 'message: Product created successfully.'
                return Response(response, status=status.HTTP_201_CREATED)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
   

    def get(self,request,*args,**kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": " Fetching Product failed"}
        id = kwargs.get("id")
        product= Product.objects.get(id=id)
        serializer= self.serializer_class(product)
        response["status"] = status.HTTP_200_OK
        response["data"] = serializer.data
        response["message"] = 'message: Product fetched successfully.'
        return Response(response, status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": " Updating Product failed"}
        id = kwargs.get("id")
        p_id= Product.objects.get(id=id)
        serializer = self.serializer_class(data=request.data,instance=p_id)
        if serializer.is_valid():
            serializer.save()
            response["status"] = status.HTTP_200_OK
            response["data"] = serializer.data
            response["message"] = 'message: Updated Product successfully.'
            return Response(response, status=status.HTTP_200_OK)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        response = {"status":status.HTTP_400_BAD_REQUEST,"message":"Product Deletion Failed"}
        id = kwargs.get("id")
        product = Product.objects.get(id=id)
        product.delete()
        response["message"] = "Product Details Are Removed"
        response["status"] = status.HTTP_200_OK
        return Response(response,status=status.HTTP_200_OK)




class CategoryView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    
    
    def get(self, request, *args, **kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Fetching Categories failed"}
        category_list = Category.objects.all()
        serializer = self.serializer_class(category_list, many=True)
        response["status"] = status.HTTP_200_OK
        response["data"] = serializer.data
        response["message"] = 'Categories Fetched Successfully'
        return Response(response, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Category Creation failed"}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["status"] = status.HTTP_200_OK
            response["data"] = serializer.data
            response["message"] = 'message: Category created successfully.'
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CategorySerializer

    def get(self,request,*args,**kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": " Fetching Category failed"}
        id = kwargs.get("id")
        category= Category.objects.get(id=id)
        serializer= self.serializer_class(category)
        response["status"] = status.HTTP_200_OK
        response["data"] = serializer.data
        response["message"] = 'message: Category fetched successfully.'
        return Response(response, status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": " Updating Category failed"}
        id = kwargs.get("id")
        ct_id= Category.objects.get(id=id)
        serializer = self.serializer_class(data=request.data,instance=ct_id)
        if serializer.is_valid():
            serializer.save()
            response["status"] = status.HTTP_200_OK
            response["data"] = serializer.data
            response["message"] = 'message: Updated Category successfully.'
            return Response(response, status=status.HTTP_200_OK)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        response = {"status":status.HTTP_400_BAD_REQUEST,"message":"Category Deletion Failed"}
        id = kwargs.get("id")
        ct = Category.objects.get(id=id)
        ct.delete()
        response["message"] = "Category Details Are Removed"
        response["status"] = status.HTTP_200_OK
        return Response(response,status=status.HTTP_200_OK)


class CartView(generics.ListAPIView):
    serializer_class =  CartSerializer
    filter_backends = [SearchFilter]
    search_fields = ['customer_id','id']

    def get(self, request, *args, **kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Fetching CartItems failed"}
        cart_list = OrderItem.objects.all()
        serializer = self.serializer_class(cart_list, many=True)
        response["status"] = status.HTTP_200_OK
        response["data"] = serializer.data
        response["message"] = 'CartItems Fetched Successfully'
        return Response(response, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Adding Item to the cart failed"}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["status"] = status.HTTP_200_OK
            response["data"] = serializer.data
            response["message"] = 'message: Items added to the cart successfully.'
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class CartDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer

    def get(self,request,*args,**kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": " Fetching Cart item failed"}
        id = kwargs.get("id")
        # product=request.data["product_id"]
        # pr= Product.objects.get(id=product)
        # print(pr.price)
        cart_item= OrderItem.objects.get(id=id)
        serializer= self.serializer_class(cart_item)
        response["status"] = status.HTTP_200_OK
        response["data"] = serializer.data
        response["message"] = 'message: CartItem fetched successfully.'
        return Response(response, status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Updating CartItem failed"}
        id = kwargs.get("id")
        crt_id= OrderItem.objects.get(id=id)
        serializer = self.serializer_class(data=request.data,instance=crt_id)
        if serializer.is_valid():
            quantity = serializer.validated_data.get("quantity")
            crt_id.quantity = quantity
            crt_id.save()
            # serializer.save()
            response["status"] = status.HTTP_200_OK
            response["data"] = serializer.data
            response["message"] = 'message: Updated Cartitem successfully.'
            return Response(response, status=status.HTTP_200_OK)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        response = {"status":status.HTTP_400_BAD_REQUEST,"message":"Cart Item Deletion Failed"}
        id = kwargs.get("id")
        ct = OrderItem.objects.get(id=id)
        ct.delete()
        response["message"] = "Cart item Removed Successfully"
        response["status"] = status.HTTP_200_OK
        return Response(response,status=status.HTTP_200_OK)

class OrderView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer


    def get(self, request, *args, **kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Fetching Orders failed"}
        order_list = OrderSerializer.objects.all()
        serializer = self.serializer_class(order_list, many=True)
        response["status"] = status.HTTP_200_OK
        response["data"] = serializer.data
        response["message"] = 'Orders Fetched Successfully'
        return Response(response, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Order Placing failed"}
        serializer = self.get_serializer(data=request.data)
        amount = Order.get_total_item_price
        print(amount)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["status"] = status.HTTP_200_OK
            response["data"] = serializer.data
            response["message"] = 'message: Order Placed successfully.'
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)