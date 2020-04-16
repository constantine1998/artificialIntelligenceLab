SECONDS=0
python tsp.py < ../Lab4/TestCases/euc_100 > results_euc_100
duration=$SECONDS
echo "$duration"

SECONDS=0
python tsp.py < ../Lab4/TestCases/euc_250 > results_euc_250
duration=$SECONDS
echo "$duration"

SECONDS=0
python tsp.py < ../Lab4/TestCases/euc_500 > results_euc_500
duration=$SECONDS
echo "$duration"

SECONDS=0
python tsp.py < ../Lab4/TestCases/noneuc_100 > results_noneuc_100
duration=$SECONDS
echo "$duration"

SECONDS=0
python tsp.py < ../Lab4/TestCases/noneuc_250 > results_noneuc_250
duration=$SECONDS
echo "$duration"

SECONDS=0
python tsp.py < ../Lab4/TestCases/noneuc_500 > results_noneuc_500
duration=$SECONDS
echo "$duration"

