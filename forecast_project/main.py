# main.py

# from flask import Flask, jsonify
from data_loader import download_data, upload_forecast
from model import generate_forecast

# app = Flask(__name__)

# @app.route("/", methods=["POST", "GET"])
# def run_forecast():
#     try:
#         df = download_data()
#         forecast_df = generate_forecast(df)
#         upload_forecast(forecast_df)

#         return jsonify({
#             "status": "success",
#             "message": "Forecast generated successfully"
#         }), 200

#     except Exception as e:
#         return jsonify({
#             "status": "error",
#             "message": str(e)
#         }), 500


# if __name__ == "__main__":
#     # Required for Cloud Run
#     import os
#     port = int(os.environ.get("PORT", 8080))
#     app.run(host="0.0.0.0", port=port)

def run():
    df = download_data()
    forecast_df = generate_forecast(df)
    upload_forecast(forecast_df)
    print("Forecast completed successfully, part 2")

if __name__ == "__main__":
    run()