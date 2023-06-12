# Write your solution here
from datetime import datetime, timedelta


def is_it_valid(pic: str):
    if len(pic) != 11:
        return False

    try:
        dd = int(pic[0:2])
        mm = int(pic[2:4])
        yy = int(pic[4:6])
        century = 0
        if pic[6] == "+":
            century = 1800
        elif pic[6] == "-":
            century = 1900
        elif pic[6] == "A":
            century = 2000
        else:
            return False
        yy += century
        no = pic[0:6] + pic[7:10]
        control_index = int(no) % 31
        control = "0123456789ABCDEFHJKLMNPRSTUVWXY"[control_index]
        if pic[10] != control:
            return False

        datetime(yy, mm, dd)
        return True
    except:
        return False


if __name__ == "__main__":
    is_it_valid("290200-1239")
