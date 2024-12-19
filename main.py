import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the pre-trained model and scaler
improved_model = joblib.load('models/improved_model3.pkl')
scaler = joblib.load('models/scaler.pkl')

# Streamlit App Title
st.title("Deteksi Produk Dengan Engagement Bagus Untuk Shoppe Affiliate")
st.write("Kamu Boleh Masukan Input Di Bawah Jika Menemukan Produk Dengan Detail Berikut Untuk Inspirasi Pembelian/Pengajuan Sampel Produk")

# Input form for manual data entry
st.header("Manual Product Input")
likes = st.number_input("Jumlah Like", min_value=0, step=1)
comments = st.number_input("Jumlah Komentar", min_value=0, step=1)
views = st.number_input("Jumlah View", min_value=0, step=1)

if st.button("Predict"):
    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        'Jumlah Like': [likes],
        'Jumlah Komentar': [comments],
        'Jumlah View': [views],
        'log_like': [np.log1p(likes)],
        'log_view': [np.log1p(views)]
    })

    # Scale the input data
    scaled_data = scaler.transform(input_data)

    # Make predictions
    prediction = improved_model.predict(scaled_data)[0]
    probability = improved_model.predict_proba(scaled_data)[0, 1]

    # Display the results
    st.write("### Prediction Results:")
    st.write(f"**Prediction:** {'Good Product' if prediction == 1 else 'Not Good Product'}")
    st.write(f"**Probability:** {probability:.2f}")

# # File Uploader for bulk predictions
# st.header("Bulk Product Prediction")
# uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# if uploaded_file is not None:
#     # Load uploaded CSV file
#     new_data = pd.read_csv(uploaded_file)

#     # Ensure the necessary columns are present
#     required_columns = ['product_name', 'Jumlah Like', 'Jumlah Komentar', 'Jumlah View']
#     if all(col in new_data.columns for col in required_columns):
#         st.write("### Uploaded Data")
#         st.write(new_data)

#         # Add log-transformed features
#         new_data['log_like'] = np.log1p(new_data['Jumlah Like'])
#         new_data['log_view'] = np.log1p(new_data['Jumlah View'])

#         # Extract product names and features
#         product_names = new_data['product_name']
#         features = new_data[['Jumlah Like', 'Jumlah Komentar', 'Jumlah View', 'log_like', 'log_view']]

#         # Scale the features
#         scaled_features = scaler.transform(features)

#         # Make predictions
#         predictions = improved_model.predict(scaled_features)
#         probabilities = improved_model.predict_proba(scaled_features)[:, 1]

#         # Combine results into a DataFrame
#         results = pd.DataFrame({
#             'product_name': product_names,
#             'is_good_product': predictions,
#             'probability': probabilities
#         })

#         # Display results
#         st.write("### Prediction Results")
#         st.write(results)

#         # Option to download results
#         csv = results.to_csv(index=False)
#         st.download_button(
#             label="Download Predictions as CSV",
#             data=csv,
#             file_name='predicted_products.csv',
#             mime='text/csv'
#         )
#     else:
#         st.error(f"The uploaded file must contain the following columns: {required_columns}")
# else:
#     st.info("Please upload a CSV file to proceed.")
