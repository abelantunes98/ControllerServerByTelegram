youtube-dl -o "/usr/games/usr/tel/videos/%(title)s.%(ext)s" $(cat url.txt)
ls /usr/games/usr/tel/videos/ > nome.txt
mv /usr/games/usr/tel/videos/"$(cat nome.txt)" /usr/games/usr/tel/videos/video.mp4
rm /usr/games/usr/tel/url.txt
bash upVideo.sh
