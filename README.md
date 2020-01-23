
## ETL Report

### Resources - 
* MLB API  - http://lookup-service-prod.mlb.com
* Kaggle dataset - kaggle.com/timschutzyang/dataset1#baseballdata.csv


* **Extraction**

  * We downloaded the baseball.csv from Kaggle and then loaded it into our pandas dataframe.
  * With our MLB API we extracted and loaded MLB information for 2017 season, named the file mlb_2017 season into a csv file and then loaded it into our pandas dataframe

* **Transform**

  * With the new Kaggle df now called "mlb_df" we extracted and renamed the columns "TM", "Year" and "Attendance" to "team_name", "year" and "attendance" and renamed the dataframe to "mlb_transformed".

  * With the MLB API df now called "mlb_2017_df" we extracted and renamed th ecolums "name_display_long", "year", "venue_name", and "city" to "team_name", "year", "city" and "venue" and renamed the dataframe "mlb_api_transformed".
  
 

* **Load**

  * We created two tables which can be found in our schema.sql called "kaggle_csv" and "mlb_api".
  * We also wrote a query.sql to check for a successful connection to the database and confirm that the tables had been created.
  * Created a connection to our database in pg admin called baseball_db.
  * Loaded the data into sql baseball_db database
  

 

