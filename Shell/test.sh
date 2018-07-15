#!/bin/bash
alo="a ba s a s"
select var in $alo
do
    case $var in
        1) echo 1
        ;;
        2|3) echo 2 or 3
        ;;
        *) echo default
        ;;
    esac
    break
done
