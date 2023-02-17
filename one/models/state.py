<<<<<<< HEAD
#!/usr/bin/python3
'''This module creates a User class'''
from models.base_model import BaseModel


class State(BaseModel):
    '''Class for managing state objects'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the State class'''
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3
'''This module creates a User class'''
from models.base_model import BaseModel


class State(BaseModel):
    '''Class for managing state objects'''
    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the State class'''
        super().__init__(*args, **kwargs)
>>>>>>> 0fcf709cac02cd9b47be8688d3b837c11c044ec5
