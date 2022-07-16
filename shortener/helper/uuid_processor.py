from uuid import uuid4

def url_uid():
    uid = str(uuid4())
    uid = uid.split("-")
    return uid[-1]