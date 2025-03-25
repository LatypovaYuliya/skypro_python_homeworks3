from Address import Address
from Mailing import Mailing

mailing = Mailing(Address("453100", "Стерлитамак", "Октября", "55", "143"),
                   Address("423516", "Самара", "Гагарина", "5", "68"), 300,
                    "PHY875PY")


print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")