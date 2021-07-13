from gym_anytrading.envs import StocksEnv

def my_processed_data(env):
  start = env.frame_bound[0] - env.window_size
  end = env.frame_bound[1]
  prices = env.df.loc[:,"Close"].to_numpy()[start:end]
  signal_features = env.df.loc[:, :].to_numpy()[start:end]# ['Close', 'Momentumbla']
  return prices, signal_features

class MyCustomEnv(StocksEnv):
  def __init__(self, df, window_size, frame_bound):
      StocksEnv.__init__(self, df, window_size, frame_bound)
      StocksEnv.trade_fee_bid_percent = 0.00075 # binance fees https://www.binance.com/en/fee/schedule
      StocksEnv.trade_fee_ask_percent = 0.00075

  _process_data = my_processed_data
