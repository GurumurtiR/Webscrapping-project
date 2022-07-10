import requests
from bs4 import BeautifulSoup

products_to_track = [

    {
        "product_url": "https://www.amazon.in/Samsung-Mystique-Storage-Purchased-Separately/dp/B09TWGDY4W/ref=sr_1_2_sspa?crid=G7ASYVSI530E&keywords=m31+samsung&qid=1655291210&sprefix=m31%2Caps%2C310&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMkM1Rk1JS0I3UlRBJmVuY3J5cHRlZElkPUEwMDM0NTM5MUdYNlQyMEM5STgzUCZlbmNyeXB0ZWRBZElkPUEwNzc0ODU0MlBRRVRCSzREVDJIQiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        "name": "Samsung Galaxy M33 5G",
        "target_price": 17000
    },

    {
        "product_url": "https://www.amazon.in/dp/B084456PC2/ref=sspa_dk_detail_5?psc=1&pd_rd_i=B084456PC2&pd_rd_w=oG5C8&content-id=amzn1.sym.5210e5d3-37e0-44be-93e0-eb50dad0d2ca&pf_rd_p=5210e5d3-37e0-44be-93e0-eb50dad0d2ca&pf_rd_r=8GKZEF72XWNGHQP4CMXP&pd_rd_wg=10LVm&pd_rd_r=79951dc0-8ff3-4c25-8450-69b556eddd66&s=electronics&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNzhVWUdJTzBHMENGJmVuY3J5cHRlZElkPUEwNTc1NTY3MTZMVzNTTlFUV0NDNiZlbmNyeXB0ZWRBZElkPUEwNjg3MjE2MTg4MUlBSVg0N0lMUCZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        "name": "OPPO A15s(Dynamic black 4GB RAM 64GB storage)",
        "target_price": 9500
    },

    {
        "product_url": "https://www.amazon.in/Apple-iPhone-SE-128-Generation/dp/B09V469LJN/ref=bmx_dp_ejj8ph1n_sccl_3_2/257-2090934-1764528?pd_rd_w=yFZF0&content-id=amzn1.sym.8a9ae28a-50bb-47e1-bee2-6d46170b1ac6&pf_rd_p=8a9ae28a-50bb-47e1-bee2-6d46170b1ac6&pf_rd_r=GX4XKDCBJ2FXRKYWK7WB&pd_rd_wg=YIBcI&pd_rd_r=7f0aaf85-a413-411d-822a-59e40f9f6f95&pd_rd_i=B09V469LJN&psc=1",
        "name": "Apple iphone SE(128gb)-midnight",
        "target_price": 50000
    },

    {
        "product_url": "https://www.amazon.in/Redmi-Note-11T-5G-Dimensity/dp/B09LHZSMRR/ref=sr_1_22_sspa?crid=3C65DV03AL2S2&keywords=m31+samsung&qid=1655303293&sprefix=%2Caps%2C305&sr=8-22-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWVFTWk4xVFBRMDJFJmVuY3J5cHRlZElkPUEwMzQ1NDk5MUpMREwxNFg2RlRWRCZlbmNyeXB0ZWRBZElkPUEwOTA4NDY0OUdUV0gxV0k3Vkc4JndpZGdldE5hbWU9c3BfYnRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
        "name": "Redme Note 11T 5G",
        "target_price": 17000
    },

    {
        "product_url": "https://www.amazon.in/dp/B0B2PKBBQX/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B0B2PKBBQX&pd_rd_w=Qh0gV&content-id=amzn1.sym.5210e5d3-37e0-44be-93e0-eb50dad0d2ca&pf_rd_p=5210e5d3-37e0-44be-93e0-eb50dad0d2ca&pf_rd_r=51CYMP8EVRR1C27FNDNF&pd_rd_wg=ltepj&pd_rd_r=d0839dd9-ba84-45bc-8912-9f60f198fbb1&s=electronics&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQzRWNjVPRk5RWUNWJmVuY3J5cHRlZElkPUExMDIyMDk5M0xWUUxPNkVKWlBaWSZlbmNyeXB0ZWRBZElkPUEwMTI3MTMyMVJKMEhHUFk1SU1MMiZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        "name": "I KALL K570 smartphone",
        "target_price": 8000
    },

]


def give_product_price(URL):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    product_price = soup.find("span", {"class": "a-offscreen"})

    if product_price == None:
        product_price = soup.find("span", {"class": "a-offscreen"})
    return product_price.getText()


result_file = open('my_result_file.text', 'w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + "--" + every_product.get("name"))

        my_product_price = product_price_returned[1:]

        my_product_price = my_product_price.replace(',', '')

        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("available at your required price")
            result_file.write(every_product.get(
                "name") + '- \t' + 'available at target price' + '- \t' 'current price-' + str(my_product_price) + '\n')

        else:
            print("still at current price")


finally:

    result_file.close()
