# Flask Serverless Starter #

This project contains the starting structure for an AWS backed serverless application using
Python and Flask.  The endpoints are agnostic to the client interface being used (React, Angular, iOS, Android).

#### IMPORTANT: This project requires access to an AWS account ####

## SSM Parameter Store Configuration (Prior to deployment) ##
The SSM Parameter Store service will be leveraged to store environment and account specific configuration details.
These values are set manually via aws console and get set as lambda environment variables at deploy time.  
If you want to change defaults then set the value in ssm and redeploy.

| Key | Description | Default |
| :--- | :--- | :--- |
| account-id | REQUIRED! the aws account id (cannot get via serverless) | None |

## Functionality: ##

* Feature 1

## Project Setup ##
 
NPM is used to install the serverless tools whereas pip is used to install runtime Python packages.

### NPM Dependencies ###

Ensure the prerequisites are installed
```
- Node LTS 10.x (for working with serverless)
    - nvm (Node Version Manager) is highly recommended 
```

Install the NPM dependencies
```
npm install
```

### Python Dependencies ###

Ensure the prerequisites are installed
```
- Python3.7
- pip (tool for installing Python packages)
    - curl https://bootstrap.pypa.io/get-pip.py | python3.7
```

Create virtual env for python3.7 inside project directory:
```
python3.7 -m venv venv 
```

Activate newly created environment
```
. venv/bin/activate
```

Install the required python packages
```
pip install -r requirements.txt
```

OPTIONAL: Exit the virtual environment using the following command
```
deactivate
```

## Serverless Deployment ##

The application can be deployed by issuing the following commands:
```
export AWS_PROFILE=test
export AWS_REGION=ca-central-1
./launch-env.sh <stage_name>
```

** NOTES: **

* Replace **test** with your assume role profile name
* Please include your name to stage name if you want to create custom AWS stack for testing purposes.  For example:
> ```
> ./launch-env.sh dev
> ```

First Time Deployment: Create a test user account
```
cd scripts
./user_sign_up.py <username> <password> -p <profile name> - s <stage_name>
```

## Running project locally ##

The project can be run locally using the following command:
```
export AWS_PROFILE=test
export AWS_REGION=ca-central-1
npm run local -- --stage <stage name> --region ca-central-1
```

**NOTES**:

* This command must be run inside an activated virtual environment
* Any environment (stage name) can be used, optionally you may want to use `config/local.yaml` configuration file
* When running locally timeout, access, and file size restrictions do not behave the same as within an AWS service
