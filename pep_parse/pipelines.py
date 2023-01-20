import csv
from pep_parse.settings import BASE_DIR, time


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses_count = {}
        self.total_count = 0

    def process_item(self, item, spider):
        status = item['status']
        value = self.statuses_count.get(status, 0) + 1
        self.statuses_count[status] = value
        self.total_count += 1
        return item

    def close_spider(self, spider):
        filename = f'status_summary_{time}.csv'
        file_path = BASE_DIR / 'results' / filename
        with open(file_path, mode='w', encoding='utf-8') as f:
            fieldnames = ('Статус', 'Количество')
            writer = csv.writer(f)
            writer.writerow(fieldnames)
            writer.writerows(self.statuses_count.items())
            writer.writerow(['Total', self.total_count])
