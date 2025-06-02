"""
============Think=============

1. Should I make Repository(ABC)..?

2. How to use multiple O(R,D)M with ABC

===========Solution============

class Repository(ABC):

    @staticmethod
    @abstractmethod
    def eg_save(foo: str, _):
        pass

class FooImpl(Repository):

    def save(self, *_, user):
        self.magical_thing.save(user)


class BeanieImpl(Repository):

    @staticmethod
    async def save(*_, user):
        await user.save()


class AlchemyImpl(Repository):

    @staticmethod
    def save(*_, user, session):
        session.add(user)


============Result=============
>> beanie = BeanieImpl()
>> alchemy = AlchemyImpl()
>> foo = FooImpl(magical_thing=session)
>>
>> beanie.save(user='')
>> foo.save(user='')
>> alchemy.save(user='', session='')
"""
