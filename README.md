# Realtime_Detect v 0.0.1 (Pre-Alpha)
Diese Software soll ein easy to use (, deutschsprachiges) KI-Model ausführungs-programm darstellen, welche über ROS eine art Schnittstelle darstellt. Diese Software funktioniert zumindest zurzeit ausschließlich mit Models des [AI_Model_Creator](https://github.com/BySuxax/AI_Model_Creator). Der [AI_Model_Creator](https://github.com/BySuxax/AI_Model_Creator) installiert Realtime_Detect normalerweise automatisch. <br>
Wenn aber Fehler bei der Installation auftreten oder sonst etwas mit dieser Software getan werden soll, kann dieses Programm auch manuell installiert werden.<br><br>

Veröffentlicht unter der GPL v3:<br>
AI_Model_Creator; an easy to use AI cumputer vision model creator.<br>
Copyright (C) 2020  Jonas Mayer<br>
<br>
This program is free software: you can redistribute it and/or modify<br>
it under the terms of the GNU General Public License as published by 
the Free Software Foundation, either version 3 of the License, or<br>
(at your option) any later version.<br>

This program is distributed in the hope that it will be useful,<br>
but WITHOUT ANY WARRANTY; without even the implied warranty of<br>
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the<br>
GNU General Public License for more details.<br>

You should have received a copy of the GNU General Public License<br>
along with this program.  If not, see <https://www.gnu.org/licenses/><br>
You can contact me by mail: bysuxaxofficial@gmail.com<br>
<br><br>


**Kompatibilität** | **Sollte Funktionieren** | **Tut auf frischem System (getestet)**
------------ | ------------- | -------------
Ubuntu 18.04.4| :heavy_check_mark: |:heavy_check_mark:	|
Linux Mint| :heavy_check_mark:	| :white_check_mark:	|
Debian basierte Linux Distros| :heavy_check_mark:| :x:|
Andere Linux Distros| :x: | :x: |
Windows| :x: | :x: |
Mac | :x: | :x: | <br>



### Um Realtime_Detect ohne AI_Model_Creator zu installieren und ein Launchfile zu generieren, musst du folgendes tun:


1. Installiere ROS Melodic wie hier beschrieben: [ROS Melodic Installieren](http://wiki.ros.org/melodic/Installation/Ubuntu)


1. Du solltest sicher sein, dass der Command `source /opt/ros/melodic/setup.bash` in jedem genutztem Terminal ausgeführt wird!


1. Nun können sie das Git Repository clonen: <br>
Dazu bietet es sich an, dass ein **neuer Ordner erstellt wird** in welchen sie wechseln und den Command ausführen (!Stellen sie sicher, dass der Ordner, in dem sie den Command ausführen, leer ist!):  <br>
`git clone https://github.com/BySuxax/Realtime_Detect.git` <br>
Es kann sein, dass es nötig ist, erst Git zu installieren: `sudo apt install git`


1. Als nächstes können sie, um das Programm zu starten **UND AUTOMATISCH GEBRAUCHTE LIBRARIES ZU INSTALLIEREN (Alle automatisch installierten Libraries stehen im File: LicenseInformation.txt)**, folgenden command ausführen: <br>**(Ich übernehme keine Haftung für Systemschäden, Dateiverlust oder ähnlichem. Es werden durch python Libraries, Programmeigene Ordner gelöscht. Eine Fehlfunktion kann nicht ausgeschlossen werden!)** <br> `python3 Realtime_Detect/startAPI.py` <br> 
**!! Achten sie auf die Konsole! Es kann sein, dass sie ihr Root Passwort eingeben müssen um die Libraries zu installieren !!** <br>Es sollte sich daraufhin ein Fenster zur Installationshilfe der ROS-libraries öffnen.

1. Sie sollten einfach auf "Automatisch installieren" drücken. <br> --> **Es werden automatisch Libraries installiert. Achten sie auf die Konsole! Es kann sein, dass sie ihr Root Passwort eingeben müssen um die Libraries zu installieren!** <br>
Wenn sie auf weiter drücken müssen die normalerweise automatisch installierten (durch das Drücken des "Automatisch installieren" Buttons) Libraries installiert sein!

1. Geben sie einen Namen ein unter dem das Launchfile gespeichert wird. ***Dann drücken sie auf Save Name!*** (Es soll keine Endung wie .launch enthalten sein) <br> 

1. Wählen sie ein Model. Das Model **muss** im Models-Ordner liegen, welcher im Hauptordner (Ein Ordner über Realtime_Detect clone Ordner) angelegt sein sollte! In diesem Model-Ordner **muss** ein Ordner mit dem Modelnamen vorhanden sein, inwelchem die Model-Datei mit dem Namen: Modelname".pt" liegt. **Es muss ein Model des AI_Model_Creators sein!**

1. Als nächstes muss noch die Kamera ausgewählt werden, die als Input für die Bilderkennung genutzt wird. Die Kamera muss dabei als Bild Stream unter /dev/ angelegt sein und den namen "video*NUMMER*" tragen.

1. Wenn sie nun auf Weiter drücken wird, falls noch nicht geschehen, ein ros_ws erstellt. Außerdem wird nach ihren Einstellungen ein personalisiertes Launchfile erstellt. 

1. Sie können nun das Programm schließen.

### Um nun auch dieses Launchfile auszuführen muss folgendes getan werden:
 1. Sie müssen sicherstellen, dass das Terminal, das sie benutzen, mit ROS und ihrem ros_ws "bekannt" gemacht wurde:  <br>
 ` source /opt/ros/melodic/setup.bash `<br>` source Realtime_Detect/ros_ws/devel/setup.bash ` <br> Wenn sie wollen können sie auch diese beiden Befehle zur .bashrc in ihrem Home-Directory hinzufügen.

1. Jetzt können sie die Bilderkennung ganz einfach mit diesem Command starten: <br> `roslaunch realtime_detect IHR_GEWÄHLTER_NAME.launch` <br> Ersetzen sie einfach noch IHR_GEWÄHLTER_NAME mit dem Namen, den sie beim Launchfile generieren angegeben haben.

 1. Die Ergebnisse können sie jetzt über das ROS-Topic `/classified_Name` auslesen. Wie sie dies in verschiedenen Programmiersprachen tun können, wird hier erklärt: <br> [Python](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29) <br>
 [C++](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29)
 <br> Sie können auch einfach über den folgenden Befehl die Ausgaben in der Konsole einsehen: <br>
 `rostopic echo /classified_Name`
 
 Wenn es irgendwelche Schwirigkeiten oder Fehler gibt, dann schreiben sie gerne einen Kommentar, um das Programm zu verbessern und ihnen weiterzuhelfen. Meine E-Mail: bysuxaxofficial@gmail.com

All automatically installed Libraries are mentioned in "LicenseInformation.txt"




