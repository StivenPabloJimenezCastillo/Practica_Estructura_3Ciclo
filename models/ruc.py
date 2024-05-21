from enum import Enum

class EnumRuc(Enum):
    EDUCATIVO = 'EDUCATIVO'
    PROFECIONAL = 'PROFECIONAL'
    
    def __str__(self):
        return self.value
