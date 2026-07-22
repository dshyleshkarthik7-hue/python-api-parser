from dataclasses import dataclass


@dataclass
class UserProfile:
    id: int
    username: str
    email: str
    city: str = "Unknown"
    zipcode: str = "Unknown"
