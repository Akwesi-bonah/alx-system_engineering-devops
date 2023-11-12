# Postmortem: Apache 500 Error Debugging and Resolution

## Issue Summary:
<b>Duration</b>: November 5, 2023, 10:00  November 9, 2023, 12:30 (UTC)
Impact: Apache server returning 500 Internal Server Error, affecting all incoming HTTP requests.

## Timeline:
Detection Time: November 5, 2023, 10:00 (UTC)
Detection Method: Increased error rates observed in server logs, triggering monitoring alerts.

## Actions Taken:
Initiated an immediate investigation into Apache server logs.
Observed recurring patterns of "Premature end of script headers" errors.
Implemented manual debugging using `strace` to trace system calls during the execution of Apache processes.

## Misleading Paths:
Initially suspected issues with PHPFPM due to common 500 errors.
Investigated Apache configurations for syntax errors or misconfigurations, with no conclusive findings.

## Escalation:
Escalated the incident to the system administration team for further collaboration and expertise.

## Resolution:
 Utilized `strace` to identify a file permission issue when Apache attempted to execute a crucial script.
Manually adjusted file permissions to allow Apache to execute the script successfully.
   Automated the permission adjustment using Puppet to prevent future occurrences.

## Root Cause and Resolution:
Root Cause:
Apache was unable to execute a critical script due to incorrect file permissions.

# Resolution:
Adjusted the file permissions to grant the necessary execution rights to the Apache user.
Automated the permission adjustment process using Puppet to ensure consistency and prevent manual errors in the future.
Implemented regular Puppet runs to enforce and maintain correct file permissions.



## Corrective and Preventative Measures:
### Improvements/Fixes:
Automated the file permission adjustment process using Puppet for consistent and repeatable configurations.
Enhanced monitoring to include specific checks for file permission issues in critical directories.
Conducted a review of server configurations to identify and rectify any other potential permission related problems.

### Tasks:
Documented the Puppet manifests for file permission adjustments to ensure clarity and facilitate future modifications.
Conducted Puppet training sessions for relevant team members to ensure proper understanding and utilization.
Scheduled regular audits of Puppet configurations to identify and address any drift from the desired state.

## Conclusion:
The Apache 500 Internal Server Error was traced back to incorrect file permissions on a crucial script. The incident was promptly resolved by manually adjusting permissions and subsequently automated using Puppet for consistent and repeatable configurations. The introduction of automated configuration management not only addressed the immediate issue but also bolstered the system's resilience against similar incidents in the future. Ongoing efforts to enhance monitoring and conduct regular audits will further strengthen the web stack's reliability.
