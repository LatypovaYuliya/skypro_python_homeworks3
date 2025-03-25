from smartphone import Smartphone
catalog = [
    Smartphone("Iphone", "16", "+79275446321"), 
    Smartphone("Samsung", "Galaxy s24", "+79174557649"),
    Smartphone("Huawey", "Pura 70", "+79876286911"),
    Smartphone("Mi", "MiPhone", "+79173696303"),
    Smartphone("Siemens", "A35", "+79621485598")
    ]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")