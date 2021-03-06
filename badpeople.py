bad_buyers = [
    'jp.podly@gmail.com',
    'rosanamiranda@usp.br',
    'notspicedham@yahoo.com',
    'bethnpatterson@gmail.com',
    'jeracafite@gmail.com',
    'alhpreston@gmail.com',
    'info@books.lk',
    'irvscr@comcast.net',
    'id2359@yahoo.com',
    'abebooks.black@ergoder.com',
    'ABE.Buy.Alpha@ergoder.com',
    'ferpat135@aol.com',
    'skeptic2@hotmail.com',
    'onemore.book1@btinternet.com',
    'novaraen@gmail.com',
    'geremiaalto93@gmail.com',
    'yfhua@ntu.edu.tw',
    'ulrichweinfurtner@gmx.de',
    'lut.sommerijns@skynet.be'
    '' #NOT BLACKLISTED for testing only.
]

bad_countries = [
    'India',
    'Russia',
    'Pakistan',
    'Afghanistan',
    'Nigeria'
]

bad_sellers = [
    'Ergodebooks',
    'ErgodeBooks',
    'Ergode',
    'Book_Outpost',
    'worldofbooksinc',
    'Bonita',
    'Books Mela',
    'ral',
    'bookfairexpress',
    'SecondSale',
    'second.sale',
    'Second.Sale',
    'Cosmic Karma',
    'Imagine -This- Music',
    'belles-books',
    'COOLCAT 11',
    'booksalexpress',
    '* Ultimate Treasures *',
    'swati21'
]

bad_titles = [
    'Trilogy',
    'TRILOGY',
    'boxed',
    'Boxed',
    'Boxset',
    'boxset',
    'volume set',
    'spiralbound',
    'spiral bound',
    'spiral-bound',
    'set',
    'Set',
    'SET',
    'Volume',
    'Bible',
    'KJV',
    'NIV',
    'VOLUME',
    'Volumes',
    'VOLUMES',
    'Books 1-7', #or any other number Regex
    'Connect Access Card',
    'Printed Access Card',
    'Digital Card',
    'Digital Cards',
    'Digital code'
    'Access Card',
    'Access Key',
    'CD',
    'CD-ROM',
    'CD ROM',
    'DVD',
    'DVD-ROM',
    'DVD ROM',
    'Card set',
    'Cards',
    'transexual',
    'racism',
    'racist',
    'black lives matter',
    'negro',
    'bundle',
    'book bundle',
    'femminism',
    'feminism',
    'femminist',
    'feminist',
    'gay',
    'lesbian',
    'homosexuality',
    'lesbians',
    'Large Print',
    'Signature',
    'Signed',
    'signed',
    'kit',
    'Encyclopedia',
    'Teacher',
    'teacher\'s',
    'vText',
    'WebSAM Code',
    'Drag Queens',
    'drag queen',
    'dragqueen',
    'dragqueens',
    'STUDENT EDITION',
    'student edition',
    'TEACHER EDITION',
    'teacher edition',
    'Teacher\'s edition',
    'Student\'s Edition'
]

bad_publishers = [
    'Brilliance Audio',
    'Blackstone Publishing',
    'Simon & Schuster Audio',
    'Neal A. Maxwell Institute for Religious Scholarship'
]

bad_isbns = [
    9781571882592,
    1571882596
]

states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}
print(states["TX"])