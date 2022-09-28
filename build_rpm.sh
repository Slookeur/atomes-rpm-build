#!/bin/bash

VERSION="1.1.5"
if [ -d atomes-$VERSION ]; then
  rm -rf atomes-$VERSION
fi
tar -zxf atomes-$VERSION.tar.gz
fedpkg --release f36 local

