from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_profile'
    )
    # 性别
    sex_choices = (
        ('male', '男'),
        ('female', '女'),
    )
    sex = models.CharField(max_length=10,
                           choices=sex_choices)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return '用户:{}'.format(self.user.username)


class RentInfo(models.Model):
    # 所属小区
    xiaoqu = models.CharField(max_length=100)
    # 面积
    area = models.FloatField()
    # 户型
    house_type = models.CharField(max_length=100)
    # 月租金
    rental_per_month = models.IntegerField()

    def __str__(self):
        return '小区:{},面积:{},户型:{},月租:{}'.format(
            self.xiaoqu, self.area, self.house_type, self.rental_per_month
        )


class SaleInfo(models.Model):
    # 所属小区
    xiaoqu = models.CharField(max_length=100)
    # 面积
    area = models.FloatField()
    # 户型
    house_type = models.CharField(max_length=100)
    # 房价
    price = models.IntegerField()

    def __str__(self):
        return '小区:{},面积:{},户型:{},房价:{}'.format(
            self.xiaoqu, self.area, self.house_type, self.price
        )


# 租房佣金
class RentCommission(models.Model):
    rent_contract = models.OneToOneField('RentContract',
                                         on_delete=models.CASCADE)

    commission = models.IntegerField()


# 售房佣金
class SaleCommission(models.Model):
    sale_contract = models.OneToOneField('SaleContract',
                                         on_delete=models.CASCADE)

    commission = models.IntegerField()


# 租房合同
class RentContract(models.Model):
    rent_info = models.ForeignKey(RentInfo,
                                  on_delete=models.PROTECT)
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT)
    rent_date = models.DateField(auto_now_add=True)

    months_of_rent = models.IntegerField()

    real_rental_per_month = models.IntegerField()

    commission_rate = models.FloatField()

    note = models.TextField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        rent_commission = RentCommission()
        rent_commission.rent_contract = self
        rent_commission.commission = int(self.real_rental_per_month * self.months_of_rent * self.commission_rate)
        rent_commission.save()


# 售房合同
class SaleContract(models.Model):
    sale_info = models.ForeignKey(SaleInfo,
                                  on_delete=models.PROTECT)
    user = models.ForeignKey(User,
                             on_delete=models.PROTECT)
    sale_date = models.DateField(auto_now_add=True)

    real_price = models.IntegerField()

    commission_rate = models.FloatField()

    note = models.TextField()




