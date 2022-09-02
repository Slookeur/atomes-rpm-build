#!/bin/bash

VERSION="1.1.0"
rm -rf atomes-$VERSION
tar -zxf atomes-$VERSION.tar.gz atomes-$VERSION
fedpkg --release f36 local

