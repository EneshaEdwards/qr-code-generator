#import qrcode
#qr = qrcode.make("https://eneshaedwards.com")
#qr.save("/Users/eneshae/Desktop/my_qr_code.png")

import qrcode

# url = input("Enter the URL to turn into a QR code: ")
# qr = qrcode.make(url)
# qr.save("/Users/eneshae/Desktop/my_qr_code.png")
# print(f"QR code saved for {url}")

import qrcode

links = {
    "website": "https://eneshadedwards.com",
    "linkedin": "https://linkedin.com/eneshaedwards",
    "github": "https://github.com/eneshaedwards"
    
}

for name, url in links.items():
    qr = qrcode.make(url)
    qr.save(f"/Users/eneshae/Desktop/{name}_qr.png")
    print(f"QR code saved for {name}: {url}")