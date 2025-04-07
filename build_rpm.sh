#!/bin/bash

# Getting the latest *.spec file from the github repo:
wget https://github.com/Slookeur/atomes-rpm-build/raw/main/Fedora/atomes.spec

# Getting the latest GNU tarball for the github repo:
version=1.1.15
wget https://github.com/Slookeur/atomes-GNU/archive/refs/tags/v$version.tar.gz
mv v$version.tar.gz $HOME/rpmbuild/SOURCES/

# Building the source rpm:
rpmname=`rpmbuild -bs atomes.spec|grep 'rpm'|awk '{printf $NF}'`

# Local build
# fedpkg --release f36 local

# Fedora review
# On the bug [https://bugzilla.redhat.com/show_bug.cgi?id=2130607]
# fedora-review -b 2130607

# localy
# cp $rpmname .
# fedora-review -n atomes

# Koji build
koid=`klist|grep slook@FEDORAPROJECT.ORG`
if [ -z "$koid" ]; then
  fkinit -u slook
fi
koji build --scratch rawhide $rpmname
