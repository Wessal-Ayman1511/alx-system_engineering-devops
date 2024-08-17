# 🛠️ Postmortem Report: NGINX Server Outage Incident

**Date:** August 15, 2024  
**Duration:** 14:30 - 16:00 UTC  
**Affected Service:** Personal Project Website  

---

## Issue Summary

- **Impact:** The personal project website experienced intermittent downtime, causing errors and slow load times for approximately 50% of visitors.
- **Root Cause:** Incorrect configuration of NGINX server settings.

---

## Timeline

- **14:30 UTC:** 🚨 **Issue Detected**  
  Users reported that the website was down. An increase in 502 Bad Gateway errors was observed in the server logs.

- **14:35 UTC:** 🔍 **Initial Investigation**  
  Began investigating the issue. NGINX was not properly routing requests.

- **14:50 UTC:** 🕵️‍♂️ **Investigated Resources**  
  Checked CPU and memory usage; all appeared normal. Assumed the issue might be network-related.

- **15:00 UTC:** 🔄 **Revised Focus**  
  Shifted investigation to NGINX configuration files. Noticed potential errors due to recent changes.

- **15:20 UTC:** 🛠️ **Root Cause Identified**  
  Found that the upstream server addresses in the NGINX configuration were incorrect.

- **15:40 UTC:** ⚙️ **Configuration Fixed**  
  Corrected the upstream server addresses in the NGINX configuration file. Restarted NGINX to apply changes.

- **15:55 UTC:** ✅ **Issue Resolved**  
  Confirmed that the website was back online and performing normally.

- **16:00 UTC:** 📝 **Documentation**  
  Documented the incident for future reference.

---

## Root Cause and Resolution

- **Cause:** Incorrect upstream server addresses in NGINX configuration caused routing failures and 502 Bad Gateway errors.
- **Resolution:** Corrected the upstream server addresses in the NGINX configuration file and restarted NGINX.

---

## Corrective and Preventative Measures

### Improvements/Fixes

- **Configuration Review:** Implement a thorough review process for all configuration changes to avoid errors before they impact the live system.
- **Staging Environment:** Set up a staging environment to test configuration updates before deploying them to production.

### Action Items

1. **Review Configuration Changes:** Ensure all configuration changes are reviewed and validated.
2. **Create Staging Environment:** Establish a staging environment to test NGINX configurations.
3. **Enhance Monitoring:** Add alerts for NGINX errors related to upstream server connections and routing issues.
4. **Document the Incident:** Write a detailed report of the incident, including resolution steps and lessons learned.

---

But of course, it will never occur again, because we're programmers, and we never make errors! 😉
