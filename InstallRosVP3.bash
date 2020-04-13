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
