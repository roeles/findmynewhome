RAW_FILENAME="$1_$2_$3_$4_$5_$6_$7"
FILENAME=$(echo "$RAW_FILENAME" | sed -r 's/[^a-zA-Z0-9_]//g')
FILENAME_OUTPUT=$FILENAME.csv
FILENAME_ANALYSIS=$FILENAME.analysis.csv
FILENAME_PLOT=$FILENAME.analysis.svg
FILENAME_DEBUG=$FILENAME.debug

python TravelTime.py "$1" "$2" "$3" "$4" "$5" "$6" "$7" > $FILENAME_OUTPUT 
cat $FILENAME_OUTPUT | python TravelTimeAnalysis.py > $FILENAME_ANALYSIS
gnuplot -e "set terminal svg size 1920 1080; set output \"$FILENAME_PLOT\"; input=\"$FILENAME_ANALYSIS\"; raw_input=\"$FILENAME_OUTPUT\"" TravelTimeAnalysis.gnuplot
