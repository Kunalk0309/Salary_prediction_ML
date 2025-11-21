import pickle
from flask import Flask, request,jsonify,render_template

import numpy as np 
import pandas as pd 
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

# import gradientboost and standard scaler pickle file
GB_model=pickle.load(open('MODEL/gradient_boost.pkl','rb'))
encoded=pickle.load(open('MODEL/Onehot_encoderr.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata", methods=['GET','POST'])
def predict_data():
    if request.method == 'POST':
        Country = request.form.get("country")
        WorkExp = int(request.form.get("workexp"))
        YearsCode = int(request.form.get("yearscode"))
        EdLevel = request.form.get("edlevel")
        DevType = request.form.get("devtype")
        OrgSize = request.form.get("orgsize")
        Industry = request.form.get("industry")
        RemoteWork = request.form.get("remotework")

        cat_features = pd.DataFrame([[Country, EdLevel, DevType, Industry, RemoteWork, OrgSize,]],
                                    columns=['Country','EdLevel','DevType','Industry','RemoteWork','OrgSize'])

        cat_encoded = encoded.transform(cat_features)
        final_input = np.concatenate(([WorkExp, YearsCode], cat_encoded[0]))
        result = int(GB_model.predict([final_input])[0])

        # Render index.html with result and sticky form values
        return render_template("home.html",
                               result=result,
                               country=Country,
                               workexp=WorkExp,
                               yearscode=YearsCode,
                               edlevel=EdLevel,
                               devtype=DevType,
                               orgsize=OrgSize,
                               industry=Industry,
                               remotework=RemoteWork)

    # 👇 GET request (when first loading the page)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0")