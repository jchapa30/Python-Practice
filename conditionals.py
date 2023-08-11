def main():
    user_requirement = "serverless_computing"
    
    if user_requirement == "file_storage":
        aws_service = "S3"
    elif user_requirement == "virtual_server":
        aws_service = "EC2"
    elif user_requirement == "serverless_computing":
        aws_service = "Lambda"
    else:
        aws_service = "Unknown"
    
    if aws_service != "Unknown":
        print(f"The recommended AWS service for your requirement is: {aws_service}")
    else:
        print(f"Error: The AWS service is {aws_service}")

# Call the main function
main()
