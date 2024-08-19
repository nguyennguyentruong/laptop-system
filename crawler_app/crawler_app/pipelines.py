import pymongo


class MongoDBPipeline:

    def open_spider(self, spider):
        # Initialize MongoDB connection with authentication
        self.client = pymongo.MongoClient(
            "mongodb://root:password123@mongodb-primary:27017/?directConnection=true"
        )
        self.db = self.client['laptops_db']
        self.collection = self.db["laptops"]

    def close_spider(self, spider):
        # Close MongoDB connection
        self.client.close()

    def process_item(self, item, spider):
        # Insert item into MongoDB
        self.collection.insert_one(dict(item))
        return item
