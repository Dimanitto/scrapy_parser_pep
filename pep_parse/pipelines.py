import csv
from pep_parse.settings import BASE_DIR, time


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses_count = {}

    def process_item(self, item, spider):
        status = item['status']
        if self.statuses_count.get(status):
            self.statuses_count[status] += 1
        else:
            self.statuses_count[status] = 1
        return item

    def close_spider(self, spider):
        filename = f'status_summary_{time}.csv'
        file_path = BASE_DIR / 'results' / filename
        with open(file_path, mode='w', encoding='utf-8') as f:
            fieldnames = ('Статус', 'Количество')
            writer = csv.writer(f)
            writer.writerow(fieldnames)
            for key, value in self.statuses_count.items():
                writer.writerow([key, value])
            total_count = sum(self.statuses_count.values())
            writer.writerow(['Total', total_count])
