from smartphone import Smartphone

catalog = [Smartphone("Apple", "iPhone 18", "+79991110022"),
           Smartphone("Google", "Pixel 11", "+79992221133"),
           Smartphone("Samsung", "Galaxy S25", "+79993332244"),
           Smartphone("OnePlus", "OnePlus 15T", "+79994443355"),
           Smartphone("Xiaomi", "Xiaomi 14", "+79995554466")
           ]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}, {phone.phone_number}")
