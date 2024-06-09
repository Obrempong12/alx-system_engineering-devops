## 0x19. Postmortem
---
# ShopMate Outage Postmortem
![image](https://github.com/Obrempong12/alx-system_engineering-devops/assets/144380171/2b16745b-44a2-471d-88de-60cd17866f77)

## Issue Summary
**Duration of Outage:**  
Start: March 22, 2024, 14:00 UTC  
End: March 22, 2024, 16:30 UTC  

**Impact:**  
ShopMate's main shopping service was down for 2.5 hours. During this period, 100% of users experienced service unavailability, resulting in an inability to browse products, add items to the cart, or complete purchases.

**Root Cause:**  
A configuration error in the database cluster during a routine update caused a cascade of failures that resulted in the entire service going offline.

## Timeline
- **14:00** - Issue detected: Automated monitoring system alerted the on-call engineer of database connectivity issues.
- **14:05** - Engineer verified the alert and observed widespread service disruption.
- **14:10** - Initial investigation focused on database servers; suspecting network issues.
- **14:20** - Misleading path: Network team checked the switches and routers; no issues found.
- **14:30** - Application team suspected a recent deployment; rolled back changes without success.
- **14:45** - Escalated to the Database team for deeper investigation.
- **15:00** - Database team identified misconfiguration in the cluster setup.
- **15:15** - Misleading path: Attempted to apply a hotfix, which didn't resolve the issue.
- **15:30** - Full rollback of the latest database configuration changes initiated.
- **16:00** - System began to stabilize; partial service restored.
- **16:30** - Full service restored and confirmed by monitoring systems.

## Root Cause and Resolution
**Root Cause:**  
During a routine update, a configuration error was introduced in the database cluster settings. Specifically, a misconfigured replication factor caused the database nodes to lose sync, leading to failures in read and write operations across the cluster.

**Resolution:**  
The Database team rolled back the configuration to the previous stable state. After the rollback, they manually verified the consistency and synchronization of the database nodes, followed by extensive testing to ensure no data was lost and that all services were fully operational.

## Corrective and Preventative Measures
**Improvements/Fixes:**  
- Enhance configuration management practices to prevent similar errors.
- Implement additional monitoring and alerts specifically for database configuration changes.
- Increase redundancy and failover capabilities in the database architecture to handle such issues without complete service disruption.

**Task List:**
1. **Patch Database Cluster Configuration:** Review and patch the database configuration settings.
2. **Add Monitoring:** Implement detailed monitoring for database configuration changes and synchronization status.
3. **Improve Rollback Procedures:** Develop and document a faster rollback process for database configurations.
4. **Training:** Conduct a training session for the engineering teams on new configuration management practices.
5. **Redundancy Enhancement:** Plan and deploy additional database redundancy and failover mechanisms.

---

### Visual Summary
![image](https://github.com/Obrempong12/alx-system_engineering-devops/assets/144380171/e347db40-eccc-41af-8165-1c80fb6a87d4)

#### Humorous Note:
"Who knew that one tiny comma in the database config could make such a big 'splat'? Next time, we'll double-check before hitting 'Save'."

## Contributors
* Peter Kwesi Obrempong Stephenson <https://github.com/Obrempong12/>

---
