import time
import datetime
import tweepy
import telepot
import emoji

usuariosStartados = []
telegramBot = telepot.Bot('741536657:AAGDEvgCkQVCUoe7dFE6lNya8BXX7WTAhMg')

def mandarMensagem(chat_id, texto):
    # def mandarMensagem(idUsuario, texto):
    telegramBot.sendMessage(chat_id, texto, parse_mode="HTML")


consumer_key = '1Jrcio6zZPMho0wVlCRE4jPkK'
consumer_secret = '3I5I9aTC5EB5NkK9fVg5Dh5AfXmVVPTylO5siErR8DYIxNfj1n'
access_token = '211965961-Bd9S6ZqY3hOHAvbgCjGAePjXHRIREtSLTywo21Nb'
access_token_secret = '0s5l0ISNAAqLsVADUbQgiQ9NE8ie7IZHGbH0xzhMzp2cu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#for tweet in tweepy.Cursor(api.search,q="@binance",count=1,
                          # lang="en",
                          # since="2019-01-08").items():
    #print (tweet.created_at, tweet.text)


def envia_msg():

    chat_id = '-320200803'
    print(chat_id)
    usuariosStartados.append(chat_id)
    u1= ''
    u2= ''
    u3= ''
    u4= ''
    u5= ''
    u6= ''
    u7= ''
    u8 = ''
    u9 = ''
    u10 = ''
    u11 = ''
    u12 = ''
    u13 = ''
    u14 = ''
    u15 = ''
    u16 = ''
    u17 = ''
    u18 = ''
    u19 = ''
    u20 = ''
    u21 = ''
    u22 = ''
    u23 = ''
    u24 = ''
    u25 = ''
    u26 = ''
    u27 = ''
    u28 = ''
    u29 = ''
    u30 = ''
    u31 = ''
    u32 = ''
    u33 = ''
    u34 = ''
    u35 = ''
    u36 = ''
    u37 = ''
    u38 = ''
    u39 = ''
    u40 = ''
    u41 = ''
    u42 = ''
    u43 = ''
    u44 = ''
    u45 = ''
    u46 = ''
    u47 = ''
    u48 = ''
    u49 = ''
    u50 = ''
    u51 = ''
    u52 = ''
    u53 = ''
    u54 = ''
    u55 = ''
    u56 = ''
    u57 = ''
    u58 = ''
    u59 = ''
    u60 = ''
    u61 = ''
    u62 = ''
    u63 = ''
    u64 = ''
    u65 = ''
    u66 = ''
    u67 = ''
    u68 = ''
    u69 = ''
    u70 = ''
    u71 = ''

    while True:
        time.sleep(30)
        tweets = api.user_timeline(screen_name='Binance', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:

            #print("Name:", tweet.author.name)
            #print("Screen-name:", tweet.author.screen_name)
            #print("Tweet created:", tweet.created_at)
            #print("Tweet:", tweet.full_text)
            ###print("Tweet:", tweet.lang)
            ####print("Location:", tweet.user.location.encode('utf8'))
            #print('##############################################')
            ultimo_tweet= tweet.full_text
            screen_name= ' @' + tweet.author.screen_name
            #criado_em = datetime.datetime.strptime(tweet.created_at, '%Y-%m-%d %H:%M:%S')
            #criado_em = criado_em.strftime('%m/%d/%y')
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
            #print(tweet.created_at)
            #print(tweet.text)
            #print(tweet.user.name)
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u1 != ultimo_tweet:
            mandarMensagem(chat_id, '<b>Binance </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u1= ultimo_tweet
        #############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='Binance_Info', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u2 != ultimo_tweet and u2 != u1:
            mandarMensagem(chat_id, '<b>Binance Info </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u2= ultimo_tweet
        ##############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='cz_binance', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u3 != ultimo_tweet and u3 != u1 and u3 != u2:
            mandarMensagem(chat_id,
                           '<b>CZ Binance </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u3 = ultimo_tweet


        ##############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='bitfinex', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u4 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bitfinex </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u4 = ultimo_tweet

        ##############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='coinbase', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u5 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Coinbase </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u5 = ultimo_tweet

        ################################# CEO COINBASE #########################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='brian_armstrong', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u6 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Brian Armstrong </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u6 = ultimo_tweet

        ##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='HuobiBrasil', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u7 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Huobi Brasil </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u7 = ultimo_tweet

        ##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='HuobiInfo', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u8 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Huobi Info </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u8 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='HuobiGlobal', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u9 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Huobi Global </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u9 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='BitMEXdotcom', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u10 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>BitMEX </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u10 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='SatoshiLite', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u11 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Charlie Lee [LTC ⚡] </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u11 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='VitalikButerin', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u12 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Vitalik Non-giver of Ether </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u12 = ultimo_tweet


##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='Poloniex', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u13 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Poloniex Exchange </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u13 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='justinsuntron', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u14 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Justin Sun </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u14 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='tronfoundation', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u15 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>TRON Foundation </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u15 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='rogerkver', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u16 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Roger Ver </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u16 = ultimo_tweet


##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='OKEx', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u17 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>OKEx </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u17 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='Cardano', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u18 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Cardano Community </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u18 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='Ripple', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u19 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Ripple </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u19 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='block_one_', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u20 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Block.one </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u20 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='StellarOrg', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u21 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Stellar </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u21 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='IOTASupport', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u22 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>IOTA Support </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u22 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='DashDinheiro', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u23 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Dash DinheiroDigital </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u23 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='monero', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u24 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Monero || #xmr </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u24 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='Bitcoin', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u25 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bitcoin </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u25 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='hitbtc', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u26 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>HitBTC </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u26 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='BTCTN', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u27 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bitcoin News </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u27 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='kucoincom', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u28 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>KUCOIN </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u28 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='scashofficial', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u29 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>SmartCash </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u29 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='NEOnewstoday', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u30 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>NEO News </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u30 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='cnLedger', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u31 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>cnLedger </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u31 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='bobbyclee', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u32 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bobby Lee </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u32 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='litecoin', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u33 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>litecoin </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u33 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='LiteCoinNews', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u34 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>LiteCoin News </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u34 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='eth_classic', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u35 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Ethereum Classic </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u35 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='NEMofficial', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u36 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>NEM </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u36 = ultimo_tweet


##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='krakenfx', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u37 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Kraken Exchange </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u37 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='Gemini', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u38 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Gemini </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u38 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='winklevoss', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u39 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Cameron Winklevoss </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u39 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='tylerwinklevoss', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u40 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Tyler Winklevoss </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u40 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='CharlieShrem', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u41 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Charlie Shrem </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u41 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='nano', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u42 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Nano </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u42 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='CoinMarketCap', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u43 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>CoinMarketCap </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u43 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='BithumbOfficial', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u44 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bithumb </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u44 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='Bitstamp', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u45 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bitstamp </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u45 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='Cointelegraph', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u46 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Cointelegraph </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u46 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='BittrexExchange', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        if u47 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bittrex </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u47 = ultimo_tweet


##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='BittrexIntl', count=1, tweet_mode='extended',
                                   wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        if u48 != ultimo_tweet and u47 != u48:
            mandarMensagem(chat_id,
                           '<b>Bittrex International </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(
                               ':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u48 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='coindesk', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u49 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>CoinDesk </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u49 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='BitcoinMagazine', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u50 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bitcoin Magazine </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u50 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='blockchain', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u51 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Blockchain </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u51 = ultimo_tweet


##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='BigONEexchange', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u52 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>BigONE Exchange </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u52 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='jespow', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u53 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Jesse Powell </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u53 = ultimo_tweet

##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='aantonop', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u54 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Andreas M. Antonopoulos </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(
                               ':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u54 = ultimo_tweet


##########################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='br_bitcointrade', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u55 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bitcointrade </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u55 = ultimo_tweet
############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='MercadoBitcoin', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u56 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Mercado Bitcoin </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u56 = ultimo_tweet

############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='foxbit', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u57 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Foxbit </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u57 = ultimo_tweet


############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='NegocieCoins', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u58 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>NegocieCoins </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u58 = ultimo_tweet


############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='stratumcoinbr', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u59 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Stratum coinBR </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u59 = ultimo_tweet

############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='bitconfBR', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u60 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bitconf </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u60 = ultimo_tweet


############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='wavesplatform', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u61 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Waves Platform </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u61 = ultimo_tweet

############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='vergecurrency', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u62 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>vergecurrency </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u62 = ultimo_tweet

############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='_BitcoinSV', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u63 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bitcoin SV </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u63 = ultimo_tweet


############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='zcashco', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u64 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Zcash Company </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(
                               ':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u64 = ultimo_tweet

############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='exodus_io', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u65 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Exodus </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u65 = ultimo_tweet

############################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='Trezor', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u66 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Trezor </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u66 = ultimo_tweet
####################################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='Tether_to', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u67 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Tether </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u67 = ultimo_tweet

####################################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='LedgerHQ', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u68 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Ledger </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u68 = ultimo_tweet

####################################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='CoinomiWallet', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u69 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>coinomi </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u69 = ultimo_tweet

####################################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='eth_classic', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u70 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Ethereum Classic </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u70 = ultimo_tweet


####################################################################################################
        time.sleep(5)
        tweets = api.user_timeline(screen_name='tradingisfun17', count=1, tweet_mode='extended', wait_on_rate_limit=True)
        for tweet in tweets:
            ultimo_tweet = tweet.full_text
            screen_name = ' @' + tweet.author.screen_name
            criado_em = tweet.created_at
            print(f'Ultimo Tweet ou resposta: {ultimo_tweet}')
        criado_em = datetime.datetime.strftime(criado_em, "%d/%m/%y ás %H:%M")
        if u71 != ultimo_tweet:
            mandarMensagem(chat_id,
                           '<b>Bitcoin addict </b>' + emoji.emojize(':right_arrow:') + screen_name + ' ' + emoji.emojize(':eight_o’clock:') + criado_em + '\n' + ultimo_tweet)
            u71 = ultimo_tweet



while True:
    time.sleep(10)
    envia_msg()
