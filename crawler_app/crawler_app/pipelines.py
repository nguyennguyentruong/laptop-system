# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlerAppPipeline:
    def process_item(self, item, spider):
        return item

import json

class JsonWriterPipeline:
    def open_spider(self, spider):
        # Mở file JSON để ghi dữ liệu
        self.file = open('output.json', 'w')
        self.data = []

    def close_spider(self, spider):
        # Ghi dữ liệu vào file JSON và đóng file
        
        json.dump(self.data, self.file, indent=4)
        self.file.close()

    def process_item(self, item, spider):
        # Thêm item vào danh sách dữ liệu
        self.data.append(dict(item))
        return item