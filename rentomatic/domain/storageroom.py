from rentomatic.shared.domain_model import DomainModel

class StorageRoom(Object):

    def __init__(self, code, size, price, latitude, longitude):
        self.code = code
        self.size = size
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    # Decorator that allow you to create class methods that are passed the actual class object within the function call,
    @classmethod
    def from_dict(cls, adict):
        room = StorageRoom(
                code=adict['code'],
                size=adict['size'],
                price=adict['price'],
                latitude=adict['latitude'],
                longitude=adict['longitude'],
        )

        return room

    def to_dict(self):
        return {
            'code': self.code
            'size': self.size
            'price': self.price
            'latitude': self.latitude
            'longitude': self.longitude
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

DomainModel.register(StorageRoom)
