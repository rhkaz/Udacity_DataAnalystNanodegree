
# Historical Default Rates of Prosper Loan Data 


### Visualisation, Tableau Public and GitHub Links

the project files can be viewed on gist from each of these links : [Tableau Public Story 1](https://public.tableau.com/profile/rashid.kazmi#!/vizhome/Story_2_HistoricalDefaultRatesofProsperLoanData/Story_2_HistoricalDefaultRatesofProsperLoanData)  :::: [Tableau Public Story 2](https://public.tableau.com/profile/rashid.kazmi#!/vizhome/Story_HistoricalDefaultRatesofProsperLoanData/Story_1_HistoricalDefaultRatesofProsperLoanData).  

And for sure the github repository [GitHub](https://github.com/rhkaz/Udacity_DataAnalystNanodegree).  

------------

### Summary  

Lending Club is the world’s largest peer-to-peer lending company, offering a platform for borrowers and lenders to work directly with one another, eliminating the need for a financial intermediary like a bank
visit [Prosper.com](https://www.prosper.com/).     

  + I filled in missing data instead of just dropping the missing data rows. I used “mice” R package for the imputation of missing values. The mice package in R, helps you imputing missing values with plausible data values. These plausible values are drawn from a distribution specifically designed for each missing data point. 

  + I extracted data the feature engineered some fields. I also eliminated a few indicative data fields that are  repetitive or too granular to be analysed, and make some formatting changes to get the data ready for analysis. 
  
  + Finally, I mapped the loan statuses to the binary “Performing” and “NonPerforming” classifiers.
  
  + Then I carried out exploratory data analysis using various plots to check how these variable are contribute to performance of the loan.
  
  + To further understand this dataset, I also visualised the interaction between two variables. 
  
  + Number of the variables provided strong indications of expected performance. Among them most telling are loan purpose, BorrowerState,  Debt-To-Income Ratio, Burrower Rate etc

--------

### Design

+  Loan purpose refers to the borrower’s stated reason for taking out the loan. So a bar chart would be best way to show what was pupose of the loan.

+ Next to pupose of the loan an obvious aspect was to look at the borrower’s geographical informaiton. I used a barplot to viusalise the distribtion of the loan each state. Furthermore, I also tried to understand the interaction between burrower satates and purpose of the loan. 

+ As we can see from this map, California, Texas, Georgia, Florida, and New York have the most borrowers. These are the most populous and economically prosperous areas as well. The number of borrowers of different states varies a lot and California, Texas, New York and Florida are the top 4 on the list of state with big borrower market.
+ I also plotted the prosper loan data using variety of graphs (box plot, scatter plot, line plots) 

-----------

### Feedback
1 -
> George Liu
Forum Mentor

Good job !

I like the story format and the distilled message for each slide. Here're several thoughts for further improvement:
Make sure you de-select the single dot on your first visualization before uploading, otherwise, your reader will see that as first impression as well  :slight_smile:

The two slides about the positive association between risk and return doesn't seem to be immediately clear to support the message. For the "Higher risk means higher returns" one, maybe you want to switch to a different graph type, for example, use a scatterplot to show the relationship at individual borrower level. For the second one, maybe you don't need it if you improve the first one?
Hope this is helpful! 

I changed the title of the graphs to make it more understandable, 

> George Liu
Forum Mentor

For the second point, apologies that I did't realize one variable is categorical. So the last visualization is good however it doesn't support the claim that risk and return is associated, so maybe consider updating the title.


---------------   

#### Resources

The loans dataset https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv .  


-------------------------

