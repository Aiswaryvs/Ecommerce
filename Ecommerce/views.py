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
    filter_backends = [SearchFilter]
    search_fields = ['c_name']
    
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


class CartView(generics.ListCreateAPIView):
    serializer_class =  CartSerializer
    
    def get(self, request, *args, **kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Fetching CartItems failed"}
        cart_list = OrderItem.objects.all()
        # cart_list = OrderItem.get_orderItems_by_customer(6)
        print(cart_list.values())
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
        order_list = Order.objects.all()
        # order_id = request.data["orderitem_id"]
        # print(order_id.product_id)
        # for i in order_list:
        #     print(i.get_total())
        # order_list= Order.get_orderItems_by_customer(4)
        print(order_list.values())
        serializer = self.serializer_class(order_list, many=True)
        response["status"] = status.HTTP_200_OK
        response["data"] = serializer.data
        response["message"] = 'Orders Fetched Successfully'
        return Response(response, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Order Placing failed"}
        serializer = self.get_serializer(data=request.data)
        sts=request.data['status']
        print(sts)
        id=request.data['orderitem_id']
        print(id)
        for i in id:
            items = OrderItem.objects.get(id=i)
            print(items.product_id.quantity_left)
            print(items.product_id.quantity_sold)
            if sts=="ordered":
                items.product_id.quantity_left=items.product_id.quantity_left-1
                items.product_id.quantity_sold=items.product_id.quantity_sold+1
                print(items.product_id.quantity_sold)
                print(items.product_id.quantity_left)
                items.product_id.save()
        
        if serializer.is_valid(raise_exception=True):
                order_object=serializer.save()
                order_object.amount = order_object.get_total()
                serializer.save()
                
                # order_obj = Order.objects.get(customer_id=request.data['customer_id'])
                # print(order_obj)
                # print('llll', order_obj.orderitem_id)
                # print(order_obj.get_total())
                # print(order_object.amount)
       
                response["status"] = status.HTTP_200_OK
                response["data"] = serializer.data
                response["message"] = 'message: Order Placed successfully.'
                return Response(response, status=status.HTTP_201_CREATED)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

   

class OrderDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = OrderSerializer
    def get(self,request,*args,**kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message":"Fetching Order failed"}
        id= kwargs.get("id")
        order= Order.objects.get(invoice_no=id)
        serializer= self.serializer_class(order)
        response["status"] = status.HTTP_200_OK
        response["data"] = serializer.data
        response["message"] = 'message: Order fetched successfully.'
        return Response(response, status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        # response = {'status':status.HTTP_400_BAD_REQUEST, "message":"Updating Order failed"}
        id = kwargs.get("id")
        r_id=request.data['orderitem_id']
        print(id)
        print(r_id)
        od_id= Order.objects.get(invoice_no=id)
        serializer = self.serializer_class(data=request.data,instance=od_id)
        if serializer.is_valid():
            status = serializer.validated_data.get("status")
            od_id.status = status
            od_id.save()
            if status=="cancel" or "return":
                for i in r_id:
                    items = OrderItem.objects.get(id=i)
                    items.product_id.quantity_left=items.product_id.quantity_left+1
                    items.product_id.quantity_sold=items.product_id.quantity_sold-1
                    print( items.product_id.quantity_left)
                    print( items.product_id.quantity_sold)
                    items.product_id.save()
                # serializer.save()
                # response["status"] = status.HTTP_200_OK
                # response["data"] = serializer.data
                # response["message"] = 'message: Updated Order successfully.'
                return Response(data=serializer.data)
            else:
                return Response({"cancellation of order failed"}) 
    
    
    def delete(self,request,*args,**kwargs):
        response = {"status":status.HTTP_400_BAD_REQUEST,"message":"Order Deletion Failed"}
        id = kwargs.get("id")
        od = Order.objects.get(invoice_no=id)
        od.delete()
        response["message"] = "Order Removed Successfully"
        response["status"] = status.HTTP_200_OK
        return Response(response,status=status.HTTP_200_OK)

class CouponView(generics.ListCreateAPIView):
    serializer_class = CouponSerializer


    def get(self, request, *args, **kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Fetching Coupons failed"}
        coupon_list = Coupon.objects.all()
        serializer = self.serializer_class(coupon_list, many=True)
        response["status"] = status.HTTP_200_OK
        response["data"] = serializer.data
        response["message"] = 'Coupons Fetched Successfully'
        return Response(response, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message": "Coupon Creation failed"}
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["status"] = status.HTTP_200_OK
            response["data"] = serializer.data
            response["message"] = 'message: Coupon Created successfully.'
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class CouponDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CouponSerializer


    def get(self,request,*args,**kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message":"Fetching Coupon failed"}
        id = kwargs.get("id")
        coupon= Coupon.objects.get(id=id)
        serializer= self.serializer_class(coupon)
        response["status"] = status.HTTP_200_OK
        response["data"] = serializer.data
        response["message"] = 'message: Coupon fetched successfully.'
        return Response(response, status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        response = {'status':status.HTTP_400_BAD_REQUEST, "message":"Updating Coupon failed"}
        id = kwargs.get("id")
        cp_id= Coupon.objects.get(id=id)
        serializer = self.serializer_class(data=request.data,instance=cp_id)
        if serializer.is_valid():
            serializer.save()
            response["status"] = status.HTTP_200_OK
            response["data"] = serializer.data
            response["message"] = 'message: Updated Coupon successfully.'
            return Response(response, status=status.HTTP_200_OK)
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        response = {"status":status.HTTP_400_BAD_REQUEST,"message":"Coupon Deletion Failed"}
        id = kwargs.get("id")
        cp = Coupon.objects.get(id=id)
        cp.delete()
        response["message"] = "Coupon Removed Successfully"
        response["status"] = status.HTTP_200_OK
        return Response(response,status=status.HTTP_200_OK)
