import mechanize
from urllib import urlretrieve
from lxml import etree
import os
import shutil 
import sys

def scrape(search_word):
    print("Returning images of " + search_word)
    directory = search_word
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)

    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Google Chrome')]
    url_start = "http://www.google.com/"

    br.open(url_start)
    br.follow_link(text='Images', nr=0)
    br.select_form(nr=0)
    br["q"] = search_word
    answer = br.submit()
    page_html = br.response().read()  

    tree = etree.HTML(page_html)
    images = tree.xpath('//img')
    i=0
    for image in images:
        link = image.attrib["src"]
        urlretrieve(link, search_word+"/"+search_word+str(i)+".jpg")
        i=i+1

def main():
    search_word = "cats"
    if len(sys.argv) < 2:
        print ("Cats it is.")
    else:
        search_word = str(sys.argv[1])
    scrape(search_word)

if __name__ == "__main__":
    main()




