10. Host-untrusted (VM) software generates a full cacheline memory write request to the same test memory address but with a non-TEE opcode and known data pattern B.

11. Host software verifies that the write returned a TEE opcode in the response.

12. Host-untrusted (VM) software generates a memory read request to the same test memory address but with a non-TEE opcode.

13. Host software verifies that the read returned a TEE opcode in the response and all 1s for the data.

14. Host-trusted TEE (TVM) software generates a memory read request to the same test memory address but with a TEE opcode.

15. Host software verifies that the read returned a TEE opcode in the response and expected data pattern A.

16. Host software issues Set Target TE State to set TE State to 0 for the test memory address.

17. Host-untrusted (VM) software generates a full cacheline memory write request to the same test memory address but with a non-TEE opcode and known data pattern A.

18. Host software verifies that the write returned a non-TEE opcode in the response.

19. Host-untrusted (VM) software generates a memory read request to the same test memory address but with a non-TEE opcode.

20. Host software verifies that the read returned a non-TEE opcode in the response and expected data pattern A.

21. Host-trusted TEE (TVM) software generates a full cacheline memory write request to the same test memory address but with a TEE opcode and known data pattern B.

22. Host software verifies that the write returned a non-TEE opcode in the response.

23. Host-trusted TEE (TVM) software generates a memory read request to the same test memory address but with a TEE opcode.

24. Host software verifies that the read returned a non-TEE opcode in the response and all 1s for the data

25. Host-untrusted (VM) software generates a memory read request to the same test memory address but with a non-TEE opcode.

26. Host software verifies that the read returned a non-TEE opcode in the response and expected data pattern A.

## Pass Criteria:

• TEE/non-TEE opcode returned is correct for all writes and reads

• Read data returned for all reads is as expected

• Data pattern of all 1s returned for reads that have a TE State mismatch

## Fail Conditions:

• Set Target Configuration results in a TSP Error Response

• Lock Target Configuration results in a TSP Error Response

• Pass criteria is not met

## 14.11.7.8 Initiator-based Memory Encryption

This test verifies basic optional initiator-based memory encryption by disabling targetbased encryption.

## Prerequisites:

• Device must support CXL.cachemem TSP security

• Device must support Compliance Mode DOE and SPDM over DOE

• Host software has established a secure SPDM link to the device

• Test 14.11.7.3 passed AND the target reports support for Explicit Out-of-band TE State Changes, Read Access Control, and Write Access Control

## Topologies:

• SHDA

## Test Steps:

1. Host software issues Set Target Configuration to disable target encryption:

a. All Memory Encryption Features Enable flag bits are cleared to 0.

2. Host software receives Set Target Configuration Response.

3. Host software issues Lock Target Configuration to make the configuration immutable and to enable the ability to receive TEE opcodes.

4. Host software receives Lock Target Configuration Response.

5. Host software encrypts data before writing.

6. Host software writes encrypted data to the locked target device with a known data pattern.

7. Host software reads encrypted data from the target.

8. Host software decrypts the data and verifies that the data matches the known data pattern.

## Pass Criteria:

• Data does not match the expected pattern after the data is decrypted by the host

## Fail Conditions:

• Set Target Configuration results in a TSP Error Response

• Lock Target Configuration results in a TSP Error Response

• Pass criteria is not met

## 14.11.7.9 Target-based CKID-based Memory Encryption Invalid CKID Range

This test verifies basic invalid CKID range handling for optional target-based CKIDbased memory encryption when the target supports a limited number of CKIDs. The following TSP-related table is tested:

• Table 11-26, “Target Behavior for Invalid CKID Ranges”

## Prerequisites:

• Device must support CXL.cachemem TSP security

• Device must support Compliance Mode DOE and SPDM over DOE

• Host software has established a secure SPDM link to the device

• Test 14.11.7.3 passed AND the target reports support for target-based CKID-based encryption and the target limits the supported CKID range (CKID Base Required is set in Test 14.11.7.3)

## Topologies:

• SHDA

## Test Steps:

1. Host software issues Set Target Configuration to enable target-based CKID-based memory encryption:

a. Encryption bit and CKID-based Encryption bit shall be set to 1 in the Memory Encryption Features Enable field.

b. Memory Encryption Algorithm Select field has a single algorithm selected that the target will utilize for data-at-rest security. (The selected algorithm shall be one that the target supports, as reported by Get Target Capabilities Response.)

c. CKID Base = Base that the target supports.

d. Number of CKIDs = Number of CKIDs that the target supports – 1, so that CKID Base + Number of CKIDs is out of range.

2. Host software receives Set Target Configuration Response.

3. Host software issues Lock Target Configuration to make the configuration immutable.

4. Host software receives Lock Target Configuration Response.

5. Host software issues Set Target CKID Specific Key to associate a key with a CKID:

a. CKID is assigned within a valid range that the target supports.

b. CKID Type = OSCKID.

c. Validity Flags, Bit[0] set.

d. Data Encryption Key to utilize for the CKID.

6. Host software receives Set Target CKID Specific Key Response.

7. Host-untrusted (VM) software generates a full cacheline memory write request to the test address with a non-TEE opcode, CKID assigned, and known data pattern A.

8. Host software verifies that the write returned a non-TEE opcode in the response.

9. Host-untrusted (VM) software generates a memory read request to the same test address but with a non-TEE opcode and the assigned CKID.

10. Host software verifies that the read returned a non-TEE opcode in the response and the data matches the known data pattern A:

// Attempt to write with CKID out of range

11. Host-untrusted (VM) software generates a full cacheline memory write request to the same test address but with a non-TEE opcode and the CKID = CKID Base + Number of CKIDs, programmed in step 1, using a known data pattern B:

// Verify write was dropped

12. Host-untrusted (VM) software generates a memory read request to the same test address but with a non-TEE opcode using the assigned CKID.

13. Host software verifies that the read returned a non-TEE opcode in the response and the data matches the known data pattern A:

// Attempt to read with CKID out of range

14. Host-untrusted (VM) software generates a memory read request to the same test address but with a non-TEE opcode with the CKID = CKID Base + Number of CKIDs programmed in step 1.

15. Host software verifies that the read returned a non-TEE opcode in the response and the data returns an all 1s pattern.

## Pass Criteria:

• Read data returned for all reads is as expected

## Fail Conditions:

• Set Target Configuration results in a TSP Error Response

• Lock Target Configuration results in a TSP Error Response

• Set Target CKID Specific Key results in a TSP Error Response

• Pass criteria is not met

## 14.11.7.10 Target-based CKID-based Memory Encryption Invalid CKID Type

This test verifies basic invalid CKID Type handling for optional target-based CKID-based memory encryption. The following TSP-related table is tested:

• Table 11-27, “Target Behavior for Verifying CKID Type”

## Prerequisites:

• Device must support CXL.cachemem TSP security

• Device must support Compliance Mode DOE and SPDM over DOE

• Host software has established a secure SPDM link to the device

• Test 14.11.7.3 passed AND the target reports support for target-based CKID-based encryption

## Topologies:

• SHDA

## Test Steps:

1. Host software issues Set Target Configuration to enable target-based CKID-based memory encryption:

a. Encryption bit and CKID-based Encryption bit shall be set to 1 in the Memory Encryption Features Enable field.

b. Memory Encryption Algorithm Select field has a single algorithm selected that the target will utilize for data-at-rest security. (The selected algorithm shall be one that the target supports, as reported by Get Target Capabilities Response.)

c. For targets that limit the CKID range, CKID Base Required is set (see Test 14.11.7.3) and CKID Base and Number of CKIDs is set to a range that the target supports.

2. Host software receives Set Target Configuration Response.

3. Host software issues Lock Target Configuration to make the configuration immutable.

4. Host software receives Lock Target Configuration Response.

5. Host software issues Set Target CKID Specific Key to associate a key with a CKID:

a. CKID is assigned within a valid range that the target supports.

b. CKID Type = OSCKID.

c. Validity Flags, Bit[0] set.

d. Data Encryption Key to utilize for the CKID.

6. Host software receives Set Target CKID Specific Key Response.

7. Host-untrusted (VM) software generates a full cacheline memory write request to the test address with the CKID assigned with a non-TEE opcode using a known data pattern A.

8. Host software verifies that the write returned a non-TEE opcode in the response.

9. Host-untrusted (VM) software generates a memory read request to the same test address but with the CKID assigned with a non-TEE opcode.

10. Host software verifies that the read returned a non-TEE opcode in the response and expected data pattern A.

11. Host-trusted TEE (TVM) software generates a full cacheline memory write request to the same test address but with the CKID assigned with a TEE opcode using a known data pattern B.

12. Host software verifies that the write returned a non-TEE opcode in the response.

13. Host-trusted TEE (TVM) software generates a memory read request to the same test address but with the CKID assigned with a TEE opcode.

14. Host software verifies that the read returned a non-TEE opcode in the response and a fixed all 1s data pattern.Host-untrusted (VM) software generates a memory read request to the same test address but with the CKID assigned with a non-TEE opcode.

15. Host software verifies that the read returned a non-TEE opcode in the response and expected data pattern A.

16. Host software issues Set Target CKID Specific Key to associate a key with a CKID:

a. CKID is assigned within valid range that the target supports.

b. CKID Type = TVMCKID.

c. Validity Flags, Bit[0] set.

d. Data Encryption Key to utilize for the CKID.

17. Host software receives Set Target CKID Specific Key Response.

18. Host-trusted TEE (TVM) software generates a full cacheline memory write request to the same test address but with the CKID assigned with a TEE opcode using a known data pattern A.

19. Host software verifies that the write returned a TEE opcode in the response.

20. Host-trusted TEE (TVM) software generates a memory read request to the same test address but with the CKID assigned with a TEE opcode.

21. Host software verifies that the read returned a TEE opcode in the response and expected data pattern A.

22. Host-untrusted (VM) software generates a full cacheline memory write request to the same test address but with the CKID assigned with a non-TEE opcode using a known data pattern B.

23. Host software verifies that the write returned a TEE opcode in the response.

24. Host-untrusted (VM) software generates a memory read request to the same test address but with the CKID assigned with a non-TEE opcode.

25. Host software verifies that the read returned a TEE opcode in the response and a fixed all 1s data pattern.

26. Host-trusted TEE (TVM) software generates a memory read request to the same test address but with the CKID assigned with a TEE opcode.

27. Host software verifies that the read returned a TEE opcode in the response and expected data pattern A.

## Pass Criteria:

• TEE/non-TEE opcode returned is correct for all writes and reads

• Read data returned for all reads is as expected

## Fail Conditions:

• Set Target Configuration results in a TSP Error Response

• Lock Target Configuration results in a TSP Error Response

• Set Target CKID Specific Key results in a TSP Error Response

• Pass criteria is not met

## 14.11.7.11 Target-based CKID-based Memory Encryption Clearing Keys

This test verifies basic clear key handling for optional target-based CKID-based memory encryption.

## Prerequisites:

• Device must support CXL.cachemem TSP security

• Device must support Compliance Mode DOE and SPDM over DOE

• Host software has established a secure SPDM link to the device

• Test 14.11.7.3 passed AND the target reports support for target-based CKID-based encryption

## Topologies:

• SHDA

## Test Steps:

1. Host software issues Set Target Configuration to enable target-based CKID-based memory encryption:

a. Encryption bit and CKID-based Encryption bit shall be set to 1 in the Memory Encryption Features Enable field.

b. Memory Encryption Algorithm Select field has a single algorithm selected that the target will utilize for data-at-rest security. (The selected algorithm shall be one that the target supports, as reported by Get Target Capabilities Response.)

c. For targets that limit the CKID range, CKID Base Required is set (see Test 14.11.7.3), and CKID Base and Number of CKIDs are both set to a range the target supports.

2. Host software receives Set Target Configuration Response.

3. Host software issues Lock Target Configuration to make the configuration immutable.

4. Host software receives Lock Target Configuration Response.

5. Host software issues Set Target CKID Random Key to associate a key with a CKID:

a. CKID is assigned within a valid range that the target supports.

b. CKID Type = OSCKID.

c. Validity Flags, Bit[0] set.

d. Data Encryption Key Entropy X to utilize for the CKID.

6. Host software receives Set Target CKID Random Key Response.

7. Host-untrusted (VM) software generates a full cacheline memory write request to the test address with the CKID assigned with a non-TEE opcode using a known data pattern A.

8. Host software verifies that the write returned a non-TEE opcode in the response.

9. Host-untrusted (VM) software generates a memory read request to the same test address but with the CKID assigned with a non-TEE opcode.

10. Host software verifies that the read returned a non-TEE opcode in the response and expected data pattern A.

11. Host software issues Clear Target CKID Key to disassociate a key from a CKID:

a. CKID assigned in valid range supported by the target.

12. Host software receives Clear Target CKID Key Response.

13. Host-untrusted (VM) software generates a memory read request to the same test address but with the CKID assigned with a non-TEE opcode.

14. Host software verifies that the read returned a non-TEE opcode in the response and the expected data pattern is NOT data pattern A.

15. Host software issues Set Target CKID Random Key to associate a key with a CKID:

a. CKID is assigned within a valid range that the target supports.

b. CKID Type = OSCKID.

c. Validity Flags, Bit[0] set.

d. Data Encryption Key Entropy X to utilize for the CKID.

16. Host software receives Set Target CKID Random Key Response.

17. Host-untrusted (VM) software generates a memory read request to the same test address but with the CKID assigned with a non-TEE opcode.

18. Host software verifies that the read returned a non-TEE opcode in the response and the expected data pattern is NOT data pattern A.

## Pass Criteria:

• TEE/non-TEE opcode returned is correct for all writes and reads

• Read data returned for all reads is as expected

## Fail Conditions:

• Set Target Configuration results in a TSP Error Response

• Lock Target Configuration results in a TSP Error Response

• Set Target CKID Specific Key results in a TSP Error Response

• Clear Target CKID Key results in a TSP Error Response

• Pass criteria is not met

## 14.11.7.12 Target-based Range-based Memory Encryption

This test verifies the basic setting and clearing of encryption keys for optional target based range-based memory encryption.

Prerequisites:

• Device must support CXL.cachemem TSP security

• Device must support Compliance Mode DOE and SPDM over DOE

• Host software has established a secure SPDM link to the device

• Test 14.11.7.3 passed AND the target reports support for target-based rangebased encryption

## Topologies:

• SHDA

## Test Steps:

1. Host software issues Set Target Configuration to enable target-based range-based memory encryption:

a. Encryption bit and Range-based Encryption bit shall be set to 1 in the Memory Encryption Features Enable field.

b. Memory Encryption Algorithm Select field has a single algorithm selected that the target will utilize for data-at-rest security. (The selected algorithm shall be one that the target supports, as reported by Get Target Capabilities Response.)

2. Host software receives Set Target Configuration Response.

3. Host software issues Lock Target Configuration to make the configuration immutable.

4. Host software receives Lock Target Configuration Response.

5. Host software issues Set Target Range Specific Key to associate a key with the first memory range:

a. Range ID = 0.

b. Range Start and Range End fields describe the test address range on the host.

c. Validity Flags, Bit[0] set.

d. Data Encryption Key to utilize for the memory Range ID.

6. Host software receives Set Target Range Specific Key Response.

7. Host software generates a full cacheline memory write request for the test address range using a known data pattern A.

8. Host software generates a memory read request to the same test address range.

9. Host software verifies that the data matches the known data pattern A.

10. Host software issues Clear Target Range Key to remove the association of a key with the memory range:

a. Range ID = 0.

11. Host software receives Clear Target Range Key Response.

12. Host software generates a full cacheline memory write request for the test address range using a known data pattern B.

13. Host software generates a memory read request to the same test address range.

14. Host software verifies that the data does NOT match the known data pattern A or B.

## Pass Criteria:

• Data does not match expected pattern after any reads

## Fail Conditions:

• Set Target Configuration results in a TSP Error Response

• Lock Target Configuration results in a TSP Error Response

• Set Target Range Specific Key results in a TSP Error Response

• Clear Target Range Key results in a TSP Error Response

• Pass criteria is not met

## 14.11.7.13 Target-based Range-based Memory Encryption Clearing Keys

This test verifies basic clear key handling for optional target-based range-based memory encryption.

## Prerequisites:

• Device must support CXL.cachemem TSP security

• Device must support Compliance Mode DOE and SPDM over DOE

• Host software has established a secure SPDM link to the device

• Test 14.11.7.3 passed AND the target reports support for target-based rangebased encryption

## Topologies:

• SHDA

## Test Steps:

1. Host software issues Set Target Configuration to enable target-based range-based memory encryption:

a. Encryption bit and Range-based Encryption bit shall be set to 1 in the Memory Encryption Features Enable field.

b. Memory Encryption Algorithm Select field has a single algorithm selected that the target will utilize for data-at-rest security. (The selected algorithm shall be one that the target supports, as reported by Get Target Capabilities Response.)

2. Host software receives Set Target Configuration Response.

3. Host software issues Lock Target Configuration to make the configuration immutable.

4. Host software receives Lock Target Configuration Response.

5. Host software issues Set Target Range Random Key to associate a key with a memory range:

a. Range ID = 0.

b. Range Start/Range End = Valid 4-KB-aligned block within the HDM memory range that contains the test address.

6. Host software receives Set Target Range Random Key Response.

7. Host-untrusted (VM) software generates a full cacheline memory write request to the test address with an address within the range for which the key was set with a non-TEE opcode using a known data pattern A.

8. Host software verifies that the write returned a non-TEE opcode in the response.

9. Host-untrusted (VM) software generates a memory read request to the same test address but with a non-TEE opcode.

10. Host software verifies that the read returned a non-TEE opcode in the response and expected data pattern A.

11. Host software issues Clear Target Range Key to disassociate the test address from the key:

a. Range ID = 0.

12. Host software receives Clear Target Range Key Response.

13. Host-untrusted (VM) software generates a memory read request to the same test address but with a non-TEE opcode.

14. Host software verifies that the read returned a non-TEE opcode in the response and the expected data pattern is NOT data pattern A.

15. Host software issues Set Target Range Random Key to associate a key with a memory range:

a. Range ID = 0.

b. Range Start/Range End = Valid 4-KB-aligned block within the HDM memory range that contains the test address.

16. Host software receives Set Target Range Random Key Response.

17. Host-untrusted (VM) software generates a memory read request to the same test address range but with a non-TEE opcode.

18. Host software verifies that the read returned a non-TEE opcode in the response and the expected data pattern is NOT data pattern A.

## Pass Criteria:

• TEE/non-TEE opcode returned is correct for all writes and reads

• Read data returned for all reads is as expected

## Fail Conditions:

• Set Target Configuration results in a TSP Error Response

• Lock Target Configuration results in a TSP Error Response

• Set Target Range Random Key results in a TSP Error Response

• Clear Target Range Key results in a TSP Error Response

• Pass criteria is not met

## 14.12 Reliability, Availability, and Serviceability

RAS testing is dependent on being able to inject and correctly detect the injected errors. For this testing, it is required that the host and the device both support error injection capabilities.

Certain Device/Host capabilities of error injection are required to enable the RAS tests. First, the required capabilities and configurations are provided. Then, the actual test procedures are laid out. Because these capabilities may only be firmware accessible, currently these are implementation specific. However, future revisions of this specification may define these under an additional capability structure.

The following register describes the required functionalities. All the registers that have an RWL attribute should be locked when DVSEC Test Lock is set to 1.

Table 14-28. Register 1 — CXL.cachemem LinkLayerErrorInjection

