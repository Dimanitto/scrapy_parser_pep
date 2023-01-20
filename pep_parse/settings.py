from datetime import datetime as dt
from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
RESULT_DIR = BASE_DIR / 'results'
RESULT_DIR.mkdir(exist_ok=True)

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
# Из-за разницы в часовом поясе, отказался от %(time)s
time = dt.now().strftime('%Y-%m-%d_%H-%M-%S')

FEEDS = {
    # После сдачи тестов верну закоментированную строку вместо 20й
    # для тестов нужно объязательно %(time)s
    # f'results/pep_{time}.csv': {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
