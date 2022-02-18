from dataclasses import dataclass


@dataclass
class User:
    profile_pic: str
    name: str
    email: str
