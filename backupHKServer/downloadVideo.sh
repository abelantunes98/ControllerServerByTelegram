youtube-dl -o "/home/mrrobot/videos/%(title)s.%(ext)s" $(cat url.txt)
ls /home/mrrobot/videos/ > /home/mrrobot/nome.txt
mv /home/mrrobot/videos/"$(cat nome.txt)" /home/mrrobot/videos/video.mp4
rm /home/mrrobot/url.txt
bash upVideo.sh
rm nome.txt
