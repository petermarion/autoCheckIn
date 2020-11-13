# Proposal

## What will (likely) be the title of your project?

autoCheckin

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

A script which will streamline the attendance check in process for my karate studio

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

My project will consist of 3 parts:
1. Allow user to make a list of students for each class by taking pictures of the attendance cards
2. Log in to karate studio's management system PerfectMind and go to check in page
3. Auto check in the list of names into their respective classes in the system

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

Not applicable

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

Not applicable

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

1. Log into perfectmind with a script
2. Take pictures of attendance cards and try to extract the student's name from the picture
3. Input list of names into input field on check in page

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

1. Log into perfectmind with a script
2. Take pictures of the cards with minimal or no issues with extracting the student's name
3. Input names into input field and wait to input the next name until the system completes their login (usually takes a few seconds)


### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

1. Log into perfectmind with a script
2. Take pictures of the cards with minimal to no issues with extracting the student's name
3. Input names into input field and wait to input the next name until the system completes their login (usually takes a few seconds)
4. Takes lists for ALL karate classes and inputs them into their respective classes in one run instead of manually switching to the next karate class and running the script individually for each class. 
5. Provide the user a list of names which FAILED to find a match in the system (sometimes there are discrepancies between names on the attendance cards and names in the system)

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

1. Login script: I will have to research how to automate logging in to a page
2. Tesseract: The library I intend to use to extract student's names from the pictures of their attendance cards
3. Website navigation: I will have to learn how to use a python script to navigate to different pages on a website so user doesn't have to manually switch to the next karate class checkin page.
