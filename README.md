# README

## 
Author: Peter Marion
CIS 1051
Final Project
Autocheckin

Demonstration Link: https://www.youtube.com/watch?v=1FYHkfVFb6M&ab_channel=PeterMarion

## The Problem
I work at a karate studio which uses paper attendance cards and an online tracking system. The students pull their cards from the box at the beginning of class, we mark them, and then must individually log them all into our online system. This can be tedious, as we average over 100 students per night, the online system is slow, and the earlier we get it done the earlier we can go home after a long day. 

## The Solution
Scan the cards, use PyTesseract to pull the names off of the cards and store them in lists separated by class. Then, run a script to log into the online system, navigate to the checkin page, and input every name.

## Successes
The program scans attendance cards and adds them to class attendance lists as specified by the user.
The program opens a chrome window and logs in to our online system before navigating to the checkin page.
The program iterates through the list of students and inputs them into the system. 

## Shortcomings
The PyTesseract library can be finicky, and sometimes does not accurately pick out student names. I was unable to add functionality to edit or remove faulty reads. 
The program cannot navigate between karate classes itself, the user must manually choose which day/class they would like to submit their attendance lists to. 

## The Future
I hope to spend more time refining this project and fixing the shortcomings. This definitely has a lot of room for improvement, but for the time I was able to commit to this project I am not disappointed in the least. Also note, I removed the login information from the submitted copy of my project, for obvious reasons. If you would like a demonstration with the login I am happy to join a zoom call to show you.
