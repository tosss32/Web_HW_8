from mongoengine import connect


def connectdb():
    database_name = "testdb.collone"
    uri = f"mongodb+srv://tosss32:Antoshyn3289@cluster0.tdfni09.mongodb.net/{database_name}?retryWrites=true&w=majority"
    connect(host=uri)
