from pydantic import BaseModel

# insert用のrequest model。id(自動採番)は入力不要のため定義しない。


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool

# update用のrequest model


class UserUpdate(BaseModel):
    id: int
    username: str
    email: str
    password: str
    is_active: bool
    is_superuser: bool

# select用のrequest model。selectでは、パスワード不要のため定義しない。


class UserSelect(BaseModel):
    username: str
    email: str
    is_active: bool
    is_superuser: bool
