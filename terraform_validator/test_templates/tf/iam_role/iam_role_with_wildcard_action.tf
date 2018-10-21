# Configure the AWS Provider
provider "aws" {
  access_key = "${var.aws_access_key}"
  secret_key = "${var.aws_secret_key}"
  region     = "us-east-1"
}


resource "aws_iam_role" "test_role" {
  name = "test_role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}


#{
#  "AWSTemplateFormatVersion": "2010-09-09",
#  "Resources": {
#    "WildcardActionRole": {
#      "Type": "AWS::IAM::Role",
#      "Properties": {
#        "AssumeRolePolicyDocument": {
#          "Version": "2012-10-17",
#          "Statement": [
#            {
#              "Effect": "Allow",
#              "Principal": {
#                "Service": [
#                  "ec2.amazonaws.com"
#                ]
#              },
#              "Action": "sts:AssumeRole"
#            }
#          ]
#        },
#        "Path": "/",
#        "Policies": [
#          {
#            "PolicyName": "root",
#            "PolicyDocument": {
#              "Version": "2012-10-17",
#              "Statement": [
#                {
#                  "Effect": "Allow",
#                  "Action": "*",
#                  "NotResource": "*"
#                }
#              ]
#            }
#          }
#        ]
#      }
#    }
#  }
#}