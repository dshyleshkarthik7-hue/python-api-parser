from models import UserProfile


class UserParser:

    @staticmethod
    def from_dict(data: dict) -> UserProfile:
        address = data.get("address") or {}

        return UserProfile(
            id=data["id"],
            username=data.get("username", "Anonymous"),
            email=data.get("email", "N/A"),
            city=address.get("city", "Unknown"),
            zipcode=address.get("zipcode", "Unknown"),
        )
