# Valheim Backup for Windows

If you've fallen in love with the world of Valheim as myself
and the Brothers of Mjolnir, you would be grateful to be spared
the same fate as us; falling victim to the world destroyer bug.

This repo holds instructions for how you can enable an automated
backup of your Valheim files on Windows, using a Python script, free 7zip software,
and the Windows Task Scheduler.

You can also run this script manually or via some other automation tool at your disposal. There is no dependency on Windows Task Scheduler.

----

## Install free software tools

### Install Python3

In order to run the script you will need to install Python3
on your computer. If you downloaded Python3 directly via the Microsoft Store, that won't work. The reason is because Windows Task Scheduler can't run that one(I was surprised too!).

[python.org downloads](https://www.python.org/downloads/)

Keep track of the installation location because you will
need it for Windows Task Scheduler.

`The default location is C:\Users\<windows_username>\AppData\Local\Programs\Python\Python39\python.exe`

### Install 7-zip

7-zip is used by the script to zip the Valheim data files into one directory and make them smaller to conserve disk space: [7-zip download](https://www.7-zip.org/download.html)

I recommend installing it here `C:\Program Files\7-Zip`

* if you choose another installation location, update the value of `zip_software_location`.

## Find your Valheim installation location

Valheim stores the game files on your computer, as well as in SteamCloud.
You will need to find your local Valheim install location.

`The default location is C:\Users\<windows_username>\AppData\LocalLow\IronGate\Valheim`

* If your isntall location is different than the above, update the value of `valheim_directory` with the location.

### World and Character files

While adventuring in Valheim or building your base, the game will
regularly back up the files on your computer with the game data.
One file, the Player.log, is always being updated and it can't be backed up using the script. Don't worry, that isn't important for
restoring the game state. Due to this, we will grab the world
and character directories only.

## Create a backup directory

Make a directory on your computer where you want to store the backups.

I recommend `C:\Users\<windows_username>\valheim_backups`

* If you choose somewhere other than the above, you will need to update the value for `backup_dir`.

The backup files will be named `valheim_backup_` followed by the date and time of the backup.

## Additional changes to the script

### Updte your Windows Username

A lot of the file locations have the windows user name in them.

* Update the value of `user_name` with your Windows Username.

### Optional : Disable auto cleanup of stale backups

You can turn off the auto cleanup by doing the following:

* change the value of `auto_cleanup` from True to False

### Optional : Turn off using 7zip 

If you prefer to not install 7zip and are okay with your files being their normal size in the backup, you can disable use of 7zip by doing the following:

* change the value of `use_7zip` from True to False

## Test the script manually

I recommend testing the script manually before configuring windows task scheduler. This will help you make sure you've changed all the fields correctly and should give you your first backup.

## Configure Windows Task Scheduler to run your script

### Create a Task

To setup the script to run automatically, you can create a task. Do not use a "Basic Task".

Be sure to set the task to run even when the user is not logged in to ensure backups are run overnight and while you're away.

### Give your task a name

Something like myValheimBackup

### Add the Action

* Click the Actions tab in the Create Task window
* Set the value of Program/Script to the location for your Python3 installation
  * example: C:\Users\<windows_username>\AppData\Local\Programs\Python\Python39\python.exe
* Set the value of "Add arguments" to the full path to where you saved the python script
  * example: C:\Users\<windows_username>\backup\backup_valheim.py

### Set the Trigger

Use the Trigger to determine when to kick off the script and for how regularly to run the backup script. I recommend having the script run every hour since you can do a lot of base building in that amount of time.
