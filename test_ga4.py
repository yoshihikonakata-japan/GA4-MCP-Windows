import os
from google.analytics.data_v1beta import BetaAnalyticsDataClient
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\パス\to\ga4-mcp-key.json"
client = BetaAnalyticsDataClient()
print("✅ GA4 credentials working!")
