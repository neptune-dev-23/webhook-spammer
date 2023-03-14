# Created by: Cringeworthy#1572
# On Telegram: @cringeworthy23
import requests, json
webhooks = open("webhooks.txt", "r").read().splitlines()
message = open("message.txt", "r").read()
config = json.loads(open("data.json", "r").read())
def log(message):
    requests.post(logging_webhook, json={"content": message})
    print(message)
    
message_count = config["message_count"]
total_spammed = config["spammed_count"]
logging_webhook = config["logging_webhook"]

log("Starting the spam...")
def spam():
    global total_spammed
    for x in range(message_count):
        if len(webhooks) == 0:
            break
        log(f"Loop {x + 1} of {message_count}...")
        log(f"Spamming on {len(webhooks)} webhooks...")
        for webhook in webhooks:
            re = requests.post(webhook, json={"content": message})
            total_spammed += 1
            if str(re.status_code) != "204":
                log(f"!!! Error {re.status_code} posting on webhook {webhook}")
                webhooks.remove(webhook)
                log(f"Removed webhook {webhook}")   
                log(f"Webhooks remaining: {len(webhooks)}")
                total_spammed -= 1
        log(f"Total spammed: {total_spammed}")
    log("Done")

def end():
    e = open("webhooks.txt", "w")
    e.write(str("\n".join(webhooks)))
    f = open("total_spammed.txt", "w")
    f.write(str(total_spammed))
try:
    spam()
    end()
except KeyboardInterrupt:
    end()