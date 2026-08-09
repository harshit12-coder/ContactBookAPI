from fastapi import APIRouter,Depends
from services.contact_service import createContactService,UpdateContactService,deleteContactService,getContactByIdService,getAllContactsService,searchContactService
from core.database import get_db
from schemas.contact_schemas import CreateContact,UpdateContact,ContactResponse


router=APIRouter(prefix="/contacts")

@router.get("/",response_model=list[ContactResponse])
def getAllContacts(db=Depends(get_db)):
    contacts=getAllContactsService(db)
    return contacts

@router.post("/",response_model=ContactResponse)
def createContact(body:CreateContact,db=Depends(get_db)):
    new_contact=createContactService(db,body.name,body.email,body.phone,body.address)
    return new_contact

@router.get("/search",response_model=list[ContactResponse])
def searchContact(name:str,db=Depends(get_db)):
    res=searchContactService(db,name)
    return res

@router.get("/{contactId}",response_model=ContactResponse)
def getContactById(contactId:int,db=Depends(get_db)):
    contact=getContactByIdService(db,contactId)
    return contact

@router.put("/{contactId}",response_model=ContactResponse)
def updateContact(body:UpdateContact,contactId:int,db=Depends(get_db)):
    updated_contact=UpdateContactService(db,contactId,body.name,body.email,body.phone,body.address)
    return updated_contact

@router.delete("/{contactId}",response_model=ContactResponse)
def deleteContact(contactId:int,db=Depends(get_db)):
    deleted_contact=deleteContactService(db,contactId)
    return deleted_contact

