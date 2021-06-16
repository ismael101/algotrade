import pandas as pd
from backtest import BacktestSMA
from matplotlib import pyplot as plt

if __name__ == '__main__':
    dataframe = pd.read_csv('eur_usd_2020.csv')
    backtest = BacktestSMA(dataframe)
    strategy = []
    returns = []
    crossovers = []
    for x in range(2, 21):
        for y in range(2, 21):
            if(x < y):
                backtest.crossover(x, y)
                backtest.trends(x, y)
                backtest.simulate()
                strategy.append(f"{x}/{y}")
                returns.append(backtest.returns)
                crossovers.append(len(backtest.crosses))
    df = pd.DataFrame({'strategy':strategy, 'returns':returns, 'crossovers':crossovers})
    df.to_csv('eur_usd_2020_backtest_sma.csv')
    
    dataframe = pd.read_csv('eur_usd_2019.csv')
    backtest = BacktestSMA(dataframe)
    strategy = []
    returns = []
    crossovers = []
    for x in range(2, 21):
        for y in range(2, 21):
            if(x < y):
                backtest.crossover(x, y)
                backtest.trends(x, y)
                backtest.simulate()
                strategy.append(f"{x}/{y}")
                returns.append(backtest.returns)
                crossovers.append(len(backtest.crosses))
    df = pd.DataFrame({'strategy':strategy, 'returns':returns, 'crossovers':crossovers})
    df.to_csv('eur_usd_2019_backtest_sma.csv')

    dataframe = pd.read_csv('eur_usd_2018.csv')
    backtest = BacktestSMA(dataframe)
    strategy = []
    returns = []
    crossovers = []
    for x in range(2, 21):
        for y in range(2, 21):
            if(x < y):
                backtest.crossover(x, y)
                backtest.trends(x, y)
                backtest.simulate()
                strategy.append(f"{x}/{y}")
                returns.append(backtest.returns)
                crossovers.append(len(backtest.crosses))
    df = pd.DataFrame({'strategy':strategy, 'returns':returns, 'crossovers':crossovers})
    df.to_csv('eur_usd_2018_backtest_sma.csv')

    # for x in range(2, 21):
    #     for y in range(2, 21):
    #         if(x < y):
    #             backtest.crossover(x, y)
    #             backtest.trends(x, y)
    #             returns = backtest.simulate()
    #             print(f'{x}/{y} ========================> {returns}')

    # crosses = []
    # for x in crossover:
    #     if x < 1000:
    #         crosses.append(x)

    # plt.plot(df['Close'][:1000], marker='P' ,markevery=crosses)
    # plt.plot(df['SMA 5'][:1000])
    # plt.plot(df['SMA 10'][:1000])

    # #modify ticks size
    # plt.legend(labels =['Close', 'SMA 5', 'SMA 10'], fontsize=14)

    # #title and labels
    # plt.title('EUR USD Close Price', fontsize=20)
    # plt.xticks(fontsize=14)
    # plt.yticks(fontsize=14)
    # plt.xlabel('Time', fontsize=16)
    # plt.ylabel('Price', fontsize=16)

    # plt.show()
