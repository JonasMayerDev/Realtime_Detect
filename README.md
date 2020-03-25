# realtime_detect
realtime ai detection: select your model and start realtime detection. the output can be read with ROS!

**Compatibilität** | **Sollte Funktionieren** | **Tut auf frischem System (getestet)**
------------ | ------------- | -------------
Ubuntu 18.04.4| :heavy_check_mark: |:heavy_check_mark:	|
Linux Mint| :heavy_check_mark:	| :white_check_mark:	|
Debian basierte Linux Distros| :heavy_check_mark:| :x:|
Andere Linux Distros| :x: | :x: |
Windows| :x: | :x: |
Mac | :x: | :x: |

### Um realtime_detect allein zu installieren musst du folgendes tun:

1. Installiere ROS wie hier beschrieben: [ROS_Installieren](http://wiki.ros.org/melodic/Installation/Ubuntu)

1. Du solltest sicher sein, dass der command `source /opt/ros/melodic/setup.bash` in jedem genutztem Terminal ausgeführt wird!

1. Nun können sie das git reposetory clonen: <br>
Dazu bitet es sich an, dass ein **neuer Ordner erstellt wird** in welchen sie wechseln und den command ausführen:  <br>
`git clone https://github.com/BySuxax/realtime_detect.git` <br>
Es kann sein, dass es nötig erst git zu installieren: `sudo apt install git`


1. Als nächstes können sie um das Programm zu starten **UND AUTOMATISCH GEBRAUCHTE LIBRARIES ZU INSTALLIEREN** folgenden command ausführen: <br>**( Ich übernehme keine Haftung für Systemschäden, Dateiverlust oder ähnlichem. Es werden durch python liberys programmeigene Ordner gelöscht. Eine Fehlfunktion kann nicht ausgeschlossen werden!)** <br> `python3 realtime_detect/startAPI.py` <br> 
**!! Achten sie auf die Console! Es kann sein, dass sie ihr root password eingeben müssen um die Libraries zu installieren !!** <br>Es sollte sich daraufhin ein Fenster zur Installationshilfe der ROS libraries öffnen.

1. Sie sollten einfach auf automatisch installieren drücken. <br> --> **Es werden automatisch Libraries installiert. Achten sie auf die Console! Es kann sein, dass sie ihr root password eingeben müssen um die Libraries zu installieren! ** <br>
Wenn sie auf weiter drücken müssen die normalerweise automatisch installierten Libraries schon installiert sein!

