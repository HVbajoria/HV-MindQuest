import openpyxl
from openpyxl import Workbook

# Create a workbook and select the active worksheet
wb = Workbook()
ws = wb.active
ws.title = "Azure Questions"

# Define the headers for the columns
headers = ["Question", "Option a", "Option b", "Option c", "Option d", "Answer"]

# Add headers to the worksheet
ws.append(headers)

# List of questions with options and answers
questions = [
    (
        "Which of the following Azure services is primarily used for creating and managing containerized applications?",
        "Azure Functions", "Azure Kubernetes Service (AKS)", "Azure Blob Storage", "Azure Logic Apps",
        "Azure Kubernetes Service (AKS)"
    ),
    (
        "In Azure Active Directory (Azure AD), what is the maximum number of directory objects that a free tenant can have?",
        "50,000", "100,000", "500,000", "1,000,000",
        "50,000"
    ),
    (
        "Which Azure service would you use to implement a DevOps pipeline for continuous integration and continuous deployment (CI/CD)?",
        "Azure DevTest Labs", "Azure DevOps", "Azure Site Recovery", "Azure Automation",
        "Azure DevOps"
    ),
    (
        "What is the primary purpose of Azure Traffic Manager?",
        "To manage and monitor network traffic within a virtual network", "To distribute network traffic across multiple Azure regions", "To secure endpoints using a firewall", "To provide DDoS protection for Azure resources",
        "To distribute network traffic across multiple Azure regions"
    ),
    (
        "Which of the following Azure services provides a fully managed relational database with built-in high availability and scalability?",
        "Azure SQL Database", "Azure Blob Storage", "Azure Cosmos DB", "Azure Data Lake",
        "Azure SQL Database"
    ),
    (
        "In Azure, what is the purpose of the Network Security Group (NSG)?",
        "To manage and scale virtual machines (VMs)", "To control inbound and outbound traffic to network interfaces (NICs)", "To provide load balancing for web applications", "To encrypt data at rest",
        "To control inbound and outbound traffic to network interfaces (NICs)"
    ),
    (
        "Which Azure service would you use to build, deploy, and manage APIs?",
        "Azure Logic Apps", "Azure API Management", "Azure Data Factory", "Azure Functions",
        "Azure API Management"
    ),
    (
        "What is the function of Azure Key Vault?",
        "To monitor and analyze log data", "To store and manage cryptographic keys, secrets, and certificates", "To deploy and manage virtual machines", "To provide a distributed cache service",
        "To store and manage cryptographic keys, secrets, and certificates"
    ),
    (
        "Which feature allows you to distribute incoming network traffic across multiple Azure VMs for higher availability?",
        "Azure Traffic Manager", "Azure Load Balancer", "Azure Application Gateway", "Azure Firewall",
        "Azure Load Balancer"
    ),
    (
        "In Azure, what is the primary use of the Azure Resource Manager (ARM) templates?",
        "To automate the deployment and management of resources", "To provide backup and disaster recovery solutions", "To monitor and analyze application performance", "To manage user identities and access",
        "To automate the deployment and management of resources"
    ),
    (
        "Which Azure service provides a fully managed platform for building, deploying, and scaling web apps?",
        "Azure SQL Database", "Azure Web Apps (App Service)", "Azure Virtual Network", "Azure Data Lake",
        "Azure Web Apps (App Service)"
    ),
    (
        "What is the main purpose of Azure Logic Apps?",
        "To build workflows for integrating apps, data, and services", "To provide serverless computing", "To manage and analyze big data", "To secure web applications",
        "To build workflows for integrating apps, data, and services"
    ),
    (
        "Which of the following services would you use to create a distributed, multi-model database with global distribution?",
        "Azure SQL Database", "Azure Cosmos DB", "Azure Data Warehouse", "Azure Table Storage",
        "Azure Cosmos DB"
    ),
    (
        "In Azure, which service would you use to create and manage a distributed, in-memory data store for caching and session storage?",
        "Azure Redis Cache", "Azure Blob Storage", "Azure File Storage", "Azure SQL Database",
        "Azure Redis Cache"
    ),
    (
        "Which Azure service allows you to create and manage virtual networks, subnets, and IP addresses?",
        "Azure Virtual Network (VNet)", "Azure Active Directory", "Azure Service Bus", "Azure Batch",
        "Azure Virtual Network (VNet)"
    )
]

# Add each question to the worksheet
for question in questions:
    ws.append(question)

# Save the workbook
wb.save("azure_questions.xlsx")

print("Excel file 'azure_questions.xlsx' has been created successfully.")