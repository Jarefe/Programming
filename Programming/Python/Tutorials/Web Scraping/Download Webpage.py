import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

if res.status_code == requests.codes.ok:
    len(res.text)
    print(res.text[:250])


# saving downloaded files to drive
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)
playFile.close()

# checking for errors
print("Finding webpage that does not exist and handling error")
error_request = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    error_request.raise_for_status()
except Exception as exc:
    print('There was a problem:\n %s' % exc)

