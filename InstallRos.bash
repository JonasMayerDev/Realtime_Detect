#!/bin/bash

filepath=$1
echo $filepath
PKGS=(python-catkin-tools)
  
echo Check if Everything reqired is installed


for ((i=0 ;i < ${#PKGS[@]};i++))
do
    
    PKG_OK=$(dpkg-query -W --showformat='${Status}\n' ${PKGS[$i]} |grep "install ok installed") 
    echo Checking for ${PKGS[$i]}: $PKG_OK
    if [ "" == "${PKG_OK}" ]; then
    echo "Package is not installed. Install: ${PKGS[$i]}"
    sudo apt-get --force-yes --yes install ${PKGS[$i]}
    fi
    
done



