from address import Address
from mailing import Mailing

to_addr = Address(index="100000",
                  city="Краснодар",
                  street="Возничья",
                  house="52",
                  apartment="12"
                  )

from_addr = Address(index="120340",
                    city="Saint-Petersburg",
                    street="Невский проспект",
                    house="10",
                    apartment="19"
                    )

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=500,
    track="RU123456789"
)

print(f"Отправление {mailing.track} из "
      f"{mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.house} - "
      f"{mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
