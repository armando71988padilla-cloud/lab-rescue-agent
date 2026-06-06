# Azure VM Network Recovery Guide Synthetic

Source type: approved synthetic lab recovery guide
Certification: AZ-104
Skill areas: virtual machines, network security groups, connectivity troubleshooting, operational verification

## Recovery pattern: NSG rule blocks approved management path

When a VM is running but the learner cannot connect through the expected management path, inspect network security rules before changing compute settings.

Common evidence:
- VM deployment completes successfully
- VM health status is running
- Connection test to the management path fails
- Effective security rules do not allow required inbound traffic

Likely cause:
- The network security group is missing an inbound allow rule for the approved synthetic management path

Safe recovery steps:
1. Confirm the VM and NSG are intended synthetic lab resources.
2. Inspect effective security rules.
3. Add or repair the least-privilege inbound rule for the approved synthetic management path.
4. Retry connectivity.
5. Verify that no broader-than-required inbound exposure was introduced.

Rollback steps:
1. Record the previous NSG rules before changing them.
2. Remove the new rule if verification fails or if access is too broad.
3. Restore the previous NSG configuration after rollback.

Verification checks:
- Effective rules include the expected inbound allow rule
- Connectivity succeeds through the approved synthetic management path
- No broad inbound exposure is introduced

Safety notes:
- Do not recommend broad inbound access
- Do not expose real public IP addresses
- Use synthetic network identifiers only for demos
