# Lab data analysis

The repo provides guidance to the Experimental data analysis, some examples are illustrated with synthetic data

<img width="989" alt="image" src="https://github.com/Molecular-Bionics-Labs/lab-data-analysis/assets/80680465/cfda36e6-e879-4a52-8e49-dea93a2c13f8">

## Data analysis workflow

### 1. Data exploration (EDA, exploratory data analysis) 
[MB_Data_analysis_template.ipynb](https://github.com/Molecular-Bionics-Labs/lab-data-analysis/blob/main/01%20Data%20exploration%20and%20hypotesis%20testing/MB_Data_analysis_template.ipynb)

Plot your data and make superficial guesses about its behavior

Perform tests for normality and homogeneity of variances 

Run a distribution fitting

### 2. Data pre-processing and normalization
[MB_Data_analysis_template.ipynb](https://github.com/Molecular-Bionics-Labs/lab-data-analysis/blob/main/01%20Data%20exploration%20and%20hypotesis%20testing/MB_Data_analysis_template.ipynb)

Once you know the distribution, make a data transformation

Keep the transformation consistent within the same population/sample

### 3. Hypothesis testing
[MB_Data_analysis_template.ipynb](https://github.com/Molecular-Bionics-Labs/lab-data-analysis/blob/main/01%20Data%20exploration%20and%20hypotesis%20testing/MB_Data_analysis_template.ipynb)

Ensure your data satisfies assumptions

Choose your test

Make it done

### 4. Modeling
[MB_Data_analysis_template_MODEL.ipynb](https://github.com/Molecular-Bionics-Labs/lab-data-analysis/blob/main/02%20Modelling%20and%20curve%20fitting/MB_Data_analysis_template_MODEL.ipynb)

If you need a model to describe or plan the next experiment, 

Split dataset into train and test, fit a model and estimate the results

### 5. Decision making

#### Power analysis
[MB_Data_analysis_template.ipynb](https://github.com/Molecular-Bionics-Labs/lab-data-analysis/blob/main/01%20Data%20exploration%20and%20hypotesis%20testing/MB_Data_analysis_template.ipynb)

If stat tests fail to detect an effect, check the power of the test

How large should be sample size to detect an effect that might be present

#### Summary

Report your results, mentioning:

assumptions for normality and heteroscedasticity check

normalization if done

test performed

p-value as is

power of the test (optional)



## Nanoparticle characterization

### 1. Image processing 
Importing .lif files and processing as it's done in ImageJ and Fiji (not implemented to due a bug in ITK library, that's is needed to run the  ImageJ API)

### 2. Human visual checkup
Saving the masks and vusiall assesment

### 3. Counting, size, intensity and EDA
Saving the processing results in txt
Exploratory data analysis

### 4. Testing, comparison

### 5. Results interpretation
