# To install our environment
echo [$(date)]: "START"
echo [$(date)]: "Creating Environment with Python v3.8"
conda create --prefix ./env python=3.8 -y         #-y = to accept all the changes
echo [$(date)]: "Activating the Environemnt"
source activate ./env
echo [$(date)]: "Installing the Dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"