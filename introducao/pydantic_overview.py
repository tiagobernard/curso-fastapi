from pydantic import BaseModel, field_validator

class User(BaseModel):
    idade: int
    nome: str
    email: str

    @field_validator('email')
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('Email must contain @')
        return value


def f(user: User):
    user.email
    pass

user = User(nome = 'Tiago Bernardes', idade=43, email='tiago@lab82.dev')