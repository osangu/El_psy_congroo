from uuid import UUID
from typing import Set, List, Optional, Union, Dict, Tuple
from dataclasses import dataclass, field


class _User:
    pass


class _Member:
    pass


class _Band:
    pass


class _Post:
    title: str
    writer: Union[_User, _Band]

    def __init__(self, title: str, writer: Union[_User, _Band]):
        self.title = title
        self.writer = writer


class _Recruit(_Post):
    """
    foobar = {'${role}' : {'desired_amount': 2, 'applied_amount': 0}}
        VS
    foo = {'${role}': {'desired_amount': 2}}
    bar = {'${role} : {'applied_amount': 0}}
    """

    pass


@dataclass
class User:
    id: UUID
    name: str
    email: str
    password: str

    phone: Optional[str]
    nic_name: Optional[str]

    def __init__(
            self,
            id: UUID,
            name: str,
            email: str,
            password: str,
            phone: Optional[str] = None,
            nic_name: Optional[str] = None
    ):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.nic_name = nic_name

    def __eq__(self, other: "User"):
        return self.id == other.id


@dataclass
class Member:
    user: User
    role: List[str]

    def __eq__(self, other: "Member"):
        return self.user.id == other.user.id  # `self.user == other.user` will do __eq__ again.


@dataclass
class Band:
    id: UUID
    name: str
    # manager: Member
    members: Set[Member]

    def __eq__(self, other):
        return self.id == other.id


@dataclass
class Post:
    writer: Union[User, Band]
    title: str


@dataclass
class Recruit(Post):
    role_t_o: Dict[str, int]
    role_apply_users: Optional[
        Dict[str, Set[User]]
    ] \
        = field(default_factory=dict)

    def __init__(self, writer, title, role_to_amt: Tuple[str, int]):
        super().__init__(writer, title)

        self.role_t_o = {
            role: amount
            for role, amount in role_to_amt
        }

    @property
    def roles(self):
        return list(self.role_t_o.keys())

    def apply(self, role: str, user: User):
        apply_users: list = self.role_apply_users.get(role)

        if user.phone is None:
            raise ValueError('PHONE_REQUIRE_TO_APPLY')

        apply_users.append(user)
