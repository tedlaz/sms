# -*- coding: utf-8 -*-
import argparse
import mechanicalsoup
# from getpass import getpass


# if args.password:
#     password = getpass()
oteurl = "https://tools.otenet.gr/index.php"
smsurl = "https://tools.otenet.gr/?_task=websms&_action=plugin.websms_compose&_framed=1"


def send_sms(email, password, mobile, message):
    '''
    connect to otenet and sent web sms (5 per day, 100 per month)
    '''
    browser = mechanicalsoup.StatefulBrowser()
    browser.set_verbose(2)
    browser.open(oteurl)
    browser.select_form('form')
    browser['_user'] = email
    browser['_pass'] = password
    resp = browser.submit_selected()
    smspage = browser.get(smsurl)
    websmsform = smspage.soup.select("#sms-compose-area")[0].select("form")[0]
    websmsform.select("#_to")[0].string = mobile
    websmsform.select("#_message")[0].string = message
    browser.submit(websmsform, smspage.url)


if __name__ == '__main__':
    desc = 'Send sms from your ΟΤΕ account'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("email", help='otenet email')
    parser.add_argument("password", help='otenet password')
    parser.add_argument("mobile", help='mobile phone number')
    parser.add_argument("message", help='message')
    args = parser.parse_args()
    send_sms(args.email, args.password, args.mobile, args.message)
