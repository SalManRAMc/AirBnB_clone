#!/usr/bin/python3
"""user.py"""
from models.base_model import BaseModel


class User(BaseModel):
    """user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
