# for future implementation
from pymongo import MongoClient

class mongo_conn:

    def send_data(self, req):
        client = MongoClient()
        db = client.calypso_test
        coll = db.text
        resp = db.coll.insert_one({ "str" : req }).inserted_id
        return "Calypso: " + str(resp)

    def retrieve_data(self, resp):
        print "dummy string"