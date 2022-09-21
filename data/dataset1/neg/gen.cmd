set n=30
:loop
set /a n+=1
copy n3.png n%n%.png 
if %n%==300 exit
goto loop