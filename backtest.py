
class BacktestSMA:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.crosses = []
        self.signals = {}
        self.returns = 0
        self.calculatesma()

    def calculatesma(self):
        for x in range(2,21):
            self.dataframe[f'SMA {x}'] = self.dataframe['Close'].rolling(window=x, min_periods=1).mean().round(5)
    
    def crossover(self, x, y):
        crosses = []
        for i in range(1, len(self.dataframe['Close'])):
            if self.dataframe[f'SMA {x}'][i] == self.dataframe[f'SMA {y}'][i]:
                crosses.append(i)
            elif self.dataframe[f'SMA {x}'][i] > self.dataframe[f'SMA {y}'][i] and self.dataframe[f'SMA {x}'][i - 1] < self.dataframe[f'SMA {y}'][i - 1]:
                crosses.append(i)
            elif self.dataframe[f'SMA {x}'][i] < self.dataframe[f'SMA {y}'][i] and self.dataframe[f'SMA {x}'][i - 1] > self.dataframe[f'SMA {y}'][i - 1]:
                crosses.append(i)      
        self.crosses = crosses

    def trends(self, x, y):
        signals = {}
        for z in range(1, len(self.dataframe['Close'])):
            for i in self.crosses:
                if z == i:
                    if self.dataframe[f'SMA {x}'][z - 1] > self.dataframe[f'SMA {y}'][z - 1]:
                        signals[z] = 'Long'
                    elif self.dataframe[f'SMA {x}'][z - 1] < self.dataframe[f'SMA {y}'][z - 1]:
                        signals[z] = 'Short'
        self.signals = signals
    
    def simulate(self):
        portfolio = 100000
        keys = list(self.signals.keys())
        for x in range(len(keys) - 1):
            if self.signals[keys[x]] == 'Long':
                diff = self.dataframe['Close'][keys[x+1]] - self.dataframe['Close'][keys[x]]
                portfolio = (diff * portfolio) + portfolio
            elif self.signals[keys[x]] == 'Short':
                diff = self.dataframe['Close'][keys[x]] - self.dataframe['Close'][keys[x+1]]
                portfolio = (diff * portfolio) + portfolio
        self.returns = portfolio - 100000
        
    
