# MSAL On-behalf-of Flow in Python
This repository contains a sample solution that demonstrates how to implement the OAuth 2.0 On-behalf-of flow using the Microsoft Identity library (MSAL) for Python. 

This solution contains two applications, a UI developed using the Django framework and an API developed using the Flask framework. 

The following list details the steps to run this sample solution locally:
<ol>
    <li>
        Follow the <a href="https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/active-directory/azuread-dev/v1-oauth2-on-behalf-of-flow.md">Azure docs</a> to create and configure app registrations in Azure Active Directory for the UI and API applications
    </li>
    <li>
        Use the production.env files in both applications to create local, development.env, files
    </li>
    <li>
        Select the Python interpreter for <a href="https://code.visualstudio.com/docs/languages/python">VS Code</a> to use and execute the debugger
    </li>
</ol>

For more information or assistance on using the On-behalf-of flow with the Python Microsoft Identity library please refer to either the [MSAL On-behalf-of documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-on-behalf-of-flow), the [Python MSAL library documentation](https://msal-python.readthedocs.io/en/latest/), or raise an issue in this repository.