#!/bin/bash

echo Hangman Game with only UNIX Commands

secret_word=astroinformatics
curr_word = "_" * ${#secret_word}

read -p "Guess a Letter: " guess

if $guess in $secret_word:
    echo "$guess appeared in the secret word"
    curr_word = ${}
