# realtime_detect
Diese Software soll ein easy to use (, deutschsprachiges) KI-Model ausführungs programm darstellen, welche über ROS eine art Schnittstelle darstellt. Diese Software funktioniert zumindest zur Zeit ausschließlich mit Models des [AI_Model_Creator](https://github.com/BySuxax/AI_Model_Creator). Der [AI_Model_Creator](https://github.com/BySuxax/AI_Model_Creator) installiert realtime_detect normalerweise automatisch. <br>
Wenn aber Fehler bei der Installation auftreten oder sonst etwas mit dieser Software getan werden soll, kann dieses programm auch manuell installiert werden.

**Compatibilität** | **Sollte Funktionieren** | **Tut auf frischem System (getestet)**
------------ | ------------- | -------------
Ubuntu 18.04.4| :heavy_check_mark: |:heavy_check_mark:	|
Linux Mint| :heavy_check_mark:	| :white_check_mark:	|
Debian basierte Linux Distros| :heavy_check_mark:| :x:|
Andere Linux Distros| :x: | :x: |
Windows| :x: | :x: |
Mac | :x: | :x: | <br>



### Um realtime_detect ohne AI_ModelCreator zu installieren und zu ein Launchfile zu generieren musst du folgendes tun:


1. Installiere ROS wie hier beschrieben: [ROS_Installieren](http://wiki.ros.org/melodic/Installation/Ubuntu)


1. Du solltest sicher sein, dass der command `source /opt/ros/melodic/setup.bash` in jedem genutztem Terminal ausgeführt wird!


1. Nun können sie das git reposetory clonen: <br>
Dazu bitet es sich an, dass ein **neuer Ordner erstellt wird** in welchen sie wechseln und den command ausführen:  <br>
`git clone https://github.com/BySuxax/Realtime_Detect.git` <br>
Es kann sein, dass es nötig erst git zu installieren: `sudo apt install git`


1. Als nächstes können sie um das Programm zu starten **UND AUTOMATISCH GEBRAUCHTE LIBRARIES ZU INSTALLIEREN** folgenden command ausführen: <br>**( Ich übernehme keine Haftung für Systemschäden, Dateiverlust oder ähnlichem. Es werden durch python liberys programmeigene Ordner gelöscht. Eine Fehlfunktion kann nicht ausgeschlossen werden!)** <br> `python3 Realtime_Detect/startAPI.py` <br> 
**!! Achten sie auf die Console! Es kann sein, dass sie ihr root password eingeben müssen um die Libraries zu installieren !!** <br>Es sollte sich daraufhin ein Fenster zur Installationshilfe der ROS libraries öffnen.

1. Sie sollten einfach auf "Automatisch installieren" drücken. <br> --> **Es werden automatisch Libraries installiert. Achten sie auf die Console! Es kann sein, dass sie ihr root password eingeben müssen um die Libraries zu installieren!** <br>
Wenn sie auf weiter drücken müssen die normalerweise automatisch installierten (durch das drücken des "Automatisch installieren" buttons) Libraries installiert sein!

1. Geben sie einen Namen ein unter dem das Launchfile gespeichert wird. ***Dann drücken sie auf Save Name!*** (Es darf keine Endung wie .launch enthalten sein) <br> 

1. Wählen sie ein Model. Die Model-Datei **muss** im Models-Ordner liegen, welcher im Hauptordner (Ein Ordner über Realtime_Detect) angelegt sein sollte!  **Es muss ein Model des AI_ModelCreators sein!**

1. Als nächstes muss noch die Kamera ausgewählt werden die als Input für die Bilderkennung genutzt wird. Die Kamera muss dabei als Bildstream unter /dev/ angelegt sein und den namen video*NUMMER* tragen.

1. Wenn sie nun auf Weiter drücken wird, falls noch nicht geschehen, ein ros_ws erstellt. Außedem wird nach ihren Einstellungen ein personalisiertes Launchfile erstellt. 

1. Sie können nun das Programm schließen.

### Um nun auch dieses Launchfile auszuführen muss folgendes getan werden:
 1. Sie müssen sicherstellen, dass das Terminal, das sie benutzen mit ROS und ihrem ros_ws "bekannt" gemacht wurde:  <br>
 ` source /opt/ros/melodic/setup.bash `<br>` source Realtime_Detect/ros_ws/devel/setup.bash ` <br> Wenn sie wollen können sie auch diese beiden Befehle zur .bashrc in ihrem Home-Directory hinzufügen.

1. Jetzt können sie die Bilderkennung ganz einfach mit diesem Command starten: <br> `roslaunch Realtime_Detect IHR_GEWÄHLTER_NAME.launch` <br> Ersetzen sie einfach noch IHR_GEWÄHLTER_NAME mit dem Namen, den sie beim Launchfile generieren angegeben haben.

 1. Die Ergebnisse können sie jetzt über das ROS Topic `/classifiedName` auslesen. Wie sie dies in verschiedenen Programmiersprachen tun können wird hier erklärt: <br> [Python](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29) <br>
 [C++](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29)
 <br> Sie können auch einfach über den folgenden Befehl die Ausgaben in der Konsole einsehen: <br>
 `rostopic echo /classifiedName`
 
 Wenn es irgendwelche Schwirichkeiten oder Fehler gibt, dann schreiben sie gerne einen Kommentar um das Programm zu verbessern und ihnen weiterzuhelfen.






