# snowflake_lambda

snowflake like id generator using lambda functions

## Aim
create a sortable id generator - initial format timestamp + machine code (0-9 , can be extended till 1024)

## Usage
use as ids for chat applications


## Learnings 

dynamodb conditional writes 

## How to Deploy

copy paste this code in the lambda handler of your AWS lambda. Attach an API Gateway endpoint with lambda integration to your lambda function and deploy the endpoint, call this endpoint concurrently


## How to Test

call this api endpoint: https://5w3s7x0xy8.execute-api.us-east-1.amazonaws.com/test/id
