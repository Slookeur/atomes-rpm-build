#!/bin/bash

# Getting the latest *.spec file from the github repo:
wget https://github.com/Slookeur/Atomes-rpm-build/raw/main/Fedora/atomes.spec

# Local build
fedpkg --release f36 local

# Koji build
version=1.1.7
wget https://github.com/Slookeur/Atomes-GNU/archive/refs/tags/v$version.tar.gz
mv v$version.tar.gz $HOME/rpmbuild/SOURCES/
rpmname=`rpmbuild -bs atomes.spec|grep 'rpm'|awk '{printf $NF}'`
koid=`klist|grep slook@FEDORAPROJECT.ORG`
if [ -z "$koid" ]; then
  fkinit -u slook
fi
koji build --scratch rawhide $rpmname
