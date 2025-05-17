import csv
import os

# Open the CSV file
folder_path = './AAA 1.3% tested on midcap shares'
    # Initialize accumulators for the values we want to collect

#some values that are standard
total_money_available=10000
percentInvested=0.025
invested_per_share=total_money_available*percentInvested
timeInterval=5          #num of minutes for each trading interval

total_net_profit = 0
average_net_profit=0
total_buy_hold_return=0
average_buy_hold_return=0
total_open_pl=0
average_open_pl=0
total_commission_paid = 0
total_sharpe_ratio=0
average_sharpe_ratio = 0
total_sortino_ratio=0
average_sortino_ratio = 0
total_profit_factor=0
average_profit_factor=0
total_closed_trades=0
total_open_trades=0
average_number_closed_trades=0
average_number_open_trades=0
total_percent_profitability=0
average_percent_profitability=0
total_avg_bars_in_trades=0
avg_avg_bars_in_trade=0

# Helper function to safely convert a value to float, or return 0 if it's 'N/A' or other non-numeric value
def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0  # Or use None if you prefer

    # Counters to calculate averages
file_count = 0
profitable_trades_count = 0
# Iterate over all CSV files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)

    # Initialize variables
    net_profit = gross_profit = gross_loss = max_run_up = max_drawdown = 0
    buy_hold_return = sharpe_ratio = sortino_ratio = profit_factor = 0
    max_contracts_held = open_pl = commission_paid = 0
    closed_trades = open_trades = 0
    number_winning_trades = number_losing_trades = 0
    percent_profitable = avg_trade = avg_winning_trade = avg_losing_trade = 0
    ratio_avg_win_loss = largest_winning_trade = largest_losing_trade = 0
    avg_bars_in_trades = avg_bars_in_winning_trades = avg_bars_in_losing_trades = 0

    #File 2 type
    num_trades=0
    trade_array_entry_date=[]
    trade_array_exit_date=[]
    trade_array_profit=[]
    trade_array_drawdown=[]
   

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        first_row = next(reader)

        # Check if file type is determined by first row's first column
        if first_row[0].startswith("Trade"):  # File Type 2: Trade records
            for row in reader:
                num=row[0]
                if row[1].startswith("Exit"):
                    #Do exit stuff
                    trade_array_exit_date[num]=row[3]
                    trade_array_profit[num]=row[6]
                    trade_array_drawdown=row[12]
                elif row[1].startswith("Entry"):
                    #Do entry stuff
                    trade_array_entry_date[num]=row[3]
                    trade_array_profit[num]=row[6]
                    trade_array_drawdown=row[12]

            print(f"Trades")
            print(f"{'Trades:':<25} {trade_array_profit}")

        #READ FILE TYPE 1
        else:
            for row in reader:
                if 'Net Profit' in row[0]:
                    net_profit = safe_float(row[1])
                elif 'Gross Profit' in row[0]:
                    gross_profit = safe_float(row[1])
                elif 'Gross Loss' in row[0]:
                    gross_loss = safe_float(row[1])
                elif 'Max Run-up' in row[0]:
                    max_run_up = safe_float(row[1])
                elif 'Max Drawdown' in row[0]:
                    max_drawdown = safe_float(row[1])
                elif 'Buy & Hold Return' in row[0]:
                    buy_hold_return = safe_float(row[1])
                elif 'Sharpe Ratio' in row[0]:
                    sharpe_ratio = safe_float(row[1])
                elif 'Sortino Ratio' in row[0]:
                    sortino_ratio = safe_float(row[1])
                elif 'Profit Factor' in row[0]:
                    profit_factor = safe_float(row[1])
                elif 'Max Contracts Held' in row[0]:
                    max_contracts_held = int(row[1])
                elif 'Open PL' in row[0]:
                    open_pl = safe_float(row[1])
                elif 'Commission Paid' in row[0]:
                    commission_paid = safe_float(row[1])
                elif 'Total Closed Trades' in row[0]:
                    closed_trades = int(row[1])
                elif 'Total Open Trades' in row[0]:
                    open_trades = int(row[1])
                elif 'Number Winning Trades' in row[0]:
                    number_winning_trades = int(row[1])
                elif 'Number Losing Trades' in row[0]:
                    number_losing_trades = int(row[1])
                elif 'Percent Profitable' in row[0]:
                    percent_profitable = safe_float(row[1])
                elif 'Avg Trade' in row[0]:
                    avg_trade = safe_float(row[1])
                elif 'Avg Winning Trade' in row[0]:
                    avg_winning_trade = safe_float(row[1])
                elif 'Avg Losing Trade' in row[0]:
                    avg_losing_trade = safe_float(row[1])
                elif 'Ratio Avg Win / Avg Loss' in row[0]:
                    ratio_avg_win_loss = safe_float(row[1])
                elif 'Largest Winning Trade' in row[0]:
                    largest_winning_trade = safe_float(row[1])
                elif 'Largest Losing Trade' in row[0]:
                    largest_losing_trade = safe_float(row[1])
                elif 'Avg # Bars in Trades' in row[0]:
                    avg_bars_in_trades = safe_float(row[1])
                elif 'Avg # Bars in Winning Trades' in row[0]:
                    avg_bars_in_winning_trades = safe_float(row[1])
                elif 'Avg # Bars in Losing Trades' in row[0]:
                    avg_bars_in_losing_trades = safe_float(row[1])

                
            #Acccumulate totals
            file_count+=1
            total_net_profit+=net_profit
            total_buy_hold_return+=(buy_hold_return*percentInvested)
            total_open_pl+=open_pl
            total_commission_paid+=commission_paid
            total_sharpe_ratio+=sharpe_ratio
            total_sortino_ratio+=sortino_ratio
            total_profit_factor+=profit_factor
            total_closed_trades+=closed_trades
            total_open_trades+=open_trades
            total_percent_profitability+=percent_profitable
            total_avg_bars_in_trades+=closed_trades*avg_bars_in_trades
        

