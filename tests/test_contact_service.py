# import pytest
# from fastapi import HTTPException
# from services.contact_service import createContactService

# @pytest.fixture
# def valid_contact_data():
#     return{
#         "name":"Harshit",
#         "email": "test@test.com",
#         "phone": "123",
#         "address": None
#     }
# def test_create_contact_empty_name(valid_contact_data):
#     data=valid_contact_data
#     with pytest.raises(HTTPException):
#         createContactService(db=None,name="",email=data["email"],phone=data["phone"],address=data["address"])

# # def test_create_contact_empty_email():
# #     with pytest.raises(HTTPException):
# #         createContactService(db=None,name="Harshit",email="",phone="123",address=None)

# # def test_create_contact_empty_phone():
# #     with pytest.raises(HTTPException):
# #         createContactService(db=None, name="Harshit", email="test@test.com", phone="", address=None)

# def test_create_contact_empty_email(valid_contact_data):
#     data = valid_contact_data
#     with pytest.raises(HTTPException):
#         createContactService(db=None, name=data["name"], email="", phone=data["phone"], address=data["address"])


# def test_create_contact_empty_phone(valid_contact_data):
#     data = valid_contact_data
#     with pytest.raises(HTTPException):
#         createContactService(db=None, name=data["name"], email=data["email"], phone="", address=data["address"])