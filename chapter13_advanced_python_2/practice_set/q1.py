# 1. Create two virtual environments, install few packages in the first one. How do you 
# create a similar environment in the second one? 


# Step 1 :- create a 2 invironment
# 1. python -m venv v1
# 2. python -m venv v2

# step 2 :- create a requirement file of one environment
# pip freeze > requirements.txt   --- this will create a file "requirements.txt"


# step 3 :- now in onother environment install the same dependecy
# pip install -r requirements.txt   --- this will intall same dependcy that same in the onother env