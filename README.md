![logo](assets/logo.png)

# centaur-recipes: Centaur's public repository for data pre-processing code recipes


## Summary

This repository contains code snippets you may integrate with your scripts to 
process your data before sending it to Centaur Labs. Some recipes might need to be used sequentially.

### The code recipes currently available are:
* [Mask Extraction](mask_extraction)

## Installation

The recipes in this repository require Python 3.9+ to run. You may install 
python from: https://www.python.org/downloads/. Generally, each recipe folder 
will contain specific instructions on how to install and use the recipe. Below
you can find instructions on how to set up a virtual environment as well as how
to use one with a Jupyter notebook.

### Virtual environment
After you've downloaded a recipe and any associated files, it is highly 
recommended creating a new virtual environment for the script you will write.

To create a virtual environment using the default python virtual environment manger:
1. Open up a terminal or command prompt and navigate to the directory 
   containing the notebook.
2. Then create a virtual environment using `python -m venv env_name` where 
   `env_name` can be changed as desired.
3. Activate the virtual environment by using one of the following commands 
   depending on your operating system:
    * Unix/macOS: `source env_name/bin/activate`
    * Windows: `.\env_name\Scripts\activate`
4. To deactivate the virtual environment you can type `deactivate` in the 
   terminal or command prompt

#### Installing Requirements and Running a Notebook

For recipes that are Jupyter notebooks, or if you are just working in one
perform these additional steps to ensure the notebook is using the correct
virtual environment and installed packages. Some IDEs may handle selecting the
correct virtual environment for you, in which case you only need to do step 1.

1. With the environment activated, run `pip install -r requirements.txt`
   from the terminal or command prompt. This should install jupyter as well as 
   the other required packages.
2. Run `python -m ipykernel install --user --name env_name` where `env_name`
   is the name of the currently activated virtual environment.
3. Now start the Jupyter notebook with `jupyter notebook path/to/notebook.ipynb`
   The notebook should open in your default browser.
4. In the top toolbar click on `Kernel` and then select `Change kernel`.
5. Select the kernel that has the same name as your virtual environment.
6. Now you may follow any remaining instructions in the notebook.
