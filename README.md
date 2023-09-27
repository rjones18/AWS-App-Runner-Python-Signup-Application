# AWS-App-Runner-Python-Signup-Application

In this project, I crafted a sophisticated Flask application utilizing a synergy of Python, HTML, and CSS. This application seamlessly captures user inputs and archives them in an Amazon DynamoDB table on AWS. Upon each user registration, an alert, powered by AWS's Simple Notification Service (SNS), is dispatched to my email, signaling a fresh user signup.

For an efficient deployment process, I employed AWS App Runner,a fully managed container application service and the codebase maintained in a GitLab repository. Integral to the application's performance monitoring and tracing, I integrated AWS X-Ray, providing real-time insights into the application's operations, helping identify bottlenecks and optimize user experience. The infrastructure is adeptly automated through Terraform, orchestrated via GitLab CI/CD pipelines, bifurcated into two distinct streams:

- Infrastructure/Application Deployment: This pipeline is dedicated to the Docker image construction and the App Runner deployment. It is fortified with unit tests for the Python segments and thorough security assessments on both the application and IAC segments, utilizing tools like Snyk, Bandit, and Pylint.

- Application Dependencies Deployment: This channel focuses on deploying ancillary components, such as the DynamoDB table and SNS. It also integrates Snyk for a meticulous IAC code scan.

Complementing the infrastructure, I established a custom domain via AWS Route 53 and fortified the application with robust SSL/TLS encryption using Certificate Manager.

By harmonizing this avant-garde tech stack with AWS's formidable cloud capabilities, I've architected a Flask application that not only scales effortlessly but also upholds the pinnacle of data privacy and security standards.


## Architecture Breakdown

The Application is broken down into the architecture below:

![python](https://github.com/rjones18/Images/blob/main/Gitlab%20project.png)

