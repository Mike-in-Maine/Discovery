from bs4 import BeautifulSoup as bs


content =  bs.get('https://www.bookfinder.com/search/?keywords=1452562865&currency=USD&destination=us&mode=basic&classic=off&ps=tp&lang=en&st=sh&ac=qr&submit=')

print(content)

