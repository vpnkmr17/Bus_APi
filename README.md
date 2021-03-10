busAPI--->Fetches the data from database
So,it fetches the data based on bus_no and stop_names

For e.g

1)Using bus_no
URL-->http://127.0.0.1:8000/busno/
JSONData--> {
     "bus_no":"545 LTD"
 }
 
2)Using stop_names
URL-->http://127.0.0.1:8000/search/
JSONData--->  {
    "source":"Airoli Bus Station",
    "destination":"Ankur Hospital"
}
