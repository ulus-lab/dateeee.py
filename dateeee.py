from datetime import datetime as dt

print(dt.now())

while True :
    print(dt.now().strftime('%H:%M:%S'))

    choice = input('нажмите х чтобы обновить время, или Y, чтобы выйти:')

    if choice.upper() == 'Y':
        break

