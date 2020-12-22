class html_tag: #defining html tag
    def __init__(self, content, name):
        self.content = content
        self.name = name
    def __call__(self, content, name):
        content

doctype = html_tag([],'!DOCTYPE html')  #listing tags used
html = html_tag([],'html')
head = html_tag([],'head')
title = html_tag([],'title')
body = html_tag([],'body')
h1 = html_tag([],'h1')
p = html_tag([],'p')

class html_page:
    def __init__(self, content):
        self.content = content
    def generate(self, path):
        print(self.content)
        page_file = open(path,'w')
        page_list = self.content
    #    if self.content[0] == doctype([], '!DOCTYPE html'):
    #        page_file.write('<' + doctype.name + '>')
    #        page_list = self.content.remove(0)
    #    else:
    #        page_file.write('<' + doctype.name + '>')
    #        page_list = self.content
        for i0 in range(len(page_list)):
            if type(page_list[i0]) == html_tag:
                page_file.write('<' + page_list[i0].name + '>')
                for i1 in range(len(page_list[i0].content)):
                    if type(page_list[i0].content[i1]) == html_tag:
                        page_file.write('<' + page_list[i0].content[i1].name + '>')
                        for i2 in range(len(page_list[i0].content[i1].content)):
                            if type(page_list[i0].content[i1].content[i2]) == html_tag:
                                page_file.write('<' + page_list[i0].content[i1].content[i2].name + '>')
                                page_file.write(page_list[i0].content[i1].content[i2].content[0])
                                page_file.write('</' + page_list[i0].content[i1].content[i2].name + '>')
                            else:
                                page_file.write(page_list[i0].content[i1].content[i2])
                            page_file.write('</' + page_list[i0].content[i1].name + '>')
                    else:
                        page_file.write(page_list[i0].content[i1])
                    page_file.write('</' + page_list[i0].name + '>')
            else:
                page_file.write(page_list[i0])
        page_file.close()

testpage = html_page
testpage.content = [doctype([],'!DOCTYPE html'),html([head([title(['you'],'title')],'head'),body([h1(['love'],'h1'),p(['i'],'p')],'body')],'html')]
print(testpage.content)
testpage.generate(testpage,'file.html')