import requests


def get_card(url):
        
    try:
        data = requests.get(url,timeout=10)
        data.raise_for_status()

        data = data.json()

        for card in data['data']:
            print(card['name'])
            for image in card['card_images']:
                print(image)

            for price in card['card_prices']:
                print(price)
         



    except requests.exceptions.RequestException as err:
        print ("Oops:",err)
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)     



#print(data)
#r.raise_for_status()

#print(len(data))
#for elemento in data:
#    print(elemento[0])
#print(len(data['data']))

   

    #print(card['card_prices'][0]['amazon_price'])

#aux=data['data'][0]

#for key in aux:
#    print(key)
