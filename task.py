from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq

# We can use Selenium to automatically click on the translate button
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# browser=webdriver.Chrome("F:/Tools/chromedriver_win32/chromedriver.exe")#pah for selenium web driver
# browser.get('https://prefeitura.pbh.gov.br/saude/licitacao/pregao-eletronico-151-2020')#url
# login_ele=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[1]/button')
# login_ele.click()

myurl="https://prefeitura.pbh.gov.br/saude/licitacao/pregao-eletronico-151-2020"

uclient = ureq(myurl) #opens the connection
req=uclient.read()  #read the complete html page and save in variable
uclient.close()       #close the connection
 
req=soup(req,'html.parser')
containers= req.findAll('div',{'class':'container'})
#print (len(containers))

#print (soup.prettify(containers[0]))
container=containers[0]

publicationDate=container.findAll('div',{'span':'col-sm-6 lbl-licitacao'})
print (publicationDate[0].text)

biddingDate=container.findAll('div',{'span':'col-sm-6 lbl-licitacao'})
#print (price[0].text)

obj=container.findAll('div',{'span':'col-sm-6 lbl-licitacao'})
#print (rating[0].text)

print(publicationDate)
print(biddingDate)
print(obj)