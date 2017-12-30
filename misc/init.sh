#!/bin/bash

set -e

SCRIPT_PATH=$(readlink -f $0)
SCRIPT_BASEDIR=`dirname $SCRIPT_PATH`

APP_BASEDIR=$HOME/apps/git

mkdir -p $APP_BASEDIR
rsync -av $SCRIPT_BASEDIR/* $APP_BASEDIR/

files=("git" "git-receive-pack" "git-shell" "git-upload-archive" "git-upload-pack")
for file in ${files[*]}; do
  if [ ! -f "${HOME}/local/bin/${file}" ]; then
    ln -s ${APP_BASEDIR}/bin/${file} ${HOME}/local/bin/${file}
  fi
done

