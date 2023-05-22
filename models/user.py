#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
import models
import os


class User(BaseModel):

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
