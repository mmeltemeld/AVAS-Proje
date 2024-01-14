from pymongo import MongoClient




self.client = MongoClient('databaselocalhostismi')

self.db = self.client('avas')
self.users_colection = self.db