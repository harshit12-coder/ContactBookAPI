from repos.contact_repo import CreateContactRepo,UpdateContactRepo,GetAllContactRepo,GetContactByIdRepo,deleteContactRepo,SearchContactRepo
from fastapi import HTTPException

def createContactService(db,name,email,phone,address):
    if name.strip() =="":
        raise HTTPException(status_code=400,detail="Name cannot be empty")
    if email.strip() =="":
        raise HTTPException(status_code=400,detail="Email cannot be empty")
    if phone.strip() =="":
        raise HTTPException(status_code=400,detail="Phone cannot be empty")
    new_contact=CreateContactRepo(db,name,email,phone,address)
    return new_contact

def UpdateContactService(db, contactId, name, email, phone, address):
    updated_contact = UpdateContactRepo(db, contactId, name, email, phone, address)
    if updated_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")   # add
    return updated_contact

def getAllContactsService(db):
    contacts=GetAllContactRepo(db)
    if contacts is None:
        raise HTTPException(status_code=404,detail="Not Found")
    return contacts

def getContactByIdService(db, contactId):
    contact = GetContactByIdRepo(db, contactId)
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")   # add
    return contact

def searchContactService(db,name):
    result=SearchContactRepo(db,name)
    return result

def deleteContactService(db, contactId):
    deleted_contact = deleteContactRepo(db, contactId)
    if deleted_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")   # add
    return deleted_contact