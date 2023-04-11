from abc import ABC, abstractmethod
from typing import List
class Observer(ABC):
    @abstractmethod
    def update(self, order_id: int):
        ...


class Subject(ABC):
    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, order_id: int) -> None:
        for observer in self._observers:
            observer.update(order_id)

class Data(Subject):
    _id: int = 1

    def __init__(self, name =''):
        Subject.__init__(self)
        self.id = Data._id
        self._data = ""
        Data._id+=1


    @property
    def data(self):
        return self._data
 

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()

class Regonizing:
    def update(self, subject):

        print('Subject' + str(subject.id) + 'has data '+str(oct(subject.data)))
 
 