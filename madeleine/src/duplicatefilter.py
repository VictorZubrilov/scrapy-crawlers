from scrapy.dupefilter import RFPDupeFilter
from scrapy.utils.job import job_dir
import os

class DupeFilter(RFPDupeFilter):
    def __init__(self, path="/", debug=True, file_seen='urls.seen'):
        self.file = None
        self.fingerprints = set()        
        self.logdupes = True
        self.debug = debug
        
        #dirname = os.path.dirname(file_seen)
        #if not os.path.exists(dirname):            
        #    os.mkdir(dirname)
            
        self.file = open(file_seen, 'a+')
        self.fingerprints.update(x.rstrip() for x in self.file)
        
    @classmethod
    def from_settings(cls, settings):
        debug = settings.getbool('DUPEFILTER_DEBUG')
        file_seen = 'urls.seen'
        return cls(job_dir(settings), debug, file_seen)

    def request_seen(self, request):
        fp = request.url
        if fp in self.fingerprints:
            return True
        self.fingerprints.add(fp)
        if not "follow" in request.meta:
            if self.file:
                self.file.write(fp + os.linesep)
