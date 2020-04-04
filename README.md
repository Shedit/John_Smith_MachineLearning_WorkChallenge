# Repr Machine Learning Work Challenge 

####General: 

This is a work challenge for a summer internship at Repr, given the following instructions: 

Your task is to visualize labour / employment data ((https://www150.statcan.gc.ca/n1/daily-quotidien/190308/dq190308a-eng.htm) for Canada by province and industry for the last 5 years which should be pivotable by demographic *(age, sex, ethnicity and industry / sector)*.

Use open skills data and job titles using this link  and visualize a mashup correlating skills and jobs to industry and employment and provide a sample for evaluation.

Suggest in detail, how you would train these two data sets over time and what machine learning algorithm you would use to make the data "smarter" over time.

####Submission Process: 

Please begin by creating a Project. Your Project should contain both the final output and a Github link to your source code. Please name all of your files and documents using the following convention:
John_Smith_MachineLearning_Nameofyourfile. Once it is completed, you will be able to submit it here to the Work Challenge. 


####Evaluation Criteria: 

25% on your approach to tackling the problem and the steps you took to get to your solution and final deliverable
25% on how well you used various tools & processes to tackle the challenge
50% on the final solution and output of your challenge

## Introduction 

To begin with lets state what is needed to be done in a clear and understandable way: 

1. Collect Data 
2. Process collected Data 
3. Present valuable information by comparing Canada's Labour Force Survey (LFS) Data with given Open skills data and job titles to evaluate accuracy of some kind. 
4. Obtain valuable insights depending on goals. 




## 1. Data Collection 

Given links:

- Canada LFS Data hub: https://www150.statcan.gc.ca/n1/daily-quotidien/190308/dq190308a-eng.htm[1]
- Open Skills Data, named job_skills.csv  (Link were given within the embedded environment for the challenge)


###1. Collect LFS Data between 2014 - 2019 by province and industry with age, sex, etnicity and industry/sector 

Given link above, gave info about multiple tables that were updated monthly and no redirection into where to collect data between 2014 and 2019. It also have data grouped by etiher age & sex (Age Group and Sex), industry & sector (Class of Worker and Industry) or Province as well as a combination of any of them. There are no tables within the soruce that mentions etnicity. [1]

Found through extensive searches an archive with all the monthly repors of LFS (https://www150.statcan.gc.ca/n1/en/catalogue/71-001-X), However none of the data is combined. To get an overview of 

More reserach also points to that the LFS is currently affected by COVID-19 and is not currently being updated with surveys, only other less effective methods such and by phone or online (https://www.statcan.gc.ca/eng/survey/household/3701). 


