# pollyanna
import random
from collections import defaultdict
import smtplib  
from datetime import datetime

emails = {
    'Sean': 'Sob0037@gmail.com',
    'Kelly Smith': 'Sob0037@gmail.com',
    'Mark': 'mfmathews@comcast.net',
    'Kelly Mathews': 'kellylaurenob@gmail.com',
    'Kevin': 'theobes1@gmail.com',
    'Dottie': 'theobes1@gmail.com',
    'Michele': 'micheleobrien76@gmail.com',
    'Paul': 'pbash16@gmail.com',
}
couples = {
    1 :[
        'Sean',
        'Kelly Smith',
    ],
    2: [
        'Mark',
        'Kelly Mathews',
    ],
    3: [
        'Kevin',
        'Dottie',
    ],
    4: ['Michele'],
    5: ['Paul'],
}

wishlists = {
    'Dottie' : {
        'gifts':
            [
                'Women\'s UA coffee run beanie hat (black)',
                'Reebok knee high fashion socks',
                'Under Armour warm knee socks for snowboarding',
            ],
        'giftcards':
            ['Dunkin Donuts', 'Victoria Secret', 'Dick\'s'],
    },
    'Kevin' : {
        'gifts':
            [
                'Under Armour mesh shorts (L)',
                'Under Armour cold gear mock neck- black (XL)',
                'Nice t-shirts to wear out (L)',
            ],
        'giftcards':
            ['Craft Beer Store', 'Golf Store', 'Dick\'s'],
    },
    'Kelly Mathews' : {
        'gifts':
            [
                'Yoga mat bag',
                'Tea kettle',
                'Fingerless gloves & infinty scarf (black or dark green)',
                'Moccasin Slippers (9)',
            ],
        'giftcards':
            ['Home Depot', 'Lowes', 'K&C Nails (Maple Ave/next to CVS)'],
    },
    'Mark' : {
        'gifts':
            [
                'Flyers baseball hat (7)',
                'The Warren Buffet Way (book)',
                'Flyers T-Shirt (XL)',
            ],
        'giftcards':
            ['Home Depot', 'Lowes'],
    },
    'Sean' : {
        'gifts':
            ['Gift cards only, please!'],
        'giftcards':
            ['Home Depot', 'Lowes', 'Bed, Bath & Beyond'],
    },
    'Kelly Smith' : {
        'gifts':
            [
                'Scarf',
                'iPhone 5 charger',
                'Kenneth Cole Black (perfume)',
            ],
        'giftcards':
            ['Ikea', 'Visa'],
    },
    'Michele' : {
        'gifts':
            [
                'Bathrobe (M)',
                'Pocketbook',
                'PJs (M)',
                'Black flat high boots (7.5)',
            ],
        'giftcards':
            ['Best Buy', 'Dunkin Donuts', 'Amazon'],
    },
    'Paul' : {
        'gifts':
            [
                'Cologne',
                'Good Earbuds',
                'Dress shirts',
                'Native by one Republic (CD)',
            ],
        'giftcards':
            ['Chipotle', 'Starbucks', 'American Eagle'],
    },
}

def select_pollyannas():
    names = []
    choices = []
    for couple, _dict in couples.iteritems():
        for name in _dict:
            names.append((name, couple))
            choices.append((name, couple))
    random.shuffle(choices)
    pollys = defaultdict()
    for name in names:
        print 'selecting for: ', name[0], name[1]
        assigned = assign_polly(choices, name[1])
        if assigned:
            pollys[name[0]] = assigned[0]
            print "Assigned:", assigned[0]
        else:
            break
    return pollys

def assign_polly(choices, couple):
    rejects = []
    try:
        p = choices.pop(0)
    except (IndexError):
        return None
    if p[0] in couples[couple]:
        print "NOPE: ", p[0]
        rejects.append(p)
        p = assign_polly(choices, couple)
    choices.extend(rejects)
    return p

def send_emails(to, polly):
    fromaddr = 'Santa Claus'
    # toaddrs  =  'kellylaurenob@gmail.com'
    toaddrs  =  emails[to]
    wishlist = wishlists[polly]
    gifts = '\nGifts: \n'
    for i in range(len(wishlist['gifts'])):
        gifts = gifts + '{0}. {1}\n'.format(i+1, wishlist['gifts'][i])

    certificates = 'Certificates: \n'
    for i in range(len(wishlist['giftcards'])):
        certificates = certificates + '{0}. {1}\n'.format(i+1, wishlist['giftcards'][i])

    wishes = '\n{0}\'s wishlist is: \n{1} \n{2}'.format(polly, gifts, certificates)

    instructions = (
        'The gift limit is $50, so you don\'t have to buy everything on the '
        'wishlist :) The date and time of our pollyanna party is still TBD, so '
        'please send me some dates that work for you!'
    )

    msg = (
        'Hey {0}, it\'s Christmas Pollyanna Time! :)\nThis year your pollyanna '
        'is: {1}! \n{2} \n{3}\n \nHappy Shopping!'
    ).format(to, polly, wishes, instructions)

    username = 'kellylaurenob@gmail.com'
    password = password

    print "sending mail to: ", toaddrs
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)

    senddate=datetime.strftime(datetime.now(), '%Y-%m-%d')
    subject="Your pollyanna has arrived!"

    print msg
    m="Date: %s\r\nFrom: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (senddate, fromaddr, toaddrs, subject)

    server.sendmail(fromaddr, toaddrs, m+msg)
    server.quit()
    print "sent"


pollys = select_pollyannas()
for to, polly in pollys.iteritems():
    send_emails(to, polly)
