D:\opencv2\build\x64\vc14\bin\opencv_createsamples.exe -info data\Train_data\pos\pos.txt -vec pos.vec -num 219 -w 24 -h 24 
pause
del .\xml\*
D:\opencv2\build\x64\vc14\bin\opencv_traincascade.exe -data xml -vec pos.vec -bg data\Train_data\neg\neg.txt -numPos 190 -numNeg 140  -numStages 30 -w 24 -h 24
copy .\xml\cascade.xml .\