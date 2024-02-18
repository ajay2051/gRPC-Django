from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("id", "username", "email", "groups")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    id: int
    username: str
    email: str
    groups: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: _Optional[int] = ..., username: _Optional[str] = ..., email: _Optional[str] = ..., groups: _Optional[_Iterable[int]] = ...) -> None: ...

class UserListRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UserRetrieveRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
