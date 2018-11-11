import ark
from random import randint
from pprint import pprint
def main():

    client = ark.ArkClient('http://localhost:4003/api')

    # this imports transfer
    from crypto.transactions.builder.transfer import Transfer
    from crypto.identity.address import address_from_passphrase
    from crypto.identity.private_key import PrivateKey
    from crypto.identity.public_key import PublicKey
    from crypto.identity.address import address_from_private_key





    # print(a)
    # delegates = client.delegates.all()
    # print(client.blocks.all())
    # print(delegates)

    # unique id that each recipient has



    # result =
    # print(result)


    # wallet = client.wallets


    # happens in recipients computer

    # recipientSecret = randomPhrase()

    # recipientSecret = "trade dog shed today law swear icon destroy goat more select praise"

    # priv = PrivateKey.from_passphrase(recipientSecret).to_hex()
    # print(priv)
    # address = address_from_private_key(priv, network_version=23)


    # print(address)
    # address = "AUXmEForVfTHqQHyVta1gyWo4BJ4hsm71k"

    address = "AJsumLTKPqzq1mcpvogMt59DvbYmad44EV"

    senderSecret = "clay harbor enemy utility margin pretty hub comic piece aerobic umbrella acquire"



    # priv = PrivateKey.from_passphrase(senderSecret).to_hex()

    # print(priv)

    # adr = address_from_private_key(priv, network_version=23)


    # print(adr)

    tx = Transfer(recipientId=address, amount=50000000)
    tx.sign(senderSecret)




    # print(tx.to_dict())
    # print("\n")

    ok = client.transactions.create([tx.transaction.to_dict()])


    pprint(ok)





    # ok = wallet.votes(recipientID, page=None, limit=1)

def randomPhrase():
    b = ""
    for i in range(6):
        a = randint(0, 9)
        if(a == 0):
            b+="hi"
        elif(i==1):
            b+="oh"
        elif(i==3):
            b+="ark"
        elif(i==4):
            b+="is"
        elif(i==5):
            b+="cool"
        elif(i==6):
            b+="so"
        elif(i==7):
            b+="much"
        elif(i==8):
            b+="ness"
        else:
            b+="real"
        return b;



if __name__ == "__main__":
    main()

