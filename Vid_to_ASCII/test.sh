PS1=""

echo "link" && read link

#fname=$(youtube-dl --get-filename -o "%(title)s" $link)
dirname=$(youtube-dl --get-filename -o "%(title)s" $link| sed 's/[^a-zA-Z0-9]//g')
mkdir created/$dirname
youtube-dl $link -o $dirname
vid_ext=$(dir $dirname.* |cut -d"." -f2)
ffmpeg -i $dirname.* -q:a 0 -map a created/$dirname/$dirname.mp3
#get 10 frames per second and create it in "created/$dirname/"
ffmpeg -i $dirname.* -r 5 -f image2 created/$dirname/image-%4d.jpeg

#play the video sound
lame --decode created/$dirname/$dirname.mp3 - | play - &

#transforms images to ASCII_art
for f in created/$dirname/*.jpeg; do jp2a -z --colors $f &&sleep 0.2 &&clear; done

source ~/.bashrc
