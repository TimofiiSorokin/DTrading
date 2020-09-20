<b>Technical task DTrading</b>

<b>Task 1</b> Writing a script to collect data for the onset of web pages: https://epbets.ueex.com.ua/public/PositionList.aspx?id_auc=3294127&view_type=positions&lan=en
The structure contains separate blocks for each position. You need to collect this data and write them in tables, from 1 row 1 position will correspond, and all data concerning a position wake up in a separate column. That is, you should get a table of the form:
Position | Type | Condition | Seller Graph type | Trade area ...

<b>Task 2</b> Attached are data on electricity consumption and production in Ukraine since 2016. Your task is to visualize the data and express your own assessment of trends. If you wish, you can use additional information resources, but this is not necessary.

<b>Step for Set Up</b>

 1. git clone https://github.com/TimofiiSorokin/DTrading.git

 2. cd DTrading

 3. python3 -m venv env

 4. source env/bin/activate

 5. pip3 install -r requirements.txt

<b>Step for Task_1</b>

 1. cd Task_1

 2. create DB -> python models.py
 
 3. run parser -> python data_collection.py
 
 <b>Step forTask_2</b>
 
 1 cd ..
 
 2. cd Task_2
 
 3. python last_year.py
 
 4. python year_2016.py

<b>Result</b>

1. We can see the SQLite DB with data from parser.

2. The difference in electricity production in Ukraine over the last four years can be seen on circular diagrams. 

![Screenshot](myplot_2016.png)
![Screenshot](myplot_2020.png)

During this time, electricity generation from renewable sources increased by 5.3%

<b>Thanks for your attention!</b>

