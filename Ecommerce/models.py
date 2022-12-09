from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, name, address, phone, password=None):
        
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            address=address,
            phone=phone
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone =models.CharField(max_length=12,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    def __str__(self):
        return self.name


class Category(models.Model):
    C_CHOICES =(
    ('Mobiles','Mobiles'),
    ('Laptops','Laptops'),
    ('PowerBank','Power Banks'),
    ('Cameras & Accessories','Cameras & Accessories'),
    ('Headphones & Speakers','Headphones & Speakers'),
)
    c_name = models.CharField(choices=C_CHOICES,max_length=30)
    created_date =models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category")
    manufacturer = models.CharField(max_length=100)
    quantity_left = models.PositiveIntegerField()
    quantity_sold = models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    image = models.ImageField(upload_to="images",null=True)
    added_date =models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    class Meta:
        unique_together=('product_name',)


    def __str__(self):
        return self.product_name
    

class Coupon(models.Model):
    code  = models. CharField(max_length=100,unique=True)
    discount = models.FloatField()



class OrderItem(models.Model):
    customer_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="customers")
    orderitem_status = (
        ('active','active'), )
    status = models.CharField(choices=orderitem_status, default="active", max_length=20)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="items")
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together=('customer_id','product_id')

    def __str__(self):
        return f"{self.quantity} of {self.product_id.product_name}"

    def get_total_price(self):
        # print(self.quantity)
        return self.quantity * self.product_id.price


    # def get_total_discount_item_price(self):
    #     return self.quantity * self.item.discount_price

    # def get_orderItems_by_customer(customer_id):
    #     instance= OrderItem.objects.filter(customer_id=customer_id)
    #     return instance

    

class Order(models.Model):
    invoice_no = models.PositiveIntegerField(primary_key=True)
    customer_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name="customer")
    orderitem_id = models.ManyToManyField(OrderItem)
    order_status = (
        ('ordered','ordered'),
        ('pending','pending'),
        ('accepted','accepted'),
        ('packed','packed'),
        ('on the way','on the way'),
        ('delivered','delivered'),
        ('cancel', 'cancel'),
        ('return','return') )
    status = models.CharField(choices=order_status, default="ordered", max_length=20)
    amount = models.PositiveIntegerField(blank=True,null=True)
    order_date = models.DateField(auto_now_add=True)
    coupon_id = models.ForeignKey(Coupon,on_delete=models.CASCADE,blank=True, null=True)

    # def get_orderItems_by_customer(customer_id):
    #     instance= Order.objects.filter(customer_id=customer_id)
    #     return instance
    
    def get_total(self):
        orders =self.orderitem_id.all()
        # print(orders)
        amount=0
        for i in orders:
            amount+=i.get_total_price()
        if self.coupon_id:
            sum=self.coupon_id.discount/100
            amount-=amount*sum
        return amount
    
    