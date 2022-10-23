# CustomerIN-Action
### A Loyalty Programme Customer Retention Recommender System

The majority of customer drop outs is caused by short-lived customers who join a Loyalty Programme, set up their profile and/or claim a reward and then choose to drop out within 50 days of joining. How to improve customer retention? Here, we show the pattern emerging from customer transaction data and build a recommender system that shows what actions, if a customer is motivated by the right marketing technique to take them, are predicted to reduce the probability of drop out.

Recommender System @ this url: https://samsonafo-hackjunction-antanvo-app-9anw0u.streamlitapp.com/
 <br/><br/>  
#### Code files
*antavo.ipynb*: jupyter notebook containing data visualisations   
   
*making_opt-out_dataset2.ipynb*: jupyter notebook containing code to make derived data file 'opt-out_customer_history.csv'  
  
#### Data files
   
*activities_junction_cut.csv*: (reduced) activity dataset containing activity codes, *etc*.   
    
*opt-out_customer_history.csv*: transaction event data on customers who drop out - with dummy action columns   
   
#### App files
The *deploy* folder contains the files for the Streamlitapp app. 
The file containing main app functionality is *app.py*.

      
 <br/><br/>   
      
<This project was created for the hackathon event *JunctionXBudapest 2022*. Challenge and data provided by Antavo.>

