# TelePyBot : Telegram Channel Downloader Bot
# Public Telegram Channel based Media\Ebook library

*This project was to create a self hosted pdf library based on the pdf and news sent on the telegram channel  and there is no need of any external service dependencies.
The script downloads the media that is sent in the channels and saves it in the specified location. However it also check for the media content that's already been downloaded to avoid duplicate files.
I run it on my Raspberry Pi 3 based NAS and the media\books can be viewed from any device in the home.
The script was developed on windows and is being used on Linux(Debian)*

#### Installation Steps:
1)	To start with you have to create your own telegram app config and get token thru https://my.telegram.org/auth (you can google it)
2)	Update the  script with **Telegram Username, App api_id, App api_hash** from step 1
3)	Make sure you are using **Python3** and install following modules
------------
pip3 install cryptg
------------
pip3 install telethon
------------
pip3 install asyncio
------------
4)	Update the Channel name **without @** against : **channel_name**
5)	Mention the path against : **download_path**
6)  Number of media files to be downloaded can be restricted using : **msg_limit **
7)	Place it in the accessible folder with required permissions.
8)	Execute it using a crontab and the media will be downloaded as per schedule.

###### Note: *Since I have limited storage I have a cron job to delete the files in 7 days.*
