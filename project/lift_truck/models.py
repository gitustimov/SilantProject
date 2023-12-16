from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class ModelEquipment(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('model_equipment_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class EngineModel(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('engine_model_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class TransmissionModel(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('transmission_model_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class DriveAxleModel(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('drive_axle_model_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class ControlledBridgeModel(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('controlled_bridge_model_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class TypeTo(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.title


class NatureRefusal(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.title


class RecoveryMethod(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    def __str__(self):
        return self.title


class Service_Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Client(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='user_client')
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Forklift(models.Model):
    machine_serial_number = models.CharField(
        max_length=32)
    model_equipment = models.ForeignKey(
        ModelEquipment, on_delete=models.CASCADE)
    engine_model = models.ForeignKey(
        EngineModel, on_delete=models.CASCADE)
    engine_serial_number = models.CharField(
        max_length=32)
    transmission_model = models.ForeignKey(
        TransmissionModel, on_delete=models.CASCADE)
    transmission_serial_number = models.CharField(
        max_length=32)
    drive_axle_model = models.ForeignKey(
        DriveAxleModel, on_delete=models.CASCADE)
    drive_axle_serial_number = models.CharField(
        max_length=32)
    controlled_bridge_model = models.ForeignKey(
        ControlledBridgeModel, on_delete=models.CASCADE)
    controlled_bridge_serial_number = models.CharField(
        max_length=32)
    delivery_contract = models.CharField(
        max_length=32)
    date_of_shipment = models.DateField()
    end_user = models.CharField(max_length=64)
    delivery_address = models.CharField(max_length=256)
    equipment = models.CharField(max_length=256)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service_company = models.ForeignKey(
        Service_Company, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('forklift_list', args=[str(self.id)])

    def __str__(self):
        return self.machine_serial_number


class To(models.Model):
    type = models.ForeignKey(
        TypeTo, verbose_name='Вид Тo', on_delete=models.CASCADE)
    date = models.DateField(
        verbose_name='Дата проведения ТО')
    operating = models.PositiveIntegerField(
        default=0, verbose_name='Наработка, м/час')
    orders_number = models.CharField(
        max_length=32, verbose_name='№ заказ-наряда')
    orders_date = models.DateField(
        verbose_name='дата заказ-наряда')
    organization = models.CharField(
        max_length=32, verbose_name='Организация, проводившая ТО',)
    car = models.ForeignKey(
        Forklift, verbose_name='Зав. № машины', on_delete=models.CASCADE)
    service_company = models.ForeignKey(
        Service_Company, verbose_name='Сервисная компания', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.orders_number


class Claim(models.Model):
    orders_date = models.DateField(verbose_name='Дата отказа')
    operating = models.PositiveIntegerField(
        default=0, verbose_name='Наработка, м/час',)
    order_note = models.ForeignKey(
        NatureRefusal, verbose_name='Узел отказа', on_delete=models.CASCADE)
    order_description = models.TextField(
        verbose_name='Описание отказа')
    recovery_method = models.ForeignKey(
        RecoveryMethod, verbose_name='Способ восстановления', on_delete=models.CASCADE)
    used_spare_parts = models.TextField(
        verbose_name='Используемые запасные части')
    recovery_date = models.DateField(
        verbose_name='Дата восстановления')
    downtime = models.IntegerField(
        default=0, verbose_name='Время простоя техники')
    car = models.ForeignKey(Forklift, verbose_name='Зав. № машины',
                            on_delete=models.CASCADE)
    service_company = models.ForeignKey(
        Service_Company, verbose_name='Сервисная компания', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-orders_date']

    def __str__(self):
        return self.order_description
