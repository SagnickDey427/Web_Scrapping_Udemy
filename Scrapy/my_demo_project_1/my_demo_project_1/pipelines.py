# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter # type: ignore


class MyDemoProject1Pipeline:
    def process_item(self, item, spider):
        return item


class BookscraperPipeline:
    def process_item(self, item, spider):

        # Clean up the whitespace in the title
        item['title'] = item['title'].strip() if item['title'] else None
        
        # Convert price to float, removing currency symbols and handling errors
        price = item.get('price', '').replace('£', '').replace('$', '').strip()
        try:
            item['price'] = float(price) if price else None
        except ValueError:
            item['price'] = None

        # Separate the rating value and map it to numerical values
        rating_map = {
            'One': 1,
            'Two': 2,
            'Three': 3,
            'Four': 4,
            'Five': 5
        }
        rating_val = item.get('rating', '')
        rating = rating_val.split()[-1] if rating_val else 'NA'
        item['rating'] = rating_map.get(rating, None)

        return item