"""
Aggregation (Has-A Relationship)

Keys words: Holds, Part of life.

Aggregation is a special type of association used when ever there exists a WHOLE PART relation ship between the two classes.

Here Whole is made up of one or more parts.
Part can be added or removed from the whole without disturbing its, functionalities.
The lifecycle of a PART class is independent of the WHOLE class’s lifecycle, in other words, WHOLE and PART are independent of each other (one can exists with out the other).
Examples:

WHOLE	     ->     PART
------------------------
Team	            Player
Club	            Member
Library	            Book
Car	Music           player
Youtube Channel	    Subscriber

"""


class Subscriber:
    def __init__(self, name, email, country) -> None:
        self.__name = name
        self.__email = email
        self.__country = country

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def country(self):
        return self.__country


class Channel:

    def __init__(self, channel_name) -> None:
        self.channel_name = channel_name
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def get_subscribers_count(self):
        return len(self.subscribers)


if __name__ == "__main__":
    s1 = Subscriber("Sahit", "sahit@gmail.com", "INDIA")
    s2 = Subscriber("Jack", "jack@gmail.com", "USA")
    s2 = Subscriber("Martin", "martin@gmail.com", "UK")

    c1 = Channel("TechTalk")
    c2 = Channel("Netflix")

    c1.subscribe(s1)
    print(f'no. of subscribes:  {c1.get_subscribers_count()}')
    print(f'no. of subscribes:  {c2.get_subscribers_count()}')
