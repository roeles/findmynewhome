set datafile separator ","
set grid
set title "Reistijd"
set xlabel "Departure time"
set ylabel "Time with traffic (minutes)"
#set cblabel "Route length"
set cblabel "Day of week, monday=0"
set palette model RGB
#set style fill transparent solid 0.2 noborder
plot input using ($1 + ($2/60)):(($3-(2*$4))/60):(($3+(2*$4))/60) with filledcurves title "95% confidence interval",\
input using ($1 + ($2/60)):(($3-(1*$4))/60):(($3+(1*$4))/60) with filledcurves title "66% confidence interval",\
input using ($1 + ($2/60)):($3/60) with lp lt 1 pt 7 ps 1.5 lw 3 title 'mean value',\
raw_input using ($5+($6/60)):($8/60):10 with lines palette title "Raw datapoints"
#raw_input using ($5+($6/60)):($8/60):($9/1000) with points palette title "Raw datapoints",\

