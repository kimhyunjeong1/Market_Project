from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    category_description = models.TextField()

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('이메일이 필요합니다.')
        email = self.normalize_email(email)
        user = self.model(user_userid=username, user_email=email)  # user_userid와 user_email을 사용
        user.set_password(password)  # 비밀번호 해시화
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)  # 사용자 고유 ID
    user_userid = models.CharField(max_length=50, unique=True)  # 사용자 계정 아이디
    user_email = models.EmailField(max_length=100, unique=True)  # 이메일
    user_name = models.CharField(max_length=255)  # 이름
    user_address = models.CharField(max_length=255, blank=True)  # 주소
    user_phoneNum = models.CharField(max_length=11, blank=True)  # 휴대폰
    user_created_at = models.DateTimeField(auto_now_add=True)  # 계정 생성 날짜

    objects = UserManager()

    USERNAME_FIELD = 'user_userid'  # 로그인할 때 사용할 필드
    REQUIRED_FIELDS = ['user_email']  # 추가로 요구할 필드

    def __str__(self):
        return self.user_userid

class Product(models.Model):
    product_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(max_length=20, default='판매 중')
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updated_at = models.DateTimeField(auto_now=True)
    product_image_url = models.CharField(max_length=255, blank=True, null=True)
    product_wish_count = models.IntegerField(default=0)

class UserProduct(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Review(models.Model):
    review_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    review_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_rating = models.IntegerField()
    review_comment = models.TextField(blank=True, null=True)
    review_created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    message_sender = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sent_messages')
    message_receiver = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='received_messages')
    message_content = models.TextField()
    message_sent_at = models.DateTimeField(auto_now_add=True)
    message_read_status = models.BooleanField(default=False)

class Wishlist(models.Model):
    wishlist_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    wishlist_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wishlist_added_at = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    notification_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    notification_message = models.TextField()
    notification_type = models.CharField(max_length=50)
    notification_read_status = models.BooleanField(default=False)
    notification_created_at = models.DateTimeField(auto_now_add=True)


class MyShop(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)  # Users 테이블의 user_id를 외래 키로 참조
    shop_name = models.CharField(max_length=100)  # 상점 이름
    shop_info = models.TextField(blank=True, null=True)  # 상점 정보
    shop_image = models.CharField(max_length=255, blank=True, null=True)  # 상점 이미지 경로

    def __str__(self):
        return self.shop_name
