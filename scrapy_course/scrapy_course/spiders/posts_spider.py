import scrapy

class PostSpider(scrapy.Spider):
    name = 'courses'
    start_urls = ['http://collegecatalog.uchicago.edu/thecollege/economics/']

    def parse(self,response):
        courses = response.css('div.courseblock.main')
        for course in courses:
            yield {
                'title' : course.css('p.courseblocktitle::text').get(),
                'desc' : course.css('p.courseblockdesc::text').get(),
                'time_prereq' : course.css('p.courseblockdetail::text').get(),
            }
