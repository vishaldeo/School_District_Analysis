# Schol_District_Analysis

## Project Overview


The School Board Chairperson having a project to analysis various performance metrics of the school district and schools. We have provided the below reports in `Phase 1` .

| School Data Anaysis |
| ----------- |  
 | The district summary   
 | The school summary   
 | The top 5 performing schools, based on the overall passing rate
 | The bottom 5 performing schools, based on the overall passing rate
 | The average math score for each grade level from each school
 | The average reading score for each grade level from each school
 | The scores by school spending per student
 | The scores by school size
 | The scores by school type


The project was successful and after rewiewing the data provided for the analysis School Board found the anomalies in the data being provided in the `students_complete.csv` file. For school `Thomas High School` , the reading and math score was altered for nine grade student. For this new analysis we need to exclude these students.

`Phase 2`
The School Board like to analysis  the impact of changing all the grade 9 math and reading scores at Thomas High School to Nan with the previous report while including those students.

## Resources

| Resource & Software |      
| ----------- |  
|  schools_complete.csv       
| students_complete.csv   
| Jupyter Notebook   
| Python   
| Pandas
| Numpy

## Deliverables

| Deliverables      | Description |
| ----------- | ----------- |
| Deliverable 1      | Replace ninth-grade reading and math scores       |
| Deliverable 2       | Repeat the school district analysis        |
| Deliverable 3       | A written report for the school district analysis        |




## Analysis Results

## Impact on School District Summary Analysis

### District Analysis - Phase 1 

<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189275413-08563ffa-a331-4505-80f1-bb543de775db.png">

### District Analysis - Phase 2 
<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189275712-1c871790-8e93-4053-9f42-1ab95f7cfbe7.png">

- When we didn't consider the 9th grade Math and reading result for Thomas High School, it has minimal impact on the district summary report. As we have only 461 students out of 39170 ( Close to ~1% of total students ) . The impacted resuluts are shown in the `RED` box on the image. 

### School Analysis   - Phase 1 
<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189277141-fba812a2-0ac8-45a0-8a66-9f43c462829f.png">

### School Analysis - Phase 2 
<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189277219-246a8478-3013-489b-8de1-3719d15adb34.png">

* Due to the anamolies in 9th grade,  Thomas High School ranking is not changed. It is on 2nd rank based on `% overall Passing` . All other school ranking ramain stable. 
* As a result of the Overall percentage of  Thomas High School , it is decreased by `.31%`

### School Analysis on Math and Reading by Grade   - Phase 1 
`Math`

<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189279627-17058bc3-bd64-46bb-bf70-d399c5db2036.png">

`Reading`

<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189279680-13e7bf04-a157-4d23-bd3c-37566ae6cd48.png">


### School Analysis on Math and Reading by Grade   - Phase 2 

`Math`

<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189279802-3bbf55e9-108a-4db1-b4a5-b23079cf8658.png">


`Reading` 

<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189279936-8e7886a0-244e-4f06-9e8b-94aa21efbae5.png">


* None other than `Thomas High School` result for grade 9th was changed for this report as we exclude those due to the requirement ( Anamolies in the grading) 



### School Spending Analysis   - Phase 1

<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189280763-67ab08a2-0d36-46ca-8ed9-c8bc000c5da4.png">

### School Spending Analysis   - Phase 2

<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189280813-b9bab3cd-3483-415b-9fd3-0a8c748cf955.png">


* In this category school spending groups scores for the $630-644 per student is changed for ~.1% and it is minimal.  `Thomas High School` is part of this group and it is driving this minimal impact.


###  Scores by School Size Analysis    - Phase 1


<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189281448-60252096-1e07-43f6-a20c-e7cea846fc87.png">


### Scores by School Size Analysis    - Phase 2
<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189281616-f50c52d2-16d8-468e-9bc9-0a178de02632.png">

* As `Thomas High School` has `1,635` students and it part of  Medium (1000-2000) size schools , there is slightly ( ~.07% ) changed in the overall passing. The above image shows the differences in `RED` color.


###  Scores by School Type Analysis    - Phase 1

<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189282172-d778cde0-726d-4050-9b06-937cdb9cf524.png">



###  Scores by School Type  Analysis   - Phase 2

<img width="860" alt="image" src="https://user-images.githubusercontent.com/22928255/189282271-1e84c5a2-2cc2-4bfd-bfca-f55da306554b.png">

* As `Thomas High School` is a ` Charter type school` we noticed there is a minimal change `.04%` decrease in the Overall Passing percentage. 



## Summary

We have provided each category impact  above with the report and data. The summary is below :

* School District Analysis - There are changes in all scores ( Math , Reading , both ) by less than `0.5%`
* Top/Bottom School Ranking -  No change in the School ranking. 
* Scores by School Size - `Medium (1000-2000) grouping` is changed due to the impacted shool is part of the group. The impact is less than `.07%` in any passing category
* Scores by School Type - The impact in `Charter type school` grouping for all scores by less than `.04%` points.
