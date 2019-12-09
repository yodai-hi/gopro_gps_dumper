#!/bin/sh
#GOPRO2GPX_FILE=./gps_dumper/bin/gopro2gpx
GPMD2GPX_FILE=./gps_dumper/bin/gpmd2csv

if [ $# -lt 1 ]; then
    echo "Usage: $0 <input_movie_file> [<output_dir>]"
    exit 1
fi

IN_FILE_EXT=$1
IN_FILE=${IN_FILE_EXT##*/}
IN_BASE=${IN_FILE%.*}
OUT_DIR=${IN_FILE_EXT%/*}

if [ $# -ge 2 ]; then
    OUT_DIR=$2
fi

ffmpeg -y -i "${IN_FILE_EXT}" -codec copy -map 0:3 -f rawvideo "${OUT_DIR}/${IN_BASE}.bin"
#${GOPRO2GPX_FILE} -i "${OUT_DIR}/${IN_BASE}.bin" -o "${OUT_DIR}/${IN_BASE}.gpx"
${GPMD2GPX_FILE} -i "${OUT_DIR}/${IN_BASE}.bin" -s ayg

