from django.db import models

# Create your models here.


class Person():

    product = "Multimedya Oynatıcı"
    ramMemory = "4GB"
    memory = "64GB"
    operatingSystem = "Android"
    display = "1280*720"
    language = "Türkçe, İngilizce, Fransızca, İtalyanca, Portekizce, Almanca, İspanyolca ,Çin, Rusça, Norveç, Çince, Japonca"
    screenSize ="8 inç"




CAR_MODELS = [
    ("Albea", "Albea"),
    ("Alfa Romeo", "Alfa Romeo"),
    ("Audi", "Audi"),
    ("BMW", "BMW"),
    ("Chevrolet", "Chevrolet"),
    ("Citroen", "Citroen"),
    ("Opel", "Opel"),
    ("Renault", "Renault"),
    ("Dacia", "Dacia"),
    ("Fiat", "Fiat"),
    ("Ford", "Ford"),
    ("Volkswagen", "Volkswagen"),
    ("Honda", "Honda"),
    ("Hyundai", "Hyundai"),
    ("Jeep", "Jeep"),
    ("Kia", "Kia"),
    ("Mazda", "Mazda"),
    ("Mercedes", "Mercedes"),
    ("Mini", "Mini"),
    ("Mitsubishi", "Mitsubishi"),
    ("Nissan", "Nissan"),
    ("Peugeot", "Peugeot"),
    ("Porsche", "Porsche"),
    ("Range Rover", "Range Rover"),
    ("Seat", "Seat"),
    ("Skoda", "Skoda"),
    ("Subaru", "Subaru"),
    ("Toyota", "Toyota"),
    ("Isuzu", "Isuzu"),
]

class Product(models.Model):
    brand = models.CharField(max_length=100)  # BLAM, Devecioğlu vb.
    title = models.CharField(max_length=255)  # Ürün başlığı
    price = models.CharField(max_length=50)   # 11.599 TL gibi
    model = models.CharField(max_length=50, choices=CAR_MODELS)
    image = models.ImageField(upload_to='products/')
    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    
    




