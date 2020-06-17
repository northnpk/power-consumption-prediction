import Saeverbank
from matplotlib import pyplot
from datetime import datetime, date, time, timedelta

for x in range(69):
	time = (x+1)*7
	start_date = datetime(2010, 11, 26)
	new_date = start_date + timedelta(time)
	print(new_date, 'New date')
	input_date = datetime.strftime(new_date, '%Y-%m-%d')
	result , result_plot = Saeverbank.ElecCostForecast(input_date)
	print(x+1, 'Week passed')
	if x == 0:
		all_result = result_plot
	else:
		all_result = all_result + result_plot
	if x == 68:
		all_result = all_result + result_plot
		pyplot.plot(all_result, marker='o', label='Forecasting')
		pyplot.show()
#input_date = '2010-11-26'
#result , result_plot = Saeverbank.ElecCostForecast(input_date)

#print(result)
#days = ['sun', 'mon', 'tue', 'wed', 'thr', 'fri', 'sat']
#pyplot.plot(days, result_plot, marker='o', label='Forecasting')
#pyplot.show()
