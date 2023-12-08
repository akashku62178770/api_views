from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import uuid 
# Create your models her


class MyUserManager(BaseUserManager):
    def create_user(self, email, phone, name, password=None):
        """
        Creates and saves a User with the given email, phone, name and password.
        """
        if not email and not phone and not name:
            raise ValueError("Users must have an email address, phone and name")

        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
            name=name,
        )

        user.set_password(password)
        user.email_verified = True

        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, name, password=None):
        """
        Creates and saves a User with the given email, phone, name and password.
        """
        user = self.create_user(
            email,
            password=password,
            phone=phone,
            name=name,
        )
        user.is_admin = True
        user.email_verified = True
        user.phone_verified = True
        user.save(using=self._db)
        return user






class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name= models.CharField(max_length=255)
    phone = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_hod = models.BooleanField(default=False)
    is_principal = models.BooleanField(default=False)
    image = models.ImageField("user_image", null=True, blank=True)

    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
 
    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone", "name"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin













class Students(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sem  = models.IntegerField()
    usn = models.CharField(max_length=10)

    def __str__(self): #string representation
        return str(self.user)


class Marks(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return str(self.student)


# s1 -> m1

# models.CASCADE
# models.SET_NULL
