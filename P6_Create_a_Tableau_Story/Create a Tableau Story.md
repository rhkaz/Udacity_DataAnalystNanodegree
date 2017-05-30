
# Historical Default Rates of Prosper Loan Data 


### Visualisation, Tableau Public and GitHub Links

the project files can be viewed on gist from each of these links : [Tableau Public Story 1](https://public.tableau.com/profile/rashid.kazmi#!/vizhome/Story_2_HistoricalDefaultRatesofProsperLoanData/Story_2_HistoricalDefaultRatesofProsperLoanData)  :::: [Tableau Public Story 2](https://public.tableau.com/profile/rashid.kazmi#!/vizhome/Story_2_HistoricalDefaultRatesofProsperLoanData/Story_2_HistoricalDefaultRatesofProsperLoanData). :::: [Tableau Public Story 2_V2](https://public.tableau.com/profile/rashid.kazmi#!/vizhome/Story_2_HistoricalDefaultRatesofProsperLoanData_V2/Story_2_HistoricalDefaultRatesofProsperLoanData_V2)

And for sure the github repository [GitHub](https://github.com/rhkaz/Udacity_DataAnalystNanodegree).  

------------

### Summary  

> Lending Club is the world’s largest peer-to-peer lending company, offering a platform for borrowers and lenders to work directly with one another, eliminating the need for a financial intermediary like a bank
visit [Prosper.com](https://www.prosper.com/).     


+ I filled in missing data instead of just dropping the missing data rows. I used “mice” R package for the imputation of missing values. The mice package in R, helps you imputing missing values with plausible data values. These plausible values are drawn from a distribution specifically designed for each missing data point. 


+ I extracted data the feature engineered some fields. I also eliminated a few indicative data fields that are  repetitive or too granular to be analysed, and make some formatting changes to get the data ready for analysis. 
  
  
+ Finally, I mapped the loan statuses to the binary “Performing” and “NonPerforming” classifiers.
  
  
+ Then I carried out exploratory data analysis using various plots to check how these variable are contribute to performance of the loan.
  
  
+ To further understand this dataset, I also visualised the interaction between number of variables indorder to understand the relationships asscoiated with loan performance. 


+ Tableau visualisation of Prosper Loan Data identifies the most hidden patterens and trends in the dataset. Thus, providing predictive power for determining expected loan performance.
 
 
+ I wanted to have my inttuion going what are are the main indicators of a quality of borrowers e.g Proser Rating (both numeric & alphabet)

 
+ I exploed variables Lender Yield and Borrower Rate and see which other related variables have the most effect on it.  This was very important step to observe any interesting relationships between the other features i.e. relationship between (Prosper Rating and Lender Yield) and (Prosper Rating and Borrower Rate). 


+ Among them most telling are loan purpose, BorrowerState,  Debt-To-Income Ratio, Burrower Rate etc

+ The chart confirmed that although there is higher lending yield for lower rating. Thus, the investors should also takes a look at the risk of the loan being defaulted. We have seen very clear in charts as the rating get worsen, the higher chance the loan getting defaulted.


> Through Tableau story telling; We’ve gotten a good understanding of the available borrower data, and we’ve seen which variables give the best indiciations of future loan performance.


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

I changed the title of the graphs to make it more understandable. Furthermore, I have created number of other viusalisation to make the story more coherent. I looked at how higher rating is associated with better yeild as well as I have created small multiples of propser rating, monthly income and thier relationship to loan orgination year.  As someone who’s completely new to the industry, I did not fully comprehend there’s a very linear and strong relationship between borrower rate and lender yield intially, howver, it was unfolded later on during bivariate analysis.

Furthermore, I also had a  closer look for lender yield vs prosper rating. The majority of loans opt-in for 36-month term and the return for 36-month and 60-month are just higher than 12-month, also considering the fact there’re less loan in 12-month term than other term.

These charts boasted my ablity to glean into the loan perfomeance. It seemed apparently prosper must have optimised their model throughout the year and as we see the borrower throughout the year, the variation between borrower rate as  not that significant anymore and we tend to have smaller standard deviation year-over-year. Something worth noticing is the amount of borrowing suddenly decreased in 2013.



> George Liu
Forum Mentor

For the second point, apologies that I did't realize one variable is categorical. So the last visualization is good however it doesn't support the claim that risk and return is associated, so maybe consider updating the title.


---------------   

#### Resources

The loans dataset https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv .  


-------------------------



```python

```
