from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    username: str = Field(..., example="joaodasilva")
    email: EmailStr = Field(..., example="joao@exemplo.com")
    full_name: str = Field(..., example="João da Silva")

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, example="senha_segura")

class UserSchema(UserBase):
    id: int

    class Config:
        orm_mode = True