<table><tr><td>Bit</td><td>Attribute</td><td>Description</td></tr><tr><td>0</td><td>RWL</td><td>CachePoisonInjectionStart:Software writes 1 to this bit to trigger a single poison injection on a CXL.cache message in the Tx direction. Hardware must override the poison field in the data header slot of the corresponding message (D2H if device, H2D if Host). This bit is required only if CXL.cache protocol is supported.</td></tr><tr><td>1</td><td>RO</td><td>CachePoisonInjectionBusy:Hardware loads 1 to this bit when the Start bit is written. Hardware must clear this bit to indicate that it has indeed finished poisoning a packet. Software is permitted to poll on this bit to determine when hardware has finished poison injection. This bit is required only if CXL.cache protocol is supported.</td></tr><tr><td>2</td><td>RWL</td><td>MemPoisonInjectionStart:Software writes 1 to this bit to trigger a single poison injection on a CXL.mem message in the Tx direction. Hardware must override the poison field in the data header slot of the corresponding message. This bit is required only if CXL.mem protocol is supported.</td></tr><tr><td>3</td><td>RO</td><td>MemPoisonInjectionBusy:Hardware loads 1 to this bit when the Start bit is written. Hardware must clear this bit to indicate that it has indeed finished poisoning a packet. Software is permitted to poll on this bit to determine when hardware has finished poison injection. This bit is required only if CXL.mem protocol is supported.</td></tr><tr><td>4</td><td>RWL</td><td>IOPoisonInjectionStart:Software writes 1 to this bit to trigger a single poison injection on a CXL.io message in the Tx direction. Hardware must override the poison field in the data header slot of the corresponding message.</td></tr><tr><td>5</td><td>RO</td><td>IOPoisonInjectionBusy:Hardware loads 1 to this bit when the Start bit is written. Hardware must clear this bit to indicate that it has indeed finished poisoning a packet. Software is permitted to poll on this bit to determine when hardware has finished poison injection.</td></tr><tr><td>7:6</td><td>RWL</td><td>CacheMemCRCInjection:Software writes to these bits to trigger CRC error injections. The number of CRC bits flipped is as follows:00b = Disable. No CRC errors are injected.01b = Single bit flipped in the CRC field for n subsequent Tx flits, where n is the value in CacheMemCRCInjectionCount.10b = Two bits flipped in the CRC field for n subsequent Tx flits, where n is the value in CacheMemCRCInjectionCount.11b = Three bits flipped in the CRC field for n subsequent Tx flits, where n is the value in CacheMemCRCInjectionCount.The specific bit positions that are flipped are implementation specific.This field is required if the CXL.cache protocol or CXL.mem protocol is supported.</td></tr><tr><td>9:8</td><td>RWL</td><td>CacheMemCRCInjectionCount:Software writes to these bits to program the number of CRC injections. This field must be programmed by software before OR at the same time as the CacheMemCRCInjection field. The number of flits where CRC bits are flipped is as follows:00b = Disable. No CRC errors are injected.01b = CRC injection is only for one flit. The CacheMemCRCInjectionBusy bit is cleared after one injection.10b = CRC injection is for two flits in succession. The CacheMemCRCInjectionBusy bit is cleared after two injections.11b = CRC injection is for three flits in succession. The CacheMemCRCInjectionBusy bit is cleared after three injections.This field is required if the CXL.cache protocol or CXL.mem protocol is supported.</td></tr><tr><td>10</td><td>RO</td><td>CacheMemCRCInjectionBusy:Hardware loads 1 to this bit when the associated Start bit is written. Hardware must clear this bit to indicate that it has indeed finished CRC injections. Software is permitted to poll on this bit to determine when hardware has finished CRC injection. This bit is required if the CXL.cache protocol or CXL.mem protocol is supported.</td></tr></table>

Table 14-29. Register 2 — CXL.io LinkLayer Error Injection

<table><tr><td>Bit</td><td>Attribute</td><td>Description</td></tr><tr><td>0</td><td>RWL</td><td>IOPoisonInjectionStart: Software writes 1 to this bit to trigger a single poison injection on a CXL.io message in the Tx direction. Hardware must override the poison field in the data header slot of the corresponding message.</td></tr><tr><td>1</td><td>RO</td><td>IOPoisonInjectionBusy: Hardware loads 1 to this bit when the Start bit is written. Hardware must clear this bit to indicate that it has indeed finished poisoning a packet. Software is permitted to poll on this bit to determine when hardware has finished poison injection.</td></tr><tr><td>2</td><td>RWL</td><td>FlowControlErrorInjection: Software writes 1 to this bit to trigger a Flow Control error on CXL.io only. Hardware must override the Flow Control DLLP.</td></tr><tr><td>3</td><td>RO</td><td>FlowControlInjectionBusy: Hardware loads 1 to this bit when the Start bit is written. Hardware must clear this bit to indicate that it has indeed finished Flow Control error injections. Software is permitted to poll on this bit to determine when hardware has finished Flow Control error injection.</td></tr></table>

Table 14-30. Register 3 — Flex Bus LogPHY Error Injections

<table><tr><td>Bit</td><td>Attribute</td><td>Description</td></tr><tr><td>0</td><td>RWL</td><td>CorrectableProtocolIDErrorInjection: Software writes 1 to this bit to trigger a correctable Protocol ID error on any CXL flit that is issued by the FlexBus LogPHY. Hardware must override the Protocol ID field in the flit.</td></tr><tr><td>1</td><td>RWL</td><td>UncorrectableProtocolIDErrorInjection: Software writes 1 to this bit to trigger an uncorrectable Protocol ID error on any CXL flit that is issued by the FlexBus LogPHY. Hardware must override the Protocol ID field in the flit.</td></tr><tr><td>2</td><td>RWL</td><td>UnexpectedProtocolIDErrorInjection: Software writes 1 to this bit to trigger an unexpected Protocol ID error on any CXL flit that is issued by the FlexBus LogPHY. Hardware must override the Protocol ID field in the flit.</td></tr><tr><td>3</td><td>RO</td><td>ProtocolIDInjectionBusy: Hardware loads 1 to this bit when the Start bit is written. Hardware must clear this bit to indicate that it has indeed finished Protocol ID error injections. Software is permitted to poll on this bit to determine when hardware has finished Protocol ID error injection. Software should only program one of the bits between the correctable, uncorrectable, and unexpected Protocol ID error injection bits.</td></tr></table>

## 14.12.1 RAS Configuration

## 14.12.1.1 AER Support

## Prerequisites:

• Errors must be reported via the PCIe AER mechanism

• AER is as an optional Extended Capability

## Test Steps:

1. Read through each Extended Capability (EC) Structure for the Endpoint, and then locate the EC structure for that type.

## Pass Criteria:

• AER Extended Capability Structure exists

## Fail Conditions:

• AER Extended Capability Structure does not exist

## 14.12.1.2 CXL.io Poison Injection from Device to Host

Prerequisites:

• CXL device must support Algorithm 1a

• CXL device must support Link Layer Error Injection capabilities for CXL.io

## Test Steps:

1. Set up the device for Multiple Write streaming:

a. Write a pattern {64{8’hFF}} to cache-aligned Address A1.

b. Write a Compliance mode DOE to inject poison:

Table 14-31. CXL.io Poison Injection from Device to Host — I/O Poison Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>8h</td><td>1</td><td>Request Code</td><td>6, Poison Injection</td></tr><tr><td>9h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>Ch</td><td>1</td><td>Protocol</td><td>0</td></tr></table>

c. Write Compliance mode DOE with the following request:

Table 14-32. CXL.io Poison Injection from Device to Host — Multi-Write Streaming Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>08h</td><td>1</td><td>Request Code</td><td>3, Multiple Write Streaming</td></tr><tr><td>09h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>0Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>0Ch</td><td>1</td><td>Protocol</td><td>0</td></tr><tr><td>0Dh</td><td>1</td><td>Virtual Address</td><td>0</td></tr><tr><td>0Eh</td><td>1</td><td>Self-checking</td><td>0</td></tr><tr><td>0Fh</td><td>1</td><td>Verify Read Semantics</td><td>0</td></tr><tr><td>10h</td><td>1</td><td>Num Increments</td><td>0</td></tr><tr><td>11h</td><td>1</td><td>Num Sets</td><td>0</td></tr><tr><td>12h</td><td>1</td><td>Num Loops</td><td>1</td></tr><tr><td>13h</td><td>1</td><td>Reserved</td><td></td></tr><tr><td>14h</td><td>8</td><td>Start Address</td><td>A1</td></tr><tr><td>1Ch</td><td>8</td><td>Write Address</td><td>0</td></tr><tr><td>24h</td><td>8</td><td>WriteBackAddress</td><td>A2 (Must be distinct from A1)</td></tr><tr><td>2Ch</td><td>8</td><td>Byte Mask</td><td>FFFF FFFF FFFF FFFFh</td></tr><tr><td>34h</td><td>4</td><td>Address Increment</td><td>0</td></tr><tr><td>38h</td><td>4</td><td>Set Offset</td><td>0</td></tr><tr><td>3Ch</td><td>4</td><td>Pattern &quot;P&quot;</td><td>AAh</td></tr><tr><td>40h</td><td>4</td><td>Increment Pattern &quot;B&quot;</td><td>0</td></tr></table>

## Pass Criteria:

• Receiver logs the poisoned received error

• Test software is permitted to read Address A1 to observe the written pattern

## Fail Conditions:

• Receiver does not log the poisoned received error

## 14.12.1.3 CXL.cache Poison Injection

## 14.12.1.3.1 Device to Host Poison Injection

## Prerequisites:

• Device is CXL.cache capable

• CXL device must support Algorithm 1a

• CXL device must support Link Layer Error Injection capabilities for CXL.cache

## Test Steps:

1. Set up the device for Multiple Write streaming:

a. Write a pattern {64{8’hFF}} to cache-aligned Address A1.

b. Write a Compliance mode DOE to inject poison:

Table 14-33. Device to Host Poison Injection — Cache Poison Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>8h</td><td>1</td><td>Request Code</td><td>6, Poison Injection</td></tr><tr><td>9h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>Ch</td><td>1</td><td>Protocol</td><td>1</td></tr></table>

c. Write Compliance mode DOE with the following request:

