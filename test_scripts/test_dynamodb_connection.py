############################################################################
# Test For local development only!
# Purpose: Quickly check if dynamodb is properly connected to the webapp
# PASS Condition: Success message indicating the DynamoTables it can access
# FAIL Condition: Exception Message
############################################################################
import boto3
import os

# Initialize DynamoDB
dynamodb = boto3.resource('dynamodb')

try:
    # Perform a simple operation such as listing tables
    tables = list(dynamodb.tables.all())
    table_names = [table.name for table in tables]
    print("Success! DynamoDB tables:", table_names)
except Exception as e:
    print(f"Error accessing DynamoDB: {str(e)}")