python3 -m venv myenv
source myenv/bin/activate
python3 -m pip install --upgrade pip
export SYSTEM_VERSION_COMPAT=1
pip3 install -r requirements.txt
streamlit run app_2.py
# python3 back_sql.py
# deactivate
# rm -rf myenv
