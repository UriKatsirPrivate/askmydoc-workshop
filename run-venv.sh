python3 -m venv myenv
source myenv/bin/activate
python3 -m pip install --upgrade pip
export SYSTEM_VERSION_COMPAT=1
pip3 install -r requirements.txt
# streamlit run app_text.py
# This one is good for both local and cloud shell execution
streamlit run app.py --server.port 8080 --browser.serverAddress 0.0.0.0 --server.enableCORS False
# deactivate
# rm -rf myenv