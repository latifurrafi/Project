
import ccxt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from ta import add_all_ta_features

exchange = ccxt.bybit()
symbol = 'BTC/USDT'
timeframe = '4h'

def get_crypto_data(symbol, timeframe, limit=1000):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

    print(df.tail)

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def add_technical_indicators(df):
    df = add_all_ta_features(
        df, open="open", high="high", low="low", close="close", volume="volume")
    return df

def train_model(df):
    features = df.drop(['timestamp', 'close'], axis=1)
    target = df['close']
    
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, shuffle=False)
    
    model = RandomForestRegressor(n_estimators=2)
    model.fit(X_train, y_train)
    
    return model, X_test, y_test

def predict_price(model, new_data):
    return model.predict(new_data)

def execute_trade(prediction, current_price):
    if prediction > current_price:
        print("Buy")
    else:
        print("Sell")

if __name__ == "__main__":
    df = get_crypto_data(symbol, timeframe)
 
    df = add_technical_indicators(df)
    
    model, X_test, y_test = train_model(df)

    prediction = predict_price(model, X_test.iloc[-1].values.reshape(1, -1))

    current_price = df['close'].iloc[-1]
    execute_trade(prediction, current_price)
