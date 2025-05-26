from dataclasses import dataclass

from fastapi import Form
from pydantic import EmailStr
from schemas.common.forms import BaseForm, convert_dc_to_pd


class Register(BaseForm):
    email: EmailStr
    nickname: str
    password: str


@dataclass
class _RegisterDC:
    email: EmailStr = Form(...)
    nickname: str = Form(...)
    password: str = Form(...)


register = convert_dc_to_pd(_RegisterDC, Register)


class Login(BaseForm):
    username: EmailStr
    password: str


@dataclass
class _LoginDC:
    username: EmailStr = Form(...)
    password: str = Form(...)


login = convert_dc_to_pd(_LoginDC, Login)
