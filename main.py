from bs4 import BeautifulSoup
import lxml
import requests
import time

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}

print("Let's find the status of your transcript document on pune university website using\nPYTHON")

with requests.session() as s :
    url = 'http://bcud.unipune.ac.in/certificate/GeneralPages/Login.aspx'
    r = s.get(url,headers=headers).text
    soup= BeautifulSoup(r,'lxml')
    viewState = soup.find('input',attrs={'name' :"__VIEWSTATE" })['value']
    EventValidation = soup.find('input', attrs={'name': '__EVENTVALIDATION'})['value']
    user_name = input('Enter your username : ')
    password = input('Enter your password : ')
    timewait = time.sleep(1)
    print("Fetching information...")
    login_data = {
        'ctl00$ContentPlaceHolder2$Login1$UserName': user_name,
        'ctl00$ContentPlaceHolder2$Login1$Password': password,
        'ctl00$ContentPlaceHolder2$Login1$LoginButton': 'Log In',
        '__VIEWSTATEGENERATOR': '0B02E4B5',
        '__PREVIOUSPAGE': 'dN2QmZ-Apklc_Zxc7T3rWG3bRpHLXjn5le1aJOGpqkciENBCwB3Fb30sFc14EW554O-PEiJ1cxIWPPx3_3xHrXeYNsid12UT6V5UBsblnnFf_lMZk9lS1vGBVkvob6nfEwCuXA2',
        '__VIEWSTATE': viewState,
        '__EVENTVALIDATION': EventValidation

    }
    req = s.post(url, data=login_data).text
    # time.sleep(2)
    soup2 = BeautifulSoup(req,'lxml')
    tables = soup2.find_all('tr', attrs={"class":"boxrows"})
    tabledata = tables[0].find_all("td")
    prn_nos = (tabledata)[0].text
    application_no = (tabledata)[1].text
    application_type = (tabledata)[2].text
    date_submitted = (tabledata)[3].text
    # status = (tabledata)[4].text
    link = "http://bcud.unipune.ac.in/certificate/Student_Default/Certificates.aspx"
    print(f'PRN NO : {prn_nos}')
    print(f'Application No : {application_no}')
    print(f'Application Type : {application_type}')
    print(f'Date Submitted : {date_submitted}')
    print(f'Status : {status}')
    print("For more info visit : "+link)





    # print(tables)
    # tabledata=[]
    # tabledata.append(tables)
    # print(tabledata)








# pip3 install -r requirements
# pip freeze > requirements.txt






















