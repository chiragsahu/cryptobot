from multiprocessing import Process
import time

def loop_a():
    while 1:
        
        time.sleep(5)
        print("loop a has started")

def loop_b():
    while 1:
        time.sleep(10)
        print("loop b has started")

if __name__ == '__main__':
    Process(target=loop_a).start()
    Process(target=loop_b).start()

# cryptos = ["/usdtinr",  "btcinr",  "/ltcinr",  "/xrpinr",
#           "/dashinr",  "/ethinr",  "/trxinr",  "/eosinr",
#             "/batinr",  "/wrxinr",  "/maticinr",  "/bchabcinr",
#           "/bnbinr",  "/bttinr",  "/yfiinr",  "/uniinr",  "/linkinr",
#           "/sxpinr",  "/adainr",  "/atominr",  "/xlminr",  "/xeminr",
#             "/zecinr",  "/busdinr",  "/usdtinr"]