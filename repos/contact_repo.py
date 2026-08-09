from models.contact_model import Contact

def CreateContactRepo(db,name,email,phone,address):
    new_contact=Contact(
        name=name,
        email=email,
        phone=phone,
        address=address
                        )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

def GetAllContactRepo(db):
    contacts=db.query(Contact).all()
    if contacts is None:
        return None
    return contacts

def GetContactByIdRepo(db,contactId):
    contact=db.query(Contact).filter(Contact.id==contactId).first()
    if contact is None:
        return None
    return contact

def SearchContactRepo(db,name):
    contact=db.query(Contact).filter(Contact.name.ilike(f"%{name}%")).all()
    if contact is None:
        return None
    return contact
# def GetContactByPhoneNumberRepo(db,phone):
#     contact=db.query(Contact).filter(Contact.phone==phone).first()
#     if contact is None:
#         return None
#     return contact

# def GetContactByEmailRepo(db,email):
#     contact=db.query(Contact).filter(Contact.email==email).first()
#     if contact is None:
#         return None
#     return contact

def UpdateContactRepo(db,contactId,name,email,phone,address):
    contact=db.query(Contact).filter(Contact.id==contactId).first()
    if contact is None:
        return None
    if name is not None:
        contact.name = name
    if email is not None:
        contact.email = email
    if phone is not None:
        contact.phone = phone
    if address is not None:
        contact.address = address
    db.commit()
    db.refresh(contact)
    return contact
    # else:
    #     if name is None and email and phone and address:
    #         contact.email=email
    #         contact.phone=phone
    #         contact.address=address
    #         db.commit()
    #         db.refresh(contact)
    #         return contact
    #     if email is None and name and phone and address:
    #         contact.name=name
    #         contact.phone=phone
    #         contact.address=address
    #         db.commit()
    #         db.refresh(contact)
    #         return contact
    #     if phone is None and name and email and address:
    #         contact.name=name
    #         contact.email=email
    #         contact.address=address
    #         db.commit()
    #         db.refresh(contact)
    #         return contact
    #     if address is None and name and email and phone:
    #         contact.name=name
    #         contact.email=email
    #         contact.phone=phone
    #         db.commit()
    #         db.refresh(contact)
    #         return contact

def deleteContactRepo(db,contactId):
    contact=db.query(Contact).filter(Contact.id==contactId).first()
    if contact is None:
        return None
    db.delete(contact)
    db.commit()
    return contact