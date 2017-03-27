import random
import radar

# We are assuming 3 securities, with 5 portfolios each, which 5 trades each port
# This script will generate random multipliers, prices, and trades for these securities and portfolios
# Modify below values to change amount of securities/portfolios
SEC_COUNT=3
PORT_COUNT=5
TRADE_COUNT=5

# Generate a dict of securities and portfolio names
secport={}
curr=1
for i in range(1,SEC_COUNT+1):
    secport["S"+str(i)]=["P"+str(x) for x in range(curr,curr+PORT_COUNT)]
    curr=curr+PORT_COUNT

# Generate random security prices and multipliers
# Multipler ranges from 1 to 9
# Price ranges from 100 to 1000
# File format: <security>,<multiplier>,<price>

wfile = "sec-price-mult"
f = open(wfile,'w')
f.write('security,multiplier,price\n')
for security in secport:
    f.write('%s,%s,%s\n' % (security,random.randint(1,9),random.randrange(100,1000)))
f.close()

# Generate random trades file
# Trades range from -1000 to 1000
wfile = "trades"
f = open(wfile,'w')
f.write('security,portfolio,timestamp,trade\n')
for security in secport:
    for portfolio in secport[security]:
        for i in range(0,TRADE_COUNT):
            f.write('%s,%s,%s,%s\n' % (security,portfolio,str(radar.random_datetime()),random.randrange(-1000,1000)))
