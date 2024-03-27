#!/bin/bash



case $(uname) in
    Linux)
        echo 'welcome linux'
        ls -al
        ;;
    Darwin)
        echo welcome macOS
        ls -al
        ;;
    Win32)
        echo welcome Windows
        dir /a
        ;;
    *) 
        echo "unknown OS: $(uname)"
esac