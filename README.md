Medicare Application Deployment Pipeline
Project Overview

This project demonstrates a full CI/CD pipeline setup using Jenkins to build, test, and deploy a Medicare application. The pipeline automates the following stages:

    Checkout: Clones the application source code from a GitHub repository.
    Compile: Compiles the application using Maven.
    Sonar Analysis: Analyzes the code quality using SonarQube.
    Build: Builds the application and creates a JAR file using Maven.
    Build and Push Docker Image: Builds a Docker image from the application, tags it, and pushes it to Docker Hub.
    Terraform Apply Test: Creates the necessary infrastructure for the test environment using Terraform.
    Deploy Test Application: Deploys the application to a Kubernetes cluster in the test environment.
    Fetch Test Service Endpoint: Retrieves the external endpoint of the application service in the test environment.
    Run Selenium Test on Test Environment: Executes automated Selenium tests against the deployed application in the test environment.
    Terraform Apply Prod: Creates the necessary infrastructure for the production environment using Terraform.
    Deploy Prod Application: Deploys the application to a Kubernetes cluster in the production environment.
    Fetch Prod Service Endpoint: Retrieves the external endpoint of the application service in the production environment.

Pipeline Structure

The pipeline is defined in a Jenkinsfile and includes the following key components:

    Maven: Used for building and compiling the application.
    SonarQube: Used for code quality analysis.
    Docker: Builds and pushes Docker images to Docker Hub.
    Terraform: Manages infrastructure provisioning for both test and production environments.
    Kubernetes (EKS): Deploys the application to an Amazon EKS cluster.
    Selenium: Runs automated browser tests to validate the deployed application.
