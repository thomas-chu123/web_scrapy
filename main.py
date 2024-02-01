import sys
from scrapy import cmdline

def main(name):
    cmdline.execute(f"scrapy crawl {sys.argv[1]} -o test.json".split())

if __name__ == '__main__':
    main('test')
