# Data analysis
- Document here the project: klarna_default_ml_pred
- Description: This Machine Learning Case Study consists of a supervised learning to predict the probability of default for the datapoints where the `default` variable is not set. The answer contains the resulting predictions in a csv file with two columns,
`uuid` and `pd` (probability of `default==1`). Once done expose this model
with an API Endpoint on AWS cloud provider. Then send us the details on how to query the endpoint, attach code used
for modelling, a short (max one page) explanation of your model and how you
validated it.
We mostly use Python for modeling at Klarna.
Don’t spend too much time on the prediction results. We evaluate how you
structure and reason about the problem rather than the predictive accuracy of
your model.
- Data Source: dataset.csv. This is a simple semicolon separated CSV file containing a unique id, the target variable `default` and a
number of features with somewhat different datatypes and meanings. Missing values are denoted as `NA` in the set. Here is a list of the variables and their types:
*Column_Name Column_Type*
uuid text
default categorical
account_amount_added_12_24m numeric
account_days_in_dc_12_24m numeric
account_days_in_rem_12_24m numeric
account_days_in_term_12_24m numeric
account_incoming_debt_vs_paid_0_24m numeric
account_status categorical
account_worst_status_0_3m categorical
account_worst_status_12_24m categorical
account_worst_status_3_6m categorical
account_worst_status_6_12m categorical
age numeric
avg_payment_span_0_12m numeric
avg_payment_span_0_3m numeric
merchant_category categorical
merchant_group categorical
has_paid boolean
max_paid_inv_0_12m numeric
max_paid_inv_0_24m numeric
name_in_email categorical
num_active_div_by_paid_inv_0_12m numeric
num_active_inv numeric
num_arch_dc_0_12m numeric
num_arch_dc_12_24m numeric
num_arch_ok_0_12m numeric
num_arch_ok_12_24m numeric
num_arch_rem_0_12m numeric
num_arch_written_off_0_12m numeric
num_arch_written_off_12_24m numeric
num_unpaid_bills numeric
status_last_archived_0_24m categorical
status_2nd_last_archived_0_24m categorical
status_3rd_last_archived_0_24m categorical
status_max_archived_0_6_months categorical
status_max_archived_0_12_months categorical
status_max_archived_0_24_months categorical
recovery_debt numeric
sum_capital_paid_account_0_12m numeric
sum_capital_paid_account_12_24m numeric
sum_paid_inv_0_12m numeric
time_hours numeric
worst_status_active_inv categorical

- Type of analysis:

Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for klarna_default_ml_pred in github.com/{group}. If your project is not set please add it:

Create a new project on github.com/{group}/klarna_default_ml_pred
Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "klarna_default_ml_pred"
git remote add origin git@github.com:{group}/klarna_default_ml_pred.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
klarna_default_ml_pred-run
```

# Install

Go to `https://github.com/{group}/klarna_default_ml_pred` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/klarna_default_ml_pred.git
cd klarna_default_ml_pred
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
klarna_default_ml_pred-run
```
