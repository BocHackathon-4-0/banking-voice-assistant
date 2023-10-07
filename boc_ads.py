import random

def get_random_ad():

    # Provide the bank with ads
    ads = ["And don't forget. Next time pay with your Bank of Cyprus card and get your antamivi points.",
    "Looking for a new car? We got you covered. Visit out website to learn more.",
    "Have you lost your card? Until found, freeze it. When found, unfreeze it. Just open BoC Mobile App!",
    "What summer means to you? Travelling, relaxing or just spending time with family and friends? However you prefer your summer, do it with Bank of Cyprus cards.",
    "Do you want to send and receive money instantly and securely through your mobile phone? Our BoC Mobile App service QuickPay, allows you to."
    ]

    # Get a random index
    random_index = random.randint(0, 4)
    random_ad = ads[random_index]
    return random_ad
