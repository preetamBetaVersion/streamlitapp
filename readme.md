At first, we created a virtual environment using the following commands:  
`python -m venv env`  
Then we activated the virtual environment using the following command:  
`env\Scripts\activate.bat`  
after this we will be able to see that we will be in the created virtual environment.  
**Note** : to see that we have entered the virtual environment, use cmd which shows (env) meaning we are in the virtual   
environment. It won't show if the terminal used is powershell.  
> Also, make sure to reactivate the virtual environment if you happen to close vsc and open it again.  
<hr>  
Once, the virtual environment is set up, we install streamlit using the command:    

`pip install streamlit`  
we then create a app.py file and use the following command to start the app  
`streamlit run app.py`  
<hr>  

We used the **pipreqs** package to create the requirements.txt file which contains the names of all the libraries needed for the app with their version. Use the following command to do that:   
`pipreqs ./`
