#basic driver for implementation of gameEngine.py
#Matt Bachman, Jan 2013

#to import from parent directory
import sys
sys.path.append("..")
import gameEngine
import blockBreaker

def main():


    bb=blockBreaker.blockBreaker()
    theGame=gameEngine.gameEngine((800,600),"Block Breaker",bb)

    theGame.run()

main()
