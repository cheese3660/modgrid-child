import requests, time, gzip, json

upload_endpoint = "http://127.0.0.1:5000/image"
shift_endpoint = "http://127.0.0.1:5000/viewport"
file_location = "/home/log2/Downloads/test_image_1600x960.png"

print("Sending request in 5 seconds")
data = b''
with open(file_location, "rb") as f:
    data = gzip.compress(f.read())
time.sleep(5)
requests.post(url=upload_endpoint,data=data)


while True:
    print("Changing viewport in 5 seconds")
    new_viewport = '{"x": 800, "y": 0, "w": 800, "h": 480}'
    time.sleep(5)
    requests.post(url=shift_endpoint,data=new_viewport)

    print("Changing viewport in 5 seconds")
    new_viewport = b'{"x": 0, "y": 480, "w": 800, "h": 480}'
    time.sleep(5)
    requests.post(url=shift_endpoint,data=new_viewport)

    print("Changing viewport in 5 seconds")
    new_viewport = b'{"x": 800, "y": 480, "w": 800, "h": 480}'
    time.sleep(5)
    requests.post(url=shift_endpoint,data=new_viewport)

    print("Changing viewport in 5 seconds")
    new_viewport = b'{"x": 0, "y": 0, "w": 800, "h": 480}'
    time.sleep(5)
    requests.post(url=shift_endpoint,data=new_viewport)
