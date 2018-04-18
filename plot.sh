#plot using gnu
gnuplot -e "plot '200output.txt' with lines, '404output.txt' with line, '500output.txt' with lines; set title 'Assignment 4'; set xlabel 'Time'; set ylabel 'RPS (1-minute rate)'; set term png; set output 'plot.png' ; replot"

#call delete file
rm "200output.txt"
rm "404output.txt"
rm "500output.txt"

