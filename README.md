____Packages, Keys, and IDs____


Step 1: Download/install the proper Python packages using the command: 'python3 -m pip install -r requirements.txt'

Step 2: Open config.py and replace 'Insert API Key Here' with your personal API key.

_____Gathering and Storing Search Data____


Step 1: Run the cse.py file with the following command: 'python3 cse.py "Insert Search Here"'.

____Setting Up Data for Indexing/Whoosh____


Step 1: Run the following sh file using this command: 'bash download_youtube_data_batch.sh'

Step 2: Run the following python file using this command: 'python3 create_data_for_indexing.py'

Step 3: Run the follwing python file using this command: 'python3 create_whoosh_index.py'

____Run a Query on Whoosh Index____

*Added commit for testing
Step 1: Run the following python file using this command: 'python3 query_on_whoosh.py "Insert Query Here"