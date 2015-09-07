__author__ = 'Vivek Gour'
__copyright__ = 'Copyright 2013, Searce'
__version__ = '1.0.0'
__maintainer__ = 'Vivek Gour'
__email__ = 'Vivek.Gour@searce.com'
__status__ = 'Development'


import os
import imp
import pysftp
import ghostscript


conf = imp.load_source('*', '/../../config.py')
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
(MONGO_HOST, MONGO_DB, BASE_DOMAIN, SESSION_COOKIE_DOMAIN,
 MONGO_PORT, MONGO_UNAME, MONGO_PASSWD, USER_DB) = conf.getDetails(PROJECT_DIR)


with pysftp.Connection('104.197.79.5', username='noramdocs', password='rrJ%o$59&UlI') as sftp:
    sftp.get_d('docs', "D:\InvoizeSuite\pdf")
    list = sftp.listdir('/docs')
    for doc in list:
        print doc
        sftp.remove('docs/'+doc)


# def tiff2pdf(width, length, files):
#     print files, "files"
#     path, filename = os.path.split(files)
#     print path, filename, "path, filename"
#     name, ext = os.path.splitext(filename)
#     print name, ext, "name, ext"
#     path = path+'/'
#     output = os.path.join(path, name + ".pdf")
#     command = 'tiff2ps -a2 -w%s -h%s "%s" | ps2pdf - "%s"' % (width, length, files, output)
#     print command
#     os.popen(command)
#
# if __name__ == '__main__':
#     newpth = 'D:/InvoizeSuite/docs/'
#     for laneFile in os.listdir(newpth):
#         tiff2pdf(8.5, 11, newpth+laneFile)
