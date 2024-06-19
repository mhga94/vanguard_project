# Vanguard A|B testing in Tableau and Python

[Summary](#Summary)
[Observations](#Observations)
[Conclusions](#Conclusions)
[Slides](#Slides)
[Install](#Install)
[Development](#Development)
[Contributors](#Contributors)


## Summary

This project is an analysis and presentation of findings from the (fictional) A|B testing undertaken by Vanguard Asset Management Ltd, as part of the Ironhack Data Analytics Bootcamp. The project seeks to incorporate hypothesis testing and data transformation in Python and visualisation and presentation in Tableau. 

## Insights

* The project found that the Control and Test groups were similarly distributed across all variables, including age, gender and income. 
* The analysis revealed improvements in linearity of the customer journey, with increased average time spent on sequential steps in the test group.
* The test group had similar numbers of backward steps in the customer journey, though the quantities were redistributed. Of particular note was the significant increase in failure at the confirm stage. 

## Conclusions

* The project concluded that the Vanguard leadership should not take a decision at this time, but rather await further findings from the A|B testing before deciding to adopt the new website model. 


## Slides

The slides presenting the data and analysis can be found at: [slides]: ['https://public.tableau.com/app/profile/matthew.asquith/vizzes']

## Install

### Python

The data cleaning and visualisations in Python used the following packages:
* numpy
* pandas
* matplotlib
* seaborn
* plotly
* ast

The versions for the above packages can be found in the requirements text file.

## Development

Data was provided by Ironhack and was analysed, transformed and plotted in Jupyter Lab and Tableau.

## Contributors

mhga94