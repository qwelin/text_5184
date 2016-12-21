
import pytesseract #识别认证码模块
from PIL import Image #识别验证码模块
import requests
from bs4 import BeautifulSoup
import re



headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'}
year = ['201301','201304','201307','201310','201401','201404','201407','201410','201501','201504','201507','201510','201601','201604','201607','201610',]
#year = ['201301','201606']


def yanzhengma():
    get = requests.get('http://query.5184.com/query/image.jsp')
    cookies_jse = get.cookies.get('JSESSIONID')
    yanzhengma = get.content
    save = open('/Users/Macx/Documents/自考/text8/1.png', 'wb')
    save.write(yanzhengma)
    save.close()
    a = Image.open('/Users/Macx/Documents/自考/text8/1.png')
    vcode = pytesseract.image_to_string(a)
    #print(vcode)
    return {'cookies_jse':cookies_jse,'vcode':vcode}


def search (name = '040214407796'):
    people = []
    cookies_vcode = yanzhengma()
    cookies_jse = cookies_vcode['cookies_jse']
    vcode = cookies_vcode['vcode']
    cookies = {'JSESSIONID': cookies_jse}
    for x in year:
        #print(x+'的成绩')
        url ='http://query.5184.com/query/zk/zk_score_'+x+'.jsp?name0='+str(name)+'&rand='+str(vcode)+'&serChecked=on'
        #print(url)
        html = requests.get(url,headers = headers,cookies = cookies)
        soup =BeautifulSoup(html.text,'lxml')
        #print(soup)
        All_data = soup.select('.query_check_box table')
        #print(len(All_data))
        if len(All_data) == 0:
            pass
        else:
            All_data = All_data[0]
            score = re.findall(r'<tr><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>',str(All_data))
            for i in score:
                if i[4] == '-- ':
                    a = '报名未参加考试'
                elif int(i [4]) < 60:
                    a = '参加考试未能及格'
                else:
                    a = '通过考试'
                data_1 = {
                    '考试时间':x,
                    '准考证号':i[0],
                    '姓名':i[1],
                    '科目代码':i[2],
                    '科目名称':i[3],
                    '考试成绩':i[4],
                    '考试状态':a
                }
                people.append(data_1)
    #            print (people)

    return (people)

'''
cookies_vcode = yanzhengma()
cookies_jse = cookies_vcode['cookies_jse']
vcode = cookies_vcode['vcode']
#print(cookies_vcode,cookies_jse,vcode)
cookies = {'JSESSIONID': cookies_jse}
#print(vcode.isdigit())


if vcode.isdigit() :
	people_search_id = input('自考准考证号（12位）：' )
	if people_search_id.isdigit and len(people_search_id) == 12 :
		people_search_name = input('考生姓名： ')
		search(str(people_search_id))
		if people[0]['姓名'] == people_search_name :
			print (people)
		else:
			print ('你输入的准考证号码与姓名不对应，请从新输入')
	else:
		print('你输的准考证号码有误')
else:
    print('识别验证码错误')
'''


