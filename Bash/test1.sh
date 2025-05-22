#!/bin/bash
line="------------------------------"
echo "Starting at: $(date)"; echo $line  

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)" echo $line

python_path=$(whereis python3)
echo "Python is installed at: $python_path"

if grep "127.0.0.1" /etc/hosts; then
	echo "Exists"
else
	echo "Doesnt exist"
fi

if [ -n "$PATH" ]; then echo  "Your path is not emptu"; fi

n=1
while [ $n -le 5 ]; do
  echo "Iteration number $n"
  ((n+=1))
done


for fruit in peach orange apple; do
	echo "I like $fruit"
done

for logile in /var/log/*log; do
	echo "processing: $logfile"
	tail $logile|cut -d' ' -f3-
done
