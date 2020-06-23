<br>
<p align="center">
<a href="https://www.insidesherpa.com/virtual-internships/prototype/R5iK7HMxJGBgaSbvk/Technology%20Virtual%20Experience" target="_blank">
<img src="https://insidesherpa-assets.s3-ap-southeast-2.amazonaws.com/icons/jpmorgan/github+repo+images/jpm+gitub+.png"></a>
</p>

<p align="center"> 
	<b><a href="#task">Task Overview</a></b>
	|
	<b><a href="#installation">Installation Instructions</a></b>
	| 
	<b>Link to Module 1</a></b>		
	| 
	<b>JP Morgan Chase & Co Software Engineering Virtual Experience</a></b>
</p>

<h1> Introduction</h1> 
<b> Experience Technology at JP Morgan Chase & Co</b>
<p>Try out what real work is like in the technology team at JP Morgan Chase & Co. Fast track to the tech team with your work.</p>

<h2 id="task"> Module 1 Task Overview </h2>
<p>Interface with a stock price data feed and set up your system for analysis of the data</p>
<p> <b>Aim:</b> We want to process the data feed of stock A and stock B’s price to enable us to analyse when trading for the stock should occur.</p>
 <h3>Project objective</h3>
<ol>
	<li>Adjust the getRatio, getDataPoint and main functions</li>
	<li>Bonus: Pass all unit tests and add more to cover edge cases</li>
	<li>Upload a git patch file as the submission to this task</li>
	
</ol>

<h2 id="installation" >Set up / Installation</h2>

<h2>How to Run</h2>
To start the server, run

	python server3.py

this will create random market called 'test.csv' in your working directory if one does not already exist.

If you encounter an issue with `datautil.parser`, run this command: 

	pip install python-dateutil

If you don't have pip yet, you can install it from: https://pip.pypa.io/en/stable/installing/

To start the example client, run:

	python client3.py

To unit test the example client, run:
	python client_test.py

<h2>How to request from the server using curl</h2>
Query:

	$ curl 'http://localhost:8080/query?id=1'
	Example {"id": "1", "top_ask": {"price": 129.18, "size": 70}, "timestamp": "2016-08-06 12:32:11.821574", "top_bid": {"price": 128.79, "size": 61}}

<h2>How to fix the code to meet objectives</h2>
<ul>
<li>#GETPOINT FUNCTION:make changes to the price return values,this change how price is been computed.</L1>
<li>#GETRATIO FUNCTION:when price_b is 0 to avoid throwing zeroDivisionError.</li>
<li>#Effect a change to return value of stock price at getratio function.</li>
<li># Query the price once every N seconds.</li>
<li>#update the getRatio output so as to return a value other than 1</li>
</ul>