average_net_profit= total_net_profit/file_count
average_buy_hold_return=total_buy_hold_return/file_count
average_open_pl=total_open_pl/file_count
average_sharpe_ratio = total_sharpe_ratio/file_count
average_sortino_ratio = total_sortino_ratio/file_count
average_profit_factor= total_profit_factor/file_count
average_number_closed_trades= total_closed_trades/file_count
average_number_open_trades= total_open_trades/file_count
average_percent_profitability= total_percent_profitability/file_count
avg_avg_bars_in_trade= total_avg_bars_in_trades/total_closed_trades
avg_commission_per_trade=(total_commission_paid/(total_closed_trades+(total_open_trades/2))/2)
#do other calculations
total= total_net_profit+total_open_pl
averagetotal= total/file_count
average_per_trade=total/(total_closed_trades+total_open_trades)
average_minutes_in_trade=avg_avg_bars_in_trade*5
average_hours_in_trade=average_minutes_in_trade/60
average_business_days_in_trade=average_hours_in_trade/6
percent_of_year_in_trade=(average_business_days_in_trade/252)*100   #based on there being 252 business days in a year
totalBuyHoldInvested=file_count*invested_per_share
buy_hold_return_percent=total_buy_hold_return/totalBuyHoldInvested*100

#Estimate max trades open (this is open to interpretation)


trade_to_yearhold_ratio=100/percent_of_year_in_trade
trade_to_year_Times_average_per=trade_to_yearhold_ratio*average_per_trade
profitability=trade_to_year_Times_average_per/average_buy_hold_return
if trade_to_year_Times_average_per < average_buy_hold_return:
    profitability=-abs(profitability)
else:
    profitability=abs(profitability)
# Print out all variables
print(f"{'Assets tested:':<25} {round(file_count):>10,}")
print(f"-------")
print(f"Totals:")
print(f"-------")
print(f"{'Total:':<25} {round(total):>10,}")
print(f"{'Total Net Profit:':<25} {round(total_net_profit):>10,}")
print(f"{'Total Open PL:':<25} {round(total_open_pl):>10,}")
print(f"{'Total # closed trades:':<25} {total_closed_trades:>10}")
print(f"{'Total # open trades:':<25} {total_open_trades:>10,}")
print(f"{'Total Commission Paid:':<25} {round(total_commission_paid):>10,}")
print(f"{'Commission as % profit:':<25} {round((total_commission_paid/total)*100,2):>10,}")
print(f"-------")
print(f"Averages (per asset):")
print(f"-------")
print(f"{'Average Total:':<25} {round(averagetotal):>10,}")
print(f"{'Average Net Profit:':<25} {round(average_net_profit):>10,}")
print(f"{'Average per trade:':<25} {round(average_per_trade, 2):>10,}")
print(f"{'Average Open PL:':<25} {round(average_open_pl):>10,}")
print(f"{'Average # Closed Trades:':<25} {round(average_number_closed_trades,2):>10,}")
print(f"{'Average # Open Trades:':<25} {round(average_number_open_trades, 2):>10,}")
print(f"{'Avg Commision per Trade:':<25} {round(avg_commission_per_trade,2):>10,}")
print(f"-------")
print(f"Ratios:")
print(f"-------")
print(f"{'Avg Sharpe Ratio:':<25} {round(average_sharpe_ratio,2):>10,}")
print(f"{'Avg Sortino Ratio:':<25} {round(average_sortino_ratio,2):>10,}")
print(f"{'Avg Profit Factor:':<25} {round(average_profit_factor,2):>10,}")
print(f"-------")
print(f"Time:")
print(f"-------")
print(f"{'Avg # Bars in Trades:':<25} {round(avg_avg_bars_in_trade):>10,}")
print(f"{'Avg min in Trades:':<25} {round(average_minutes_in_trade):>10,}")
print(f"{'Avg hours in Trade:':<25} {round(average_hours_in_trade):>10,}")
print(f"{'Avg days in Trade:':<25} {round(average_business_days_in_trade,2):>10,}")
print(f"{'Avg % of Year in Trade:':<25} {round(percent_of_year_in_trade,2):>10,}")
print(f"-------")
print(f"Comaprisons to Buy/Hold")
print(f"-------")
print(f"{'Total Buy Hold Return:':<25} {round(total_buy_hold_return):>10,}")
print(f"{'Total money invested:':<25} {round(totalBuyHoldInvested):>10,}")
print(f"{'Buy hold return %:':<25} {round(buy_hold_return_percent, 2):>10,}")
print(f"{'A) # trades to make 100%:':<25} {round(trade_to_yearhold_ratio,2):>10,}") #How many trades are equivelant to holding a single trade for a year
print(f"{'B) A*avg per trade':<25} {round(trade_to_year_Times_average_per,2):>10,}")   #The above number times average profit per trade
print(f"{'Average Buy Hold Return:':<25} {round(average_buy_hold_return):>10,}")
print(f"{'profit% compare Buyhold:':<25} {round(profitability,2):>10,}")
print(f"----------------")
print(f"----------------")
