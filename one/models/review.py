<<<<<<< HEAD
#!/usr/bin/python3
'''This module creates a Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Class for managing review objects'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the review class'''
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3
'''This module creates a Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''Class for managing review objects'''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the review class'''
        super().__init__(*args, **kwargs)
>>>>>>> 0fcf709cac02cd9b47be8688d3b837c11c044ec5
