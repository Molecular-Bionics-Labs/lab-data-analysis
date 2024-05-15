# Lab data analysis

The repo provides guidance to the Experimental data analysis, some examples are illustrated with synthetic data

<img width="989" alt="image" src="https://github.com/Molecular-Bionics-Labs/lab-data-analysis/assets/80680465/cfda36e6-e879-4a52-8e49-dea93a2c13f8">

## Data analysis workflow

### (Step 1) 
### Data exploration (EDA, exploratory data analysis)
Plot your data and make superficial guesses about its behavior
Perform tests for normality and homogeneity of variances 
Run a distribution fitting

### (Step 2) Data pre-processing and normalization
Once you know the distribution, make a data transformation
Keep the transformation consistent within the same population/sample

### (Step 3) Hypothesis testing
Ensure your data satisfies assumptions
Choose your test
Make it done

### (Step 4) Modeling
If you need a model to describe or plan the next experiment, 
Split dataset into train and test, fit a model and estimate the results

### (Step 5) Decision making

#### Power analysis
If stat tests fail to detect an effect, check the power of the test
How large should be sample size to detect an effect that might be present

#### Summary
Report your results, mentioning:
assumptions for normality and heteroscedasticity check
normalization if done
test performed
power of the test
p-value as is


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
