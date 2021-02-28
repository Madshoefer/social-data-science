Please see the instruction for the assignment attached, for the purpose of context. Please also note that parts of the data used in the coursework are paid for, and can therefore not be accessed by third-party users.


# Fundamentals of Social Data Science in Python Assessment

The final essay will allow you to consolidate many of the skills you’ve learned in the course thus far in a single report. This report should be submitted as a Jupyter notebook with working code as well as a description of the work you have done. You should also submit a backup PDF of your notebook.

This essay will have two parts. The combined word total should be 3500 words. The structure of the notebook should look as follows: (with the grade weighting for each section):

## Part 1.
The first part will involve the use of the OxCOVID19 database (https://oxcovid19.eng.ox.ac.uk) , which has an extensive set of data not only including COVID-related data but data on world values, geographic mobility, sociodemographic data, and more. Each table can be linked to others using identifiers as discussed on the database website. You should come up with a research question, justify that research question in a literature review section (of less than 750 words), and then proceed to query the database for the relevant data which you should merge, visualise and make claims about. You do not have to include any statistics on COVID-related data itself should you wish not to. You can instead simply use the additional extensive supplementary data. You should be able to plot the merged data in such a way that it speaks to your research question and report on descriptive statistics where relevant. You are asked not to do any complex multivariate modelling. This question should be primarily descriptive in nature. You should interpret the resulting output and summarise it in a report section of not more than 750 words. It is assumed that the evaluators should be able to reproduce your findings by running the Jupyter notebook themselves. One important caveat is that this work should not require the installation of any external libraries not featured in class.

#### Example research questions include:

Did areas of the world with different social values (as measured by some question on the World Values Survey) have different proportions of COVID infections in April?
Are people in the UK more mobile on days when the weather was above average? Did this hold during lockdown?
Is air pressure more variable in coastal countries (or coastal regions) or inland countries (or inland regions)? 

## Part 2.
Develop a second research question that will require you to build in additional data (in less than 750 words). You will select an API (or direct URL) from the web which will allow you to download said data that you should merge in with the OxCOVID19 data. This second question does not need to be linked thematically to the first. Consider it like a second blog post. . You will first have to justify the choice of external data, your specific choice of API endpoints or URL, time frames or other ranges for this data. You should then report on the merged data through descriptive statistics and plots where appropriate. Data sources could include anything from reddit, Wikipedia, Facebook, Twitter, StackOverflow, or another source not covered in class (as long as it is publicly available either openly or through a free registered account). You can use external libraries (such as praw) in order to collect this data. Please do not submit any private API keys with this data. We suggest that private keys be written in an external file that is read by the notebook just to be safe. You should interpret the resulting output and summarise it in a report section of not more than 750 words.

It is not assumed that the evaluators will be able to reproduce this section with your code since it might involve the use of user-generated API keys or other forms of authentication not available to the evaluators. However, the section should include all relevant code and output other than the keys. You should consider an approach that does not require you to repeatedly request the same data from the API, such as writing it to file and then working on it in a different cell, or from the data you have now stored.

#### Example research questions for this section:
Do countries with longer Wikipedia pages also have more extensive government responses to COVID?
Comparing two countries, one with a high number of active cases and one with a low number: does the one with active cases have a higher proportion of tweets mentioning COVID in a window of time for Twitter streaming requests.
Which countries are mentioned most often in /r/coronavirus and do they relate to statistics concerning COVID
Examples of non-COVID research questions: Do countries with longer Wikipedia pages (external) correlate with higher GDP (from the World Bank tables)? Does a country’s democracy index (e.g., https://en.wikipedia.org/wiki/Democracy_Index) relate to more stable weather?

Finally, please write a reflective conclusion (of not more than 500 words) that discusses the limitations of the data in relation to your claims. You are also encouraged to build in any concerns about insights arising from this data, ethical issues with the analysis, and potential future avenues for analysis based on your work.

This work, while in a report style, should be referenced like any scholarly work. Please include a cell at the bottom of your notebook which includes all the references.
