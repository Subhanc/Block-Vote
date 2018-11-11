import ark
import pprint
import datetime
from pprint import pprint
def main():



    from crypto.transactions.builder.transfer import Transfer
    from crypto.identity.address import address_from_private_key
    from crypto.identity.private_key import PrivateKey
    from crypto.identity.public_key import PublicKey
    from crypto.identity.address import address_from_private_key
    import time
    from crypto.configuration.network import set_custom_network
    from crypto.transactions.builder.transfer import Transfer

    # from tbw import parse_config
    # from util.sql import SnekDB
    # from util.dynamic import Dynamic
    from ark import ArkClient

    client = ArkClient('http://localhost:4003/api')

    from datetime import datetime

    epoch = datetime(2017, 1, 1, 13, 00, 00)
    version = 23
    wif = 130

    work = set_custom_network(epoch, version, wif)

    # userInput

    # passPhrase = "clay harbor enemy utility margin pretty hub comic piece aerobic umbrella acquire"
    phrase = "outside tilt cluster film husband truck install fringe purse door build wire"




    candidate = "ANBkoGqWeTSiaEVgVzSKZd3jS7UWzv9PSo"
    # chooseVoter("Donald Trump")
    print(candidate)

    # priv = PrivateKey.from_passphrase(candidate).to_hex()

    tx = Transfer(recipientId=candidate, amount=50000)
    tx.sign(phrase)


    # print(tx.verify())

    ok = client.transactions.create([tx.transaction.to_dict()])

    pprint(ok)

def chooseVoter(s):
    if s == "Donald Trump":
        return "AapTzNLAeAwBq5pMvBGcfg4fDgaoRE4QhW"
    elif s == "Hilary Clinton":
        return "ARHE2vskTTUg219Yddv4VZaeBrpjBkcCwK"
    else:
        return "AP5CY4MtjXAsB2Tx8nmLXGxrzumkXq2ixU"



if __name__ == "__main__":
    main()