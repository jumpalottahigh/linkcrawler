import urllib.request
from bs4 import BeautifulSoup

'''
This function takes in an URL and follows it and checks the return status code
'''
def followLink(link):
    req = urllib.request.urlopen(link)
    if req.getcode() == 200:
        print("200 OK!")
    elif req.getcode() == 404:
        print("404! Broken link is:", link)
    else:
        print("Link is throwing:", link, req.getcode())



'''
Main
'''
url = input('Enter URL: ')
print("Url to fetch links from:", url)
req = urllib.request.urlopen(url)
print (req.getcode(), "Success! Grabbing links!")
html = req.read()
soup = BeautifulSoup(html, "html.parser")
linksText = soup('a')
allImages = soup('img')

count = 0
print("Found",len(allImages), "images.")
for img in allImages:
    print (img.get('alt'))
    if img.get('alt') != '':
        print(img.get('alt'))
        count = count + 1
print("Images that have an alt attribute:", count)

# for l in linksText:
#     print (l.get('href'))
#     if l.get('href').startswith("#"):
#         print("Anchor tag found:", l.get('href'), ". Skipping link follow.")
#     elif l.get('href').startswith("http://"):
#         print("Unsecure link found. Might want to update that:", l.get('href'))
#         followLink(l.get('href'))
#     else:
#         followLink(l.get('href'))
