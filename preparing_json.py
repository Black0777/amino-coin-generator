from json import dump
from contextlib import suppress
import os
try: os.system("pip install --upgrade amino.fix")
finally: import aminofix


################
savePath = "accounts.json"
#############


clear = lambda: os.system('cls' if os.name=='nt' else 'clear')


info = (
    "~ e: Exit\n"
    "~ Press Enter to continue\n"
)


infoError =(
    "~ Invalid account, do you want to save it? [Y/N]: "
)


clear()


print(
    "save accounts in {}\n".upper().format(repr(savePath)) +
    "necessary data:".capitalize(),
    "email,".capitalize(), "password".capitalize()
)


Format = {
    "email": None,
    "password": None,
    "deviceId": None,
    "uid": None,
    "sid": None
}


def show_accounts():
    print("\n~ Accounts: %d" % len(accounts))


def get_data(
    email: str=None,
    password=None,
    deviceId: str=None,
    uid: str=None,
    sid: str=None
) -> dict:
    return dict(zip(
        ("email", "password", "device", "uid", "sid"),
        (email, password, device, uid, sid)
    ))


accounts = []
while True:
    email, password = None, None
    deviceId, sid, uid = None, None, None
    show_accounts()
    email = input("~ Email: ")
    password = input("~ Password: ")
    with suppress(Exception):
        amino = aminofix.Client()
        deviceId = amino.device_id
        amino.login(email, password)
        sid = amino.sid
        uid = amino.userId
    
    data = get_data(
        email=email,
        password=password,
        deviceId=deviceId,
        sid=sid,
        uid=uid
    )
    
    if not sid and input(infoError).lower().strip() == "n":pass
    else:
        accounts.append(data)
        with open(savePath, "w") as file:
            dump(accounts, file, indent=4)
            print("~ %r saved!" % email)
            os.remove("device.json")
