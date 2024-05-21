from typing import TypeVar, Generic, Type
from controls.linked.linkedList import Linked_List
import os.path

import json
import os

T = TypeVar('T')
class DaoAdapter(Generic[T]):
    atype: T
    def __init__(self, atype: T):
        self.atype = atype
        self.lista = Linked_List()
        self.file = atype.__name__.lower() + ".json"
        self.URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+"/data/"
    
    def _list(self) -> T:
        if os.path.isfile(self.URL+self.file):
            with open(self.URL+self.file, "r") as f:
                datos = json.load(f)
                self.lista.clear
                for data in datos:
                    a = self.atype.deserializar(data)
                    self.lista.add(a, self.lista._length)
        return self.lista
    
    
    def __tranform__(self):
        return json.dumps([self.lista.get(i).serializable for i in range(self.lista._length)])
    
    
    def to_dic(self):
        return [self.lista.get(i).serializable for i in range(self.lista._length)]
            
        
    def _save(self, data: T):
        self._list()
        self.lista.add(data, self.lista._length)
        with open(self.URL + self.file, "w") as a:
            a.write(self.__tranform__())
            
                
    def _merge(self, data: T, pos):
        self._list()
        self.lista.edit(data, pos)
        with open(self.URL + self.file, "w") as a:
            a.write(self.__tranform__())