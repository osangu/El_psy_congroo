from .register import UserRegister
from .profile import UserProfile


class UserService:
    profile: UserProfile = UserProfile
    register: UserRegister = UserRegister
