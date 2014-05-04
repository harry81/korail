import simplejson
import sys
import getopt
from korail import Korail

def main(argv=None):
    print '0. preparation ----------'
    korail = Korail()

    user_obj = simplejson.loads((open('userinfo.json').read()))
    user_id = user_obj['id'] if user_obj.has_key('id') else raw_input("ID: ")
    password = user_obj['pw'] if user_obj.has_key('pw') else getpass()
    phone_signing = False
    try:
        rv = korail.login(user_id, password, phone_signing)
    except KorailError as e:
        self.fail(e.message.encode('utf-8'))
            
    print '1. search ----------'
    reserve_obj = simplejson.loads((open('reservetraininfo.json').read()))
    dep = reserve_obj['dep']
    arr = reserve_obj['arr']
    date = reserve_obj['date']
    time = reserve_obj['time']
    
    try:
        trains = korail.search_train(dep, arr, date, time, train='02')
    except KorailError as e:
        self.fail(e.message.encode('utf-8'))

    for train in trains:
        print train

    print '2. reserve ----------'
    try:
        korail.reserve(trains[0])
    except KorailError as e:
        self.fail(e.message.encode('utf-8'))
    print korail.tickets()
    
    print '3. end ----------'

if __name__ == "__main__":
    sys.exit(main())
