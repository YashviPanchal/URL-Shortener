import pyshorteners as shr
shortener = shr.Shortener()
URL = input("Enter the URL: ")
shortURL = shortener.tinyurl.short(URL)
print(f"Short URL is: {shortURL}")