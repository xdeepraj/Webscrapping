from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


def main(request):
  return render(request, "main.html")

def showUrl(request):
  if request.method.lower() == 'post':
    URL = request.POST['site_url']
    source = requests.get(URL)
    soup = BeautifulSoup(source.text, 'lxml')
    
  
    images = soup.find_all('img')
    # find image urls & texts from webpage & store them in data_url dictionary
    img_url = []
    text_list = []
    data_url ={}

    #for image_urls
    for image in images:
      temp = (image['src'])
      if temp.startswith('https'):
        img_url.append(temp)
  
    #for texts
    for tag in soup.select('span'):
      text_list.append(tag.next)

    data_url['first'] = img_url  
    data_url['second'] = text_list

    # print(data_url)
    return render(request, "result.html", data_url)

  