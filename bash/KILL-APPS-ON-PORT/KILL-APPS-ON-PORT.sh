# script name : kill-all-apps-on-port.sh
#!/bin/bash
timestamp=$(date +"%d%m%Y%H%M%S") 
filename="killed_pids_$timestamp.log"
port=$1 

# pid_list=$(netstat -ano | findstr ${port})
netstat -ano | findstr ${port}>list_off_apps.txt


echo "list_off_apps :">"$filename"
cat list_off_apps.txt 

list_of_pids=$(awk '{print $5}' list_off_apps.txt | sort -u)
echo "list_off_pids :"
echo $list_of_pids

echo "deleting   pids now ...  "
for pid in $list_of_pids; do
    echo "Killing process with PID: $pid"
    kill -9 $pid >> killed_pids.log
done



# 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