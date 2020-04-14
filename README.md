# What this script does
This script creates an Excel spread sheet version of a Contentful space's content model.

# Requirements
You must have Python3 installed on your machine. It won't work with 2.7.

It's also a good idea to create virtual environment based on requirements.txt.

# How to use it
1. Activate your virtual environment
2. Have your Personal Access Token as an environment variable named `PERSONAL_ACCESS_TOKEN`.
3. `python main.py <space_id> <environment_id>`

This will create a file of `<space_id>_content_model_<today's date>.xlsx`.