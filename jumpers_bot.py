import urllib.request
import json


with urllib.request.urlopen("https://www.jumpers-fitness.com/club-checkin-number/7/Jumpers.JumpersFitnessTld") as url:
    data = json.load(url)

    max_check_ins = data["maxCheckinsAllowed"]
    checked_in = data["countCheckedInCustomer"]
    print(max_check_ins)
    print(checked_in)
