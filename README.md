# Fake XP start 

### Install requirements 
## To use in safemode install icewm 


'''sudo apt install icewm'''

## Put the winXPsound.mp4 in some place that you **remember** 
## The path in script **xp_sound.py** /home/kali/.icewm have to be changed to alctualy path.<h2>
### if .icewm doesnt exist. <h3>
´´´
mkdir .icewm
´´´
## Put the _themes/menu/icons/keys_ from _/usr/share/icewm/*_ <h2>
´´´
cp FakeXPstart/* .icewm/ 
´´´
´´´
chmod +x startup
chmod 777 startup
´´´
´´´
icewm -r 
´´´
´´´
service lightdm restart
´´´
### _**Finish!**_<h3>

