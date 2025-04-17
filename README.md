# Fake XP start 
<br>
Install requirements <br><br>
To use in safemode on startup install icewm. 
<br>

`sudo apt install icewm`

<br>
Put the winXPsound.mp4 in some place that you _**remember**_; like mv winXPsound.mp4 actualy_path/. 
The path in script **xp_sound.py** /home/kali/.icewm have to be changed to actualy path.<br><br>
<h3> if .icewm doesnt exist.
<br>
in home<br>
  
`mkdir .icewm`
<br><br>


`cp FakeXPstart/* .icewm/`
<br>
`chmod +x startup`<br>
`chmod 777 startup`
<br><br>

`icewm -r`


`service lightdm restart`
<br><br>
if you want a winXP theme in icewm: [github: spartrekus](https://github.com/spartrekus/icewm-xp) 
<br>
### _**Finish!**_<h3>

