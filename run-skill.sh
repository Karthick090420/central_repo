#!/bin/bash

skill_name=$1
input_content=$2

prompt=$(cat skills/$skill_name.md)

echo "$input_content" | claude -p "$prompt"