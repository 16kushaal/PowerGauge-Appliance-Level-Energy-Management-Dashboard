import pandas as pd # type: ignore
from prophet import Prophet # type: ignore
import mysql.connector
from dotenv import load_dotenv # type: ignore
import os
load_dotenv()
def predict_next_day_usage(user_id, meter_id):
    """
    Uses Prophet to predict the next day's energy usage based on historical data.
    
    Args:
        db_connection: Database connection object
        user_id: User ID to filter data
        meter_id: Meter ID to filter data
        
    Returns:
        float: Predicted usage value for the next day
        str: Error message if prediction fails
    """
    try:
        # Database connection configuration from environment variables
        host = os.getenv('db_host_local')
        user = os.getenv('db_user_local')
        password = os.getenv('db_password_local')
        database = os.getenv('db_name_local')
        port = os.getenv('db_port')

        host_online = os.getenv('db_host_online')
        user_online = os.getenv('db_user_online')
        password_online = os.getenv('db_password_online')
        database_online = os.getenv('db_name_online')


        # Connect to database
        db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        
        cursor = db.cursor()

        # Query to get historical usage data
        query = """
            SELECT date, SUM(usageAmount) AS daily_usage
            FROM usages
            WHERE userID = %s AND meterID = %s
            GROUP BY date
            ORDER BY date;
        """
        
        cursor.execute(query, (user_id, meter_id))
        records = cursor.fetchall()
        
        # Convert result to DataFrame
        df = pd.DataFrame(records, columns=["ds", "y"])

        # Close DB connection
        cursor.close()
        db.close()
        
        # Check if we have enough data for reliable forecasting
        if len(df) < 5:
            return None, "Not enough historical data for prediction."
        
        # Convert date column to datetime format
        df["ds"] = pd.to_datetime(df["ds"])

        # Initialize and train Prophet model
        model = Prophet()
        model.fit(df)
        
        # Create future dataframe (1 day ahead)
        future = model.make_future_dataframe(periods=1, freq="D")
        
        # Make prediction
        forecast = model.predict(future)

        # Extract next day's prediction
        next_day_prediction = forecast.iloc[-1]["yhat"]

        return next_day_prediction, None

    except mysql.connector.Error as db_err:
        return None, f"Database error: {str(db_err)}"
    
    except Exception as e:
        return None, f"Prediction error: {str(e)}"