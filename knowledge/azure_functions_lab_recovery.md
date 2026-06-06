# Azure Functions Lab Recovery Guide Synthetic

Source type: approved synthetic lab recovery guide
Certification: AZ-204
Skill areas: Azure Functions, app settings, storage configuration, deployment verification

## Recovery pattern: missing AzureWebJobsStorage

When an Azure Functions lab deploys successfully but the function host cannot start, inspect application settings before changing code.

Common evidence:
- Function host starts but HTTP trigger is unavailable
- Error text mentions AzureWebJobsStorage missing or empty
- Host initialization fails because storage connection cannot be resolved

Likely cause:
- The Function App is missing the AzureWebJobsStorage application setting

Safe recovery steps:
1. Confirm the Function App target is the intended synthetic lab resource.
2. Inspect current application settings.
3. Add or repair AzureWebJobsStorage using a synthetic lab storage account value.
4. Restart the Function App.
5. Verify the HTTP trigger responds successfully.

Rollback steps:
1. Record the previous app setting value before changing it.
2. Restore the previous value if verification fails.
3. Restart the Function App again after rollback.

Verification checks:
- Function host starts without storage configuration errors
- HTTP trigger endpoint responds
- Deployment logs no longer mention missing AzureWebJobsStorage

Safety notes:
- Do not print real connection strings in logs
- Do not commit secrets to Git
- Use synthetic lab identifiers only for demos
