from django.db import models, transaction
from django.forms import ValidationError

# User аккаунта 
class Customer(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=200, verbose_name='Телефон', null=True, blank=True)
    balance = models.IntegerField(default=0)
    
    def debit(self, amount):
        self.balance -= amount
        self.save()

    def credit(self, amount):
        self.balance += amount
        self.save()

    def __str__(self):
        return f'{self.name}, {self.balance}'


class Transaction(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sender')
    reseiver = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reseiver')
    amount = models.DecimalField(max_digits=10, decimal_places=2)


    def clean(self):
        if self.sender.balance < self.amount:
            raise ValidationError('Недостаточно средств')
        if self.sender == self.reseiver:
            raise ValidationError('Нельзя перевести самому себе')
        if self.amount <= 0:
            raise ValidationError('Сумма должна быть больше 0')


    def save(self, *args, **kwargs):
        with transaction.atomic():
            self.sender.debit(self.amount)
            self.reseiver.credit(self.amount)
            super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.sender} -> {self.reseiver} : {self.amount}'
        
