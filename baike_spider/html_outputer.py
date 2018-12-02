# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 22:18:58 2018
@author: zxr323
"""
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border='1'>")
        # python默认编码是ascii,故要转为utf-8
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'][0:51])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()