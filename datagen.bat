set pathsrc=.\data\dataset3
set pathdst=.\data\Train_data
del %pathdst%\pos\*
del %pathdst%\neg\*
for  %%i in (%pathsrc%\pos\*) do (copy %%i %pathdst%\pos\)
dir %pathdst%\pos /b > pos.txt
.\addarg.exe
del pos.txt
move pos_.txt %pathdst%\pos\pos.txt

for  %%i in (%pathsrc%\neg\*) do (copy %%i %pathdst%\neg\)
dir %pathdst%\neg /b/s > neg.txt
move neg.txt %pathdst%\neg

dir  %pathsrc%\pos