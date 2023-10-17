import time
from binance.client import Client
from binance.enums import *
import config

client = Client(config.api_key, config.api_secret)

choix = input("Crypto a trade : ")
selection = (choix + "busd").upper()

crypto_trade = selection                       # indiquer la crypto à trader
crypto =crypto_trade

choixMise = input("indiquer votre mise en busd : ")
mise = float(choixMise)# indiquez la mise en dollars

#ecart prix achat
ecartBuy = input("indiquer ecart prix achat : ")
choixEcartBuy = float(ecartBuy)

#ecart prix vente
ecartSell = input("indiquer ecart prix vente : ")
choixEcartSell = float(ecartSell)


def delay():
    delais = time.sleep(10)


def run():


    go = True
    while go:


        micro_cap_coins = [
            crypto ]  # si besoin de changer de crypto c'est la qu il faut le mettre ex : ['FILUSDT'], ['BNBUSDT']....
        # time_horizon = "Short"
        # Risk = "High"
        print("\n\n---------------------------------------------------------\n\n")


        #prix achat
        infoBuy = client.get_ticker(symbol=selection)
        realtimePrice = infoBuy.get('lastPrice')
        prixAchat = float(realtimePrice) - choixEcartBuy


        for coin in micro_cap_coins:
            scalping_orders(coin, 1, 1)



def market_depth(sym, num_entries=20):
    # Get market depth
    # Retrieve and format market depth (order book) including time-stamp
    i = 0  # Used as a counter for number of entries
    # print("Order Book: ", convert_time_binance(client.get_server_time()))
    depth = client.get_order_book(symbol=sym)
    # print(depth)
    # print(depth['asks'][0])
    ask_tot = 0.0
    ask_price = []
    ask_quantity = []
    bid_price = []
    bid_quantity = []
    bid_tot = 0.0
    place_order_ask_price = 0
    place_order_bid_price = 0
    max_order_ask = 0
    max_order_bid = 0
    # print("\n", sym, "\nDepth     ASKS:\n")
    # print("Price     Amount")
    for ask in depth['asks']:
        if i < num_entries:
            if float(ask[1]) > float(max_order_ask):
                # Determine Price to place ask order based on highest volume
                max_order_ask = ask[1]
                place_order_ask_price = round(float(ask[0]), 5) - 0.0001
            # ask_list.append([ask[0], ask[1]])
            ask_price.append(float(ask[0]))
            ask_tot += float(ask[1])
            ask_quantity.append(ask_tot)
            # print(ask)
            i += 1
    j = 0  # Secondary Counter for Bids
    # print("\n", sym, "\nDepth     BIDS:\n")
    # print("Price     Amount")
    for bid in depth['bids']:
        if j < num_entries:
            if float(bid[1]) > float(max_order_bid):
                # Determine Price to place ask order based on highest volume
                max_order_bid = bid[1]
                place_order_bid_price = round(float(bid[0]), 5) + 0.0001
            bid_price.append(float(bid[0]))
            bid_tot += float(bid[1])
            bid_quantity.append(bid_tot)
            # print(bid)
            j += 1
    return ask_price, ask_quantity, bid_price, bid_quantity, place_order_ask_price, place_order_bid_price
    # Plot Data


def scalping_orders(coin, wait=1, tot_time=1):

    details = client.get_ticker(symbol=crypto)
    last_price = float(details.get('lastPrice'))
    # ordre achat a boucler
    qty = ("%.1f" % (mise / last_price))
    print(qty)

    prixAchat = last_price - choixEcartBuy
    #print("Le prix d'achat est de : ", prixAchat)

    order_buy = client.create_order(
        symbol= crypto,
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity= qty,
        price=("%.4f" % prixAchat))





    running = True

    while running:

        try:

            # placer order limit sell
            prixVente = prixAchat + choixEcartSell
            #print("le prix de vente est de : ", prixVente)

            order_sell = client.create_order(
                symbol= crypto,  # Indiquez le coin a trader!!!!!!!!!!!!!!!!!!!!!!!!
                side=SIDE_SELL,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity= qty,
                price=("%.4f" % prixVente))
            #print("La vente à été demandée .....")

            running = False



        except:

            #print("l'ordre d achat nest pas encore passé....' ")
            continue
    #essaye de relancer le run()
    continuer = True
    while continuer:

        try :
            #mettre un delais de 10 secondes pour eviter le bannissement
            delay()
            run() #probleme si vente pas assez rapide le run fail car manque de moyen
        except:
            #print("la vente n'a pas été réalisée pour le moment ...")
            continue








# def buy_sell_bot():
#     pass



if __name__ == "__main__":
    run() #entre et lance a partir de run()
