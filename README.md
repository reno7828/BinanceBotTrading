# BinanceBotTrading

Bot de trading Binance (achat/vente)

1. Créez un fichier `config.py` et ajoutez les lignes suivantes :
    ```python
    api_key=""
    api_secret=""
    ```

2. Indiquez votre mise en BUSD
3. Indiquez l'écart d'achat (`ecartBuy`) par rapport au prix en temps réel
4. Indiquez l'écart de vente (`ecartSell`) en fonction du prix d'achat

Exemple : 
- Prix en temps réel : 1000
- Prix d'achat : 990 (donc `ecartBuy = 10`)
- Prix de vente : 1020 (`ecartSell = 30`)

- Modifier order_buy et order_sell => %.4f coresspond à 4 chiffres apres la virgule donc modifier 4 par le nombre corespondant à votre crypto.

**Remarque :** Utilisez toujours des BUSD car sur Binance, il y a des frais de transaction uniquement en ordre limit et avec des BUSD, il n'y a pas de frais.

