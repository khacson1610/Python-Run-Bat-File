import datetime
import subprocess
import os

DIR_FOLDER = r"E:\Project\Python\Python"

def funFailed(responseCode, file):
    print("\n\n" + file + "Response: " + str(responseCode)  + " - Failed")
    print(datetime.datetime.now())
    print("Stop")

def funPassed(responseCode, file):
    print("\n\n" + file + " Response: " + str(responseCode) + " - Passed")
    print(datetime.datetime.now())
    print("Continue")

if __name__ =="__main__":
    #List batch 
    listBatchFile = ["BAT2.BAT", "BAT3.BAT"]
    
    #Run Batch 
    for file in listBatchFile:
        output = DIR_FOLDER + r"\LOG\\" + str(file[0:-4]) + ".LOG"
        
        #input Param
        inputParam  = " " + DIR_FOLDER + r"\SQL\input.sql "
        param = inputParam + output
        
        dir_file = r"\\" + file
        bat_file = DIR_FOLDER + dir_file + param

        response = subprocess.call(bat_file, shell=True)
        if response == 0:
            funPassed(response, file)
        else:
            funFailed(response, file)
            #break