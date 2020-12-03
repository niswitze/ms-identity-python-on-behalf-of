---
page_type: sample
languages:
- python
products:
- azure-active-directory
- microsoft identity platform
description: "This sample demonstrates a Python web application calling a Python web API that then calls the Azure Management API subscriptions endpoint. The web application and api are secured using Azure Active Directory."
urlFragment: ms-identity-python-on-behalf-of
---

# Microsoft identity platform and OAuth 2.0 On-Behalf-Of flow in Python
This repository contains a sample solution that demonstrates how to implement the OAuth 2.0 On-behalf-of flow using the Microsoft Identity platform (MSAL) for Python. 

This solution contains two applications, a UI developed using the Django framework and an API developed using the Flask framework. 

The following list details the steps to run this sample solution locally:

1. Follow the [Register the application and service in Azure AD](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/active-directory/azuread-dev/v1-oauth2-on-behalf-of-flow.md#register-the-application-and-service-in-azure-ad) section in the Azure Docs to create and configure app registrations in Azure Active Directory for the UI and API applications.

    * Ensure the property [accessTokenAcceptedVersion](https://docs.microsoft.com/en-us/azure/active-directory/develop/reference-app-manifest?WT.mc_id=Portal-Microsoft_AAD_RegisteredApps#accesstokenacceptedversion-attribute) has been updated, in both app registration manifests, to have a value of **2**.
>[!NOTE] Only use the [Register the application and service in Azure AD](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/active-directory/azuread-dev/v1-oauth2-on-behalf-of-flow.md#register-the-application-and-service-in-azure-ad) section for configuring the required app registrations in Azure Active Directory from step 1. For examples and further reference, please use the [Microsoft Identity platform](https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/active-directory/develop/v2-oauth2-on-behalf-of-flow.md) documentation instead.

2. Use the production.env files in both applications to create local, development.env, files.

3. Select the Python interpreter for <a href="https://code.visualstudio.com/docs/languages/python">VS Code</a> to use and execute the debugger.
    * For this sample, each application will need to be opened in a seperate VS Code instance.


For more information or assistance on using the On-behalf-of flow with the Python Microsoft Identity library please refer to either the [MSAL On-behalf-of documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow), the [Python MSAL library documentation](https://msal-python.readthedocs.io/en/latest/), or raise an issue in this repository.
