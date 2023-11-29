from django.db import models

# Create your models her


class Students(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    usn = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, unique=True)

    def __str__(self): #string representation
        return str(self.id)


class Marks(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return str(self.student)


# s1 -> m1

# models.CASCADE
# models.SET_NULL
