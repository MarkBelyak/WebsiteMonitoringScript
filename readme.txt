First run trafficgen, then collector, then plotFiles, then plot.sh

I think my results are overall ok, but because I used a random int so all 3 cases are generally pretty equal. I think I should have made it so that it creates a random int between 0-8, where 0-1 would be 404 errors, 2-4 would be 500 errors and 5-8 would be 200s. This would my my data more readable, unfortunatly I don't have the time to run this for another hour.

When I first thought I finished with this assignment I had a weird issue where I always got the same rps. 
It was weird because I recalculated the rps every second, but somehow it was always the same.
After trying a few different things, something really minor fixed it. Before, I was using an if statement
to make sure I hit both 500 and 404 errors. it was just (x % (random number) == 0) and I thought that would
be good enough. I changed it to actually just do a random int and suddenly my rps issue was completely fixed. I'm still not really sure why it didn't work initially.

overall I think my code is ok. I could have done collector with regex instead of splits but I don't think it was a big difference. I'm not really sure if the flags work 100% correctly, but at the very least the defaults do. I think that I could cut down plot.py a little bit because there is some repeated code.

I'm not sure if the try except pass thing is allowed, but I didn't know how else to make the program not crash when accessing the /fail and 404 pages. 

I also had a fun issue with try/except. I was putting code after the urllib2 call that threw exceptions, so it never actually ran. It took me a while to remember that. 

Making sure trafficgen did something the correct amount of times per second:
http://code.activestate.com/recipes/413137-call-a-functionmethod-x-times-per-second/

Option parser:
https://docs.python.org/2/library/optparse.html

try except:
https://docs.python.org/3/tutorial/errors.html

urllib2:
https://docs.python.org/2/library/urllib2.html

random.uniform:
https://docs.python.org/2/library/random.html

I plotted the graph with 

plot '500output.txt' with lines, '404output.txt' with lines, '200output.txt' with lines
