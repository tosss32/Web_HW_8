from mongoengine import Document, StringField, BooleanField
from mongoengine import connect

database_name = "testdb.collone"
uri = f"mongodb+srv://tosss32:antoshyn3289@cluster0.tdfni09.mongodb.net/{database_name}?retryWrites=true&w=majority"
connect(host=uri)


class Contact(Document):
    fullname = StringField(required=True, max_length=255)
    email = StringField(required=True, max_length=255)
    message_sent = BooleanField(default=False)
    # Add other fields as needed

    meta = {"collection": "contacts"}
