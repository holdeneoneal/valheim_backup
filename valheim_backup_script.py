import datetime
import os
import subprocess
import shutil

##############################################################################################
# Make changes here
# Important Notes while making changes
# 1. Quotations("a value") around values are important. Don't delete them!
# 2. Backslashes(\) are important too. Where there are two, there need to be.
##############################################################################################
# windows username
user_name = "your_username_here"

# the location of 7zip
# this is needed so the script can create an archive file in the backup location you specify
zip_software_location = "C:\\Program Files\\7-Zip"

# change from True to False if you don't want to use 7zip
# IMPORTANT: Using 7zip compresses the files to save on disk space
use_7zip = True

# location of the Valheim server and character save data
# you may need to update this if your installation of Valheim is somewhere else
valheim_directory = "C:\\Users\\" + user_name + "\AppData\LocalLow\IronGate\Valheim"

# directory location where you want store backups
# default to C:\\Users\\<windows_user>\\valheim_backups\\
backup_dir = "C:\\Users\\" + user_name + "\\valheim_backups\\"

# how many days to keep backups
# default value is 2
# If you want to save on space you can reduce this to 1, but not 0.
backup_days = 2

# change True to False if you don't want the backups cleaned up automatically
auto_cleanup = True

##############################################################################################
# that's all the changes you should need to make
##############################################################################################

# creates the backup dir if it does not already exist
if not os.path.isdir(backup_dir):
  os.mkdir(backup_dir)

# the valheim backup logfile is stored in the same place as the backups
log_name = "backup_script_log.log"
backup_logfile = backup_dir + log_name

# capture the current time
current_time = datetime.datetime.now()
# format the timestamp for the backup file
timestamp = str(current_time.month)+"_"+str(current_time.day)+"_"+str(current_time.year)+"_"+str(current_time.hour)+"_"+str(current_time.minute)+"_"+str(current_time.second)
# determine what day was two days ago
stale = current_time - datetime.timedelta(backup_days)
# format the staledate to match the backup file format
staledate = str(stale.month)+"_"+str(stale.day)+"_"+str(stale.year)

# The prefix for the file name
fileprefix = "valheim_data_"
# the timestamp embedded direcotry that holds the backed up world and characters
vbackup = fileprefix + timestamp
# open our log file for writing to
logfile = open(backup_dir+backup_logfile, "a")

logfile.write("-----------------------------------------------------------" + "\n")
logfile.write("Time of this backup run: " + str(current_time) + "\n")
logfile.write("Files will be considered stale if created on : " + str(staledate) + "\n")
logfile.write("Valheim directory: " + valheim_directory + "\n")
logfile.write("Location of backups: " + backup_dir + "\n")
logfile.write("Name of this backup directory : " + vbackup + "\n")
logfile.write("Use 7zip is set to: " + str(use_7zip))

# Run back up the data
logfile.write("starting backup.." + "\n")
# if not using 7zip, we will just do a copy
if use_7zip is False:
  shutil.copytree(valheim_directory+"\\worlds", backup_dir+vbackup+"\\worlds")
  shutil.copytree(valheim_directory+"\\characters", backup_dir+vbackup+"\\characters")
  logfile.write("copy complete" + "\n")
else:
  os.chdir(zip_software_location)
  out=subprocess.run(["7z", "a", "-mmt", "-mx1", "-t7z", backup_dir+backup_file, valheim_directory+"\\worlds", valheim_directory+"/characters", valheim_directory+"\\characters"], capture_output=True)
  if out.returncode != 0:
    logfile.write("ZIP FAILED!!!" + "\n")
    logfile.write(str(out) + "\n")
    logfile.write(str(stdout) + "\n")
    logfile.write(str(stderr) + "\n")
  logfile.write("zip complete" + "\n")

if auto_clean == true:
  # Cleanup stale files
  # for each file in the backup directory location
  logfile.write("checking for stale files to delete" + "\n")
  for filename in os.listdir(backup_dir):
    # make sure the file is one our backups
    # by checking if the fileprefix is in the filename
    if fileprefix in filename:
        # if the stale date(day_month_year) is in the filename
        if staledate in filename:
          logfile.write("removing the stale backup: " + backup_dir+filename + "\n")
          # delete the file
          os.remove(backup_dir+filename)
  logfile.write("stale file cleanup completed" + "\n")

logfile.write("backup complete" + "\n")
logfile.write("-----------------------------------------------------------" + "\n")
logfile.close()