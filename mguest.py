import bs4 as bs                        # pip install BeautifulSoup4
import urllib.request
import subprocess
from datetime import datetime

sauce = urllib.request.urlopen('http://wireless.mot.com/guest/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')                                  # Create object that is HTML of the web page

text_table = soup.find("table", class_="PageSubHeaderiMOTO")            # Find first table with class PageSubHeaderiMOTO (NOT LIST)
table_rows = text_table.find_all("tr")                                  # Find all Table Rows in the table. (LIST)

item_list = []
for tr in table_rows:                   # For each item in table_rows list
    td =  tr.find_all('td')             # Table Data is: find all items with tag td (table data) (LIST)
    for i in td:                        # For each item in td list...
        item_list.append(i.text)        # append text (no html tags) to item_list

dates = str(item_list[-4]).split()      # dates (LIST)
new_pass = item_list[-1]                # The password is the last item from the item_list
date_til = datetime.strptime("{} {} {}".format(dates[-3], dates[-2], dates[-1]), '%d %b %Y')    # Re-Format date to standard (instead 10 Feb 2018)

if date_til < datetime.now():   # Compare dates to determine if it's after date_til.
    print('Wi-Fi Password has changed to: {}. Reconnecting...'.format(new_pass))
    subprocess.call(['nmcli', 'device', 'wifi', 'connect', 'M-Guest', 'password', new_pass]) # subprocess.call() - each arg is a list item
    # print(new_pass)
else:
    print('Old password is still valid')

# print(date_til)
# print(datetime.now())
print('')
print(46 * '-')
print('|' + str(item_list[-6]).center(25) + '|' + str(item_list[-5]).center(18) + '|')
print(46 * '-')
print('|' + str(item_list[-4]).center(25) + '|' + str(item_list[-3]).center(18) + '|')
print(46 * '-')
print('|' + str(item_list[-2]).center(25) + '|' + str(new_pass).center(18) + '|')
print(46 * '-')
