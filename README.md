# Dashboard_application

## Aim					
My aim to creat the multipage dash application was to make a convenient all-in-one portal where the employees with minimal data science skills could easily access the up-to-date, realtime information from the database, and to have self-explanatory visualization and tables of key findings of my analyses. Viewing the data and the results were possible with few clicks (with help of graphical user interface (GUI)).
					
## Technicality				
This multi page app is made using Dash library in python. Bootstrap was used to style the app. Plotly library was used to produce graphs. VS code IDE was used for the purpose. The dashboard_application repo has following files: 
1. apps folder: The apps folder has individual files for each page of the multi page application. Following files are in the apps folder:
   1. home.py is the main page where you can select which subpage you would want to enter./
   2. Local_database.py is one of the subpage (and the only present in the github version of this app). This is an interactive page with various analyses outputs, the outputs are either in graphical or tabular format. User can select categories and subcategories of data for with they want the analyses to be performed, respective visualization and tables will be displayed realtime.
   3. __ init __.py is an empty file.
3. index.py file: this file links all the individual pages.
4. (Optional) you can make another folder to keep aesthetics like image files for the application.   
