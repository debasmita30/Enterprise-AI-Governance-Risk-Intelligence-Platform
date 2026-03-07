## Enterprise AI Governance & Risk Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)
![Dockerized](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![Deployment](https://img.shields.io/badge/Deployment-Cloud_Ready-green)
![License](https://img.shields.io/badge/Status-Production_Style-success)

[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge&logo=render)](https://enterprise-ai-governance-risk.streamlit.app/)

A Dockerized, production-style AI evaluation and governance system designed to help enterprises evaluate, select, deploy, and monitor AI technologies responsibly at scale.

This platform simulates real-world internal AI deployment workflows across IT, Security, Procurement, and Engineering teams.

## Project Overview

Enterprises adopting AI must balance:

Security risk

Compliance requirements

Data residency constraints

Vendor lock-in

Cost efficiency

SLA reliability

Organizational productivity impact

This platform provides a structured, auditable, and role-based governance framework to support enterprise AI decision-making.

Why This Project Matters

Organizations deploying AI internally must:

Compare multiple AI vendors objectively

Quantify tradeoffs

Ensure compliance alignment

Prevent shadow AI adoption

Track deployment impact

Maintain governance audit trails

This project demonstrates structured AI deployment governance rather than experimental AI usage.

## Key Features
Vendor Risk Evaluation Engine

Multi-dimensional risk scoring

Security, compliance, cost, SLA, and lock-in modeling

Monte Carlo cost simulation (300 iterations)

Automated risk categorization (Low / Moderate / High)

Radar visualization of risk profile

Executive PDF report generation

Executive AI Dashboard

Total vendors evaluated

Average risk score

Safest vendor identification

Evaluation history visualization

ID-based traceable analytics

Enterprise Governance Board

Ranked vendor leaderboard

Color-coded risk levels

Filtering by risk category

Status filtering (Approved / Pending)

Versioned evaluation history

Audit-friendly view

Role-Based Workflow System

Admin / Analyst / Viewer roles

Analyst submissions require admin approval

Vendor approval workflow

Soft delete with recovery

Action logging per user

Audit Logging

Every governance action is recorded:

Vendor creation

Approval actions

Soft delete

Recovery

Ensures accountability and traceability across departments.

Export & Reporting

Executive PDF risk reports

Excel export of vendor rankings

Structured deployment summaries

API Benchmark Simulation

Simulates enterprise AI platform evaluation:

Latency distribution

P95 measurement

Throughput simulation

SLA tier classification

System health scoring

Designed to mirror AI deployment performance evaluation workflows.

## Technical Architecture
Frontend

Streamlit SaaS-style UI

Matplotlib visualizations

Styled enterprise dashboard

Backend

SQLite governance database

Role-based authentication (bcrypt)

Structured vendor schema

Audit log tracking

Modeling

Multi-factor weighted risk scoring

Monte Carlo cost simulation

Rule-based compliance scoring

SLA tier modeling

Database Schema
Vendors Table

Stores governance metadata:

Risk dimensions

Final score

Risk category

Status (approved / pending)

Created by

Approved by

Soft delete flag

Timestamp

Audit Logs Table

Tracks governance activity:

User

Action

Vendor

Timestamp

Supports enterprise-grade traceability.

## Deployment
Dockerized Deployment

This application is containerized for production-style deployment.

Build:

docker build -t ai-governance-platform .

Run:

docker run -p 8501:8501 ai-governance-platform

Access:

http://localhost:8501
Cloud Deployment (Render Compatible)

The Docker configuration supports deployment to:

Render

Railway

AWS ECS

Azure Container Apps

Google Cloud Run

The container dynamically binds to the assigned cloud port.

Installation (Local Without Docker)
pip install -r requirements.txt
streamlit run app.py
Demo Credentials
# Admin

Username: admin
Password: admin123

# Analyst

Username: analyst
Password: analyst123

# Viewer

Username: viewer
Password: viewer123

## Enterprise Use Cases

AI vendor procurement evaluation

Internal AI deployment governance

Security risk comparison

Cross-functional AI approval workflows

Compliance-aligned AI adoption

Deployment readiness assessment

## Demonstrated Competencies

AI technology evaluation

Deployment tradeoff analysis

Governance system design

Risk modeling & simulation

Cross-functional workflow automation

Audit-based decision systems

Production containerization

Cloud deployment readiness

## Future Enhancements

Real-time AI API benchmarking integration

PostgreSQL migration for production scalability

Immutable audit ledger

Multi-region compliance mapping

Role-based granular permission controls

CI/CD automation

Kubernetes deployment support

Author

Debasmita Chatterjee
Computer Science Undergraduate
Applied AI | Governance Systems | AI Deployment Strategy
