\# Real-Time On-Prem to Amazon S3 Data Ingestion



\## Overview

This project demonstrates a real-time on-premise data ingestion pipeline that continuously generates enterprise-like operational data (audit logs, inventory updates, and transaction records) and streams them to Amazon S3 using the AWS CLI.



The goal is to simulate how organizations migrate live operational data from on-prem systems to cloud storage for analytics, auditing, and archival purposes.



---



\## Architecture

On-premise system (simulated using local file system and Python scripts) generates data at regular intervals.  

The generated data is organized into domain-specific folders:

\- `audit/` – system and compliance logs  

\- `inventory/` – stock and inventory updates  

\- `transactions/` – order and transaction records  



A scheduled AWS CLI sync process uploads new files in near real time to Amazon S3, preserving folder structure.



\*\*Flow:\*\*

On-prem data generation → Local folders → AWS CLI sync → Amazon S3 bucket



---



\## Implementation Details

\- \*\*Data Generation:\*\*  

&nbsp; A Python script continuously generates SAP-like business records every fixed interval (30 seconds).

\- \*\*Streaming Mechanism:\*\*  

&nbsp; The `aws s3 sync` command is used to push newly generated files to S3, simulating real-time ingestion.

\- \*\*Cloud Storage:\*\*  

&nbsp; Amazon S3 stores incoming data under structured prefixes (`audit/`, `inventory/`, `transactions/`) for downstream analytics.



---



\## How to Run

1\. Configure AWS CLI with IAM credentials:

&nbsp;  ```bash

&nbsp;  aws configure
Provide your Access Key, Secret Key, region, and output format when prompted.

Create required AWS resources:

An EC2 Launch Template with the provided user-data script

An Application Load Balancer (ALB)

An Auto Scaling Group (ASG) attached to the ALB target group

These resources can be created via the AWS Management Console or Infrastructure-as-Code tools.

Verify the Auto Scaling setup:

Navigate to the EC2 Auto Scaling Groups console

Confirm that instances are launching successfully

Ensure instances are registered as healthy targets behind the ALB

Access the application:

Copy the ALB DNS name from the EC2 → Load Balancers section

Open the DNS name in a web browser

You should see a response showing:

Instance ID

Hostname

Refreshing the page multiple times demonstrates load balancing across instances.



