import requests, time, gzip, json

upload_endpoint = "http://127.0.0.1:5000/image"
shift_endpoint = "http://127.0.0.1:5000/viewport"
side_endpoint = "http://127.0.0.1:5000/side"
file_location = "/home/log2/Downloads/test_image_1600x960.png"

data = b''
with open(file_location, "rb") as f:
    data = gzip.compress(f.read())
requests.post(url=upload_endpoint,data=data)

LEFT_VIEWPORT = '{"x": 800, "y": 0, "w": 800, "h": 480}'
RIGHT_VIEWPORT = '{"x": 0, "y": 0, "w": 800, "h": 480}'
ABOVE_VIEWPORT = '{"x": 0, "y": 480, "w": 800, "h": 480}'
BELOW_VIEWPORT = '{"x": 0, "y": 0, "w": 800, "h": 480}'

while True:
    time.sleep(1)
    response = requests.get(side_endpoint)
    j = response.json()
    print(type(j), j)
    if j == "above":
        requests.post(url=shift_endpoint,data=ABOVE_VIEWPORT)
    elif j == "below":
        requests.post(url=shift_endpoint,data=BELOW_VIEWPORT)
    elif j == "left":
        requests.post(url=shift_endpoint,data=LEFT_VIEWPORT)
    elif j == "right":
        requests.post(url=shift_endpoint,data=RIGHT_VIEWPORT)
