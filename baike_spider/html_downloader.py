# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 22:18:58 2018
@author: zxr323
"""
from urllib import request as urllib2


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()