import sqlalchemy
from db import metadata, engine

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("username", sqlalchemy.String(400), index=True),
    sqlalchemy.Column("email", sqlalchemy.String(400), index=True),
    sqlalchemy.Column("hashed_password", sqlalchemy.String(400)),
    sqlalchemy.Column("is_active", sqlalchemy.Boolean(), default=True),
    sqlalchemy.Column("is_superuser", sqlalchemy.Boolean(), default=False)
)

metadata.create_all(bind=engine)
