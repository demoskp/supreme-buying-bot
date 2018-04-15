from splinter import Browser
browser = Browser()
# browser.visit('http://www.supremenewyork.com/shop/all/sweatshirts')
browser.visit('http://www.supremenewyork.com/shop/all/jackets')
'''
try:
    clothing_link_pale_lime = browser.find_link_by_text('Pale Lime')
except FileNotFoundError as err:
    print(err)
try:
    clothing_link_rust = browser.find_link_by_text('Rust')
except FileNotFoundError as err:
    print(err)
try:
    clothing_link_heather_grey = browser.find_link_by_text('Heather Grey')
except FileNotFoundError as err:
    print(err)
try:
    clothing_link_ice_blue = browser.find_link_by_text('Ice Blue')
except FileNotFoundError as err:
    print(err)
try:
    clothing_link_black = browser.find_link_by_text('Black')
except FileNotFoundError as err:
    print(err)
    clothing_link_magenta = browser.find_link_by_text('Magenta')
except FileNotFoundError as err:
    print(err)
'''
try:
    clothing_link_red = browser.find_link_by_text('Red')
except FileNotFoundError as err:
    print(err)




clothing_link_red[0].click()


browser.select('size','41999')

addtocart = browser.find_by_name('commit')
addtocart.click()

checkout = browser.find_link_by_href('https://www.supremenewyork.com/checkout')
checkout.click()


def buying():
    browser.fill('order[billing_name]' , 'name surname')
    browser.fill('order[email]' , 'test@hotmail.com')
    browser.fill('order[tel]' , '07xxxxxxxxx')
    browser.fill('order[billing_address]' , 'my address')
    browser.fill('order[billing_city]' , 'City')
    browser.fill('order[billing_zip]' , 'ln355td')
    browser.fill('credit_card[cnb]' , '1234567891234567')
    browser.select('credit_card[month]' , '04')
    browser.select('credit_card[year]' , '2020')
    browser.fill('credit_card[vval]','768')
    browser.find_by_id('order_terms').click()
    browser.find_by_name('commit').click()

buying()
