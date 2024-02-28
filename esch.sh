#!/bin/bash

# file the file does not exist or is not a markdown file, exit
if [ ! -f $1 ] || [[ $1 != *.md ]]; then
  echo "File does not exist or is not a markdown file"
  exit 1
fi

# get header from markdown file (between first and second ---)
header=$(awk '/^---$/{c++;if(c==2)exit} c' $1 | sed 1d)
DIR="$( cd "$( dirname "$(realpath "${BASH_SOURCE[0]}")" )" &> /dev/null && pwd )"

# if type is not specified, default to "page"
if [[ $header != *type* ]]; then
  header="type: paper\n$header"
fi

# if there is no date, default to today
if [[ $header != *date* ]]; then
  header="date: $(date +%Y-%m-%d)\n$header"
fi

# use src/{type}.sh to generate the file
type=$(echo -e "$header" | awk '/^type:/{print $2}')
src=src/$type.sh

# call the src file
"$DIR/$src" $1