Table 14-34. Device to Host Poison Injection — Multi-Write Streaming Request (Sheet 1 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>08h</td><td>1</td><td>Request Code</td><td>3, Multiple Write Streaming</td></tr><tr><td>09h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>0Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>0Ch</td><td>1</td><td>Protocol</td><td>1</td></tr><tr><td>0Dh</td><td>1</td><td>Virtual Address</td><td>0</td></tr><tr><td>0Eh</td><td>1</td><td>Self-checking</td><td>0</td></tr><tr><td>0Fh</td><td>1</td><td>Verify Read Semantics</td><td>0</td></tr><tr><td>10h</td><td>1</td><td>Num Increments</td><td>0</td></tr><tr><td>11h</td><td>1</td><td>Num Sets</td><td>0</td></tr></table>

Table 14-34. Device to Host Poison Injection — Multi-Write Streaming Request (Sheet 2 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>12h</td><td>1</td><td>Num Loops</td><td>1</td></tr><tr><td>13h</td><td>1</td><td>Reserved</td><td></td></tr><tr><td>14h</td><td>8</td><td>Start Address</td><td>A1</td></tr><tr><td>1Ch</td><td>8</td><td>Write Address</td><td>0</td></tr><tr><td>24h</td><td>8</td><td>WriteBackAddress</td><td>A2 (Must be distinct from A1)</td></tr><tr><td>2Ch</td><td>8</td><td>Byte Mask</td><td>FFFF FFFF FFFF FFFFh</td></tr><tr><td>34h</td><td>4</td><td>Address Increment</td><td>0</td></tr><tr><td>38h</td><td>4</td><td>Set Offset</td><td>0</td></tr><tr><td>3Ch</td><td>4</td><td>Pattern &quot;P&quot;</td><td>AAh</td></tr><tr><td>40h</td><td>4</td><td>Increment Pattern &quot;B&quot;</td><td>0</td></tr></table>

## Pass Criteria:

• Receiver (host) logs the poisoned received error

• Test software is permitted to read Address A1 to observe the written pattern

## Fail Conditions:

• Receiver does not log the poisoned received error

## 14.12.1.3.2 Host to Device Poison Injection

This test ensures that if a CXL.cache device receives poisoned data from the host, the device returns the poison indication in the write-back phase. The Receiver on the CXL device must also log and escalate the poisoned received error.

## Prerequisites:

• Device is CXL.cache capable

• CXL device must support Algorithm 1a with DirtyEvict and RdOwn semantics

## Test Steps:

1. Repeatedly write a predetermined pattern to cacheline-aligned Address A1 (example pattern — all 1s — {64{8’hFF}}). A1 should belong to Host-attached memory.

a. Write a Compliance mode DOE to the host to inject poison:

Table 14-35. Host to Device Poison Injection — Cache Poison Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>8h</td><td>1</td><td>Request Code</td><td>6, Poison Injection</td></tr><tr><td>9h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>Ch</td><td>1</td><td>Protocol</td><td>1</td></tr></table>

## Pass Criteria:

• Receiver (device) logs the poisoned received error

• Test software is permitted to read Address A1 to observe the written pattern

## Fail Conditions:

• Receiver does not log the poisoned received error

## 14.12.1.4 CXL.cache CRC Injection

## 14.12.1.4.1 Device to Host CRC Injection

Test Equipment:

• Protocol Analyzer

## Prerequisites:

• Device is CXL.cache capable

• CXL device must support Algorithm 1a

• CXL device must support Link Layer Error Injection capabilities for CXL.cache

## Test Steps:

1. Setup is the same as Test 14.3.6.1.2.

a. Write a Compliance mode DOE to inject CRC:

## Table 14-36. Device to Host CRC Injection — Cache Poison Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>8h</td><td>1</td><td>Request Code</td><td>7, CRC Injection</td></tr><tr><td>9h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>Ch</td><td>1</td><td>Protocol</td><td>1</td></tr></table>

## Pass Criteria:

• Same as Test 14.3.6.1.2

• Monitor and verify that CRC errors are injected (using the Protocol Analyzer), and that Retries are triggered as a result

## Fail Conditions:

• Same as Test 14.3.6.1.2

## 14.12.1.4.2 Host to Device CRC Injection

Test Equipment:

• Protocol Analyzer

Prerequisites:

• Device is CXL.cache capable

• CXL device must support Algorithm 1a

## Test Steps:

1. Setup is the same as Test 14.3.6.1.2.

a. While a test is running, software will periodically write a Compliance mode DOE to inject CRC:

Table 14-37. Host to Device CRC Injection — Cache Poison Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>8h</td><td>1</td><td>Request Code</td><td>7, CRC Injection</td></tr><tr><td>9h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>Ch</td><td>1</td><td>Protocol</td><td>1</td></tr></table>

## Pass Criteria:

• Same as Test 14.3.6.1.2

• Monitor and verify that CRC errors are injected (using the Protocol Analyzer), and that Retries are triggered as a result

## Fail Conditions:

• Same as Test 14.3.6.1.2

## 14.12.1.5 CXL.mem Link Poison Injection

## 14.12.1.5.1 Host to Device Poison Injection

Prerequisites:

• Device is CXL.mem capable

Test Steps:

1. Write {64{8’hFF}} to Address B1 from the host. B1 must belong to deviceattached memory.

2. Set up the host Link Layer for poison injection:

a. Write a Compliance mode DOE to the host to inject poison:

Table 14-38. Host to Device Poison Injection — Mem Poison Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>8h</td><td>1</td><td>Request Code</td><td>6, Poison Injection</td></tr><tr><td>9h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>Ch</td><td>1</td><td>Protocol</td><td>3</td></tr></table>

3. Write {64{8’hAA}} to Address B1 from the host.

## Pass Criteria:

• Receiver (device) logs the poisoned received error

• Test software is permitted to read Address B1 to observe the written pattern

Fail Conditions:

• Receiver does not log the poisoned received error

## 14.12.1.6 CXL.mem CRC Injection

## 14.12.1.6.1 Host to Device CRC Injection

Test Equipment:

• Protocol Analyzer

Prerequisites:

• Device is CXL.mem capable

Test Steps:

1. Write {64{8’hFF}} to Address B1 from the host (B1 must belong to deviceattached memory).

2. Set up the host Link Layer for CRC injection.

a. Write a Compliance mode DOE to the host to inject CRC errors:

Table 14-39. Host to Device CRC Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>8h</td><td>1</td><td>Request Code</td><td>7, CRC Injection</td></tr><tr><td>9h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>Ch</td><td>1</td><td>Protocol</td><td>3</td></tr></table>

3. Write {64{8’hAA}} to Address B1 from the host.

4. Read Address B1 from the host, and compare to {64{8’hAA}}.

## Pass Criteria:

• Read data == {64{8’hAA}}

• CRC error and Retry observed on the link (Protocol Analyzer used for observation)

Fail Conditions:

• Read data != {64{8’hAA}}

## 14.12.1.7 Flow Control Injection

This is an optional but strongly recommended test that is applicable only for CXL.io.

## 14.12.1.7.1 Device to Host Flow Control Injection

Prerequisites:

• CXL device must support Algorithm 1a

• CXL device must support Link Layer Error Injection capabilities

Test Steps:

1. Setup is the same as Test 14.3.6.1.1.

2. Write a Compliance mode DOE to the Device to set up flow control injection:

Table 14-40. Compliance Mode Flow Control Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>8h</td><td>1</td><td>Request Code</td><td>8, Flow Control Injection</td></tr><tr><td>9h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>Ch</td><td>1</td><td>Protocol</td><td>1</td></tr></table>

3. Write a Compliance DOE request to set up Algorithm 1a traffic:

Table 14-41. Compliance Mode Multiple Write Streaming Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>08h</td><td>1</td><td>Request Code</td><td>3, Multiple Write Streaming</td></tr><tr><td>09h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>0Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>0Ch</td><td>1</td><td>Protocol</td><td>1</td></tr><tr><td>0Dh</td><td>1</td><td>Virtual Address</td><td>0</td></tr><tr><td>0Eh</td><td>1</td><td>Self-checking</td><td>0</td></tr><tr><td>0Fh</td><td>1</td><td>Verify Read Semantics</td><td>0</td></tr><tr><td>10h</td><td>1</td><td>Num Increments</td><td>0</td></tr><tr><td>11h</td><td>1</td><td>Num Sets</td><td>0</td></tr><tr><td>12h</td><td>1</td><td>Num Loops</td><td>1</td></tr><tr><td>13h</td><td>1</td><td>Reserved</td><td></td></tr><tr><td>14h</td><td>8</td><td>Start Address</td><td>A1</td></tr><tr><td>1Ch</td><td>8</td><td>Write Address</td><td>0</td></tr><tr><td>24h</td><td>8</td><td>WriteBackAddress</td><td>A2 (Must be distinct from A1)</td></tr><tr><td>2Ch</td><td>8</td><td>Byte Mask</td><td>FFFF FFFF FFFF FFFFh</td></tr><tr><td>34h</td><td>4</td><td>Address Increment</td><td>0</td></tr><tr><td>38h</td><td>4</td><td>Set Offset</td><td>0</td></tr><tr><td>3Ch</td><td>4</td><td>Pattern &quot;P&quot;</td><td>AAh</td></tr><tr><td>40h</td><td>4</td><td>Increment Pattern &quot;B&quot;</td><td>0</td></tr></table>

Pass Criteria:

• Same as Test 14.3.6.1.1

Fail Conditions:

• Same as Test 14.3.6.1.1

14.12.1.7.2 Host to Device Flow Control Injection

Prerequisites:

• CXL device must support Algorithm 1a

Test Steps:

1. Setup is the same as Test 14.3.6.1.1.

2. Write a Compliance mode DOE to the host to set up flow control injection:

Table 14-42. Compliance Mode Flow Control Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>8h</td><td>1</td><td>Request Code</td><td>8, Flow Control Injection</td></tr><tr><td>9h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>Ch</td><td>1</td><td>Protocol</td><td>1</td></tr></table>

3. Write {64{8’hAA}} to Address B1 from the host.

4. Read Address B1 from the host, and compare to {64{8’hAA}}.

Pass Criteria:

• Same as Test 14.3.6.1.1

Fail Conditions:

• Same as Test 14.3.6.1.1

## 14.12.1.8 Unexpected Completion Injection

This is an optional but strongly recommended test that is applicable only for CXL.io.

14.12.1.8.1 Device to Host Unexpected Completion Injection

Prerequisites:

• CXL device must support Algorithm 1a

• CXL device must support Device Error Injection capabilities

Test Steps:

1. Write a Compliance mode DOE to set up Unexpected Completion:

Table 14-43. Compliance Mode Unexpected MAC Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>8h</td><td>1</td><td>Request Code</td><td>Bh, Unexpected MAC injection</td></tr><tr><td>9h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>Ch</td><td>1</td><td>Protocol</td><td>1</td></tr></table>

2. Write a Compliance DOE request to set up Algorithm 1a traffic:

Table 14-44. Compliance Mode Multiple Write Streaming Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>08h</td><td>1</td><td>Request Code</td><td>3, Multiple Write Streaming</td></tr><tr><td>09h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>0Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>0Ch</td><td>1</td><td>Protocol</td><td>1</td></tr><tr><td>0Dh</td><td>1</td><td>Virtual Address</td><td>0</td></tr><tr><td>0Eh</td><td>1</td><td>Self-checking</td><td>0</td></tr><tr><td>0Fh</td><td>1</td><td>Verify Read Semantics</td><td>0</td></tr><tr><td>10h</td><td>1</td><td>Num Increments</td><td>0</td></tr><tr><td>11h</td><td>1</td><td>Num Sets</td><td>0</td></tr><tr><td>12h</td><td>1</td><td>Num Loops</td><td>1</td></tr><tr><td>13h</td><td>1</td><td>Reserved</td><td></td></tr><tr><td>14h</td><td>8</td><td>Start Address</td><td>A1</td></tr><tr><td>1Ch</td><td>8</td><td>Write Address</td><td>0</td></tr><tr><td>24h</td><td>8</td><td>WriteBackAddress</td><td>A2 (Must be distinct from A1)</td></tr><tr><td>2Ch</td><td>8</td><td>Byte Mask</td><td>FFFF FFFF FFFF FFFFh</td></tr><tr><td>34h</td><td>4</td><td>Address Increment</td><td>0</td></tr><tr><td>38h</td><td>4</td><td>Set Offset</td><td>0</td></tr><tr><td>3Ch</td><td>4</td><td>Pattern &quot;P&quot;</td><td>AAh</td></tr><tr><td>40h</td><td>4</td><td>Increment Pattern &quot;B&quot;</td><td>0</td></tr></table>

Pass Criteria:

• Unexpected completion error is logged

Fail Conditions:

• No errors are logged

## 14.12.1.9 Completion Timeout

This is an optional but strongly recommended test that is applicable only for CXL.io.

14.12.1.9.1 Device to Host Completion Timeout

Prerequisites:

• CXL device must support Algorithm 1a

• CXL device must support Device Error Injection capabilities

Test Steps:

1. Write a Compliance mode DOE to the Device to set up MAC Delay injection:

Table 14-45. Compliance Mode MAC Delay Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>8h</td><td>1</td><td>Request Code</td><td>Ah, MAC Delay injection</td></tr><tr><td>9h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>Ch</td><td>1</td><td>Protocol</td><td>1</td></tr></table>

2. Write a Compliance DOE request to set up Algorithm 1a traffic:

Table 14-46. Compliance Mode Multiple Write Streaming Request (Sheet 1 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td><td></td></tr><tr><td>08h</td><td>1</td><td>Request Code</td><td>3, Multiple Write Streaming</td></tr><tr><td>09h</td><td>1</td><td>Version</td><td>2</td></tr><tr><td>0Ah</td><td>2</td><td>Reserved</td><td></td></tr><tr><td>0Ch</td><td>1</td><td>Protocol</td><td>1</td></tr><tr><td>0Dh</td><td>1</td><td>Virtual Address</td><td>0</td></tr><tr><td>0Eh</td><td>1</td><td>Self-checking</td><td>0</td></tr><tr><td>0Fh</td><td>1</td><td>Verify Read Semantics</td><td>0</td></tr><tr><td>10h</td><td>1</td><td>Num Increments</td><td>0</td></tr><tr><td>11h</td><td>1</td><td>Num Sets</td><td>0</td></tr><tr><td>12h</td><td>1</td><td>Num Loops</td><td>1</td></tr><tr><td>13h</td><td>1</td><td>Reserved</td><td></td></tr><tr><td>14h</td><td>8</td><td>Start Address</td><td>A1</td></tr><tr><td>1Ch</td><td>8</td><td>Write Address</td><td>0</td></tr><tr><td>24h</td><td>8</td><td>WriteBackAddress</td><td>A2 (Must be distinct from A1)</td></tr><tr><td>2Ch</td><td>8</td><td>Byte Mask</td><td>FFFF FFFF FFFF FFFFh</td></tr><tr><td>34h</td><td>4</td><td>Address Increment</td><td>0</td></tr></table>

Table 14-46. Compliance Mode Multiple Write Streaming Request (Sheet 2 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td><td>Value</td></tr><tr><td>38h</td><td>4</td><td>Set Offset</td><td>0</td></tr><tr><td>3Ch</td><td>4</td><td>Pattern &quot;P&quot;</td><td>AAh</td></tr><tr><td>40h</td><td>4</td><td>Increment Pattern &quot;B&quot;</td><td>0</td></tr></table>

Pass Criteria:

• Completion timeout is logged and escalated to the error manager

Fail Conditions:

• No errors are logged and data corruption is seen

## 14.12.1.10 CXL.mem Media Poison Injection

## 14.12.1.10.1Host to Memory Device Poison Injection

Prerequisites:

• Device is CXL.mem capable

## Test Steps:

1. Select error injection target address Device Physical Address (DPA) that belongs to the DUT.

2. Translate the DPA to the Host Physical Address (HPA).

3. Request Poison error injection via Enable Memory Device Poison Injection DOE specifying the DPA where the error is to be injected.

4. Poll on the Poison Injection Response DOE. Successful completion status indicates that the device has injected the poison into memory.

5. Host performs a memory read at the error injection target HPA and the device responds to the read with the poison indicator set.

## Pass Criteria:

• Receiver (device) logs the poisoned received error

• When injecting poison into persistent memory regions of the CXL.mem device:

— The device shall add the new physical address to the device’s poison list and the error source should be set to an injected error and reported through the Get Poison List command

— In addition, the device should add an appropriate poison creation event to its internal Informational Event Log, update the Event Status register, and if configured, interrupt the host

— Poison shall be persistent across warm reset or cold reset until explicitly cleared by overwriting the cacheline with new data with the poison indicator cleared

## Fail Conditions:

• Receiver does not log the poisoned received error

## 14.12.1.11 CXL.mem LSA Poison Injection

## .12.1.11.1Host to Memory Device LSA Poison Injection

## Prerequisites:

• Device is CXL.mem capable

## Test Steps:

1. Select error injection LSA byte offset that belongs to the DUT.

2. Request LSA Poison error injection via Enable Memory Device LSA Poison Injection Compliance DOE, specifying the LSA byte offset where the error is to be injected.

3. Poll on the Poison Injection Response DOE. Successful completion status indicates that the device has injected the poison into memory.

4. Host performs a GetLSA mailbox command that includes the LSA byte offset at which the poison was injected into the LSA. The device responds to the read with an error in the mailbox GetLSA command and appropriate error log generation.

## Pass Criteria:

• Receiver (device) errors the GetLSA command to the injected LSA byte offset

• When injecting poison into the persistent memory Label Storage Area of the CXL.mem device:

— Device should add an appropriate poison creation event to its internal Informational Event Log, update the Event Status register, and if configured, interrupt the host

— Poison shall be persistent across warm reset or cold reset until explicitly cleared by a SetLSA with new data that overwrites the poisoned data at the original poison injection LSA byte offset

## Fail Conditions:

• Receiver does not log the poisoned received error

## 14.12.1.12 CXL.mem Device Health Injection

## 14.12.1.12.1Host to Device Poison Injection

## Prerequisites:

• Applicable only for devices that support Device Health Injection with the DOE transport

• Device is CXL.mem capable

## Test Steps:

1. Request device health injection via Enable CXL.mem Device Health Injection Compliance DOE, specifying the health status field to inject.

2. Poll on the Poison Injection Response DOE. Successful completion status indicates that the device has injected the health status change into the device.

3. Host verifies device health status changes by inspecting Event Log Records and device health status changes.

## Pass Criteria:

• Device notifies host of state change through appropriate Event Log Records, and the resulting change in device health can be verified through the Get Health Info command

## Fail Conditions:

• Receiver does not see correct event logs or change in health status

## 14.13 Memory Mapped Registers

## 14.13.1 CXL Capability Header

## Test Steps:

1. The base address for these registers is at Offset 4K from the Register Base Low and Register Base High found in the Register Locator DVSEC.

2. Read Offset 00h, Length 4 bytes.

3. Decode this into:

Bits Variable 15:0 CXL\_Capability\_ID 19:16 CXL\_Capability\_Version 23:20 CXL\_Cache\_Mem\_Version 31:24 Array\_Size

4. Save the Array\_Size to be used for finding the remaining capability headers in the subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0001h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>1h</td><td>Always</td></tr><tr><td>CXL_Cache_Mem_Version</td><td>1h</td><td>Always</td></tr></table>

## Pass Criteria:

• Test 14.8.2 passed

• Verify Conditions are met

## Fail Conditions:

• Verify Conditions failed

## 14.13.2 CXL RAS Capability Header

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

Bits Variable 15:0 CXL\_Capability\_ID 19:16 CXL\_Capability\_Version

## 31:20 CXL\_RAS\_Capability\_Pointer

4. Save CXL\_RAS\_Capability\_Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0002h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>2h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.3 CXL Security Capability Header

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

Bits Variable 15:0 CXL\_Capability\_ID 19:16 CXL\_Capability\_Version 31:20 CXL\_Security\_Capability\_Pointer

4. Save CXL\_Security\_Capability\_Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0003h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>1h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.4 CXL Link Capability Header

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

Bits Variable 15:0 CXL\_Capability\_ID 19:16 CXL\_Capability\_Version 31:20 CXL\_Link\_Capability\_Pointer

4. Save CXL\_Link\_Capability\_Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0004h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>2h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.5 CXL HDM Decoder Capability Header

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

Bits Variable 15:0 CXL\_Capability\_ID 19:16 CXL\_Capability\_Version 31:20 CXL\_HDM\_Decoder\_Capability\_Pointer

4. Save CXL\_HDM\_Decoder\_Capability\_Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0005h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>3h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.6 CXL Extended Security Capability Header

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

Bits Variable 15:0 CXL\_Capability\_ID 19:16 CXL\_Capability\_Version 31:20 CXL\_Extended\_Security\_Capability\_Pointer

4. Save CXL\_Extended\_Security\_Capability\_Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0006h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>2h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.7 CXL IDE Capability Header

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

Bits Variable 15:0 CXL\_Capability\_ID 19:16 CXL\_Capability\_Version 31:20 CXL IDE Capability Pointer

4. Save CXL IDE Capability Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0007h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>2h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.8 CXL HDM Decoder Capability Register

Prerequisites:

• HDM Decoder Capability is implemented

## Test Steps:

1. Read register, CXL\_HDM\_Interleave\_Capability\_Pointer + Offset 00h, Length 2 bytes.

2. Decode this into:

Bits Variable 3:0 Decoder Count 7:4 Target Count

3. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>Decoder Count</td><td>&lt; Dh</td><td>Always</td></tr><tr><td>Target Count</td><td>&lt; 9h</td><td>Always</td></tr></table>

## Pass Criteria:

• 14.13.5 Device Present passed

• Verify Conditions are met

## Fail Conditions:

• Verify Conditions failed

## 14.13.9 CXL HDM Decoder Commit

## Prerequisites:

• HDM Decoder Capability is implemented

## Test Steps:

1. Program an address range in the Decoder[m+1].Base and Decoder[m+1].Size registers such that:

— Decoder[m+1].Base ≥ (Decoder[m].Base+Decoder[m].Size), and

— Decoder[m+1].Base ≤ Decoder[m+1].Base+Decoder[m+1].Size

2. Program distinct Target Port Identifiers for Interleave Way=0 through $2 ^ { * * } \mathrm { I W } \mathrel { - } 1$ (not applicable to Devices).

3. Set the Commit bit in the Decoder[m+1].Control register.

## Pass Criteria:

• Committed bit in the Decoder[m+1].Control register is set

• Error Not Committed bit in the Decoder[m+1].Control register is not set

## Fail Conditions:

• Committed bit in the Decoder[m+1].Control register is not set within 10 ms

• Error Not Committed bit in the Decoder[m+1].Control register is set

## 14.13.10 CXL HDM Decoder Zero Size Commit

## Prerequisites:

• HDM Decoder Capability is implemented

## Test Steps:

1. Program 0 in the Decoder[m].Size register.

2. Set the Commit bit in the Decoder[m].Control register.

## Pass Criteria:

• Committed bit in the Decoder[m].Control register is set

• Error Not Committed bit in the Decoder[m].Control register is not set

## Fail Conditions:

• Committed bit in the Decoder[m].Control register is not set within 10 ms

• Error Not Committed bit in the Decoder[m].Control register is set

## 14.13.11 CXL Snoop Filter Capability Header

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

Bits Variable 15:0 CXL\_Capability\_ID 19:16 CXL\_Capability\_Version 31:20 CXL Snoop Filter Capability Pointer

4. Save CXL Snoop Filter Capability Pointer, which is used in subsequent tests.

5. Verify

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0008h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>1h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.12 CXL Device Capabilities Array Register

This test locates all the CXL Device Capability Headers, in addition to the Verify Conditions listed below.

## Test Steps:

1. The base address for this register is obtained from the Register Locator DVSEC.

2. Read Offset 00h, Length 8 bytes.

3. Decode this into:

Bits Variable 15:0 Capability ID 19:16 Version 47:32 Capabilities Count

4. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>Capability ID</td><td>0000h</td><td>Always</td></tr><tr><td>Version</td><td>01h</td><td>Always</td></tr></table>

5. For N, where N ranges from 1 through Capabilities\_Count, find each Capability Header Element by reading 2 bytes at Offset N\*10h.

6. Decode this into:

## Bits Variable

15:0 CXL\_Capability\_ID\_Arr[N]

7. If CXL\_Capability\_ID\_Arr[N] == 0001h, save Offset N\*10h as Device\_Status\_Registers\_Capabilities\_Header\_Base.

8. If CXL\_Capability\_ID\_Arr[N] == 0002h, save Offset N\*10h as Primary\_Mailbox\_Registers\_Capabilities\_Header\_Base.

9. If CXL\_Capability\_ID\_Arr[N] == 0003h, save Offset N\*10h as Secondary\_Mailbox\_Registers\_Capabilities\_Header\_Base.

10. If CXL\_Capability\_ID\_Arr[N] == 4000h, save Offset N\*10h as Memory\_Device\_Status\_Registers\_Capabilities\_Header\_Base.

## Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.13 Device Status Registers Capabilities Header Register

## Test Steps:

1. Read offset Device\_Status\_Registers\_Capabilities\_Header\_Base, Length 4 bytes. Device\_Status\_Registers\_Capabilities\_Header\_Base is obtained in the test performed in Test 14.13.12.

2. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr></table>

3. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0001h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>1h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

## Fail Conditions:

• Verify Conditions failed

## 14.13.14 Primary Mailbox Registers Capabilities Header Register

## Test Steps:

1. Read offset Primary\_Mailbox\_Registers\_Capabilities\_Header\_Base, Length 4 bytes. Primary\_Mailbox\_Registers\_Capabilities\_Header\_Base is obtained in the test performed in Test 14.13.12.

2. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr></table>

3. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0002h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>1h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.15 Secondary Mailbox Registers Capabilities Header Register

## Test Steps:

1. Read offset Secondary\_Mailbox\_Registers\_Capabilities\_Header\_Base, Length 4 bytes. Secondary\_Mailbox\_Registers\_Capabilities\_Header\_Base is obtained in the test performed in Test 14.13.12.

2. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr></table>

3. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0003h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>1h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.16 Memory Device Status Registers Capabilities Header Register

## Test Steps:

1. Read offset Memory\_Device\_Status\_Registers\_Capabilities\_Header\_Base, Length 4 bytes. Memory\_Device\_Status\_Registers\_Capabilities\_Header\_Base is obtained in the test performed in Test 14.13.12.

2. Find the CXL Device Capability Header register as described in Test 14.13.12, step 5, Length 4 bytes.

3. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr></table>

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>4000h</td><td>Always</td></tr></table>

<table><tr><td>CXL_Capability_Version</td><td>1h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.17 CXL Timeout and Isolation Capability Header

## Prerequisites:

• Device supports 256B Flit mode and 256B Flit mode is enabled

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr><tr><td>31:20</td><td>CXL_Timeout_and_Isolation_Capability_Pointer</td></tr></table>

4. Save CXL\_Timeout\_and\_Isolation\_Capability\_Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>09h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>01h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.18 CXL.cachemem Extended Register Header

## Prerequisites:

• Device supports 256B Flit mode and 256B Flit mode is enabled

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr></table>

31:20 CXL.cachemem Extended Register Capability Pointer

4. Save CXL.cachemem Extended Register Capability Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0Ah</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>01h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

## Fail Conditions:

• Verify Conditions failed

## 14.13.19 CXL BI Route Table Capability Header

## Prerequisites:

• Device supports 256B Flit mode and 256B Flit mode is enabled

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr><tr><td>31:20</td><td>CXL BI Route Table Capability Pointer</td></tr></table>

4. Save CXL BI Route Table Capability Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0Bh</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>01h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.20 CXL BI Decoder Capability Header

## Prerequisites:

• Device supports 256B Flit mode and 256B Flit mode is enabled

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr><tr><td>31:20</td><td>CXL BI Decoder Capability Pointer</td></tr></table>

4. Save CXL BI Decoder Capability Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0Ch</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>01h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.21 CXL Cache ID Route Table Header

Prerequisites:

• Device supports 256B Flit mode and 256B Flit mode is enabled

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr><tr><td>31:20</td><td>CXL Cache ID Route Table Capability Pointer</td></tr></table>

4. Save CXL Cache ID Route Table Capability Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0Dh</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>01h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.22 CXL Cache ID Decoder Capability Header

Prerequisites:

• Device supports 256B Flit mode and 256B Flit mode is enabled

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr><tr><td>31:20</td><td>CXL Cache ID Local Decoder Capability Pointer</td></tr></table>

4. Save CXL Cache ID Local Decoder Capability Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0Eh</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>01h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.13.23 CXL Extended HDM Decoder Capability Header

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr><tr><td>31:20</td><td>CXL Extended HDM Decoder Capability Pointer</td></tr></table>

4. Save CXL Extended HDM Decoder Capability Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0Fh</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>03h</td><td>Always</td></tr></table>

## Pass Criteria:

• Verify Conditions are met

## Fail Conditions:

• Verify Conditions failed

## 14.13.24 CXL Extended Metadata Capability Header

## Test Steps:

1. Find this capability by reading all the elements within the Array\_Size.

2. Read this element (1 DWORD).

3. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>15:0</td><td>CXL_Capability_ID</td></tr><tr><td>19:16</td><td>CXL_Capability_Version</td></tr><tr><td>31:20</td><td>CXL Extended Metadata Capability Pointer</td></tr></table>

4. Save CXL Extended Metadata Capability Pointer, which is used in subsequent tests.

5. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>CXL_Capability_ID</td><td>0010h</td><td>Always</td></tr><tr><td>CXL_Capability_Version</td><td>1h</td><td>Always</td></tr></table>

Pass Criteria:

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.14

## Memory Device Tests

This section covers tests that are applicable to devices that support the CXL.mem protocol.

## 14.14.1 DVSEC CXL Range 1 Size Low Registers

## Prerequisites:

• Not applicable to FM-owned LD

• Device is CXL.mem capable

## Test Steps:

1. Read Configuration Space for DUT, CXL\_DEVICE\_DVSEC\_BASE + Offset 1Ch, Length 2 bytes.

2. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>7:5</td><td>Memory_Class</td></tr><tr><td>12:8</td><td>Desired_Interleave</td></tr></table>

<table><tr><td colspan="3">3. Verify:</td></tr><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>Memory_Class</td><td>010b</td><td>Always</td></tr><tr><td>Desired_Interleave</td><td>00h, 01h, or 02h</td><td>Always</td></tr><tr><td>Desired_Interleave</td><td>03h, 04h, 05h, 06h, or 07h</td><td>CXL 2.0 and higher</td></tr></table>

## Pass Criteria:

• Test 14.8.4 passed

• Verify Conditions are met

## Fail Conditions:

• Verify Conditions failed

## 14.14.2 DVSEC CXL Range 2 Size Low Registers

## Prerequisites:

• Not applicable to FM-owned LD

• Device is CXL.mem capable

• HDM\_Count=10b

## Inputs:

• Type: Volatile or Non-volatile

• Class: Memory or Storage

## Test Steps:

1. Read Configuration Space for DUT, CXL\_DEVICE\_DVSEC\_BASE + Offset 2Ch, Length 2 bytes.

## 2. Decode this into:

<table><tr><td>Bits</td><td>Variable</td></tr><tr><td>4:2</td><td>Media_Type</td></tr><tr><td>7:5</td><td>Memory_Class</td></tr><tr><td>12:8</td><td>Desired_Interleave</td></tr></table>

3. Verify:

<table><tr><td>Variable</td><td>Value</td><td>Condition</td></tr><tr><td>Media_Type</td><td>000b, 001b, or 010b</td><td>Always</td></tr><tr><td>Memory_Class</td><td>000b, 001b, or 010b</td><td>Always</td></tr><tr><td>Desired_Interleave</td><td>0h, 1h or 2h</td><td>Always</td></tr><tr><td>Desired_Interleave</td><td>03h, 04h, 05h, 06h, or 07h</td><td>CXL 2.0 and higher</td></tr></table>

## Pass Criteria:

• Test 14.8.4 passed

• Verify Conditions are met

## Fail Conditions:

• Verify Conditions failed

## Sticky Register Tests

This section covers tests applicable to registers that are sticky through a reset.

## 14.15.1 Sticky Register Test

## Test Steps:

1. Read and record the value of the following ROS registers for step 5:

<table><tr><td colspan="2">Error Capabilities and Control Register (Offset 14h)</td></tr><tr><td>Bits</td><td>Variable</td></tr><tr><td>5:0</td><td>First_Error_Pointer</td></tr></table>

<table><tr><td colspan="2">Header Log Registers (Offset 18h)</td></tr><tr><td>Bits</td><td>Variable</td></tr><tr><td>511:0</td><td>Header Log</td></tr></table>

Register contents may or may not be 0.

2. Set the following RWS registers to settings as per list and record the written values for step 5.

## RWS Registers and settings:

Uncorrectable Error Mask Register (Offset 04h)

<table><tr><td>Bits</td><td>Variable</td><td>Settings</td></tr><tr><td>11:0</td><td>Error Mask registers</td><td>Set to FFFh</td></tr><tr><td>14:14</td><td>Internal_Error_Mask</td><td>Set to 1</td></tr><tr><td>15:15</td><td>CXL_IDE_Tx_Mask</td><td>Set to 1</td></tr><tr><td>16:16</td><td>CXL_IDE_Rx_Mask</td><td>Set to 1</td></tr></table>

## Uncorrectable Error Severity Register (Offset 08h)

<table><tr><td>Bits</td><td>Variable</td><td>Settings</td></tr><tr><td>11:0</td><td>Error Severity registers</td><td>Set to FFFh</td></tr><tr><td>14:14</td><td>Internal_Error_Severity</td><td>Set to 1</td></tr><tr><td>15:15</td><td>CXL_IDE_Tx_Severity</td><td>Set to 1</td></tr><tr><td>16:16</td><td>CXL_IDE_Rx_Severity</td><td>Set to 1</td></tr></table>

## Correctable Error Mask Register (Offset 10h)

<table><tr><td>Bits</td><td>Variable</td><td>Settings</td></tr><tr><td>6:0</td><td>Error Mask registers</td><td>Clear to 00h</td></tr></table>

Error Capabilities and Control Register (Offset 14h)

<table><tr><td>Bits</td><td>Variable</td><td>Settings</td></tr><tr><td>13:13</td><td>Poison_Enabled</td><td>Set to 1</td></tr></table>

## CXL Link Layer Capability Register (Offset 00h)

<table><tr><td>Bits</td><td>Variable</td><td>Settings</td></tr><tr><td>3:0</td><td>CXL Link Version Supported</td><td>Set to 2h</td></tr><tr><td>15:8</td><td>LLR Wrap Value Supported</td><td>Set to FFh</td></tr></table>

Intention is to set the register to a nonzero value.

CXL Link Layer Control and Status Register (Offset 08h)

<table><tr><td>Bits</td><td>Variable</td><td>Settings</td></tr><tr><td>1:1</td><td>LL_Init_Stall</td><td>Set to 1</td></tr><tr><td>2:2</td><td>LL_Crd_Stall</td><td>Set to 1</td></tr></table>

CXL Link Layer Rx Credit Control Register (Offset 10h)

<table><tr><td>Bits</td><td>Variable</td><td>Settings</td></tr><tr><td>9:0</td><td>Cache Req Credits</td><td>Set to 3FFh</td></tr><tr><td>19:10</td><td>Cache Rsp Credits</td><td>Set to 3FFh</td></tr><tr><td>29:20</td><td>Cache Data Credits</td><td>Set to 3FFh</td></tr><tr><td>39:30</td><td>Mem Req_Rsp Credits</td><td>Set to 3FFh</td></tr><tr><td>49:40</td><td>Mem Data Credits</td><td>Set to 3FFh</td></tr><tr><td>59:50</td><td>BI Credits</td><td>Set to 3FFh</td></tr></table>

CXL Link Layer Ack Timer Control Register (Offset 28h)

<table><tr><td>Bits</td><td>Variable</td><td>Settings</td></tr><tr><td>7:0</td><td>Ack Force Threshold</td><td>Set to FFh</td></tr><tr><td>17:8</td><td>Ack or CRD Flush Retimer</td><td>Set to 1FFh</td></tr></table>

CXL Link Layer Defeature Register (Offset 30h)

<table><tr><td>Bits</td><td>Variable</td><td>Settings</td></tr><tr><td>0:0</td><td>MDH Disable</td><td>Set to 1</td></tr></table>

DVSEC CXL Control2 (Offset 10h)

<table><tr><td>Bits</td><td>Variable</td><td>Settings</td></tr><tr><td>4:4</td><td>Desired Volatile HDM State after Hot Reset</td><td>Set to 1 if DVSEC CXL Capability3 (Offset 38h) bit[3] Volatile HDM State after Hot Reset - Configurability == 1</td></tr></table>

3. Issue a link Hot Reset.  
4. Wait for the link to train back to CXL.

5. Verify:

a. ROS register values before and after link Hot Reset are matching.

b. RWS register values before and after link Hot Reset are matching.

## Pass Criteria:

• Test 14.8.2 passed

• Verify Conditions are met

Fail Conditions:

• Verify Conditions failed

## 14.16 Device Capability and Test Configuration Control

Implementations are expected to provision a Data Object Exchange (DOE) Interface to enable compliance capabilities.

## 14.16.1 CXL Device Test Capability Advertisement

Figure 14-19. PCIe DVSEC for Test Capability

<table><tr><td rowspan="8"></td><td>31</td><td>16</td><td>15</td><td>0</td></tr><tr><td colspan="4">PCI Express Extended Capability Header</td></tr><tr><td colspan="4">Designated Vendor-specific Header 1</td></tr><tr><td colspan="2">DVSEC CXL Test Lock</td><td colspan="2">Designated Vendor-specific Header 2</td></tr><tr><td colspan="4">DVSEC CXL Test Capability 1</td></tr><tr><td colspan="2">Reserved</td><td colspan="2">DVSEC CXL Test Capability 2</td></tr><tr><td colspan="4">DVSEC CXL Test Configuration Base Low</td></tr><tr><td colspan="4">DVSEC CXLTest Configuration Base High</td></tr></table>

To advertise Test capabilities, the standard DVSEC register fields should be set as below:

Table 14-47. DVSEC Registers

<table><tr><td>Register</td><td>Bit Location</td><td>Field</td><td>Value</td></tr><tr><td rowspan="3">Designated Vendor-Specific Header 1 (Offset 04h)</td><td>15:0</td><td>DVSEC Vendor ID</td><td>1E98h</td></tr><tr><td>19:16</td><td>DVSEC Revision</td><td>0h</td></tr><tr><td>31:20</td><td>DVSEC Length</td><td>1Ch</td></tr><tr><td>Designated Vendor-Specific Header 2 (Offset 08h)</td><td>15:0</td><td>DVSEC ID</td><td>00Ah</td></tr></table>

Table 14-48. DVSEC CXL Test Lock (Offset 0Ah)

<table><tr><td>Bit</td><td>Attribute</td><td>Description</td></tr><tr><td>0</td><td>RWO</td><td>TestLock: Software writes 1 to lock the relevant test configuration registers.</td></tr><tr><td>15:1</td><td>N/A</td><td>Reserved</td></tr></table>

Table 14-49. DVSEC CXL Test Configuration Base Low (Offset 14h)

<table><tr><td>Bit</td><td>Attribute</td><td>Description</td></tr><tr><td>0</td><td>RO</td><td>MemorySpaceIndicator: The test configuration registers are in memory space.Device must hardwire this bit to 0.</td></tr><tr><td>2:1</td><td>RO</td><td>Type00b = Base register is 32 bits wide and can be mapped anywhere in the 32-bit address space01b = Reserved10b = Base register is 64 bits wide and can be mapped anywhere in the 64-bit address space11b = Reserved</td></tr><tr><td>3</td><td>RO</td><td>Reserved: Device must hardwire this bit to 0.</td></tr><tr><td>31:4</td><td>RW</td><td>BaseLow: Bits [31:4] of the base address where the test configuration registers exist.</td></tr></table>

Table 14-50. DVSEC CXL Test Configuration Base High (Offset 18h)

<table><tr><td>Bit</td><td>Attribute</td><td>Description</td></tr><tr><td>31:0</td><td>RW</td><td>BaseHigh: Bits[63:32] of the base address where the test configuration registers exist.</td></tr></table>

## 14.16.2 Debug Capabilities in Device

## 14.16.2.1 Error Logging

The following capabilities in a device are strongly recommended to support ease of verification and compliance testing.

A device that supports self-checking must include an error status and header log register with the following fields:

Table 14-51. Register 9 — ErrorLog1 (Offset 40h)

<table><tr><td>Bit</td><td>Attribute</td><td>Description</td></tr><tr><td>31:0</td><td>RW</td><td>ExpectedPattern: Expected data pattern as per device hardware.</td></tr><tr><td>63:32</td><td>RW</td><td>ObservedPattern: Observed data pattern as per device hardware.</td></tr></table>

Table 14-52. Register 10 — ErrorLog2 (Offset 48h)

<table><tr><td>Bit</td><td>Attribute</td><td>Description</td></tr><tr><td>31:0</td><td>RW</td><td>ExpectedPattern: Expected data pattern as per device hardware.</td></tr><tr><td>63:32</td><td>RW</td><td>ObservedPattern: Observed data pattern as per device hardware.</td></tr></table>

Table 14-53. Register 11 — ErrorLog3 (Offset 50h)

<table><tr><td>Bit</td><td>Attribute</td><td>Description</td></tr><tr><td>7:0</td><td>RW</td><td>ByteOffset: First byte offset within the cacheline where the data mismatch was observed.</td></tr><tr><td>15:8</td><td>RW</td><td>LoopNum: Loop number where data mismatch was observed.</td></tr><tr><td>16</td><td>RW1C</td><td>ErrorStatus: Set to 1 by device if data mismatch was observed.</td></tr></table>

## 14.16.2.2 Event Monitors

It is strongly recommended that a device advertise at least two event monitors, which can be used to count device-defined events. An event monitor consists of two 64-bit registers:

• An event controller: EventCtrl

• An event counter: EventCount

The usage model is for software to program EventCtrl to count an event of interest, and then read the EventCount to determine how many times the event has occurred. At a minimum, a device must implement the ClockTicks event. When the ClockTicks event is selected via the event controller, the event counter will increment once every clock cycle, based on the application layer’s clock. Further suggested events may be published in the future. Examples of other events that a device may choose to implement are:

• Number of times a particular opcode is sent or received

• Number of retries or CRC errors

• Number of credit returns sent or received

• Device-specific events that may help visibility on the platform or with statistical calculation of performance

Table 14-54 and Table 14-55 list the EventCtrl and EventCount register formats, respectively.

Table 14-54. Register 12 — EventCtrl (Offset 60h)

<table><tr><td>Bit</td><td>Attribute</td><td>Description</td></tr><tr><td>7:0</td><td>RW</td><td>EventSelect:Field that is used to select which of the available events should be counted in the paired EventCount register $^{1}$ .</td></tr><tr><td>15:8</td><td>RW</td><td>SubEventSelect:Field that is used to select which sub-conditions of an event should be counted in the paired EventCount register $^{1}$ . This field is a bitmask, where each bit represents a different condition. The EventCount should increment if any of the selected sub-conditions occurs.For example, an event might be Transactions Received, with three sub-conditions of Read, Write and Completion.</td></tr><tr><td>16</td><td>N/A</td><td>Reserved</td></tr><tr><td>17</td><td>RW</td><td>Reset:When set to 1, the paired EventCount register $^{1}$  will be cleared to all 0s. Writing a 0 to this bit has no effect.</td></tr><tr><td>18</td><td>RW</td><td>EdgeDetect0 = Counter will increment once within each cycle that the event has occurred1 = Counter will increment when a 0 to 1 transition (i.e., rising edge) is detected</td></tr><tr><td>63:19</td><td>N/A</td><td>Reserved</td></tr></table>

1. See Table 14-55.

Table 14-55. Register 13 — EventCount (Offset 68h)

<table><tr><td>Bit</td><td>Attribute</td><td>Description</td></tr><tr><td>63:0</td><td>RO</td><td>EventCount: Hardware load register that is updated with a running count of the occurrences of the event programmed in the EventCtrl register. The count monotonically increases unless software explicitly writes the count to a lower value or writes to the Reset bit in the paired EventCtrl register (see Table 14-54).</td></tr></table>

## 14.16.3 Compliance Mode DOE

Function 0 of a CXL device must support the DOE mailbox for the compliance modes to be controlled through it. The Vendor ID must be set to the CXL Vendor ID to indicate that this Object type is defined by the CXL specification. The Data Object Type must be cleared to 00h to advertise that this is a Compliance Mode type of data object.

Table 14-56. Compliance Mode — Data Object Header

<table><tr><td>Bits Location</td><td>Field</td><td>Value</td></tr><tr><td>15:0</td><td>Vendor ID</td><td>1E98h</td></tr><tr><td>23:16</td><td>Data Object Type</td><td>00h</td></tr></table>

Table 14-57. Compliance Mode Return Values

<table><tr><td>Value</td><td>Description</td><td>Value</td><td>Description</td></tr><tr><td>0000 0000h</td><td>Success</td><td>0000 0005h</td><td>Target Busy</td></tr><tr><td>0000 0001h</td><td>Not Authorized</td><td>0000 0006h</td><td>Target Not Initialized</td></tr><tr><td>0000 0002h</td><td>Unknown Failure</td><td>0000 0007h</td><td>Invalid Address Specified</td></tr><tr><td>0000 0003h</td><td>Unsupported Injection Function</td><td>0000 0008h</td><td>Invalid Injection Parameter</td></tr><tr><td>0000 0004h</td><td>Internal Error</td><td></td><td></td></tr></table>

## 14.16.3.1 Compliance Mode Capability

Request and response pair for determining the device’s compliance capabilities.

Table 14-58. Compliance Mode Availability Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 0, Query Capabilities.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested: Supply 0 here for the highest supported Compliance DOE version, or specify a specific version (e.g., 3).</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr></table>

Table 14-59. Compliance Mode Availability Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>08h</td><td>1</td><td>Response Code: Value is 0, Query Capabilities.</td></tr><tr><td>09h</td><td>1</td><td>Version of Capability Returned: Returns supported version of the Compliance mode DOE, by the spec revision number (e.g., 3).</td></tr><tr><td>0Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>0Bh</td><td>1</td><td>Status: See Table 14-57 for error codes.</td></tr><tr><td>0Ch</td><td>8</td><td>Available Compliance Capabilities Bitmask</td></tr><tr><td>14h</td><td>8</td><td>Enabled Compliance Capabilities Bitmask</td></tr><tr><td>1Ch</td><td>8</td><td>Compliance Capabilities Options: See Table 14-60 for Compliance Option value descriptions.</td></tr></table>

The Available Capabilities and Enabled Capabilities bitmask values correspond to the request codes of each capability. For example:

• Bit[1] will be set if the DOE supports Request Code 1 (Status)

• Bit[3] will be set if the DOE supports Request Code 3 (Multiple Write Streaming)

Table 14-60. Compliance Options Value Descriptions

<table><tr><td>Bits</td><td>Description</td></tr><tr><td>15:0</td><td>Write Semantics Supported: Bitmask with the corresponding values:Bit[0]: Set to 1 if Device supports CXL.cache and ItoMWr opcodes as requesterBit[1]: Set to 1 if Device supports CXL.cache and WrCur opcodes as requesterBit[2]: Set to 1 if Device supports CXL.cache and DirtyEvict opcodes as requesterBit[3]: Set to 1 if Device supports CXL.cache and WOWrInv opcodes as requesterBit[4]: Set to 1 if Device supports CXL.cache and WOWrInvF opcodes as requesterBit[5]: Set to 1 if Device supports CXL.cache and WrInv opcodes as requesterBit[6]: Set to 1 if Device supports CXL.cache and CLFlush opcodes as requesterBit[7]: Set to 1 if Device supports CXL.cache and CleanEvict opcodes as requesterBit[8]: Set to 1 if Device supports CXL.cache and CleanEvictNoData opcodes as requesterBits[15:9]: Reserved</td></tr><tr><td>31:16</td><td>Read Semantics Supported: Bitmask with the corresponding values:Bit[16]: Set to 1 if Device supports CXL.cache and RdCurr opcodes as requesterBit[17]: Set to 1 if Device supports CXL.cache and RdOwn opcodes as requesterBit[18]: Set to 1 if Device supports CXL.cache and RdShared opcodes as requesterBit[19]: Set to 1 if Device supports CXL.cache and RdAny opcodes as requesterBit[20]: Set to 1 if Device supports CXL.cache and RdOwnNoData opcodes as requesterBits[31:21]: Reserved</td></tr><tr><td>47:32</td><td>Bit[32]: Set to 1 if Device supports CXL.cache and CacheFlushed opcodes as requesterBits[47:33]: Reserved</td></tr><tr><td>63:48</td><td>Reserved</td></tr></table>

The Available Compliance Capabilities and Enabled Compliance Capabilities bitmask values correspond to the request codes of each capability. For example:

• Bit[1] will be set if the DOE supports Request Code 1 (Status)

• Bit[3] will be set if the DOE supports Request Code 3 (Multiple Write Streaming)

## 14.16.3.2 Compliance Mode Status

Shows which compliance mode capabilities are enabled or in use.

Table 14-61. Compliance Mode Status

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 1, Query Status.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr></table>

Table 14-62. Compliance Mode Status Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Header</td></tr><tr><td>08h</td><td>1</td><td>Response Code: Value is 1, Query Status.</td></tr><tr><td>09h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>0Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>0Bh</td><td>4</td><td>Capability Bitfield</td></tr><tr><td>0Eh</td><td>2</td><td>Cache Size</td></tr><tr><td>10h</td><td>1</td><td>Cache Size Units</td></tr></table>

## 14.16.3.3 Compliance Mode Halt All

Table 14-63. Compliance Mode Halt All

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 2, Halt All.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr></table>

Table 14-64. Compliance Mode Halt All Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 2, Halt All.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>Bh</td><td>1</td><td>Status: See Table 14-57 for error codes.</td></tr></table>

## 14.16.3.4 Compliance Mode Multiple Write Streaming

Table 14-65. Enable Multiple Write Streaming Algorithm on the Device

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>08h</td><td>1</td><td>Request Code: Value is 3, Multiple Write Streaming.</td></tr><tr><td>09h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>0Ah</td><td>2</td><td>Reserved</td></tr><tr><td>0Ch</td><td>1</td><td>Protocol</td></tr><tr><td>0Dh</td><td>1</td><td>Virtual Address</td></tr><tr><td>0Eh</td><td>1</td><td>Self-checking</td></tr><tr><td>0Fh</td><td>1</td><td>Verify Read Semantics</td></tr><tr><td>10h</td><td>1</td><td>Num Increments</td></tr><tr><td>11h</td><td>1</td><td>Num Sets</td></tr><tr><td>12h</td><td>1</td><td>Num Loops</td></tr><tr><td>13h</td><td>1</td><td>Reserved</td></tr><tr><td>14h</td><td>8</td><td>Start Address</td></tr><tr><td>1Ch</td><td>8</td><td>Write Address</td></tr><tr><td>24h</td><td>8</td><td>Writeback Address</td></tr><tr><td>2Ch</td><td>8</td><td>Byte Mask</td></tr><tr><td>34h</td><td>4</td><td>Address Increment</td></tr><tr><td>38h</td><td>4</td><td>Set Offset</td></tr><tr><td>3Ch</td><td>4</td><td>Pattern &quot;P&quot;</td></tr><tr><td>40h</td><td>4</td><td>Increment Pattern &quot;B&quot;</td></tr></table>

Table 14-66. Compliance Mode Multiple Write Streaming Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 3, Multiple Write Streaming.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>Bh</td><td>1</td><td>Status: See Table 14-57 for error codes.</td></tr></table>

If the device only supports Virtual Addresses and the Virtual Address is cleared to 0, then the return value shall be 01h (Not Authorized). If the device only supports Physical Addresses and the Virtual Address is set to 1, then the return value shall be 01h (Not Authorized).

## 14.16.3.5 Compliance Mode Producer-Consumer

Table 14-67. Enable Producer-Consumer Algorithm on the Device

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>08h</td><td>1</td><td>Request Code: Value is 4, Producer-Consumer.</td></tr><tr><td>09h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>0Ah</td><td>2</td><td>Reserved</td></tr><tr><td>0Ch</td><td>1</td><td>Protocol</td></tr><tr><td>0Dh</td><td>1</td><td>Num Increments</td></tr><tr><td>0Eh</td><td>1</td><td>Num Sets</td></tr><tr><td>0Fh</td><td>1</td><td>Num Loops</td></tr><tr><td>10h</td><td>1</td><td>Write Semantics</td></tr><tr><td>11h</td><td>3</td><td>Reserved</td></tr><tr><td>14h</td><td>8</td><td>Start Address</td></tr><tr><td>1Ch</td><td>8</td><td>Byte Mask</td></tr><tr><td>24h</td><td>4</td><td>Address Increment</td></tr><tr><td>28h</td><td>4</td><td>Set Offset</td></tr><tr><td>2Ch</td><td>4</td><td>Pattern</td></tr></table>

Table 14-68. Compliance Mode Producer-Consumer Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 4, Producer-Consumer.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>Bh</td><td>1</td><td>Status: See Table 14-57 for error codes.</td></tr></table>

If the device only supports Virtual Addresses and the Virtual Address is cleared to 0, then the return value shall be 01h (Not Authorized). If the device only supports Physical Addresses and the Virtual Address is set to 1, then the return value shall be 01h (Not Authorized).

14.16.3.6 Test Algorithm 1b Multiple Write Streaming with Bogus Writes

Table 14-69. Enable Algorithm 1b, Write Streaming with Bogus Writes (Sheet 1 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>08h</td><td>1</td><td>Request Code: Value is 5, Test Algorithm 1b.</td></tr><tr><td>09h</td><td>1</td><td>Version of Capability Requested</td></tr></table>

Table 14-69. Enable Algorithm 1b, Write Streaming with Bogus Writes (Sheet 2 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0Ah</td><td>2</td><td>Reserved</td></tr><tr><td>0Ch</td><td>1</td><td>Protocol</td></tr><tr><td>0Dh</td><td>1</td><td>Virtual Address</td></tr><tr><td>0Eh</td><td>1</td><td>Self-checking</td></tr><tr><td>0Fh</td><td>1</td><td>Verify Read Semantics</td></tr><tr><td>10h</td><td>1</td><td>Num Increments</td></tr><tr><td>11h</td><td>1</td><td>Num Sets</td></tr><tr><td>12h</td><td>1</td><td>Num Loops</td></tr><tr><td>13h</td><td>1</td><td>Reserved</td></tr><tr><td>14h</td><td>8</td><td>Start Address</td></tr><tr><td>1Ch</td><td>8</td><td>Writeback Address</td></tr><tr><td>24h</td><td>8</td><td>Byte Mask</td></tr><tr><td>2Ch</td><td>4</td><td>Address Increment</td></tr><tr><td>30h</td><td>4</td><td>Set Offset</td></tr><tr><td>34h</td><td>4</td><td>Pattern &quot;P&quot;</td></tr><tr><td>38h</td><td>4</td><td>Increment Pattern &quot;B&quot;</td></tr><tr><td>3Ch</td><td>1</td><td>Bogus Writes Count</td></tr><tr><td>3Dh</td><td>3</td><td>Reserved</td></tr><tr><td>40h</td><td>4</td><td>Bogus Writes Pattern</td></tr></table>

Table 14-70. Algorithm 1b Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 5, Test Algorithm 1b.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>Bh</td><td>1</td><td>Status: See Table 14-57 for error codes.</td></tr></table>

14.16.3.7 Inject Link Poison

Table 14-71. Enable Poison Injection into (Sheet 1 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 6, Poison Injection.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested</td></tr></table>

Table 14-71. Enable Poison Injection into (Sheet 2 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr><tr><td>Ch</td><td>1</td><td>Protocol00h = CXL.io01h = CXL.cache02h = CXL.mem</td></tr></table>

Table 14-72. Poison Injection Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 6, Poison Injection.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>Bh</td><td>1</td><td>Status: See Table 14-57 for error codes.</td></tr></table>

14.16.3.8 Inject CRC

Table 14-73. Enable CRC Error into Traffic

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 7, CRC Injection.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr><tr><td>Ch</td><td>1</td><td>Num Bits Flipped</td></tr><tr><td>Dh</td><td>1</td><td>Num Flits Injected</td></tr></table>

Table 14-74. CRC Injection Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 7, CRC Injection.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>Bh</td><td>1</td><td>Status: See Table 14-57 for error codes.</td></tr></table>

## 14.16.3.9 Inject Flow Control

Table 14-75. Enable Flow Control Injection

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 8, Flow Control Injection.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr><tr><td>Ch</td><td>1</td><td>Inject Flow Control</td></tr></table>

Table 14-76. Flow Control Injection Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 8, Flow Control Injection.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>Bh</td><td>1</td><td>Status: See Table 14-57 for error codes.</td></tr></table>

14.16.3.10 Toggle Cache Flush

Table 14-77. Enable Cache Flush Injection

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 9, Cache Flush.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr><tr><td>Ch</td><td>1</td><td>00h = Cache Flush Disabled01h = Cache Flush Enabled</td></tr></table>

Table 14-78. Cache Flush Injection Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 9, Cache Flush.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>Bh</td><td>1</td><td>Status: See Table 14-57 for error codes.</td></tr></table>

## 14.16.3.11 Inject MAC Delay

Delay MAC on IDE secure link until it no longer meets spec, flit 6+.

Table 14-79. MAC Delay Injection

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 0Ah, Delay MAC.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr><tr><td>Ch</td><td>1</td><td>• 00h = Disable• 01h = Enable MAC Delay</td></tr><tr><td>Dh</td><td>1</td><td>Mode• 00h = CXL.io• 01h = CXL.cachemem</td></tr><tr><td>Eh</td><td>1</td><td>Delay: Number of flits to delay MAC. 6+ = error condition.</td></tr></table>

Table 14-80. MAC Delay Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 0Ah, MAC delay injection.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>Bh</td><td>1</td><td>Status• 00h = Success• See Table 14-57 for other error codes</td></tr></table>

## 14.16.3.12 Insert Unexpected MAC

Insert an unexpected MAC on a non-IDE secured channel.

## Table 14-81. Unexpected MAC Injection

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 0Bh, Unexpected MAC injection.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr><tr><td>Ch</td><td>1</td><td>00h = Disable01h = Insert message02h = Delete message</td></tr><tr><td>Dh</td><td>1</td><td>Mode00h = CXL.io01h = CXL.cachemem</td></tr></table>

Table 14-82. Unexpected MAC Injection Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 0Bh, Unexpected MAC injection.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr></table>

14.16.3.13 Inject Viral

Table 14-83. Enable Viral Injection

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 0Ch, Inject Viral.</td></tr><tr><td>9h</td><td>1</td><td>Version</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr><tr><td>Ch</td><td>1</td><td>Protocol• 00h = CXL.io• 01h = CXL.cache• 02h = CXL.mem</td></tr></table>

Table 14-84. Flow Control Injection Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 0Ch, Inject Viral.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>Bh</td><td>1</td><td>Status• 00h = Success• See Table 14-57 for other error codes</td></tr></table>

## 14.16.3.14 Inject ALMP in Any State

Insert an ALMP in the ARB/MUX regardless of state.

Table 14-85. Inject ALMP Request (Sheet 1 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 0Dh, Inject ALMP in any state.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested</td></tr></table>

Table 14-85. Inject ALMP Request (Sheet 2 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr><tr><td>Ch</td><td>1</td><td>00h = Disable01h = Insert ALMP</td></tr><tr><td>Dh</td><td>3</td><td>Reserved</td></tr></table>

Table 14-86. Inject ALMP Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 0Dh, Inject ALMP in any state.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>6</td><td>Reserved</td></tr></table>

## 14.16.3.15 Ignore Received ALMP

Ignore the next ALMPs received.

Table 14-87. Ignore Received ALMP Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code = 0Eh, Ignore received ALMPs.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr><tr><td>Ch</td><td>1</td><td>• 00h = Disable• 01h = Ignore ALMPs</td></tr><tr><td>Dh</td><td>3</td><td>Reserved</td></tr></table>

Table 14-88. Ignore Received ALMP Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 0Eh, Ignore received ALMPs.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>6</td><td>Reserved</td></tr></table>

## 14.16.3.16 Inject Bit Error in Flit

Inject a single bit error into the lower 16 bytes of a 528-bit flit.

Table 14-89. Inject Bit Error in Flit Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Request Code: Value is 0Fh, Inject Bit Error in Flit.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>Ah</td><td>2</td><td>Reserved</td></tr><tr><td>Ch</td><td>1</td><td>00h = Disable; no action taken01h = Inject single Bit error in next 528 flits</td></tr><tr><td>Dh</td><td>3</td><td>Reserved</td></tr></table>

Table 14-90. Inject Bit Error in Flit Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 0Fh, Inject Bit Error in Flit.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>6</td><td>Reserved</td></tr></table>

## 14.16.3.17 Inject Memory Device Poison

Table 14-91. Memory Device Media Poison Injection Request (Sheet 1 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>08h</td><td>1</td><td>Request Code: Value is 10h, Memory Device Media Poison Injection.</td></tr><tr><td>09h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>0Ah</td><td>2</td><td>Reserved</td></tr><tr><td>0Ch</td><td>1</td><td>Protocol• 02h = CXL.mem</td></tr><tr><td>0Dh</td><td>1</td><td>Reserved</td></tr><tr><td>0Eh</td><td>1</td><td>Action• 00h = Inject Poison• 01h = Clear Poison</td></tr><tr><td>0Fh</td><td>1</td><td>Reserved</td></tr></table>

Table 14-91. Memory Device Media Poison Injection Request (Sheet 2 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>10h</td><td>8</td><td>Device Physical Address: When Protocol = 2, the device shall inject poison into the media at this requested address. If this address specifies a persistent memory address, the injected poison shall persist across warm resets or cold resets. Device shall report Invalid Address Specified poison injection response status if the DPA is out of range.• Bits[5:0]: Reserved• Bits[7:6]: DPA[7:6]• Bits[15:8]: DPA[15:8]• ...• Bits[63:56]: DPA[63:56]</td></tr><tr><td>18h</td><td>40h</td><td>Clear Poison Write Data: When Protocol = 2 and Action = 1, the device shall write this replacement data into the requested physical address, atomically, while clearing poison. If the device is configured with nonzero Metadata bits as defined by the HDM-H Metabits Storage Configuration field in the Metabits Storage Feature Readable Attributes (see Table 8-282), then for a subsequent read to the DPA, the device shall return MetaField=00b (Meta0-State (MS0)) and MetaValue=00b.</td></tr></table>

Table 14-92. Memory Device Media Poison Injection Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 10h, Memory Device Media Poison Injection.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>6</td><td>Reserved</td></tr></table>

Table 14-93. Memory Device LSA Poison Injection Request

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>08h</td><td>1</td><td>Request Code: Value is 11h, Memory Device LSA Poison Injection.</td></tr><tr><td>09h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>0Ah</td><td>2</td><td>Reserved</td></tr><tr><td>0Ch</td><td>1</td><td>Protocol• 02h = CXL.mem</td></tr><tr><td>0Dh</td><td>1</td><td>Reserved</td></tr><tr><td>0Eh</td><td>1</td><td>Action• 00h = Inject Poison• 01h = Clear Poison</td></tr><tr><td>0Fh</td><td>1</td><td>Reserved</td></tr><tr><td>10h</td><td>4</td><td>LSA Byte Offset: When Protocol = 2, the device shall inject poison into the Label Storage Area of the device at this requested byte offset. Because the LSA is persistent, the injected poison shall persist across warm resets or cold resets. Device shall report Invalid Address Specified poison injection response status if the byte offset is out of range. The poison can be cleared through this interface or with SetLSA.</td></tr></table>

Table 14-94. Memory Device LSA Poison Injection Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: Value is 11h, Memory Device LSA Poison Injection.</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>6</td><td>Reserved</td></tr></table>

Table 14-95. Inject Memory Device Health Enable Memory Device Health Injection (Sheet 1 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>08h</td><td>1</td><td>Request Code: 12h, Memory Device Health Injection</td></tr><tr><td>09h</td><td>1</td><td>Version of Capability Requested</td></tr><tr><td>0Ah</td><td>2</td><td>Reserved</td></tr><tr><td>0Ch</td><td>1</td><td>Protocol• 02h = CXL.mem</td></tr><tr><td>0Dh</td><td>1</td><td>Injection Type• 00h = Error is injected immediately and remains in effect until it is cleared using this command or by a CXL warm reset or cold reset of the device• 01h = Error is not injected until after a cold reset, the injection will only occur once, and will be auto-disabled after the first occurrence</td></tr><tr><td>0Eh</td><td>1</td><td>Valid Device Health Injection: Indicators of which Device Health Injection fields are valid in the supplied in the payload.• Bit[0]:— 1 = Health Status Injection Enabled field shall be valid• Bit[1]:— 1 = Media Status Injection Enabled field shall be valid• Bit[2]:— 1 = Life Used Injection Enabled field shall be valid• Bit[3]:— 1 = Dirty Shutdown Count Injection Enabled field shall be valid• Bit[4]:— 1 = Device Temperature Injection Enabled field shall be valid• Bits[7:5]: Reserved</td></tr></table>

Table 14-95. Inject Memory Device Health Enable Memory Device Health Injection (Sheet 2 of 2)

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0Fh</td><td>1</td><td>Enable Device Health Injection: The device shall enable the following error injection:Bit[0]:Health Status Injection Enabled:- 0 = Device shall disable its Health Status injection- 1 = Health Status field shall be valid and the device shall enable its Health Status injectionBit[1]:Media Status Injection Enabled:- 0 = Device shall disable its Media Status injection- 1 = Media Status field shall be valid and the device shall enable its Media Status injectionBit[2]:Life Used Injection Enabled:- 0 = Device shall disable its Life Used injection- 1 = Life Used field shall be valid and the device shall enable its Life Used injectionBit[3]:Dirty Shutdown Count Injection Enabled:- 0 = Device shall disable its Dirty Shutdown Count injection- 1 = Dirty Shutdown Count field shall be valid and the device shall enable its Dirty Shutdown Count injectionBit[4]:Device Temperature Injection Enabled:- 0 = Device shall disable its Device Temperature injection- 1 = Device Temperature field shall be valid and the device shall enable its Device Temperature injectionBits[7:5]:Reserved</td></tr><tr><td>10h</td><td>1</td><td>Health Status: The injected Health Status. One of the defined Get Health Info values fromSection 8.2.10.9. Return Invalid Injection Parameter for invalid or unsupported injection values.</td></tr><tr><td>11h</td><td>1</td><td>Media Status: The injected Media Status. One of the defined Get Health Info values fromSection 8.2.10.9. Return Invalid Injection Parameter for invalid or unsupported injection values.</td></tr><tr><td>12h</td><td>1</td><td>Life Used: The injected Life Used. See the Get Health Info command inSection 8.2.10.9for legal range. Return Invalid Injection Parameter for invalid or unsupported injection values.</td></tr><tr><td>13h</td><td>1</td><td>Reserved</td></tr><tr><td>14h</td><td>4</td><td>Dirty Shutdown Count: The injected Dirty Shutdown Count. See the Get Health Info command inSection 8.2.10.9. Return Invalid Injection Parameter for invalid or unsupported injection values.</td></tr><tr><td>18h</td><td>2</td><td>Device Temperature: The injected Device Temperature. See the Get Health Info command inSection 8.2.10.9. Return Invalid Injection Parameter for invalid or unsupported injection values.</td></tr></table>

Table 14-96. Device Health Injection Response

<table><tr><td>Data Object Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Standard DOE Request Header</td></tr><tr><td>8h</td><td>1</td><td>Response Code: 12h, Device Health Injection</td></tr><tr><td>9h</td><td>1</td><td>Version of Capability Returned</td></tr><tr><td>Ah</td><td>1</td><td>Length of Capability Package</td></tr><tr><td>Bh</td><td>1</td><td>Status: See Table 14-57 for error codes.</td></tr></table>

This appendix was included in the original release of CXL and has not been updated since. It is being included as reference for some original usage and implementation options/ideas for CXL devices. It does not cover features that were added after the initial release, including Back-Invalidate Snoop (BISnp) messages that enable new ways of handling coherence of Host-managed Device Memory (HDM), and new memory device expansion proposals around pooling and Fabric-Attached memory (FAM). See Chapter 2.0, “CXL System Architecture,” for a more-complete set of use cases.

## A.1 Accelerator Usage Taxonomy

Table A-1. Accelerator Usage Taxonomy (Sheet 1 of 2)

<table><tr><td>Accelerator Type</td><td>Description</td><td>Challenges and Opportunities</td><td>CXL Support</td></tr><tr><td>Producer-ConsumerAccelerators that don&#x27;t execute against &quot;Memory&quot; without special requirements</td><td>Works on data streams or large contiguous data objectsLittle interaction with the hostStandard P/C ordering model works well</td><td>Efficient work submissionEfficient exchange of metadata (flow control)</td><td>Basic PCIe*CXL.io</td></tr><tr><td>Producer-Consumer PlusAccelerators that don&#x27;t execute against &quot;Memory&quot; with special requirements</td><td>Same as above, but...P/C ordering model doesn&#x27;t work wellNeeds special data operations such as atomics</td><td>Device Coherency can be used to implement varied ordering models and special data operations</td><td>CXL.cache on CXL with baseline snoop filter supportCXL.io</td></tr><tr><td>Software-assisted SVM MemoryAccelerators that execute against &quot;Memory&quot; with software-supportable data management</td><td>Local memory is often needed for bandwidth or latency predictabilityLittle interaction with the hostData management is easily implemented in software (e.g., few and simple data buffers)</td><td>Host software should be able to interact directly with accelerator memory (e.g., SVM, Google, etc.)Reduces copies, replication, and pinningOptimizing coherency impact on performance is a challengeSoftware can provide best optimization of coherency impact</td><td>CXL Bias model with software-managed biasCXL.ioCXL.cacheCXL.mem</td></tr><tr><td>Autonomous SVM MemoryAccelerators that execute against &quot;Memory&quot; where software-supported data management is impractical</td><td>Local memory is often needed for bandwidth or latency predictabilityInteraction with the host is commonData movement is difficult to manage in software (e.g., sparse data structures, pointer-based data structures, etc.)</td><td>Host software should be able to interact directly with accelerator memory (SVM)Reduces copies, replication, and pinningOptimizing coherency impact on performance is a challengeCannot count on software for bias management</td><td>CXL Bias model with hardware-managed biasCXL.ioCXL.cacheCXL.mem</td></tr></table>

Table A-1. Accelerator Usage Taxonomy (Sheet 2 of 2)

<table><tr><td>Accelerator Type</td><td>Description</td><td>Challenges and Opportunities</td><td>CXL Support</td></tr><tr><td>Giant CacheAccelerators that execute against “Memory” where local memory and caching is required</td><td>Local memory is needed for bandwidth or latency predictabilityData footprint is larger than local memoryInteraction with the host is commonData must be cycled through accelerator memory in small blocksData movement is difficult to manage in software</td><td>Accelerator memory needs to work like a cache (not SVM/system memory)Ideally, cache misses are detected in hardware, but cache replacements can be managed in software</td><td>CXL.cache on CXL with “Enhanced Directory” snoop filter supportCXL.ioCXL.cache</td></tr><tr><td>Disaggregated Memory ControllerTypically for memory controllers with remote persistent memory, which may be in 2 Level-Memory or App Direct mode</td><td>PCIe semantics are needed for device enumeration, driver support, and device managementMost operational flows rely on being able to communicate directly with a Home Device or Near Memory Controller on the Host</td><td>Device needs high-bandwidth and low-latency path from memory controller to Home Device in the CPU</td><td>CXL.ioCXL.mem</td></tr></table>

## A.2

## Bias Model Flow Example — From CPU

1. Start with pages in Device Bias:

— Pages are guaranteed to not be cached in host cache hierarchy

2. Software allocates pages from device memory:

a. Software pushes operands to allocated pages from the peer CPU core:

• For example, Software may use OpenCL\* API to flip operand pages to Host Bias

• Data copies or cache flushes are not required

b. Host CPUs generate operand data in target pages — data arrives in an arbitrary location within the host cache hierarchy.

3. Device uses operands to generate results:

— For example, Software may use OpenCL API to flip operand pages back to Device Bias

a. API call causes a work descriptor submission to the device — descriptor asks the device to flush operand pages from the host cache.

b. Cache flush is executed using RdOwnNoData on CXL.cache protocol (see Table 3-22).

c. When Device Bias flip is complete, Software submits work to the accelerator.

d. Accelerator executes without any host-related coherency overhead.

e. Accelerator dumps data to results pages.

4. Software pulls results from the allocated pages:

— For example, Software uses OpenCL API to flip results pages to Host Bias

— This action causes some bias states to be changed, but does not cause any coherency or cache-flushing actions

— Host CPUs can access, cache, and share results data as needed

5. Software releases the allocated pages.

OpenCL defines a Coarse-grained buffer Shared Virtual Memory model. Under that model, memory consistency is guaranteed only at explicit synchronization points and these points provide an opportunity to perform bias flip.

Here are some example of OpenCL calls where bias flip can be performed:

• clEnqueueSVMMap provides host access to this buffer. Software may flip the bias from Device bias to Host bias during this call.

• clEnqueueSVMUnmap revokes host access to this buffer. At this point, an OpenCL implementation for a CXL device could flip the bias from Host bias to Device bias.

There are other OpenCL calls where the CPU and the Device share OpenCL buffer objects. Software could flip the bias during those calls.

## CPU Support for Bias Modes

There are two envisaged models of support that the CPU would provide for Bias Modes. These are described below.

## A.3.1

## Remote Snoop Filter

• Remote socket-owned lines that belong to accelerator-attached memory are tracked by a Remote Snoop-Filter (SF) located in the host CPU Home Agent (HA). Remote SF does not track lines that belong to Host memory. The above removes the need for a directory in device memory. Please note this is only possible in Host Bias mode since in Device Bias mode, local/remote sockets can’t cache lines that belong to device memory.

• Local socket-owned lines that belong to accelerator-attached memory will be tracked by a local SF in the host CPU Last Level Cache (LLC) controller. Please note this is only possible in Host Bias mode since in Device Bias mode, local/remote sockets can’t cache lines that belong to device memory.

• Device-owned lines that belong to accelerator-attached memory (in Host Bias mode) will NOT be tracked by a local SF in the host CPU LLC controller. These will be tracked by the Device Coherency Engine (DCOH) using a device-specific mechanism (device SF). In Device Bias mode, no coherent tracking is done in the host CPU because the accesses are completed within the device and the host does not see the requests.

• Device-owned lines that belong to host memory (in Host mode or Device mode) will be tracked by a local SF in the host CPU LLC controller. This may cause the device to receive snoops through CXL (CXL.cache) for such lines.

## A.3.2

## Directory in Accelerator-attached Memory

• Remote socket-owned lines that belong to device memory are tracked by a directory in device memory metadata. The host HA may choose to do broadcast snooping for some cases to avoid reading the metadata.

• Local socket-owned lines that belong to device memory will be tracked by a local SF in the host CPU LLC controller. For access by device, local socket-owned lines that belong to device memory will also update the directory.

• Device-owned lines that belong to device memory will NOT be tracked by a local SF in the host CPU LLC controller. These will be tracked by the Device Coherency Engine (DCOH) using a device-specific mechanism (device SF).

• Device-owned lines that belong to host memory (in Host mode or Device mode) will be tracked by a local SF in the host CPU LLC controller. This may cause the device to receive snoops through CXL (CXL.cache) for such lines.

• Bias Table is located in stolen memory within the device memory and is accessed through the DCOH.

## Giant Cache Model

For problems whose data sets exceed the device-attached memory size, the memory attached to the accelerator needs to be a cache, not memory:

• Typically, the full data set will reside in processor-attached memory

• Subsets of this larger data set are cycled through accelerator memory as the calculation proceeds

• For such use cases, caching is the correct solution:

— Accelerator memory is not mapped into the system address map — data set is built up in host memory

— Single-page table entry per page in data set — no page table manipulation as pages are cycled through accelerator memory

— Copies of data can be created under driver control and/or hardware control with no OS intervention

Figure A-1. Profile D — Giant Cache Model  
![](images/ea4296f6d0434b3a3ad36a17854a82b08ae29fe9e6a623e8f7300564ed3994ef.jpg)

Critical issues with a Giant Cache:

• Cache is too large for tracking in the Host on-die SF

• Snoop latency for a Giant Cache is likely to be much higher than standard on-die cache snoop latency

Recommended CXL solution:

• Implements SF in processor’s coherency directory (stored in DRAM ECC bits), which essentially becomes a highly scalable SF

• Minimizes impact to processor operations that are unrelated to accelerators

• Allows accelerator to access data over CXL.cache as a caching Device

• Provides support on CXL.cache to allow an accelerator to explicitly request directory snoop filtering for Giant Cache

• Processor infrastructure differentiates between low-latency and high-latency requester types

• Support for simultaneous use of a small, low-latency cache associated with the ondie snoop filter is included

## Appendix B Appendix B Unordered I/O to Support Peer-to-Peer Directly to HDM-DB

Revision 3.0 of the CXL specification added this appendix to document the planned CXL use of Unordered I/O (UIO) protocol for the CXL UIO Direct P2P to HDM-DB use case. At the time, UIO protocol was still under development within the PCI-SIG\* as an ECN against the PCIe\* Base Specification. The PCIe UIO ECN became final in March 2023, and is available from the PCI-SIG website.

The CXL use of UIO protocol as originally described in this appendix as well as additional use cases are covered elsewhere within this version of the CXL specification. UIO protocol details should be obtained from the final PCIe UIO ECN or other PCI-SIG specifications.

# Appendix C Memory Protocol Tables

To formalize the protocol expectations of the Memory Protocol, this appendix captures the allowed request encodings, states, and responses in the host and the device. In this appendix, the flows are referred to in the context of three HDM region types as defined in Section 3.3.

This appendix uses field name abbreviations to fit into the table format captured in Table C-1.

Table C-1. Field Encoding Abbreviations (Sheet 1 of 2)

<table><tr><td>Field Name</td><td>Encoding Name</td><td>Abbreviation</td><td>Notes</td></tr><tr><td rowspan="5">MetaField</td><td>Meta0-State</td><td>MS0</td><td></td></tr><tr><td>Extended Meta-State</td><td>EMS</td><td></td></tr><tr><td>Meta0-State OR Extended Meta-State</td><td>MS0-EMS</td><td></td></tr><tr><td>Meta0-State OR No-Op</td><td>MS0-NO</td><td></td></tr><tr><td>Extended Meta-State OR No-Op</td><td>EMS-NO</td><td>For table rows that allow these two encodings in a DRS response, the No-Op encoding should be sent only when the device has an uncorrectable error on the Extended Metadata Stored such that it cannot return it.</td></tr><tr><td rowspan="3">DRS Trailer and RwD Trailer</td><td>Extended MetaValue</td><td>EMV</td><td>Extended MetaValue in the trailer.For DRS Trailer, this state comes from EMD state stored in the device at the time the request is received.For RwD Trailer, this is the state to become the final EMD state when the write is complete.</td></tr><tr><td>Not Applicable</td><td>N/A</td><td>Indicates that no trailer is returned</td></tr><tr><td>Extended MetaValue or Not Applicable</td><td>EMV-NA</td><td>Indicates that a trailer of EMV is sent, but only if the MetaField encoding is EMS. The table may allow for No-Op to be sent in MetaField, in which case no trailer is included.</td></tr><tr><td rowspan="3">MetaValue</td><td>Not Applicable</td><td>N/A</td><td>Used when MetaValue is undefined and should never be consumed, which is when MetaField is set to No-Op. The encoding rules follow the definition for Reserved which must be cleared to 0 by sender and ignored by receiver.</td></tr><tr><td>Any Value</td><td></td><td>Indicates any legal encoding that matches rules for the HDM memory region. In support of Extended Metadata with HDM-DB, the device must return the current host state (same as Meta0-State).</td></tr><tr><td>Explicit No-Op</td><td>E-No-Op</td><td>This is an encoding defined for use only when EMV encoding to indicate the MetaField= No-Op equivalent coherent behavior in the device for HDM-DB.</td></tr><tr><td>Host State</td><td>UnChanged</td><td>UC</td><td>Used to indicate that the device should not change its bias state.</td></tr></table>

Table C-1.  
Field Encoding Abbreviations (Sheet 2 of 2)

<table><tr><td>Field Name</td><td>Encoding Name</td><td>Abbreviation</td><td>Notes</td></tr><tr><td>SnpType</td><td>Snp*</td><td>All Snoop types: SnpInv, SnpData, SnpCur</td><td>Used when a row applies to all different snoop options.</td></tr><tr><td>Device State</td><td>Extended Metadata</td><td>EMD</td><td>Data stored in the device for up to 32 bits of meta state. This mode is mutually exclusive with standard Meta0-State in HDM-H devices, but supplemental to coherence state in HDM-DB devices. Not applicable to HDM-D.</td></tr></table>

The term “Host State” is used in this section to describe the device tracking of the host coherence state for the address. The implementation of this may vary and has been referred to as a “Bias Table” or “Bias State” or “Directory” for HDM-D/HDM-DB. For HDM-DB more implementations are possible, including an inclusive Snoop-Filter, which uses the BISnp/BIRsp channels to keep the Snoop Filter inclusive.

In the tables that follow, “Y(1)” in the Legal column indicates that the table row contents are also defined in other tables within the CXL specification and also existed in the CXL 1.1 specification. A “Y\*” in the Legal column indicates that a destination must accept the message, and the rows of the table indicate the legal responses to the message. The $" 0 ^ { \prime \prime }$ defines optional rows that may not be supported. All “O” cases will include details as to the discovery/enabling method in Table C-2.

<table><tr><td>Option Code</td><td>Option Name</td><td>Description</td></tr><tr><td>O-1</td><td>Cmp-M Support</td><td>Mode that can be enabled in a device. This message is optional for the host to support and is thus expected to be applied to CXL.mem traffic from a given initiator (host or peer device). For MLD/GFD, this mode could be different for each initiator.</td></tr><tr><td>O-2</td><td>EMD Support</td><td>This mode would apply to a given HDM region. Hosts are expected to support EMD or Traditional Metadata for each region of HDM-H. For HDM-DB, the MetaValue is treated in the same way (defining coherence state); however, the EMD value is also supported.</td></tr><tr><td>O-3</td><td>MemSpecRd Support</td><td>These messages are supported only on interfaces that train as 256B or that are supported by links that train as 256B Flit mode or as CXL 68B Flit and VH Capable.</td></tr><tr><td>O-4</td><td>TEE Requests</td><td>TSP features are enabled in the host.</td></tr></table>

## HDM-DB Requests with TEE Support

Table C-3 defines messages on the request channel of CXL.mem protocol. Table C-4 additionally defines the Forward flows that apply only for HDM-D memory regions for Type 2 devices when the devices are accessing device-attached memory. Table C-5 defines the BISnp channel method of managing device-attached memory coherence for the HDM-DB memory region of Type 2 devices or Type 3 devices.

Table C-3 includes a footnote that disallows the downgrade of “host state” from the current state if there is a TE mismatch detected at the target for read access. For example, if the current state is A and the normal resulting state is S-state, it is not permitted to downgrade to S-state if there is a TE State mismatch.

Use of the term UnChanged Mismatch (“UCM”) reflects cases in which the device cache or requester state in the HDM-DB target remains unchanged when a TEE State mismatch occurs. Targets that take advantage of this allowance will rely on software clean-up of any coherence violation that may result. For additional details related to requirements for this behavior, see Section 11.5.4.11.

Ta ble C-3 <sub>.</sub> H D M - D B M emory Req uests with TE State (Sheet 1 of 6)

<table><tr><td rowspan="2">Legal</td><td colspan="4">Host Request</td><td colspan="5">Device Response</td><td colspan="3">Final Device State</td><td rowspan="2">Description</td></tr><tr><td><img src="images/af6662bc904dba12062ff64741b4cc22080558537b2e75c55493c0c883f0c80a.jpg"/></td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td>DRS Trailer</td><td>Device Cache</td><td> $DTRCS^1$ </td><td>EMD</td></tr><tr><td>Y</td><td rowspan="6"><img src="images/be142007528142fee5b68c14ed9de70aa26cee004847375b29050d5a9b2cd36e.jpg"/>MemRd&lt;Only for Non-TSP targets&gt;<img src="images/e4891b2551125b39715a033143e5ee6411aff76ea356a31c608afab75a251437.jpg"/></td><td>MS0</td><td rowspan="6">I</td><td rowspan="2">SnpInv</td><td rowspan="2">Cmp</td><td rowspan="6">MemData</td><td>MS0-NO</td><td rowspan="2"></td><td>N/A</td><td rowspan="2">I</td><td rowspan="2">I</td><td rowspan="2">UC</td><td>The host is requesting a non-cacheable but current value of the cacheline and is forcing the device to flush its cache.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMS-NO</td><td>EMV-NA</td><td></td></tr><tr><td>N</td><td></td><td>SnpData</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>MS0</td><td rowspan="2">SnpCur</td><td rowspan="2">Cmp</td><td>MS0-NO</td><td rowspan="2"></td><td>N/A</td><td></td><td>I</td><td rowspan="2">UC</td><td>The host is requesting a non-cacheable but current value of the cacheline and is thereby leaving data in the device&#x27;s cache.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMS-NO</td><td>EMV-NA</td><td></td><td></td><td></td></tr><tr><td>N</td><td></td><td>No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>O-1</td><td rowspan="14"><img src="images/859c3ef960f251cf5669b30b36d5f9d51ebbea3a9b89075bc2eb20278a3d6c41.jpg"/>MemRd/MemRdTEE</td><td>MS0</td><td rowspan="7">A</td><td rowspan="4">SnpInv</td><td rowspan="2"> $Cmp-M^2$ </td><td rowspan="14">MemData/MemDataTEE</td><td>MS0-NO</td><td rowspan="4"></td><td>N/A</td><td rowspan="4">I or UCM</td><td rowspan="4">A or UCM</td><td rowspan="4">UC</td><td rowspan="2">Supported for host that can accept M-state.</td></tr><tr><td>O-1 &amp; O-2</td><td>EMS</td><td>EMS-NO</td><td>EMV-NA</td></tr><tr><td>Y(1)</td><td>MS0</td><td rowspan="2">Cmp-E</td><td>MS0-NO</td><td>N/A</td><td rowspan="2">The host wants an exclusive copy of the cacheline.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMS-NO</td><td>EMV-NA</td></tr><tr><td>N</td><td></td><td>SnpData</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td></td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td></td><td>No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td></td><td rowspan="7">S</td><td>SnpInv</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y(1)</td><td>MS0</td><td rowspan="4">SnpData</td><td rowspan="2">Cmp-S</td><td>MS0-NO</td><td rowspan="4"></td><td>N/A</td><td rowspan="2">S or UCM</td><td rowspan="2"> $S^3$  or UCM</td><td rowspan="4">UC</td><td rowspan="4">The host is requesting a shared copy of the cacheline, but Rsp types allow the device to return S-state or E-state to the host. Cmp-E response is not recommended because the host did not request this state.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMS-NO</td><td>EMV-NA</td></tr><tr><td>Y(1)</td><td>MS0</td><td rowspan="2">Cmp-E</td><td>MS0-NO</td><td>N/A</td><td rowspan="2">I or UCM</td><td rowspan="2">A or UCM</td></tr><tr><td>O-2</td><td>EMS</td><td>EMS-NO</td><td>EMV-NA</td></tr><tr><td>N</td><td></td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td></td><td>No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

![](images/7e633f36a6cb988c070f91d9701e329bedbbed432e9e2771347cd4952be5b75e.jpg)

![](images/4b278efb017ded8ed588ff1b210a796dde17355236e09dc261f21a19fc3d1dbd.jpg)

Ta ble C-3 <sub>.</sub> H DM - DB Memory Req uests with TE State (Sheet 2 of 6)

<table><tr><td rowspan="2">Legal</td><td colspan="4">Host Request</td><td colspan="5">Device Response</td><td colspan="3">Final Device State</td><td rowspan="2">Description</td></tr><tr><td><img src="images/a05bd62af619efac54be61459021e54e9062c926115ea63926c0cdd2be168fba.jpg"/></td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td>DRS Trailer</td><td>Device Cache</td><td> $DTRCS^1$ </td><td>EMD</td></tr><tr><td>Y(1)</td><td rowspan="9">MemRd/MemRdTEE <img src="images/4fbacd814bfadd5d6f8249e308abd1d629335994b715e3cde8980d066db98a4e.jpg"/></td><td>No-Op</td><td>N/A</td><td rowspan="2">SnpInv</td><td rowspan="2">Cmp</td><td rowspan="8">MemData/MemDataTEE</td><td>MSO-NO</td><td rowspan="2"></td><td>N/A</td><td rowspan="2">I or UCM</td><td rowspan="2">UC</td><td rowspan="2">UC</td><td rowspan="2">The host wants to read the cacheline without changing the state expected in the host cache, and the device should invalidate the cacheline from its cache.</td></tr><tr><td>O-2</td><td>EMS</td><td>No-Op</td><td>EMS-NO</td><td>EMV-NA</td></tr><tr><td>N</td><td>EMS-NO</td><td>N/A</td><td rowspan="2">SnpData</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>EMS</td><td>E-No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y(1)</td><td>No-Op</td><td>N/A</td><td rowspan="2">SnpCur</td><td rowspan="2">Cmp</td><td>MSO-NO</td><td rowspan="2"></td><td>N/A</td><td rowspan="2"></td><td rowspan="2">UC</td><td rowspan="4">UC</td><td rowspan="2">The host wants a current value of the cacheline without changing the state expected in the host cache.</td></tr><tr><td>O-2</td><td>EMS</td><td>E-No-Op</td><td>EMS-NO</td><td>EMV-NA</td></tr><tr><td>Y</td><td>No-Op</td><td>N/A</td><td rowspan="2">No-Op</td><td rowspan="2">Cmp</td><td>MSO-NO</td><td rowspan="2"></td><td>N/A</td><td rowspan="2"></td><td rowspan="2">UC</td><td rowspan="2">The host wants the value of the memory location without snooping the device cache and without changing the cache state expected in the host cache. A use case for this would be if the host includes E-state or S-state without data so that the host is requesting data only and does not want to change the cache state, and because the host has E-state or S-state, the host can know that the device cache does not need to be snooped.</td></tr><tr><td>O-2</td><td>EMS</td><td>E-No-Op</td><td>EMS-NO</td><td>EMV-NA</td></tr><tr><td>Y</td><td></td><td></td><td></td><td></td><td>MemData-NXM</td><td>No-Op</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>The special case MemData-NXM response is used if the fabric or the device is unable to positively decode the Address. This is a common response type for both Type 2 devices and Type 3 devices to avoid an ambiguous case in which the host is unsure of whether the host should expect an NDR message.See Section 3.3.11 for additional details.</td></tr></table>

Ta ble C-3 <sub>.</sub> H DM - DB Memory Req uests with TE State (Sheet 3 of 6)

<table><tr><td rowspan="2">Legal</td><td colspan="4">Host Request</td><td colspan="5">Device Response</td><td colspan="3">Final Device State</td><td rowspan="2">Description</td></tr><tr><td><img src="images/fe4dffbd89f8cac477fbf455d71408e84eaf3c3a0095c102aa1e659ce043e315.jpg"/></td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td>DRS Trailer</td><td>Device Cache</td><td> $DTRCS^1$ </td><td>EMD</td></tr><tr><td>Y(1)</td><td rowspan="8"><img src="images/313a2cda569f331b4293b435d075def89c6218a9ffc3eb3008038cd4c79639bc.jpg"/></td><td rowspan="8">MSO</td><td rowspan="4">A</td><td>SnpInv</td><td> $Cmp-E^4$ </td><td rowspan="16"></td><td></td><td></td><td rowspan="16">N/A</td><td>I or UCM</td><td>A or UCM</td><td>UC</td><td>The host wants ownership of the cacheline but does not require the data.</td></tr><tr><td>N</td><td>SnpData</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td rowspan="4">S</td><td>SnpInv</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>SnpData</td><td> $Cmp-S^4$ </td><td></td><td></td><td>S or I or UCM</td><td>S or UCM</td><td>UC</td><td>The host wants the device to degrade to S-state in its caches, and wants the shared state for the cacheline (but does not require the data).</td></tr><tr><td>N</td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>No-Op</td><td rowspan="5"></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y(1)</td><td rowspan="9"><img src="images/4fbacd814bfadd5d6f8249e308abd1d629335994b715e3cde8980d066db98a4e.jpg"/></td><td rowspan="4">I</td><td>SnpInv</td><td>Cmp</td><td></td><td></td><td>I or UCM</td><td>I</td><td>UC</td><td>The host wants the device to invalidate the cacheline from its caches and does not require the data.</td></tr><tr><td>N</td><td>SnpData</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td rowspan="4">No-Op</td><td rowspan="4">N/A</td><td>SnpInv</td><td>Cmp</td><td></td><td></td><td>I or UCM</td><td>UC</td><td>UC</td><td>The host wants the device to invalidate the cacheline from its caches and does not require the data.</td></tr><tr><td>N</td><td>SnpData</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>EMS</td><td>N/A</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Ta ble C-3 <sub>.</sub> H DM - DB Memory Req uests with TE State (Sheet 4 of 6)

<table><tr><td rowspan="2">Legal</td><td colspan="4">Host Request</td><td colspan="5">Device Response</td><td colspan="3">Final Device State</td><td rowspan="2">Description</td></tr><tr><td><img src="images/fe4dffbd89f8cac477fbf455d71408e84eaf3c3a0095c102aa1e659ce043e315.jpg"/></td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td>DRS Trailer</td><td>Device Cache</td><td> $DTRCS^1$ </td><td>EMD</td></tr><tr><td>Y(1)</td><td rowspan="12"><img src="images/313a2cda569f331b4293b435d075def89c6218a9ffc3eb3008038cd4c79639bc.jpg"/><img src="images/f4d47453a73e400e8be8fb41f2546d1f35d82af43313b1f0288d90706bf6091a.jpg"/></td><td rowspan="12">MSO</td><td rowspan="4">A</td><td>SnpInv</td><td>Cmp-ECmpTEE-E4</td><td rowspan="16">&lt;none&gt;</td><td></td><td></td><td rowspan="16">N/A</td><td>I or UCM</td><td>A or UCM</td><td>UC</td><td>The host wants ownership of the cacheline but does not require the data.</td></tr><tr><td>N</td><td>SnpData</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td rowspan="4">S</td><td>SnpInv</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>SnpData</td><td>Cmp-S/CmpTEE-S4</td><td></td><td></td><td>S or I or UCM</td><td>S or UCM</td><td>UC</td><td>The host wants the device to degrade to S-state in its caches, and wants the shared state for the cacheline (but does not require the data).</td></tr><tr><td>N</td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y(1)</td><td rowspan="4">I</td><td>SnpInv</td><td>Cmp/CmpTEE</td><td></td><td></td><td>I or UCM</td><td>I</td><td>UC</td><td>The host wants the device to invalidate the cacheline from its caches and does not require the data.</td></tr><tr><td>N</td><td>SnpData</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td rowspan="5"><img src="images/caa6e086d28e4e3a04e64f43618eef615d4a6441396edee0fbc7acdab1f505c7.jpg"/></td><td rowspan="4">No-Op</td><td rowspan="4">N/A</td><td>SnpInv</td><td>Cmp/CmpTEE</td><td></td><td></td><td>I or UCM</td><td>UC</td><td>UC</td><td>The host wants the device to invalidate the cacheline from its caches and does not require the data.</td></tr><tr><td>N</td><td>SnpData</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>EMS</td><td>N/A</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Ta ble C-3 <sub>.</sub> H DM - DB Memory Req uests with TE State (Sheet 5 of 6)

<table><tr><td rowspan="2">Legal</td><td colspan="4">Host Request</td><td colspan="5">Device Response</td><td colspan="3">Final Device State</td><td rowspan="2">Description</td></tr><tr><td>M2S Req</td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td>DRS Trailer</td><td>Device Cache</td><td> $DTRCS^1$ </td><td>EMD</td></tr><tr><td>N</td><td rowspan="10">MemRdData/MemRdDataTEE</td><td>&lt;all&gt;</td><td rowspan="10">N/A</td><td>SnpInv</td><td></td><td rowspan="9">MemData/MemDataTEE</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y(1)</td><td>MS0-NO</td><td rowspan="6">SnpData</td><td rowspan="2">Cmp-E</td><td>MS0</td><td rowspan="2">I or A</td><td>N/A</td><td rowspan="2">I or UCM</td><td rowspan="2">A or UCM</td><td rowspan="6">UC</td><td rowspan="6">The host wants a cacheable copy in either E-state or S-state.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMS</td><td>EMV</td></tr><tr><td>Y(1)</td><td>MS0-NO</td><td rowspan="2">Cmp-S</td><td>MS0</td><td rowspan="2">S</td><td>N/A</td><td rowspan="2">I or S or UCM</td><td rowspan="2"> $S^3$  or UCM</td></tr><tr><td>O-2</td><td>EMS</td><td>EMS</td><td>EMV</td></tr><tr><td>Y</td><td rowspan="5">&lt;all&gt;</td><td>Cmp-E</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2">N/A</td><td>I or UCM</td><td>A or UCM</td></tr><tr><td>Y</td><td>Cmp-S</td><td>I or S or UCM</td><td> $S^3$  or UCM</td></tr><tr><td>N</td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td></td><td></td><td>MemData-NXM</td><td>No-Op</td><td>N/A</td><td>N/A</td><td>N/A</td><td>UC</td><td>UC</td><td>The special case MemData-NXM response is used if the fabric or the device is unable to positively decode the Address. This is a common response type for both Type 2 devices and Type 3 devices to avoid an ambiguous case in which the host is unsure of whether the host should expect an NDR message.See Section 3.3.11 for additional details.</td></tr><tr><td>N</td><td rowspan="3">MemSpecRd/MemSpecRdTEE</td><td>MS0-EMD</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td>Snp*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>O-3</td><td>No-Op</td><td></td><td></td><td></td><td></td><td>N/A</td><td>UC</td><td>UC</td><td>UC</td><td>Speculative memory read. A Demand read following this with the same address will be merged in the device. No completion is expected for this transaction. Completion is returned with demand read.</td></tr><tr><td>N</td><td rowspan="4">MemClnEvctU&lt;Requester does not know TE State&gt;</td><td rowspan="3">MS0</td><td>A or S</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td rowspan="2">I</td><td>No-Op</td><td>Cmp</td><td></td><td>No-Op</td><td>N/A</td><td>N/A</td><td>UC</td><td>I</td><td>UC</td><td>The host will only issue this request from E-state or from S-state.Target should make best estimate of TE State if required for coherence resolution.</td></tr><tr><td>N</td><td>Snp*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>EMS-NO</td><td>N/A</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Ta ble C-3 <sub>.</sub> H DM - DB Memory Req uests with TE State (Sheet 6 of 6)

<table><tr><td rowspan="2">Legal</td><td colspan="4">Host Request</td><td colspan="5">Device Response</td><td colspan="3">Final Device State</td><td rowspan="2">Description</td></tr><tr><td>M2S Req</td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td>DRS Trailer</td><td>Device Cache</td><td> $DTRCS^1$ </td><td>EMD</td></tr><tr><td>N</td><td rowspan="4">MemCInEvct/MemCInEvctTEE</td><td rowspan="3">MS0</td><td>A or S</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td rowspan="2">I</td><td>No-Op</td><td>Cmp</td><td></td><td>No-Op</td><td>N/A</td><td>N/A</td><td>UC</td><td>I</td><td>UC</td><td>The host will only issue these requests from E-state or from S-state. Requester should use these commands if TE State is known.</td></tr><tr><td>N</td><td>Snp*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>EMS-NO</td><td>N/A</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">N</td><td>MemRdFwd</td><td rowspan="2" colspan="11"></td><td rowspan="2">Not supported (these requests are only used with HDM-D).</td></tr><tr><td>MemWrFwd</td></tr></table>

1 . D ev i ce Tra c ked Req u este r Co h e re n cy Sta te ( see S ecti o n 1 1 . 5 . 4 . 1 1 . 3 fo r a d d i ti o n a l d eta i l s ) .  
2 . C m <sub>p</sub> - M res <sub>p</sub>o n se i s d i s - a l l owed fro m ta r<sub>g</sub> et i f TE m i s m a tc h i s d etected .  
4 N X M ca se exce <sub>p</sub>ti o n See Secti o n 3 3 1 1 fo r d eta i l s  
3 . Ta r<sub>g</sub> et m u st n ot d ow n <sub>g</sub> ra d e to S - sta te o n TE m i s m a tc h i f t h e c u rre n t sta te tra c ked i s A- sta te .

## C <sub>.</sub> 1 <sub>.</sub> 1 Forwa rd Flows for H D M - D

Ta b l e C -4 s h ows th e fl ows th a t ca n <sub>g</sub> e n e ra te M e m <sup>\*</sup> Fwd m essa <sub>g</sub> es o n CX L <sub>.</sub> m e m fro m CX L <sub>.</sub> ca c h e re<sub>q</sub> u ests <sub>.</sub> Th ese fl ows a re tri <sub>g g</sub> e red w h e n a d ev i ce i ss u es a D 2 H Re<sub>q</sub> u est to a n a d d ress th a t i s m a <sub>p p</sub>ed w i th i ts ow n CX L <sub>.</sub> m e m a d d ress re<sub>g</sub> i o n <sub>.</sub> Th i s re<sub>g</sub> i o n i s refe rred to a s d evi ce -atta ch ed m e m o r<sub>y.</sub>

Note : Th e H D M - D re<sub>g</sub> i o n i s i n te n d ed to be u sed o n l <sub>y</sub> fo r ca ses i n w h i c h th e d ev i ce o r h ost d oes n ot s u <sub>p p</sub>o rt 2 5 6 B Fl i t m od e <sub>.</sub> I n ca ses w h e re th e h ost<sub>,</sub> sw itc h <sub>,</sub> a n d d ev i ce s u <sub>p p</sub>o rts 2 5 6 B Fl i t m od e <sub>,</sub> th e H D M - D B m u st be u sed <sub>.</sub>

Ta ble C-4<sub>.</sub> H D M - D Req uest Forwa rd Su b-ta ble (Sheet 1 of 2)

<table><tr><td rowspan="2">Legal</td><td>Device Request</td><td colspan="4">Host Response on M2S Req</td><td colspan="2">Final Device State</td><td rowspan="2">Description</td></tr><tr><td>D2H Req</td><td>M2S Req</td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>Device Cache</td><td>Host State</td></tr><tr><td>Y</td><td rowspan="5">RdCurr</td><td rowspan="5">MemRdFwd</td><td rowspan="4">MS0</td><td>A</td><td rowspan="3">No-Op</td><td rowspan="3">I</td><td>A</td><td rowspan="3">MemRdFwd will reflect the final cache state of the host and for RdCurr it is recommended that the host not change the cache state.</td></tr><tr><td>Y</td><td>S</td><td>S</td></tr><tr><td>Y</td><td>I</td><td>I</td></tr><tr><td>N</td><td></td><td>Snp*</td><td></td><td></td><td></td></tr><tr><td>N</td><td>EMS-NO</td><td>N/A</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td rowspan="5">RdShared</td><td rowspan="5">MemRdFwd</td><td rowspan="4">MS0</td><td>A</td><td rowspan="3">No-Op</td><td></td><td></td><td></td></tr><tr><td>Y</td><td>S</td><td rowspan="2">S</td><td>S</td><td rowspan="2">The host must only be in S-state or I-state.</td></tr><tr><td>Y</td><td>I</td><td>I</td></tr><tr><td>N</td><td></td><td>Snp*</td><td></td><td></td><td></td></tr><tr><td>N</td><td>EMS-NO</td><td>N/A</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td rowspan="5">RdAny</td><td rowspan="5">MemRdFwd</td><td rowspan="4">MS0</td><td>A</td><td rowspan="3">No-Op</td><td></td><td></td><td></td></tr><tr><td>Y</td><td>S</td><td>S</td><td>S</td><td rowspan="2">The host must be in S-state or I-state.</td></tr><tr><td>Y</td><td>I</td><td>E</td><td>I</td></tr><tr><td>N</td><td></td><td>Snp*</td><td></td><td></td><td></td></tr><tr><td>N</td><td>EMS-NO</td><td>N/A</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td rowspan="5">RdOwn/RdOwnNoData</td><td rowspan="5">MemRdFwd</td><td rowspan="4">MS0</td><td>A</td><td rowspan="3">No-Op</td><td></td><td></td><td></td></tr><tr><td>N</td><td>S</td><td></td><td></td><td></td></tr><tr><td>Y</td><td>I</td><td>E</td><td>I</td><td>The host must be in I-state.</td></tr><tr><td>N</td><td></td><td>Snp*</td><td></td><td></td><td></td></tr><tr><td>N</td><td>EMS-NO</td><td>N/A</td><td></td><td></td><td></td><td></td></tr></table>

![](images/90a324c30c615686afa8b945bea86a4b90d293c28a3bbf1a6e7bbc300d80ad3f.jpg)

Ta ble C-4<sub>.</sub> H D M - D Req uest Forwa rd Su b-ta ble (Sheet 2 of 2)

<table><tr><td rowspan="2">Legal</td><td>Device Request</td><td colspan="4">Host Response on M2S Req</td><td colspan="2">Final Device State</td><td rowspan="2">Description</td></tr><tr><td>D2H Req</td><td>M2S Req</td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>Device Cache</td><td>Host State</td></tr><tr><td>N</td><td rowspan="5">CLFlush</td><td rowspan="5">MemRdFwd</td><td rowspan="4">MS0</td><td>A</td><td rowspan="3">No-Op</td><td></td><td></td><td></td></tr><tr><td>N</td><td>S</td><td></td><td></td><td></td></tr><tr><td>Y</td><td>I</td><td>I</td><td>S</td><td>The host must indicate invalid, but the device must assume that S-state is possible in the host as part of the CLFlush definition.</td></tr><tr><td>N</td><td></td><td>Snp*</td><td></td><td></td><td></td></tr><tr><td>N</td><td>EMS-NO</td><td>N/A</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td rowspan="5">WOWrInv/WOWrInvF</td><td rowspan="5">MemWrFwd</td><td rowspan="4">MS0</td><td>A</td><td rowspan="3">No-Op</td><td></td><td></td><td></td></tr><tr><td>N</td><td>S</td><td></td><td></td><td></td></tr><tr><td>Y</td><td>I</td><td>NC</td><td>I</td><td>The host must be in I-state.</td></tr><tr><td>N</td><td></td><td>Snp*</td><td></td><td></td><td></td></tr><tr><td>N</td><td>EMS-NO</td><td>N/A</td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>CleanEvict/DirtyEvict/CleanEvictNoData</td><td>N/A</td><td></td><td></td><td></td><td></td><td></td><td>Messages are not sent to the host for device-attached memory.</td></tr><tr><td>N</td><td>ItoMWr/WrCur/WrInv/CacheFlushed</td><td>None</td><td></td><td></td><td></td><td></td><td></td><td>Standard CXL.cache flows are used for these requests.</td></tr></table>

## C <sub>.</sub> 1 <sub>.</sub> 2 BISn <sub>p</sub> for H D M - DB

Ta b l e C - 5 s h ows th e fl ows th a t th e d evi ce ca n <sub>g</sub> e n e ra te <sub>.</sub> Th ese fl ows a re o n l <sub>y</sub> s u <sub>p p</sub>o rted to a n a d d ress th a t i s m a <sub>p p</sub>ed i n th e d evi ces ow n CX L <sub>.</sub> m e m a d d ress re<sub>g</sub> i o n <sub>.</sub> Th i s re<sub>g</sub> i o n i s refe rred to a s d evi ce - a tta c h ed m e m o r<sub>y.</sub>

Ta ble C-5 <sub>.</sub> H D M - D B BISn <sub>p</sub> Flow (Sheet 1 of 2)p

<table><tr><td rowspan="2">Legal</td><td>Device Request</td><td>Host Response</td><td colspan="3">Final Device State</td><td rowspan="2">Description</td></tr><tr><td>S2M BISnp</td><td>M2S BIRsp</td><td>Device Cache</td><td>Host  $State^1$ </td><td>EMD</td></tr><tr><td>Y</td><td rowspan="4">BISnpCur/BISnpCurTEE</td><td>BIRspI</td><td rowspan="3">I</td><td>I</td><td rowspan="18">UC</td><td rowspan="3">Used when the device is requesting a current copy of the cacheline but is not installing the data into its cache.</td></tr><tr><td>Y</td><td>BIRspS</td><td>S</td></tr><tr><td>Y</td><td>BIRspE</td><td>A</td></tr><tr><td>N</td><td>BIRsp*Blk</td><td></td><td></td><td>Block responses are not supported.</td></tr><tr><td>Y</td><td rowspan="4">BISnpData/BISnpDataTEE</td><td>BIRspI</td><td>E, S, or I</td><td>I</td><td rowspan="2">Used when the device is requesting Shared or Exclusive state of the cacheline.</td></tr><tr><td>Y</td><td>BIRspS</td><td>S or I</td><td>S</td></tr><tr><td>N</td><td>BIRspE</td><td></td><td></td><td></td></tr><tr><td>N</td><td>BIRsp*Blk</td><td></td><td></td><td></td></tr><tr><td>Y</td><td><img src="images/f67d1f2c5255c0a7b4d6b831d5b741d536985f15fabd7f990a0ff668954e55f2.jpg"/></td><td>BIRspI</td><td>E, S, or I</td><td>I</td><td>Used when device is requesting Exclusive state of the cacheline including capacity evictions for device Inclusive Snoop Filter evictions. The device may choose to install only in its cache in S-state for device-specific reasons.</td></tr><tr><td>N</td><td rowspan="3">BISnpInv/BISnpInvTEE</td><td>BIRspS</td><td></td><td></td><td></td></tr><tr><td>N</td><td>BIRspE</td><td></td><td></td><td></td></tr><tr><td>N</td><td>BIRsp*Blk</td><td></td><td></td><td></td></tr><tr><td>Y</td><td rowspan="6"><img src="images/e787550d50b2ecfca5bc59b022b6b7005fb32d79565990dc88d5ff839cd80dd8.jpg"/></td><td>BIRspI</td><td rowspan="6">I</td><td>I</td><td rowspan="3">Used when device is requesting a current copy of a multiple line block but is not installing into its cache. Response is per cacheline.</td></tr><tr><td>Y</td><td>BIRspS</td><td>S</td></tr><tr><td>Y</td><td>BIRspE</td><td>A</td></tr><tr><td>Y</td><td>BIRspIBlk</td><td>I — Blk</td><td rowspan="3">Used when device is requesting current copy of multiple line block but is not installing into its cache. Response is for the entire block.</td></tr><tr><td>Y</td><td>BIRspSBlk</td><td>S — Blk</td></tr><tr><td>Y</td><td>BIRspEBlk</td><td>A — Blk</td></tr></table>

Ta ble C-5 <sub>.</sub> H DM - DB BISn p Flow (Sheet 2 of 2)

<table><tr><td rowspan="2">Legal</td><td>Device Request</td><td>Host Response</td><td colspan="3">Final Device State</td><td rowspan="2">Description</td></tr><tr><td>S2M BISnp</td><td>M2S BIRsp</td><td>Device Cache</td><td>Host  $State^1$ </td><td>EMD</td></tr><tr><td>Y</td><td rowspan="6">BISnpDataBlk/BISnpDataBlkTEE</td><td>BIRspI</td><td>E, S, or I</td><td>I</td><td rowspan="12">UC</td><td rowspan="2">Used when device is requesting a Shared or Exclusive copy of a multiple cacheline block. Response is per cacheline.</td></tr><tr><td>Y</td><td>BIRspS</td><td>S or I</td><td>S</td></tr><tr><td>N</td><td>BIRspE</td><td></td><td></td><td></td></tr><tr><td>Y</td><td>BIRspIBlk</td><td>E, S, or I</td><td>I — Blk</td><td rowspan="2">Used when device is requesting a Shared or Exclusive copy of a multiple cacheline block. Response is for the entire block.</td></tr><tr><td>Y</td><td>BIRspSBlk</td><td>S or I</td><td>S — Blk</td></tr><tr><td>N</td><td>BIRspEBlk</td><td></td><td></td><td></td></tr><tr><td>Y</td><td rowspan="6">BISnpInvBlk/BISnpInvBlkTEE</td><td>BIRspI</td><td>E, S, or I</td><td>I</td><td>Used when device is requesting an Exclusive copy of a multiple cacheline block. Response is per line.</td></tr><tr><td>N</td><td>BIRspS</td><td></td><td></td><td></td></tr><tr><td>N</td><td>BIRspE</td><td></td><td></td><td></td></tr><tr><td>Y</td><td>BIRspIBlk</td><td>E, S, or I</td><td>I — Blk</td><td>Used when device is requesting an Exclusive copy of a multiple cacheline block. Response is for the entire block.</td></tr><tr><td>N</td><td>BIRspSBlk</td><td></td><td></td><td></td></tr><tr><td>N</td><td>BIRspEBlk</td><td></td><td></td><td></td></tr></table>

1 . H ost Sta te ( a ka B i a s Sta te ) t ra c ki n g i n t h e d ev i ce ca n be i m p l e m e n ted w it h a fu l l Ta b l e o r i n c l u s i ve S F .

## C<sub>.</sub> 2 H DM - H Re<sub>q</sub> uests

H D M - H i s u sed o n l <sub>y</sub> b<sub>y</sub> T<sub>y p</sub>e 3 d ev i ces fo r s i m <sub>p</sub> l e m e m o r<sub>y</sub> ex <sub>p</sub>a n s i o n <sub>.</sub> Re<sub>q</sub> u ests fro m th e h ost to th i s re<sub>g</sub> i o n a l wa<sub>y</sub>s e n cod e S n <sub>p</sub>T<sub>y p</sub>e a s N o - O <sub>p</sub> a n d th e h ost ca n a l so m a ke a rb i tra r<sub>y</sub> u se of th e M etaVa l u e fi e l d to sto re 2 - b it e n cod i n <sub>g</sub> s w h i c h th e d evi ce s h o u l d n ot i n te r<sub>p</sub> ret <sub>.</sub> Ta b l e C - 6 ca ptu res th e fl ows fo r th ese d ev i ces .p

Ta ble C-6 <sub>.</sub> H DM - H Memory Req uest (Sheet 1 of 2)

<table><tr><td rowspan="2">Legal</td><td colspan="4">Host Request</td><td colspan="5">Device Response</td><td>Device State</td><td rowspan="2">Description</td></tr><tr><td>M2S-Req</td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td>DRS Trailer</td><td>Metadata/ EMD</td></tr><tr><td>N</td><td></td><td></td><td></td><td>Snp*</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Snoop encodings are never sent to the HDM-H address region.</td></tr><tr><td>Y</td><td rowspan="4">MemRd/MemRdTEE1</td><td>MS0</td><td></td><td rowspan="6">No-Op</td><td rowspan="4"></td><td rowspan="2">MemData/MemDataTEE1/MemData-NXM2</td><td rowspan="2"></td><td rowspan="2"></td><td>N/A</td><td>MetaValue</td><td>Read that is requesting Meta State field updates to new values.</td></tr><tr><td>Y</td><td>No-Op</td><td>N/A</td><td>N/A</td><td>UC</td><td>Read that does not expect a Meta State field update.</td></tr><tr><td>O-2</td><td rowspan="2">EMS</td><td rowspan="2">N/A</td><td>MemData/MemDataTEE1</td><td>EMS-NO</td><td>N/A</td><td>EMV-NA</td><td>UC</td><td>EMS in DRS indicates EMV trailer is returned. No Metadata is changed as a result of this message.</td></tr><tr><td>O-2</td><td>MemData-NXM2</td><td>No-Op</td><td>N/A</td><td rowspan="3">N/A</td><td>UC</td><td>NXM response must only return No-Op MetaField for decode errors of requests with MetaField of EMS.</td></tr><tr><td>Y</td><td rowspan="2">MemInv/MemInvNT</td><td>MS0</td><td></td><td rowspan="2">Cmp</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td>MetaValue</td><td>The host wants to read the Meta State field and update it.</td></tr><tr><td>Y</td><td>No-Op</td><td>N/A</td><td>UC</td><td>The host wants to read the Meta State field but does not want to update it.</td></tr><tr><td>N</td><td rowspan="4">MemRdData/MemRdDataTEE1</td><td>MS0 or EMS</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td rowspan="3">No-Op</td><td rowspan="3">N/A</td><td rowspan="3">No-Op</td><td rowspan="3"></td><td rowspan="3">MemData/MemDataTEE1/MemData-NXM2</td><td>MS0</td><td>I or A</td><td rowspan="3">N/A</td><td>A</td><td rowspan="2">Used for implicit directory state updates in the HDM-H address region. This is the only case in which devices with HDM-H must decode the MetaValue field.</td></tr><tr><td>Y</td><td>MS0</td><td>S</td><td>S</td></tr><tr><td>Y</td><td>No-Op</td><td>N/A</td><td>N/A</td><td>Used for devices that do not store the MetaValue field or if the MetaValue field is corrupted.</td></tr><tr><td>N</td><td rowspan="3">MemSpecRd/MemSpecRdTEE1</td><td>MS0 or EMS</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td>Snp*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>O-3</td><td>No-Op</td><td></td><td></td><td></td><td></td><td>N/A</td><td>UC</td><td>Speculative memory read. A demand read that follows this with the same address will be merged in the device. No completion is expected for this transaction. Completion is returned with a demand read.</td></tr></table>

Ta ble C-6<sub>.</sub> H DM - H Memory Req uest (Sheet 2 of 2)

<table><tr><td rowspan="2">Legal</td><td colspan="4">Host Request</td><td colspan="5">Device Response</td><td>Device State</td><td rowspan="2">Description</td></tr><tr><td>M2S Req</td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td>DRS Trailer</td><td>Metadata/ EMD</td></tr><tr><td>N</td><td>MemClnEvct</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan="3">These messages are not used for the HDM-H address region.</td></tr><tr><td>N</td><td>MemRdFwd</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>MemWrFwd</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>O-4</td><td rowspan="4">TEUpdate</td><td rowspan="3">MS0</td><td>00b (clear TE)</td><td rowspan="4"></td><td rowspan="2">Cmp</td><td rowspan="2"></td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2">N/A</td><td rowspan="2">UC</td><td rowspan="2">Commands used to set or clear TE State for region of memory. The TE is set when MetaValue is 01b and cleared when MetaValue is 00b. This command is optionally supported by devices that support TSP.</td></tr><tr><td>O-4</td><td>01b (set TE)</td></tr><tr><td>N</td><td>10b or 11b</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>No-Op or EMS</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

1 . TE E o <sub>p</sub>cod es a re o <sub>p</sub>ti o n a l l <sub>y</sub> e n a b l ed .  
2 . Retu rn ed w h e n th e Sw itc h o r D ev i ce ca n n ot <sub>p</sub>os i ti ve l <sub>y</sub> d ecod e th a t th e a d d ress i s H D M - H vs . H D M - D <sup>\*</sup> a d d ress re<sub>g</sub> i o n . Th i s res <sub>p</sub>o n se a l l ows th e h ost to co m <sub>p</sub> l ete th e re<sub>q</sub> u est b<sub>y</sub> co n ve r<sub>g</sub> i n <sub>g</sub> th e fl ows fo r th i s Decod e M i ss e rro r betwee n th e H D M - H a n d H D M - D <sup>\*</sup> . S ee Secti o n 3 . 3 . 1 1 fo r d eta i l s .

C<sub>.</sub> 3 H DM-D RwD

Ta b l e C - 7 ca ptu res th e Req u est w i th Da ta ( Rw D ) fl ows fo r H D M - D a d d ress reg i o n s u sed by Ty pe 2 d ev i ces <sub>.</sub> E M D i s n ot a p p l i ca b l e fo r H D M - D <sub>.</sub>

Ta ble C-7 <sub>.</sub>

H DM-D Memor<sub>y</sub> RwD

<table><tr><td rowspan="2">Legal</td><td colspan="5">Host Request</td><td colspan="4">Device Response</td><td colspan="2">Device State</td><td rowspan="2">Description</td></tr><tr><td>M2S RWD</td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>RwD Trailer</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td>Dev Cache</td><td>Host State</td></tr><tr><td>N</td><td rowspan="15">MemWr/MemWrPtl</td><td>MS0-EMS</td><td rowspan="3">A</td><td>Snp*</td><td></td><td></td><td rowspan="14">&lt;none&gt;</td><td></td><td></td><td></td><td></td><td>Snoop encodings are never sent with A-state because the host must have an exclusive copy of the cacheline.</td></tr><tr><td>Y(1)</td><td>MS0</td><td rowspan="2">No-Op</td><td>N/A</td><td rowspan="2">Cmp</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2">I</td><td rowspan="2">A</td><td rowspan="2">The host wants to update memory and keep an exclusive copy of the cacheline.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMV</td></tr><tr><td>N</td><td>MS0-EMS</td><td rowspan="3">S</td><td>Snp*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>MS0</td><td rowspan="2">No-Op</td><td>N/A</td><td rowspan="2">Cmp</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2">I</td><td rowspan="2">S</td><td rowspan="2">The host wants to update memory and keep a shared copy of the cacheline.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMV</td></tr><tr><td>Y(1)</td><td>MS0</td><td rowspan="6">I</td><td rowspan="2"> $SnpInv^1$ </td><td>N/A</td><td rowspan="2">Cmp</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2">I</td><td rowspan="2">I</td><td rowspan="2">The host wants to write the cacheline back to memory and does not retain a cacheable copy. In addition, the host was not granted ownership of the cacheline before performing this write and needs the device to invalidate the device&#x27;s caches before performing the writeback to memory.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMV</td></tr><tr><td>N</td><td rowspan="2">MS0-EMS</td><td>SnpData</td><td></td><td></td><td></td><td></td><td></td><td></td><td>No use case.</td></tr><tr><td>N</td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y(1)</td><td>MS0</td><td rowspan="2">No-Op</td><td>N/A</td><td rowspan="2">Cmp</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2">I</td><td rowspan="2">I</td><td rowspan="2">The host wants to update memory and will end with host caches in I-state. Use is for Dirty (M-state) Cache Evictions in the host.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMV</td></tr><tr><td>N</td><td>MS0-EMS</td><td></td><td></td><td></td><td rowspan="2">Cmp</td><td>MS0</td><td></td><td></td><td></td><td>The device never returns the Meta State field for a write.</td></tr><tr><td>N</td><td>No-Op</td><td>N/A</td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan="2">The host must always define the MetaValue field for writes.</td></tr><tr><td>N</td><td>EMD</td><td>E-No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>BIConflict</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>BISnp conflict handling flow is not supported for HDM-D.</td></tr><tr><td>N</td><td>MemRdFill/MemWrTEE/MemWrPtlTEE/MemRdFillTEE/TEUpdate</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>TEE is not supported for HDM-D in this revision of the specification.</td></tr></table>

1 . S n oo <sub>p</sub>a b l e W rites a re n ot s u <sub>p p</sub>o rted i n S h a red FA M u se ca ses .

![](images/e1a65828dbb1fdbb0077577c2c0cfe5a8c2409095a265982e11f81500a237170.jpg)

![](images/588be3e8a16bfe7bd37d3d8ab15076a87ff18c7c8bda418e6600c5e6941bec61.jpg)  
Ta ble C-8 <sub>.</sub>

## C<sub>.</sub>4 H DM-DB RwD

Ta b l e C - 8 ca ptu res th e Req u est w i th Da ta ( Rw D ) fl ows fo r H D M - D B a d d ress reg i o n s u sed by Ty pe 2 d evi ces a n d Ty pe 3 d evi ces <sub>.</sub>

<table><tr><td rowspan="2">Legal</td><td colspan="5">Host Request</td><td colspan="4">Device Response</td><td colspan="3">Device State</td><td rowspan="2">Description</td></tr><tr><td>M2S RWD</td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>RwD Trailer</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td>Dev Cache</td><td>Host State</td><td> $EMD^1$ </td></tr><tr><td>N</td><td rowspan="15">MemWr/MemWrTEE2/MemWrPtl/MemWrPtITEE2</td><td>MS0-EMS</td><td rowspan="3">A</td><td>Snp*</td><td></td><td></td><td rowspan="14"></td><td></td><td></td><td></td><td></td><td></td><td>Snoop encodings are never sent with A-state because the host must have an exclusive copy of the cacheline.</td></tr><tr><td>Y(1)</td><td>MS0</td><td rowspan="2">No-Op</td><td>N/A</td><td rowspan="2">Cmp</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2">I</td><td rowspan="2">A</td><td>UC</td><td rowspan="2">The host wants to update memory and keep an exclusive copy of the cacheline.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMV</td><td>EMV</td></tr><tr><td>N</td><td>MS0-EMS</td><td rowspan="3">S</td><td>Snp*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td>MS0</td><td rowspan="2">No-Op</td><td>N/A</td><td rowspan="2">Cmp</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2">I</td><td rowspan="2">S</td><td>UC</td><td rowspan="2">The host wants to update memory and keep a shared copy of the cacheline.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMV</td><td>EMV</td></tr><tr><td>Y(1)</td><td>MS0</td><td rowspan="6">I</td><td rowspan="2"> $SnpInv^3$ </td><td>N/A</td><td rowspan="2">Cmp</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2">I</td><td rowspan="2">I</td><td>UC</td><td rowspan="2">The host wants to write the cacheline back to memory and does not retain a cacheable copy. In addition, the host was not granted ownership of the cacheline before performing this write and needs the device to invalidate the device&#x27;s caches before performing the writeback to memory.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMV</td><td>EMV</td></tr><tr><td>N</td><td rowspan="2">MS0-EMS</td><td>SnpData</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>No use case.</td></tr><tr><td>N</td><td>SnpCur</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y(1)</td><td>MS0</td><td rowspan="2">No-Op</td><td>N/A</td><td rowspan="2">Cmp</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2">I</td><td rowspan="2">I</td><td>UC</td><td rowspan="2">The host wants to update memory and will end with host caches in I-state. Use is for Dirty (M-state) Cache Evictions in the host.</td></tr><tr><td>O-2</td><td>EMS</td><td>EMV</td><td>EMV</td></tr><tr><td>N</td><td>MS0-EMS</td><td></td><td></td><td></td><td>Cmp</td><td>MS0</td><td></td><td></td><td></td><td></td><td>The device never returns the Meta State field for a write.</td></tr><tr><td>N</td><td>No-Op</td><td>N/A</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan="2">The host must always define the MetaValue field for writes.</td></tr><tr><td>N</td><td>EMD</td><td>E-No-Op</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Y</td><td rowspan="3">BIConflict</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td>No-Op</td><td>N/A</td><td>BIConflict Ack</td><td></td><td>No-Op</td><td>N/A</td><td>UC</td><td>UC</td><td>UC</td><td>Used as part of the BISnp conflict handling flow.</td></tr><tr><td>N</td><td>Snp*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>MS0-EMS</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Ta ble C-8<sub>.</sub> H DM - DB Memory RwD (Sheet 2 of 2)

<table><tr><td rowspan="2">Legal</td><td colspan="5">Host Request</td><td colspan="4">Device Response</td><td colspan="3">Device State</td><td rowspan="2">Description</td></tr><tr><td>M2S RwD</td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>RwD Trailer</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td>Dev Cache</td><td>Host State</td><td> $EMD^1$ </td></tr><tr><td>O-4</td><td rowspan="4">MemRdFill/MemRdFillTEE $^2$ </td><td rowspan="3">No-Op</td><td rowspan="3">N/A</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2"></td><td>MemData/MemDataTEE $^2$ </td><td rowspan="2"></td><td rowspan="2"></td><td></td><td></td><td>UC</td><td rowspan="2">Support for this command is required by devices that support TSP to support host-side memory encryption. The result of this read does not change meta-state and returns only data to the host. The use case is expected for partial write merging that is not possible in the device with host-side encryption.</td></tr><tr><td>O-4</td><td>MemData-NXM</td><td></td><td></td><td></td></tr><tr><td>N</td><td>Snp*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>MS0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>O-4</td><td rowspan="4">TEUpdate $^2$ </td><td rowspan="3">MS0</td><td>00b (clear TE)</td><td rowspan="4"></td><td rowspan="3">N/A</td><td rowspan="2">Cmp</td><td rowspan="2"></td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td></td><td></td><td rowspan="2">UC</td><td rowspan="2">Commands used to set or clear TE State for region of memory. The TE is set when MetaValue is 01b and cleared when MetaValue is 00b. This command is optionally supported by devices that support TSP.</td></tr><tr><td>O-4</td><td>01b (set TE)</td><td></td><td></td></tr><tr><td>N</td><td>10b or 11b</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>No-Op or EMS</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

1 A<sub>p p</sub> l i ca b l e o n l<sub>y</sub> w ith E M D e n a b l ed<sup>i</sup>  
2 TE E o <sub>p</sub>cod es a re o <sub>p</sub>ti o n a l l <sub>y</sub> e n a b l ed  
<sub>3 S n oo pa b l e W rites a re n ot s u p po rted i n S h a red FAM u se ca ses</sub>t

## C<sub>.</sub> 5 H DM-H RwD

Ta b l e C - 9 ca ptu res th e Req u est w i th Da ta ( Rw D ) fl ows fo r th e H D M - H m e m o ry reg i o n <sub>.</sub>

Ta ble C-9 <sub>.</sub>

<table><tr><td rowspan="2">Legal</td><td colspan="5">Host Request</td><td colspan="4">Device Response</td><td>Device State</td><td rowspan="2">Description</td></tr><tr><td>M2S RwD</td><td>MetaField</td><td>MetaValue</td><td>SnpType</td><td>RwD Trailer</td><td>S2M NDR</td><td>S2M DRS</td><td>MetaField</td><td>MetaValue</td><td> $Metadata/EMD^1$ </td></tr><tr><td>N</td><td rowspan="5">MemWr/MemWrPtl/MemWrTEE2/MemWrPtITEE2</td><td>MS0-EMS</td><td></td><td>Snp*</td><td></td><td></td><td rowspan="5"></td><td></td><td></td><td></td><td>SnpType encodings are never sent to the HDM-H.</td></tr><tr><td>Y</td><td>MS0</td><td></td><td rowspan="2">No-Op</td><td>N/A</td><td rowspan="2">Cmp $CmpTEE^2$ </td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td>MetaValue</td><td>The host wants to update memory. The host sets a value in the MetaValue field. The device optionally stores that MetaValue field value.</td></tr><tr><td>O-2</td><td>EMS</td><td>N/A</td><td>EMV</td><td>EMV</td><td>Note: MemWrPtl is not expected to be used with host-side encryption.</td></tr><tr><td>N</td><td></td><td></td><td>No-Op</td><td></td><td>Cmp</td><td>MS0</td><td></td><td></td><td>The host never needs the Meta State field value returned from a write.</td></tr><tr><td>N</td><td>No-Op</td><td>N/A</td><td></td><td></td><td></td><td></td><td></td><td></td><td>The host always sends MS0 to avoid the need for a Read-modify-write in the device for the MetaValue field.</td></tr><tr><td>N</td><td>BIConflict</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>This message is not used for the HDM-H memory region.</td></tr><tr><td>O-4</td><td rowspan="4">MemRdFll/MemRdFllITEE2</td><td rowspan="3">No-Op</td><td rowspan="3">N/A</td><td rowspan="2">No-Op</td><td rowspan="2">N/A</td><td rowspan="2"></td><td>MemData/MemDataTEE2</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2">UC</td><td rowspan="2">Support for this command is required by devices that support TSP to support host-side memory encryption. The result of this read does not change meta-state and returns only data to the host. The use case is expected for partial write merging that is not possible in the device with host-side encryption.</td></tr><tr><td>O-4</td><td>MemData-NXM</td></tr><tr><td>N</td><td>Snp*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>MS0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

1 E M D i s a <sub>p p</sub> l i ca b l e o n l <sub>y</sub> if e n a b l ed

2 . TE E o <sub>p</sub>cod es a re o <sub>p</sub>ti o n a l l <sub>y</sub> e n a b l ed .<sub>l</sub>

![](images/a87a4138575a0d688e6be05db5203b456ef09cacdce8db165e68586a0ea6f0a1.jpg)