Overview

This project demonstrates a scalable and highly available web application architecture on AWS using EC2 Auto Scaling Groups and an Application Load Balancer (ALB).

EC2 instances are automatically launched using a Launch Template and bootstrapped with a user-data script that installs NGINX and securely retrieves instance metadata using IMDSv2. Incoming traffic is distributed across instances via an internet-facing ALB, demonstrating load balancing and horizontal scaling.

Refreshing the ALB DNS endpoint shows responses from different EC2 instances, proving traffic distribution.

Architecture Components

Amazon EC2 instances running Ubuntu

EC2 Launch Template

Auto Scaling Group (minimum 1, maximum 2 instances)

Application Load Balancer (ALB)

ALB Target Group

NGINX web server

IMDSv2 for secure instance metadata access

User-Data Script

EC2 instances are bootstrapped using a user-data script that:

Updates the system packages

Installs NGINX

Enables and starts the NGINX service

Retrieves instance metadata using IMDSv2

Displays the Instance ID and Hostname on the default web page

Script location in the repository:

user-data/ubuntu-nginx-imdsv2.sh

Prerequisites

An active AWS account

IAM user or role with permissions for:

EC2

Auto Scaling

Elastic Load Balancing

AWS CLI installed and configured

Basic understanding of EC2, ALB, and Auto Scaling concepts

How to Run
Step 1: Configure AWS CLI

Configure the AWS CLI with your credentials, region, and preferred output format.

You will need to provide:

Access Key

Secret Key

AWS region

Output format

Step 2: Create Required AWS Resources

Create the following resources using the AWS Management Console or Infrastructure-as-Code tools:

EC2 Launch Template

Use an Ubuntu AMI

Instance type: t2.micro (free-tier eligible)

Attach the provided user-data script

Application Load Balancer

Internet-facing

Listener on port 80

Target group configured for EC2 instances

Auto Scaling Group

Attach to the ALB target group

Desired capacity: 1

Minimum capacity: 1

Maximum capacity: 2

Step 3: Verify Auto Scaling

Navigate to the EC2 Auto Scaling Groups console

Confirm that instances are launching successfully

Ensure instances are marked healthy in the ALB target group

Step 4: Access the Application

Copy the ALB DNS name from the EC2 → Load Balancers section

Open the DNS name in a web browser

The page will display:

Instance ID

Hostname

Refreshing the page multiple times demonstrates load balancing across instances.

What This Project Demonstrates

EC2 Auto Scaling for high availability

Load balancing using Application Load Balancer

Secure use of IMDSv2

Automated instance bootstrapping with user-data

Real-world AWS infrastructure design principles

Notes

This project focuses on architecture, scalability, and AWS best practices rather than application logic. It is designed to reflect production-style cloud infrastructure commonly used in real-world environments.
