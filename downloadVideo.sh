youtube-dl -o "/usr/bin/usr/tel/videos/%(title)s.%(ext)s" $(cat url.txt)
ls /usr/bin/usr/tel/videos/ > nome.txt
mv /usr/bin/usr/tel/videos/"$(cat nome.txt)" /usr/bin/usr/tel/videos/video.mp4
rm /usr/bin/usr/tel/url.txt
bash upVideo.sh
rm nome.txt
