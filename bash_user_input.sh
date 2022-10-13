#!/bin/bash

echo "What is your user name?"
read USER_NAME

if [ "$USER_NAME" == "Dave" ]
then
	echo "Get off my computer Dave!"
elif [ "$USER_NAME" == "Angela" ]
then
	echo "I know it's you Dave! Go away!"
else
	echo "Come on in!"
fi

CREDITS=120

if [ $CREDITS -ge 120 ]
then
	echo "You have enough credits to graduate!"
else
	echo "You don't have enough credits to graduate!"
fi
