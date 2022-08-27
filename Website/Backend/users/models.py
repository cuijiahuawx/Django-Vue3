from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, user_name, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            user_name=user_name,
            **other_fields,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        max_length=50,
        unique=True,
        verbose_name='注册邮箱'
    )
    user_name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='用户名'
    )
    regtime = models.DateTimeField(
        default=timezone.now,
        verbose_name='注册时间'
    )
    avatar = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        verbose_name='头像'
    )

    musicEmail = models.EmailField(
        max_length=50,
        unique=True,
        null=True,
        blank=True,
        verbose_name='音乐邮箱'
    )
    musicID = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='音乐号'
    )

    objects = CustomUserManager()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        ordering = ['-regtime']
        verbose_name = '用户'
        verbose_name_plural = '用户们'

    def __str__(self):
        return self.user_name
