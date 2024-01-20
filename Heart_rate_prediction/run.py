import sys
import json
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
__model=None
def play(input_file,output_file):
    global __model
    with open("./Heart_rate_prediction.pickle","rb") as f:
        __model=pickle.load(f)
    print("Model loading done....")

    df=pd.read_csv(input_file)
    uuid=df["uuid"]
    df=df.drop(["uuid","datasetId"],axis=1)
    le=LabelEncoder()
    df["condition"]=le.fit_transform(df["condition"])
    scaler=MinMaxScaler()
    df_scaled=scaler.fit_transform(df) 


    predictions=__model.predict(df_scaled)

    preds=[np.round(i,2) for i in predictions]

    result_df=pd.DataFrame()
    result_df["uuid"]=uuid
    result_df["HR"]=preds

    result_df.to_csv(output_file,index=False)
if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: python run.py input_file.csv output_file.csv")
        sys.exit(1)
    input_file=sys.argv[1]
    output_file=sys.argv[2] if len(sys.argv) == 3 else "output_results.csv"
    play(input_file,output_file)
    print("Results saved")