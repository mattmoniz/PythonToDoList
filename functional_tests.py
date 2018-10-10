from selenium import webdriver
browser = webdriver.Firefox()

# Johnny starts using this brand new To-Do List App
browser.get('http://localhost:8000')

#John sees the name of the new app in the header
assert 'To-Do' in browser.title

#He types in his first to-do item name.
#He hits enter and the page updates.
#There will be another textbox to enter another item to the to-do list.
#He hits enter again and the page updates and the list shows two items.
#The site remembers his list and generates a unique URL for his list.
#He visits his URL and the to-do list is still there.

browser.quit()
