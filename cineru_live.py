import requests
import json
import time
#------------------------------------------------
def slicetext(text, start, end):
    try:
        return text.split(start)[1].split(end)[0]
    except:
        return ""
#------------------------------------------------
bot_token = '2011182942:AAF0IqAiI9aH6gdSfDLduXvIbA90u3Kf_8M'
chat_id = '-1001633326523'

headers = {
    'authority': 'www.cineru.lk','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','sec-gpc': '1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}

#-----------------------------------------------

while True:

#-----------------------------------------------

    response = requests.get('https://cineru.lk/', headers=headers, verify=False)
    html = response.text

    html = slicetext(f"{html}", "ඔක්කොම එකට</a></h2>", " rel=\"bookmark")
    l_link = slicetext(f"{html}", "a href=\"", "\"")
    #l_link = "https://www.cineru.lk/%e0%b7%84%e0%b6%ba%e0%b7%92%e0%b6%9a%e0%b7%92%e0%b6%ba%e0%b7%94-s01-e16-sinhala-subtitles/"
    print(l_link)

#-------------------------------------------------------

    with open('cineru.txt') as f:
        contents = f.read()

#-------------------------------------------------------

    if contents==l_link:
        print(None)

    else:
#-------------------------------------------------------

        with open('cineru.txt', 'w') as f:
            f.write(l_link)

#------------------------------------------------------

        sub_link = requests.get(l_link, headers=headers)
        sub_link = sub_link.text

        zip_link = slicetext(f"{sub_link}", "download\" href=\"javascript:;\" data-link=\"", "\"")
        print(zip_link)

#----------------------------------------------

        sub_send = requests.get(f'https://api.telegram.org/bot{bot_token}/sendDocument?chat_id={chat_id}&document={zip_link}')
        jsondata = json.loads(sub_send.text)
        done=jsondata['ok']
        print(f"MSG send : {done}")

#----------------------------------------------

    time.sleep(1000)