import ark
from pprint import pprint

def main():

    from crypto.transactions.builder.transfer import Transfer
    from crypto.identity.private_key import PrivateKey
    from crypto.identity.public_key import PublicKey
    from crypto.identity.address import address_from_private_key

    client = ark.ArkClient('https://localhost:4003')

    phrase = "outside tilt cluster film husband truck install fringe purse door build wire"
    priv = PrivateKey.from_passphrase(phrase).to_hex()



    # address = "AUXmEForVfTHqQHyVta1gyWo4BJ4hsm71k"
    # tx = Transfer(recipientId=address, amount=1)
    # tx.sign(passPhrase)

    # phrase = "clay harbor enemy utility margin pretty hub comic piece aerobic umbrella acquire"
    # priv = PrivateKey.from_passphrase(phrase).to_hex()

    address = address_from_private_key(priv, network_version=23)

    print(address)


    # pprint(priv)


if __name__ == "__main__":
    main()