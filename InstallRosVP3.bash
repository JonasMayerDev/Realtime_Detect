
#AI_Model_Creator; an easy to use AI cumputer vision model creator.
#Copyright (C) 2020  Jonas Mayer

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by    
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
#You can contact me by mail: bysuxaxofficial@gmail.com

cd $1

. $1/VirtualPython3/bin/activate
cd $1/VirtualPython3

PKGS="opencv-python==4.2.0.34 catkin_tools==0.4.5 Pillow==6.2.2 pandas==1.0.3 rospkg==1.2.4 catkin_pkg==0.4.16"

echo Check if all python libarys are installed...

pip3 install pip==20.0.2 setuptools==46.1.3

pip3 install ${PKGS}


pip3 uninstall -y pyyaml
pip3 install pyyaml==5.3.1

echo $1/VirtualPython3/lib/python3.6/site-packages
export PYTHONPATH=$PYTHONPATH:$1/VirtualPython3/lib/python3.6/site-packages
mkdir catkin_build_ws && cd catkin_build_ws
catkin config -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/x86_64-linux-gnu/libpython3.6m.so

catkin config --install

mkdir src
cd src
git clone -b melodic https://github.com/ros-perception/vision_opencv.git
cd ..

source /opt/ros/melodic/setup.bash
catkin build cv_bridge
source install/setup.bash --extend
mv install/lib/python3/dist-packages ../lib/python3.6/dist-packages
rm -rf ../catkin_build_ws
cd ..

pip3 install pyyaml==5.3.1
