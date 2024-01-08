# todoify, the first most project that i publishing on internet for opensource
Hello this is a python project that can get input from user which is their **TODO NAME**,**DUE DATE**,**DUE TIME** and store it in a local datafile(logs.txt)

what does this python program does?
ans: As I said before it stores the users data by getting input fronm themselves and if the due time matches the current time of their local area , it just pops up the notepad.exe and start writing on how to complete the 
task more efficiently like recommendations using **OPEN-AI** api uses engine gpt-turbo-3.5 to write output.

USES:
tkinter framework
pyautogui
openai(!Latest version)

Bugs:
There are few bugs in the program involves..
1.Date is not checked which is the program will run even if the user gives past date
2.For the first time running the python file.The **logs.txt** will be empty because of that the program will cause a exception during runtime maybe I fixed it if reading this late.
3.The program will run only the first most todo of the program and not upcoming lines or dues

i'm leaving this program for further development which may enriches its usage
