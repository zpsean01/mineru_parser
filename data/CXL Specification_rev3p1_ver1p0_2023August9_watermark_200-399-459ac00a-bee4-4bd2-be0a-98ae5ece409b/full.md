Figure 4-11. H5 - M2S Req  
![](images/d4575b9a2f84f73a2bbaa4bc6d6d41bcfd0998e19ba0ef54494f8fe944a811ca.jpg)

Figure 4-12. H6 - MAC  
![](images/7393a38b1930e791f407fc1a6dc1f0190d7a93b37c9e52c0e03c986029d1f6c7.jpg)

Figure 4-13. G0 - H2D/M2S Data  
![](images/6030e45583507eddc8bc7e80a29630d784e9c06459636d0d1097299d314e3925.jpg)

Figure 4-14. G0 - M2S Byte Enable  
![](images/492ea77828a12180aa8c437b7381bf333692f49706db2bb0f741c277ca82be10.jpg)

Figure 4-15. G1 - 4 H2D Rsp  
![](images/84e780cc188ce5df02026dad4547d8fe0ca0d411d894ab0a6e4abd6209e2cf47.jpg)

Figure 4-16. G2 - H2D Req + H2D Data Header + H2D Rsp  
![](images/d3d2eea8e5b4f3ebbe0438649a0b814e1953e81eaafffdde9f1ce8bb57a3ffd1.jpg)

Figure 4-17. G3 - 4 H2D Data Header + H2D Rsp  
![](images/457d97b6e9cd691d8b43e56ed9a65873f364c05f6d1d69adf82b21a1f24ce552.jpg)

Figure 4-18. G4 - M2S Req + H2D Data Header  
![](images/3763023010af578e86d492feedfc64593ba459bb29558a2cceeb95d5efcccb69.jpg)

Figure 4-19. G5 - M2S RwD Header + H2D Rsp  
![](images/7c4a21895bcfeb6c9281f283377a3c719c2e16d87ab5c791348f77111acab8d8.jpg)

## 4.2.3.2 D2H and S2M Formats

The original slot definitions ensured that all header bits for a message are in contiguous bits. The S2M NDR message expanded by two bits to fit the 2-bit DevLoad field. Some slot formats that carry NDR messages include non-contiguous bits within the slot to account for the DevLoad. The formats impacted are H4, G4, and G5 and the noncontiguous bits are denoted as “DevLoad\*” (“\*” is the special indicator with separate color/pattern for the NDR message with non-contiguous bits). By expanding the slots in this way, backward compatibility with the original contiguous bit definition is maintained by ensuring that only RSVD slot bits are used to expand the headers. Other slot formats that carry a single NDR message can be expanded and keep the contiguous header bits because the NDR message is the last message in the slot formats (see Formats H0 and H3).

Figure 4-20. H0 - D2H Data Header + 2 D2H Rsp + S2M NDR  
![](images/777ee3259d1495c704a79576c21285ba62bfef7078c9af6b8fff8aa74734722f.jpg)

Figure 4-21. H1 - D2H Req + D2H Data Header  
![](images/ba779483d84ad4cfda5089d47bd8b2eff34210dfdb9514aa52c7df1f0bf2209c.jpg)

Figure 4-22. H2 - 4 D2H Data Header + D2H Rsp

<table><tr><td colspan="8">Bit #</td></tr><tr><td></td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td></tr><tr><td>0</td><td colspan="3">Slot0</td><td>Sz</td><td>BE</td><td>Ak</td><td>RV</td></tr><tr><td>1</td><td colspan="2">Slot3 [1:0]</td><td colspan="2">Slot2</td><td colspan="3">Slot1</td></tr><tr><td>2</td><td colspan="4">RspCrd</td><td colspan="2">RSVD</td><td>SI3</td></tr><tr><td>3</td><td colspan="4">DataCrd</td><td colspan="3">ReqCrd</td></tr><tr><td>4</td><td colspan="6">UQID[6:0]</td><td>Val</td></tr><tr><td>5</td><td>Poi</td><td>Bg</td><td>Ch</td><td colspan="4">UQID[11:7]</td></tr><tr><td>6</td><td colspan="5">UQID[5:0]</td><td>Val</td><td>RV</td></tr><tr><td>7</td><td>Bg</td><td>Ch</td><td colspan="5">UQID[11:6]</td></tr><tr><td>8</td><td colspan="4">UQID[4:0]</td><td>Val</td><td>RV</td><td>Poi</td></tr><tr><td>9</td><td>Ch</td><td colspan="6">UQID[11:5]</td></tr><tr><td>10</td><td colspan="4">UQID[3:0]</td><td>Val</td><td>RV</td><td>Poi</td></tr><tr><td>11</td><td colspan="7">UQID[11:4]</td></tr><tr><td>12</td><td colspan="2">Opcode[2:0]</td><td>Val</td><td>RV</td><td>Poi</td><td>Bg</td><td>Ch</td></tr><tr><td>13</td><td colspan="5">UQID[5:0]</td><td colspan="2">Opcode[4:3]</td></tr><tr><td>14</td><td>RSVD</td><td colspan="6">UQID[11:6]</td></tr><tr><td>15</td><td colspan="7">RSVD</td></tr></table>

Figure 4-23. H3 - S2M DRS Header + S2M NDR

<table><tr><td rowspan="17">Byte #</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td colspan="2">Slot0</td><td>Sz</td><td>BE</td><td>Ak</td><td>RV</td><td>Type</td></tr><tr><td>1</td><td>Slot3 [1:0]</td><td colspan="3">Slot2</td><td colspan="3">Slot1</td></tr><tr><td>2</td><td colspan="3">RspCrd</td><td colspan="3">RSVD</td><td>SI3</td></tr><tr><td>3</td><td colspan="3">DataCrd</td><td colspan="4">ReqCrd</td></tr><tr><td>4</td><td>MetaValue</td><td colspan="2">MetaField</td><td colspan="3">MemOp</td><td>Val</td></tr><tr><td>5</td><td colspan="7">Tag[7:0]</td></tr><tr><td>6</td><td colspan="7">Tag[15:8]</td></tr><tr><td>7</td><td>RV</td><td>DevLoad</td><td colspan="4">LD-ID[3:0]</td><td>Poi</td></tr><tr><td>8</td><td colspan="7">RSVD</td></tr><tr><td>9</td><td>MetaValue</td><td colspan="2">MetaField</td><td colspan="3">MemOp</td><td>Val</td></tr><tr><td>10</td><td colspan="7">Tag[7:0]</td></tr><tr><td>11</td><td colspan="7">Tag[15:8]</td></tr><tr><td>12</td><td>RSVD</td><td colspan="2">DevLoad</td><td colspan="4">LD-ID[3:0]</td></tr><tr><td>13</td><td colspan="7">RSVD</td></tr><tr><td>14</td><td colspan="7">RSVD</td></tr><tr><td>15</td><td colspan="7">RSVD</td></tr></table>

Figure 4-24. H4 - 2 S2M NDR

<table><tr><td rowspan="17">Byte #</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>0</td><td colspan="2">Slot0</td><td>Sz</td><td>BE</td><td>Ak</td><td>RV</td><td>Type</td></tr><tr><td>1</td><td>Slot3 [1:0]</td><td colspan="2">Slot2</td><td colspan="4">Slot1</td></tr><tr><td>2</td><td colspan="3">RspCrd</td><td colspan="3">RSVD</td><td>SI3</td></tr><tr><td>3</td><td colspan="3">DataCrd</td><td colspan="4">ReqCrd</td></tr><tr><td>4</td><td>MetaValue</td><td colspan="2">MetaField</td><td colspan="3">MemOp</td><td>Val</td></tr><tr><td>5</td><td colspan="7">Tag[7:0]</td></tr><tr><td>6</td><td colspan="7">Tag[15:8]</td></tr><tr><td>7</td><td colspan="2">MemOp</td><td>Val</td><td colspan="4">LD-ID[3:0]</td></tr><tr><td>8</td><td colspan="3">Tag[3:0]</td><td>MetaValue</td><td colspan="3">MetaField</td></tr><tr><td>9</td><td colspan="7">Tag[11:4]</td></tr><tr><td>10</td><td colspan="3">LD-ID[3:0]</td><td colspan="4">Tag[15:12]</td></tr><tr><td>11</td><td colspan="3">RSVD</td><td>DevLoad*</td><td colspan="3">DevLoad</td></tr><tr><td>12</td><td colspan="7">RSVD</td></tr><tr><td>13</td><td colspan="7">RSVD</td></tr><tr><td>14</td><td colspan="7">RSVD</td></tr><tr><td>15</td><td colspan="7">RSVD</td></tr></table>

Figure 4-25. H5 - 2 S2M DRS Header  
![](images/c671431e6cdccdf655813be4b785256d96ad4927e506a59bec5f9d89c6944ec4.jpg)

Figure 4-26. H6 - MAC  
![](images/655c6889c6ba7e04dc2a1f208313debbe2a13cbaae15e3c2676722249952e84b.jpg)

Figure 4-27. G0 - D2H/S2M Data  
![](images/b76812acf09d58224bf9bedcca7238de69d3ee415bb2743fc3d86dec55b74bd3.jpg)

![](images/2534279b6a61bd01e6cd65e9abd862f3ca8be8d1842fb0f06ad97024921b75d0.jpg)

Figure 4-28. G0 - D2H Byte Enable  
Figure 4-29. G1 - D2H Req + 2 D2H Rsp  
![](images/894bab0e60693e3e925d8e4aabbada29db9be535cbb41d46190154914d11777c.jpg)

Figure 4-30. G2 - D2H Req + D2H Data Header + D2H Rsp  
![](images/ab9ad3315b6a1adf0ac52819ea29b50525e10bca19fd20c9766b6e8f5cbd0242.jpg)

Figure 4-31. G3 - 4 D2H Data Header

<table><tr><td colspan="7">Bit #</td></tr><tr><td></td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td></tr><tr><td>0</td><td colspan="5">UQID[6:0]</td><td>Val</td></tr><tr><td>1</td><td>Poi</td><td>Bg</td><td>Ch</td><td colspan="3">UQID[11:7]</td></tr><tr><td>2</td><td colspan="4">UQID[5:0]</td><td>Val</td><td>RV</td></tr><tr><td>3</td><td>Bg</td><td>Ch</td><td colspan="4">UQID[11:6]</td></tr><tr><td>4</td><td colspan="4">UQID[4:0]</td><td>Val</td><td>RV</td></tr><tr><td>5</td><td>Ch</td><td colspan="5">UQID[11:5]</td></tr><tr><td>6</td><td colspan="3">UQID[3:0]</td><td>Val</td><td>RV</td><td>Poi</td></tr><tr><td>7</td><td colspan="6">UQID[11:4]</td></tr><tr><td>8</td><td colspan="3">RSVD</td><td>RV</td><td>Poi</td><td>Bg</td></tr><tr><td>9</td><td colspan="6">RSVD</td></tr><tr><td>10</td><td colspan="6">RSVD</td></tr><tr><td>11</td><td colspan="6">RSVD</td></tr><tr><td>12</td><td colspan="6">RSVD</td></tr><tr><td>13</td><td colspan="6">RSVD</td></tr><tr><td>14</td><td colspan="6">RSVD</td></tr><tr><td>15</td><td colspan="6">RSVD</td></tr></table>

Figure 4-32. G4 - S2M DRS Header + 2 S2M NDR

<table><tr><td colspan="6">Bit #</td></tr><tr><td></td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td></tr><tr><td>0</td><td colspan="2">MetaValue</td><td colspan="2">MetaField</td><td>MemOp</td></tr><tr><td>1</td><td colspan="5">Tag[7:0]</td></tr><tr><td>2</td><td colspan="5">Tag[15:8]</td></tr><tr><td>3</td><td>RV</td><td colspan="2">DevLoad</td><td colspan="2">LD-ID[3:0]</td></tr><tr><td>4</td><td colspan="5">RSVD</td></tr><tr><td>5</td><td colspan="2">MetaValue</td><td colspan="2">MetaField</td><td>MemOp</td></tr><tr><td>6</td><td colspan="5">Tag[7:0]</td></tr><tr><td>7</td><td colspan="5">Tag[15:8]</td></tr><tr><td>8</td><td colspan="2">MemOp</td><td colspan="2">Val</td><td>LD-ID[3:0]</td></tr><tr><td>9</td><td colspan="3">Tag[3:0]</td><td>MetaValue</td><td>MetaField</td></tr><tr><td>10</td><td colspan="5">Tag[11:4]</td></tr><tr><td>11</td><td colspan="3">LD-ID[3:0]</td><td colspan="2">Tag[15:12]</td></tr><tr><td>12</td><td colspan="3">RSVD</td><td>DevLoad*</td><td>DevLoad</td></tr><tr><td>13</td><td colspan="5">RSVD</td></tr><tr><td>14</td><td colspan="5">RSVD</td></tr><tr><td>15</td><td colspan="5">RSVD</td></tr></table>

Figure 4-33. G5 - 2 S2M NDR

<table><tr><td colspan="5">Bit #</td></tr><tr><td></td><td>7</td><td>6</td><td>5</td><td>4</td></tr><tr><td>0</td><td>MetaValue</td><td>MetaField</td><td>MemOp</td><td>Val</td></tr><tr><td>1</td><td colspan="4">Tag[7:0]</td></tr><tr><td>2</td><td colspan="4">Tag[15:8]</td></tr><tr><td>3</td><td>MemOp</td><td>Val</td><td colspan="2">LD-ID[3:0]</td></tr><tr><td>4</td><td colspan="2">Tag[3:0]</td><td>MetaValue</td><td>MetaField</td></tr><tr><td>5</td><td colspan="4">Tag[11:4]</td></tr><tr><td>6</td><td colspan="2">LD-ID[3:0]</td><td colspan="2">Tag[15:12]</td></tr><tr><td>7</td><td colspan="2">RSVD</td><td>DevLoad*</td><td>DevLoad</td></tr><tr><td>8</td><td colspan="4">RSVD</td></tr><tr><td>9</td><td colspan="4">RSVD</td></tr><tr><td>10</td><td colspan="4">RSVD</td></tr><tr><td>11</td><td colspan="4">RSVD</td></tr><tr><td>12</td><td colspan="4">RSVD</td></tr><tr><td>13</td><td colspan="4">RSVD</td></tr><tr><td>14</td><td colspan="4">RSVD</td></tr><tr><td>15</td><td colspan="4">RSVD</td></tr></table>

Figure 4-34. G6 - 3 S2M DRS Header

<table><tr><td colspan="5">Bit #</td></tr><tr><td></td><td>7</td><td>6</td><td>5</td><td>4</td></tr><tr><td>0</td><td>MetaValue</td><td>MetaField</td><td>MemOp</td><td>Val</td></tr><tr><td>1</td><td colspan="4">Tag[7:0]</td></tr><tr><td>2</td><td colspan="4">Tag[15:8]</td></tr><tr><td>3</td><td>RV</td><td>DevLoad</td><td>LD-ID[3:0]</td><td>Poi</td></tr><tr><td>4</td><td colspan="4">RSVD</td></tr><tr><td>5</td><td>MetaValue</td><td>MetaField</td><td>MemOp</td><td>Val</td></tr><tr><td>6</td><td colspan="4">Tag[7:0]</td></tr><tr><td>7</td><td colspan="4">Tag[15:8]</td></tr><tr><td>8</td><td>RV</td><td>DevLoad</td><td>LD-ID[3:0]</td><td>Poi</td></tr><tr><td>9</td><td colspan="4">RSVD</td></tr><tr><td>10</td><td>MetaValue</td><td>MetaField</td><td>MemOp</td><td>Val</td></tr><tr><td>11</td><td colspan="4">Tag[7:0]</td></tr><tr><td>12</td><td colspan="4">Tag[15:8]</td></tr><tr><td>13</td><td>RV</td><td>DevLoad</td><td>LD-ID[3:0]</td><td>Poi</td></tr><tr><td>14</td><td colspan="4">RSVD</td></tr><tr><td>15</td><td colspan="4">RSVD</td></tr></table>

## 4.2.4 Link Layer Registers

Architectural registers associated with CXL.cache and CXL.mem are defined in Section 8.2.4.19.

## 4.2.5 68B Flit Packing Rules

The packing rules are defined below. It is assumed that a given queue has credits toward the Rx and any protocol dependencies (SNP-GO ordering, for example) have already been considered:

• Rollover is defined as any time a data transfer needs more than one flit. Note that a data chunk that contains 128b (Format G0), can only be scheduled in Slot 1, Slot 2, and Slot 3 of a protocol flit since Slot 0 has only 96b available, as 32b are taken up by the flit header. The following rules apply to Rollover data chunks:

— If there’s a rollover of more than 3 16B data chunks, the next flit must necessarily be an all-data flit.

— If there’s a rollover of 3 16B data chunks, Slot 1, Slot 2, and Slot 3 must necessarily contain the 3 rollover data chunks. Slot 0 will be packed independently (it is allowed for Slot 0 to have the Data Header for the next data transfer).

— If there’s a rollover of 2 16B data chunks, Slot 1 and Slot 2 must necessarily contain the 2 rollover data chunks. Slot 0 and Slot 3 will be packed independently.

— If there’s a rollover of 1 16B data chunk, Slot 1 must necessarily contain the rollover data chunk. Slot 0, Slot 2, and Slot 3 will be packed independently.

— If there’s no rollover, each of the 4 slots will be packed independently.

• Care must be taken to ensure fairness between packing of CXL.cache and CXL.mem transactions. Similarly, care must be taken to ensure fairness between channels within a given protocol. The exact mechanism to ensure fairness is implementation specific.

• Valid messages within a given slot must be tightly packed. Which means, if a slot contains multiple possible locations for a given message, the Tx must pack the message in the first available location before advancing to the next available location.

• Valid messages within a given flit must be tightly packed. Which means, if a flit contains multiple possible slots for a given message, the Tx must pack the message in the first available slot before advancing to the next available slot.

• Empty slots are defined as slots without any valid bits set and they may be mixed with other slots in any order as long as all other packing rules are followed. For an example refer to Figure 4-5 where slot H3 could have no valid bits set indicating an empty slot, but the 1st and 2nd generic slots, G1 and G2 in the example, may have mixed valid bits set.

• If a valid Data Header is packed in a given slot, the next available slot for data transfer (Slot 1, Slot 2, Slot 3 or an all-data flit) will be guaranteed to have data associated with the header. The Rx will use this property to maintain a shadow copy of the Tx Rollover counts. This enables the Rx to expect all-data flits where a flit header is not present.

• For data transfers, the Tx must send 16B data chunks in cacheline order. That is, chunk order 01 for 32B transfers and chunk order 0123 for 64B transfers.

• A slot with more than one data header (e.g., H5 in the S2M direction, or G3 in the H2D direction) is called a multi-data header slot or an MDH slot. MDH slots can only be sent for full cacheline transfers when both 32B chunks are immediately available to pack (i.e., BE = 0, Sz = 1). An MDH slot can only be used if both agents support MDH (defeature is defined in Section 8.2.4.19.7). If MDH is received when it is disabled it is considered a fatal error.

• An MDH slot format may be selected by the Tx only if there is more than 1 valid Data Header to pack in that slot.

• Control flits cannot be interleaved with all-data flits. This also implies that when an all-data flit is expected following a protocol flit (due to Rollover), the Tx cannot send a Control flit before the all-data flit.

• For non-MDH containing flits, there can be at most 1 valid Data Header in that flit. Also, an MDH containing flit cannot be packed with another valid Data Header in the same flit.

• The maximum number of messages that can be sent in a given flit is restricted to reduce complexity in the receiver, which writes these messages into credited queues. By restricting the number of messages across the entire flit, the number of write ports into the receiver’s queues are constrained. The maximum number of messages per type within a flit (sum, across all slots) is:

```txt
D2H Request --> 4
D2H Response --> 2
D2H Data Header --> 4
D2H Data --> 4*16B
S2M NDR --> 2
S2M DRS Header --> 3
S2M DRS Data --> 4*16B
```

```txt
H2D Request --> 2
H2D Response --> 4
H2D Data Header --> 4
H2D Data --> 4*16B
M2S Req --> 2
M2S RwD Header --> 1
M2S RwD Data --> 4*16B
```

• For a given slot, lower bit positions are defined as bit positions that appear starting from lower order Byte #. That is, bits are ordered starting from (Byte 0, Bit 0) through (Byte 15, Bit 7).

• For multi-bit message fields like Address[MSB:LSB], the least significant bits will appear in lower order bit positions.

• Message ordering within a flit is based on flit bit numbering (i.e., the earliest messages are placed at the lowest flit bit positions and progressively later messages are placed at progressively higher bit positions). Examples: An M2S Req 0 packed in Slot 0 precedes an M2S Req 1 packed in Slot 1. Similarly, a Snoop packed in Slot 1 follows a GO packed in Slot 0, and this ordering must be maintained. Finally, for Header Slot Format H1, an H2D Response packed starting from Byte 7 precedes an H2D Response packed starting from Byte 11.

## 4.2.6 Link Layer Control Flit

Link Layer Control flits do not follow flow control rules applicable to protocol flits. That is, they can be sent from an entity without any credits. These flits must be processed and consumed by the receiver within the period to transmit a flit on the channel since there are no storage or flow control mechanisms for these flits. Table 4-9 lists all the Controls flits supported by the CXL.cachemem link layer.

Table 4-9. CXL.cachemem Link Layer Control Types

<table><tr><td>LLCTRL Encoding</td><td>LLCTRL Type Name</td><td>Description</td><td>Retryable? (Enters the LLRB)</td></tr><tr><td>0001b</td><td>RETRY</td><td>Link layer RETRY flit</td><td>No</td></tr><tr><td>0000b</td><td>LLCRD</td><td>Flit containing link layer credit return and/or Ack information, but no protocol information.</td><td>Yes</td></tr><tr><td>0010b</td><td>IDE</td><td>Integrity and Data Encryption control messages.Use in flows described in Chapter 11.0 that were introduced in CXL 2.0.</td><td>Yes</td></tr><tr><td>1100b</td><td>INIT</td><td>Link layer initialization flit</td><td>Yes</td></tr><tr><td>Others</td><td>Reserved</td><td>N/A</td><td>N/A</td></tr></table>

The 3-bit CTL\_FMT field was added to control messages and uses bits that were reserved in CXL 1.1 control messages. All control messages used in CXL 1.1 have this field encoded as 000b to maintain backward compatibility. This field is used to distinguish formats added in CXL 2.0 control messages that require a larger payload field. The new format increases the payload field from 64 bits to 96 bits and uses CTL\_FMT encoding of 001b.

A detailed description of the control flits is presented below.

Table 4-10. CXL.cachemem Link Layer Control Details (Sheet 1 of 2)

<table><tr><td>Flit Type</td><td>CTL_FMT/LLCTRL</td><td>SubType</td><td>SubType Description</td><td>Payload</td><td>Payload Description</td></tr><tr><td rowspan="6">LLCRD</td><td rowspan="6">000b/0000b</td><td>0000b</td><td>RSVD</td><td>63:0</td><td>RSVD</td></tr><tr><td rowspan="4">0001b</td><td rowspan="4">Acknowledge</td><td>2:0</td><td>Acknowledge[2:0]</td></tr><tr><td>3</td><td>RSVD</td></tr><tr><td>7:4</td><td>Acknowledge[7:4]</td></tr><tr><td>63:8</td><td>RSVD</td></tr><tr><td>Others</td><td>RSVD</td><td>63:0</td><td>RSVD</td></tr><tr><td rowspan="17">RETRY</td><td rowspan="17">000b/0001b</td><td>0000b</td><td>RETRY.Idle</td><td>63:0</td><td>RSVD</td></tr><tr><td rowspan="5">0001b</td><td rowspan="5">RETRY.Req</td><td>7:0</td><td>Requester&#x27;s Retry Sequence Number (Eseq)</td></tr><tr><td>15:8</td><td>RSVD</td></tr><tr><td>20:16</td><td>Contains NUM_RETRY</td></tr><tr><td>25:21</td><td>Contains NUM_PHY_REINIT (for debug)</td></tr><tr><td>63:26</td><td>RSVD</td></tr><tr><td rowspan="9">0010b</td><td rowspan="9">RETRY.Ack</td><td>0</td><td>Empty: The Empty bit indicates that the LLR contains no valid data and therefore the NUM_RETRY value should be reset</td></tr><tr><td>1</td><td>Viral: The Viral bit indicates that the transmitting agent is in a Viral state</td></tr><tr><td>2</td><td>RSVD</td></tr><tr><td>7:3</td><td>Contains an echo of the NUM_RETRY value from the LLR.Req</td></tr><tr><td>15:8</td><td>Contains the WrPtr value of the retry queue for debug purposes</td></tr><tr><td>23:16</td><td>Contains an echo of the Eseq from the LLR.Req</td></tr><tr><td>31:24</td><td>Contains the NumFreeBuf value of the retry queue for debug purposes</td></tr><tr><td>47:32</td><td>Viral LD-ID Vector[15:0]: Included for MLD links to indicate which LD-ID is impacted by viral. Applicable only when the Viral bit (bit 1 of this payload) is set. Bit 0 of the vector encodes LD-ID=0, bit 1 is LD-ID=1, etc. Field is treated as Reserved for ports that do not support LD-ID.</td></tr><tr><td>63:48</td><td>RSVD</td></tr><tr><td>0011b</td><td>RETRY.Frame</td><td>63:0</td><td>Payload is RSVD.Flit required to be sent before a RETRY.Req or RETRY.Ack flit to allow said flit to be decoded without risk of aliasing.</td></tr><tr><td>Others</td><td>RSVD</td><td>63:0</td><td>RSVD</td></tr></table>

Table 4-10. CXL.cachemem Link Layer Control Details (Sheet 2 of 2)

<table><tr><td>Flit Type</td><td>CTL_FMT/LLCTRL</td><td>SubType</td><td>SubType Description</td><td>Payload</td><td>Payload Description</td></tr><tr><td rowspan="4">IDE</td><td rowspan="4">001b/0010b</td><td>0000b</td><td>IDE.Idle</td><td>95:0</td><td>Payload RSVDMessage Sent as part of IDE flows to pad sequences with idle flits.Refer to Chapter 11.0 for details on the use of this message.</td></tr><tr><td>0001b</td><td>IDE.Start</td><td>95:0</td><td>Payload RSVDMessage sent to begin flit encryption.</td></tr><tr><td>0010b</td><td>IDE.TMAC</td><td>95:0</td><td>MAC Field uses all 96 bits of payload.Truncated MAC Message sent to complete a MAC epoch early. Only used when no protocol messages exist to send.</td></tr><tr><td>Others</td><td>RSVD</td><td>95:0</td><td>RSVD</td></tr><tr><td rowspan="7">INIT</td><td rowspan="7">000b/1100b</td><td rowspan="6">1000b</td><td rowspan="6">INIT.Param</td><td>3:0</td><td>Interconnect Version: Version of CXL the port is compliant with.CXL 1.0/1.1 = 0001bCXL 2.0 and above = 0010bOthers Reserved</td></tr><tr><td>7:4</td><td>RSVD</td></tr><tr><td>12:8</td><td>RSVD</td></tr><tr><td>23:13</td><td>RSVD</td></tr><tr><td>31:24</td><td>LLR Wrap Value: Value after which LLR sequence counter should wrap to 0.</td></tr><tr><td>63:32</td><td>RSVD</td></tr><tr><td>Others</td><td>RSVD</td><td>63:0</td><td>RSVD</td></tr></table>

In the LLCRD flit, the total number of flit acknowledgments being returned is determined by creating the Full\_Ack return value, where:

Full\_Ack = {Acknowledge[7:4],Ak,Acknowledge[2:0]}, where the Ak bit is from the flit header.

The flit formats for the control flit are illustrated below.

Figure 4-35. LLCRD Flit Format (Only Slot 0 is Valid; Others are Reserved)

<table><tr><td colspan="6">Bit #</td></tr><tr><td></td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td></tr><tr><td>0</td><td colspan="2">CTL_FMT=0h</td><td colspan="2">RSVD</td><td>Ak</td></tr><tr><td>1</td><td colspan="5">RSVD</td></tr><tr><td>2</td><td colspan="3">RspCrd</td><td colspan="2">RSVD</td></tr><tr><td>3</td><td colspan="3">DataCrd</td><td colspan="2">ReqCrd</td></tr><tr><td>4</td><td colspan="3">SubType</td><td colspan="2">LLCTRL</td></tr><tr><td>5</td><td rowspan="3" colspan="5">0h</td></tr><tr><td>6</td></tr><tr><td>7</td></tr><tr><td>8</td><td colspan="5">Payload[7:0]</td></tr><tr><td>9</td><td colspan="5">Payload[15:8]</td></tr><tr><td>10</td><td colspan="5">Payload[23:16]</td></tr><tr><td>11</td><td colspan="5">Payload[31:24]</td></tr><tr><td>12</td><td colspan="5">Payload[39:32]</td></tr><tr><td>13</td><td colspan="5">Payload[47:40]</td></tr><tr><td>14</td><td colspan="5">Payload[55:48]</td></tr><tr><td>15</td><td colspan="5">Payload[63:56]</td></tr></table>

Figure 4-36. RETRY Flit Format (Only Slot 0 is Valid; Others are Reserved)  
![](images/db0c2bd6629be8f937c5c840d010bb98e89eb48b19c7e406798bc4fe3e366edb.jpg)

Figure 4-37. IDE Flit Format (Only Slot 0 is Valid; Others are Reserved)  
![](images/ea04d1d307e3c4a7a5d8e866bf6a57ea55c91444c04590451542707b71b8a6e8.jpg)

Figure 4-38. INIT Flit Format (Only Slot 0 is Valid; Others are Reserved)  
![](images/d70ff18323c259d23ca948fc43f8498c0eec6aa7ac4f4a9dc0197145d3568c8d.jpg)

## Note:

The RETRY.Req and RETRY.Ack flits belong to the type of flit to which receiving devices must respond, even in the shadow of a previous CRC error. In addition to checking the CRC of a RETRY flit, the receiving device should also check as many defined bits (those listed as having hardcoded 1/0 values) as possible to increase confidence in qualifying an incoming flit as a RETRY message.

## 4.2.7 Link Layer Initialization

Link Layer Initialization must be started after a Physical Layer Link Down to Link Up transition and the link has trained successfully to L0. During Initialization and after the INIT flit has been sent, the CXL.cachemem Link Layer can only send Control-RETRY flits until Link Initialization is complete. The following describes how the link layer is initialized and credits are exchanged.

• The Tx portion of the Link Layer must wait until the Rx portion of the Link Layer has received at least one valid flit that is CRC clean before sending the Control-INIT.Param flit. Before this condition is met, the Link Layer must transmit only Control-RETRY flits (i.e., RETRY.Frame/Req/Ack/Idle flits).

— If for any reason the Rx portion of the Link Layer is not ready to begin processing flits beyond Control-INIT and Control-RETRY, the Tx will stall transmission of LLCTR-INIT.Param flit

— RETRY.Frame/Req/Ack are sent during this time as part of the regular Retry flow.

— RETRY.Idle flits are sent prior to sending a INIT.Param flit even without a retry condition to ensure the remote agent can observe a valid flit.

• The Control-INIT.Param flit must be the first non-Control-RETRY flit transmitted by the Link Layer

• The Rx portion of the Link Layer must be able to receive a Control-INIT.Param flit immediately upon completion of Physical Layer initialization because the first valid flit may be a Control-INIT.Param

• Received Control-INIT.Param values (i.e., LLR Wrap Value) must be made “active”, that is, applied to their respective hardware states within 8 flit clocks of error-free reception of Control-INIT.Param flit.

— Until an error-free INIT.Param flit is received and these values are applied, LLR Wrap Value shall assume a default value of 9 for the purposes of ESEQ tracking.

• Any non-RETRY flits received before Control-INIT.Param flit will trigger an Uncorrectable Error.

• Only a single Control-INIT.Param flit is sent. Any CRC error conditions with a Control-INIT.Param flit will be dealt with by the Retry state machine and replayed from the Link Layer Retry Buffer.

• Receipt of a Control-INIT.Param flit after a Control-INIT.Param flit has already been received should be considered an Uncorrectable Error.

• It is the responsibility of the Rx to transmit credits to the sender using standard credit return mechanisms after link initialization. Each entity should know how many buffers it has and set its credit return counters to these values. Then, during normal operation, the standard credit return logic will return these credits to the sender.

• Immediately after link initialization, the credit exchange mechanism will use the LLCRD flit format.

• It is possible that the receiver will make more credits available than the sender can track for a given message class. For correct operation, it is therefore required that the credit counters at the sender be saturating. Receiver will drop all credits it receives for unsupported channels (e.g., Type 3 device receiving any CXL.cache credits).

• Credits should be sized to achieve desired levels of bandwidth considering roundtrip time of credit return latency. This is implementation and usage dependent.

## 4.2.8 CXL.cachemem Link Layer Retry

The link layer provides recovery from transmission errors using retransmission, or Link Layer Retry (LLR). The sender buffers every retryable flit sent in a local Link Layer Retry Buffer (LLRB). To uniquely identify flits in this buffer, the retry scheme relies on sequence numbers which are maintained within each device. Unlike in PCIe, CXL.cachemem sequence numbers are not communicated between devices with each flit to optimize link efficiency. The exchange of sequence numbers occurs only through link layer control flits during an LLR sequence. The sequence numbers are set to a predetermined value (0) during Link Layer Initialization and they are implemented using a wraparound counter. The counter wraps back to 0 after reaching the depth of the retry buffer. This scheme makes the following assumptions:

• The round-trip delay between devices is more than the maximum of the link layer clock or flit period.

• All protocol flits are stored in the retry buffer. See Section 4.2.8.5.1 for further details on the handling of non-retryable control flits.

Note that for efficient operation, the size of the retry buffer must be larger than the round-trip delay. This includes:

• Time to send a flit from the sender

• Flight time of the flit from sender to receiver

• Processing time at the receiver to detect an error in the flit

• Time to accumulate and, if needed, force Ack return and send embedded Ack return back to the sender

• Flight time of the Ack return from the receiver to the sender

• Processing time of Ack return at the original sender

Otherwise, the LLR scheme will introduce latency, as the transmitter will have to wait for the receiver to confirm correct receipt of a previous flit before the transmitter can free space in its LLRB and send a new flit. Note that the error case is not significant because transmission of new flits is effectively stalled until successful retransmission of the erroneous flit anyway.

## 4.2.8.1 LLR Variables

The retry scheme maintains two state machines and several state variables. Although the following text describes them in terms of one transmitter and one receiver, both the transmitter and receiver side of the retry state machines and the corresponding state variables are present at each device because of the bidirectional nature of the link. Since both sides of the link implement both transmitter and receiver state machines, for clarity this discussion will use the term “local” to refer to the entity that detects a CRC error, and “remote” to refer to the entity that sent the flit that was erroneously received.

The receiving device uses the following state variables to keep track of the sequence number of the next flit to arrive.

• ESeq: This indicates the expected sequence number of the next valid flit at the receiving link layer entity. ESeq is incremented by one (modulo the size of the LLRB) on error-free reception of a retryable flit. ESeq stops incrementing after an error is detected on a received flit until retransmission begins (RETRY.Ack message is received). Link Layer Initialization sets ESeq to 0. Note that there is no way for the receiver to know that an error was for a non-retryable vs. retryable flit. For any

CRC error, it will initiate the link layer retry flow as usual, and effectively the transmitter will resend from the first retryable flit sent.

The sending entity maintains two indexes into its LLRB, as indicated below.

• WrPtr: This indexes the entry of the LLRB that will record the next new flit. When an entity sends a flit, it copies that flit into the LLRB entry indicated by the WrPtr and then increments the WrPtr by one (modulo the size of the LLRB). This is implemented using a wraparound counter that wraps around to 0 after reaching the depth of the LLRB. Non-Retryable Control flits do not affect the WrPtr. WrPtr stops incrementing after receiving an error indication at the remote entity (RETRY.Req message) except as described in the implementation note below, until normal operation resumes again (all flits from the LLRB have been retransmitted). WrPtr is initialized to 0 and is incremented only when a flit is placed into the LLRB.

## IMPLEMENTATION NOTE

WrPtr may continue to increment after receiving RETRY.Req message if there are pre scheduled All Data Flits that are not yet sent over the link. This implementation will ensure that All Data Flits not interleaved with other flits are correctly logged into the Link Layer Retry Buffer.

• RdPtr: This is used to read the contents out of the LLRB during a retry scenario. The value of this pointer is set by the sequence number sent with the retransmission request (RETRY.Req message). The RdPtr is incremented by one (modulo the size of the LLRB) whenever a flit is sent, either from the LLRB in response to a retry request or when a new flit arrives from the transaction layer and regardless of the states of the local or remote retry state machines. If a flit is being sent when the RdPtr and WrPtr are the same, then it indicates that a new flit is being sent; otherwise, it must be a flit from the retry buffer.

The LLR scheme uses an explicit acknowledgment that is sent from the receiver to the sender to remove flits from the LLRB at the sender. The acknowledgment is indicated via an ACK bit in the headers of flits flowing in the reverse direction. In CXL.cachemem, a single ACK bit represents 8 acknowledgments. Each entity keeps track of the number of available LLRB entries and the number of received flits pending acknowledgment through the following variables.

• NumFreeBuf: This indicates the number of free LLRB entries at the entity. NumFreeBuf is decremented by 1 whenever an LLRB entry is used to store a transmitted flit. NumFreeBuf is incremented by the value encoded in the Ack/ Full\_Ack (Ack is the protocol flit bit AK, Full\_Ack defined as part of LLCRD message) field of a received flit. NumFreeBuf is initialized at reset time to the size of the LLRB. The maximum number of retry queue entries at any entity is limited to 255 (8-bit counter). Also, note that the retry buffer at any entity is never filled to its capacity, therefore NumFreeBuf is never 0. If there is only 1 retry buffer entry available, then the sender cannot send a Retryable flit. This restriction is required to avoid ambiguity between a full or an empty retry buffer during a retry sequence that may result into incorrect operation. This implies if there are only 2 retry buffer entries left (NumFreeBuf = 2), then the sender can send an Ack bearing flit only if the outgoing flit encodes a value of at least 1 (which may be a Protocol flit with Ak bit set), else an LLCRD control flit is sent with Full\_Ack value of at least 1. This is required to avoid deadlock at the link layer due to retry buffer becoming full at both entities on a link and their inability to send ACK through header flits. This rule also creates an implicit expectation that you cannot start a sequence of “All Data Flits” that cannot be completed before NumFreeBuf=2 because you must be able to inject the Ack bearing flit when NumFreeBuf=2 is reached.

• NumAck: This indicates the number of acknowledgments accumulated at the receiver. NumAck increments by 1 when a retryable flit is received. NumAck is decremented by 8 when the ACK bit is set in the header of an outgoing flit. If the outgoing flit is coming from the LLRB and its ACK bit is set, NumAck does not decrement. At initialization, NumAck is set to 0. The minimum size of the NumAck field is the size of the LLRB. NumAck at each entity must be able to keep track of at least 255 acknowledgments.

The LLR protocol requires that the number of retry queue entries at each entity must be at least 22 entries (Size of Forced Ack (16) + Max All-Data-Flit (4) + 2) to prevent deadlock.

## 4.2.8.2 LLCRD Forcing

Recall that the LLR protocol requires space available in the LLRB to transmit a new flit, and that the sender must receive explicit acknowledgment from the receiver before freeing space in the LLRB. In scenarios where the traffic flow is asymmetric, this requirement could result in traffic throttling and possibly even starvation.

Suppose that the A→B direction has heavy traffic, but there is no traffic in the B→A direction. In this case, A could exhaust its LLRB size, while B never has any return traffic in which to embed Acks. In CXL, we want to minimize injected traffic to reserve bandwidth for the other traffic stream(s) sharing the link.

To avoid starvation, CXL must permit LLCRD Control message forcing (injection of a non-traffic flit to carry an Acknowledge and a Credit return (ACK/CRD)), but this function must be constrained to avoid wasting bandwidth. In CXL, when B has accumulated a programmable minimum number of Acks to return, B’s CXL.cachemem link layer will inject an LLCRD flit to return an Acknowledge. The threshold of pending Acknowledges before forcing the LLCRD can be adjusted using the “Ack Force Threshold” field in the CXL Link Layer Ack Timer Control register (see Section 8.2.4.19.6).

There is also a timer-controlled mechanism to force LLCRD when the timer reaches a threshold. The timer will clear whenever an ACK/CRD carrying message is sent. It will increment every link layer clock in which an ACK/CRD carrying message is not sent and any Credit value to return is greater than 0 or Acknowledge to return is greater than 1. The reason the Acknowledge threshold value is specified as “greater than $1 ^ { \prime \prime }$ instead of “greater than $0 ^ { \prime \prime }$ is to avoid repeated forcing of LLCRD when no other retryable flits are being sent. If the timer incremented when the pending Acknowledge count is “greater than $\mathrm { ~ \ i ~ } 0 , "$ there would be a continuous exchange of LLCRD messages carrying Acknowledges on an otherwise idle link; this is because the LLCRD is itself retryable and results in a returning Acknowledge in the other direction. The result is that the link layer would never be truly idle when the transaction layer traffic is idle. The timer threshold to force LLCRD is configurable using the Ack or CRD Flush Retimer field in the CXL Link Layer Ack Timer Control register. It should also be noted that the CXL.cachemem link layer must accumulate a minimum of 8 Acks to set the ACK bit in a CXL.cachemem flit header. If LLCRD forcing occurred after the accumulation of 8 Acks, it could result in a negative beat pattern where real traffic always arrives soon after a forced Ack, but not long enough after for enough Acks to re-accumulate to set the ACK bit. In the worst case, this could double the bandwidth consumption of the CXL.cachemem side. By waiting for at least 16 Acks to accumulate, the CXL.cachemem link layer ensures that it can still opportunistically return Acks in a protocol flit avoiding the need to force an LLCRD for Ack return. It is recommended that the Ack Force Threshold value be set to 16 or greater in the CXL Link Layer Ack Timer Control register to reduce overhead of LLCRD injection.

It is recommended that link layer prioritize other link layer flits before LLCRD forcing.

## Pseudo-code for forcing function below:

IF (SENDING\_ACK\_CRD\_MESSAGE==FALSE AND (ACK\_TO\_RETURN >1 OR CRD\_TO\_RETURN>0)) TimerValue++ ELSE TimerValue=0 IF (TimerValue >=Ack\_or\_CRD\_Flush\_Retimer OR ACK\_TO\_RETURN >= Ack Force\_Threshold) Force\_LLCRD = TRUE ELSE Force\_LLCRD=FALSE

## Note:

Ack or CRD Flush Retimer and Ack Force Threshold are values that come from the CXL Link Layer Ack Timer Control register (see Section 8.2.4.19.6).

## Figure 4-39. Retry Buffer and Related Pointers

![](images/fae2bdb8142df2c893221ad615c7a63bdb0baddc1e13c482ff45a2297bb7bc36.jpg)

## 4.2.8.3 LLR Control Flits

The LLR Scheme uses several link layer control flits of the RETRY format to communicate the state information and the implicit sequence numbers between the entities.

• RETRY.Req: This flit is sent from the entity that received a flit in error to the sending entity. The flit contains the expected sequence number (ESeq) at the receiving entity, indicating the index of the flit in the retry queue at the remote entity that must be retransmitted. It also contains the NUM\_RETRY value of the sending entity which is defined in Section 4.2.8.5.1. This message is also triggered as part of the Initialization sequence even when no error is observed as described in Section 4.2.7.

• RETRY.Ack: This flit is sent from the entity that is responding to an error detected at the remote entity. It contains a reflection of the NUM\_RETRY value from the corresponding RETRY.Req message. The flit contains the WrPtr value at the sending entity for debug purposes only. The WrPtr value should not be used by the retry state machines in any way. This flit will be followed by the flit identified for retry by the ESeq number.

• RETRY.Idle: This flit is sent during the retry sequence when there are no protocol flits to be sent (see Section 4.2.8.5.2 for details) or a retry queue is not ready to be sent. For example, it can be used for debug purposes for designs that need additional time between sending the RETRY.Ack and the actual contents of the LLR queue.

• RETRY.Frame: This flit is sent along with a RETRY.Req or RETRY.Ack flit to prevent aliased decoding of these flits (see Section 4.2.8.5 for further details).

Table 4-11 describes the impact of RETRY messages on the local and remote retry state machines. In this context, the “sender” refers to the Device sending the message and the “receiver” refers to the Device receiving the message. Note that how this maps to which device detected the CRC error and which sent the erroneous message depends on the message type. For example, for a RETRY.Req sequence, the sender detected the CRC error, but for a RETRY.Ack sequence, it’s the receiver that detected the CRC error.

## 4.2.8.4 RETRY Framing Sequences

Recall that the CXL.cachemem flit formatting specifies an all-data flit for link efficiency. This flit is encoded as part of the header of the preceding flit and contains no header information of its own. This introduces the possibility that the data contained in this flit could happen to match the encoding of a RETRY flit.

This introduces a problem at the receiver. It must be certain to decode the actual RETRY flit, but it must not falsely decode an aliasing data flit as a RETRY flit. In theory it might use the header information of the stream it receives in the shadow of a CRC error to determine whether it should attempt to decode the subsequent flit. Therefore, the receiver cannot know with certainty which flits to treat as header-containing (decode) and which to ignore (all-data).

CXL introduces the RETRY.Frame flit for this purpose to disambiguate a control sequence from an All-Data Flit (ADF). Due to MDH, 4 ADF can be sent back-to-back. Hence, a RETRY.Req sequence comprises 5 RETRY.Frame flits immediately followed by a RETRY.Req flit, and a RETRY.Ack sequence comprises 5 RETRY.Frame flits immediately followed by a RETRY.Ack flit. This is shown in Figure 4-40.

Table 4-11. Control Flits and Their Effect on Sender and Receiver States

<table><tr><td>RETRY Message</td><td>Sender State</td><td>Receiver State</td></tr><tr><td>RETRY.Idle</td><td>Unchanged.</td><td>Unchanged.</td></tr><tr><td>RETRY.Frame + RETRY.Req Sequence</td><td>Local Retry State Machine (LRSM) is updated. NUM_RETRY is incremented. See Section 4.2.8.5.1.</td><td>Remote Retry State Machine (RRSM) is updated. RdPtr is set to ESeq sent with the flit. See Section 4.2.8.5.3.</td></tr><tr><td>RETRY.Frame + RETRY.Ack Sequence</td><td>RRSM is updated.</td><td>LRSM is updated.</td></tr><tr><td>RETRY.Frame, RETRY.Req, or RETRY.Ack message that is not as part of a valid framed sequence</td><td>Unchanged.</td><td>Unchanged (drop the flit).</td></tr></table>

## Note:

A RETRY.Ack sequence that arrives when a RETRY.Ack is not expected will be treated as an error by the receiver. Error resolution in this case is device specific though it is recommended that this results in the machine halting operation. It is recommended that this error condition not change the state of the LRSM.

## 4.2.8.5 LLR State Machines

The LLR scheme is implemented with two state machines: Remote Retry State Machine (RRSM) and Local Retry State Machine (LRSM). These state machines are implemented by each entity and together determine the overall state of the transmitter and receiver at the entity. The states of the retry state machines are used by the send and receive controllers to determine what flit to send and the actions needed to process a received flit.

## 4.2.8.5.1 Local Retry State Machine (LRSM)

This state machine is activated at the entity that detects an error on a received flit. The possible states for this state machine are:

• RETRY\_LOCAL\_NORMAL: This is the initial or default state indicating normal operation (no CRC error has been detected).

• RETRY\_LLRREQ: This state indicates that the receiver has detected an error on a received flit and a RETRY.Req sequence must be sent to the remote entity.

• RETRY\_LOCAL\_IDLE: This state indicates that the receiver is waiting for a RETRY.Ack sequence from the remote entity in response to its RETRY.Req sequence. The implementation may require substates of RETRY\_LOCAL\_IDLE to capture, for example, the case where the last flit received is a Frame flit and the next flit expected is a RETRY.Ack.

• RETRY\_PHY\_REINIT: The state machine remains in this state for the duration of the virtual Link State Machine (vLSM) being in Retrain.

• RETRY\_ABORT: This state indicates that the retry attempt has failed and the link cannot recover. Error logging and reporting in this case is device specific. This is a terminal state.

The local retry state machine also has the three counters described below. The counters and thresholds described below are implementation specific.

• TIMEOUT: This counter is enabled whenever a RETRY.Req request is sent from an entity and the LRSM state becomes RETRY\_LOCAL\_IDLE. The TIMEOUT counter is disabled and the counting stops when the LRSM state changes to some state other than RETRY\_LOCAL\_IDLE. The TIMEOUT counter is reset to 0 at link layer initialization and whenever the LRSM state changes from RETRY\_LOCAL\_IDLE to RETRY\_LOCAL\_NORMAL or RETRY\_LLRREQ. The TIMEOUT counter is also reset when the vLSM transitions from Retrain to Active (the LRSM transition through RETRY\_PHY\_REINIT to RETRY\_LLRREQ). If the counter has reached its threshold without receiving a RETRY.Ack sequence, then the RETRY.Req request is sent again to retry the same flit. See Section 4.2.8.5.2 for a description of when TIMEOUT increments.

## Note:

It is suggested that the value of TIMEOUT should be no less than 4096 transfers.

• NUM\_RETRY: This counter is used to count the number of RETRY.Req requests sent to retry the same flit. The counter remains enabled during the whole retry sequence (state is not RETRY\_LOCAL\_NORMAL). It is reset to 0 at initialization. It is also reset to 0 when a RETRY.Ack sequence is received with the Empty bit set or whenever the LRSM state is RETRY\_LOCAL\_NORMAL and an error-free retryable flit is received. The counter is incremented whenever the LRSM state changes from RETRY\_LLRREQ to RETRY\_LOCAL\_IDLE. If the counter reaches a threshold (called MAX\_NUM\_RETRY), then the local retry state machine transitions to the RETRY\_PHY\_REINIT. The NUM\_RETRY counter is also reset when the vLSM transitions from Retrain to Active (the LRSM transition through RETRY\_PHY\_REINIT to RETRY\_LLRREQ).

## Note:

It is suggested that the value of MAX\_NUM\_RETRY should be no less than Ah.

• NUM\_PHY\_REINIT: This counter is used to count the number of transitions to RETRY\_PHY\_REINIT that are generated during an LLR sequence due to the number of retries that exceed MAX\_NUM\_RETRY. The counter remains enabled during the whole retry sequence (state is not RETRY\_LOCAL\_NORMAL). It is reset to 0 at initialization and after successful completion of the retry sequence. The counter is incremented whenever the LRSM changes from RETRY\_LLRREQ to RETRY\_PHY\_REINIT due to the number of retries that exceed MAX\_NUM\_RETRY. If the counter reaches a threshold (called MAX\_NUM\_PHY\_REINIT) instead of transitioning from RETRY\_LLRREQ to RETRY\_PHY\_REINIT, the LRSM will transition to RETRY\_ABORT. The NUM\_PHY\_REINIT counter is also reset whenever a RETRY.Ack sequence is received with the Empty bit set.

## Note:

It is suggested that the value of MAX\_NUM\_PHY\_REINIT should be no less than Ah.

Note that the condition of TIMEOUT reaching its threshold is not mutually exclusive with other conditions that cause the LRSM state transitions. RETRY.Ack sequences can be assumed to never arrive at the time at which the retry requesting device times out and sends a new RETRY.Req sequence (by appropriately setting the value of TIMEOUT – see Section 4.2.8.5.2). If this case occurs, no guarantees are made regarding the behavior of the device (behavior is “undefined” from a Spec perspective and is not validated from an implementation perspective). Consequently, the LLR Timeout value should not be reduced unless it can be certain this case will not occur. If an error is detected at the same time as TIMEOUT reaches its threshold, then the error on the received flit is ignored, TIMEOUT is taken, and a repeat RETRY.Req sequence is sent to the remote entity.

Table 4-12. Local Retry State Transitions (Sheet 1 of 2)

<table><tr><td>Current Local Retry State</td><td>Condition</td><td>Next Local Retry State</td><td>Actions</td></tr><tr><td>RETRY_LOCAL_NORMAL</td><td>An error free retryable flit is received.</td><td>RETRY_LOCAL_NORMAL</td><td>Increment NumFreeBuf using the amount specified in the ACK or Full_Ack fields.Increment NumAck by 1.Increment Eseq by 1.NUM_RETRY is reset to 0.NUM_PHY_REINIT is reset to 0.Received flit is processed normally by the link layer.</td></tr><tr><td>RETRY_LOCAL_NORMAL</td><td>Error free non-retryable flit (other than RETRY.Req sequence) is received.</td><td>RETRY_LOCAL_NORMAL</td><td>Received flit is processed.</td></tr><tr><td>RETRY_LOCAL_NORMAL</td><td>Error free RETRY.Req sequence is received.</td><td>RETRY_LOCAL_NORMAL</td><td>RRSM is updated.</td></tr><tr><td>RETRY_LOCAL_NORMAL</td><td>Error is detected on a received flit.</td><td>RETRY_LLRREQ</td><td>Received flit is discarded.</td></tr><tr><td>RETRY_LOCAL_NORMAL</td><td>PHY_RESET $^{1}$  / PHY_REINIT $^{2}$  is detected.</td><td>RETRY_PHY_REINIT</td><td>None.</td></tr><tr><td>RETRY_LLRREQ</td><td>NUM_RETRY == MAX_NUM_RETRY and NUM_PHY_REINIT == MAX_NUM_PHY_REINIT</td><td>RETRY_ABORT</td><td>Indicate link failure.</td></tr><tr><td>RETRY_LLRREQ</td><td>NUM_RETRY == MAX_NUM_RETRY and NUM_PHY_REINIT &lt; MAX_NUM_PHY_REINIT</td><td>RETRY_PHY_REINIT</td><td>If an error-free RETRY.Req or RETRY.Ack sequence is received, process the flit.Any other flit is discarded.RetrainRequest is sent to physical layer. Increment NUM_PHY_REINIT.</td></tr></table>

Table 4-12. Local Retry State Transitions (Sheet 2 of 2)

<table><tr><td>Current Local Retry State</td><td>Condition</td><td>Next Local Retry State</td><td>Actions</td></tr><tr><td>RETRY_LLRREQ</td><td>NUM_RETRY &lt; MAX_NUM_RETRY and a RETRY.Req sequence has not been sent.</td><td>RETRY_LLRREQ</td><td>If an error-free RETRY.Req or RETRY.Ack sequence is received, process the flit.Any other flit is discarded.</td></tr><tr><td>RETRY_LLRREQ</td><td>NUM_RETRY &lt; MAX_NUM_RETRY and a RETRY.Req sequence has been sent.</td><td>RETRY_LOCAL_IDLE</td><td>If an error free RETRY.Req or RETRY.Ack sequence is received, process the flit.Any other flit is discarded.Increment NUM_RETRY.</td></tr><tr><td>RETRY_LLRREQ</td><td>PHY_RESET $^{1}$  / PHY_REINIT $^{2}$  is detected.</td><td>RETRY_PHY_REINIT</td><td>None.</td></tr><tr><td>RETRY_LLRREQ</td><td>Error is detected on a received flit</td><td>RETRY_LLRREQ</td><td>Received flit is discarded.</td></tr><tr><td>RETRY_PHY_REINIT</td><td>Physical layer is still in reinit.</td><td>RETRY_PHY_REINIT</td><td>None.</td></tr><tr><td>RETRY_PHY_REINIT</td><td>Physical layer returns from Reinit.</td><td>RETRY_LLRREQ</td><td>Received flit is discarded.NUM_RETRY is reset to 0.</td></tr><tr><td>RETRY_LOCAL_IDLE</td><td>RETRY.Ack sequence is received and NUM_RETRY from RETRY.Ack matches the value of the last RETRY.Req sent by the local entity.</td><td>RETRY_LOCAL_NORMAL</td><td>TIMEOUT is reset to 0.If RETRY.Ack sequence is received with Empty bit set, NUM_RETRY is reset to 0 and NUM_PHY_REINIT is reset to 0.</td></tr><tr><td>RETRY_LOCAL_IDLE</td><td>RETRY.Ack sequence is received and NUM_RETRY from RETRY.Ack does NOT match the value of the last RETRY.Req sent by the local entity.</td><td>RETRY_LOCAL_IDLE</td><td>Any received retryable flit is discarded.</td></tr><tr><td>RETRY_LOCAL_IDLE</td><td>TIMEOUT has reached its threshold.</td><td>RETRY_LLRREQ</td><td>TIMEOUT is reset to 0.</td></tr><tr><td>RETRY_LOCAL_IDLE</td><td>Error is detected on a received flit.</td><td>RETRY_LOCAL_IDLE</td><td>Any received retryable flit is discarded.</td></tr><tr><td>RETRY_LOCAL_IDLE</td><td>A flit other than RETRY.Ack/ RETRY.Req sequence is received.</td><td>RETRY_LOCAL_IDLE</td><td>Any received retryable flit is discarded.</td></tr><tr><td>RETRY_LOCAL_IDLE</td><td>A RETRY.Req sequence is received.</td><td>RETRY_LOCAL_IDLE</td><td>RRSM is updated.</td></tr><tr><td>RETRY_LOCAL_IDLE</td><td>PHY_RESET $^{1}$  / PHY_REINIT $^{2}$  is detected.</td><td>RETRY_PHY_REINIT</td><td>None.</td></tr><tr><td>RETRY_ABORT</td><td>A flit is received.</td><td>RETRY_ABORT</td><td>All received flits are discarded.</td></tr></table>

1. PHY\_RESET is the condition of the vLSM informing the Link Layer that it needs to initiate a Link Layer Retry due to exit from Retrain state.  
2. PHY\_REINIT is the condition of the Link Layer instructing the Phy to retrain.

## 4.2.8.5.2 TIMEOUT Definition

After the local receiver has detected a CRC error, triggering the LRSM, the local Tx sends a RETRY.Req sequence to initiate LLR. At this time, the local Tx also starts its TIMEOUT counter.

The purpose of this counter is to decide that either the RETRY.Req sequence or corresponding RETRY.Ack sequence has been lost, and that another RETRY.Req attempt should be made. Recall that it is a fatal error to receive multiple RETRY.Ack sequences (i.e., a subsequent Ack without a corresponding Req is unexpected). To reduce the risk of this fatal error condition we check NUM\_RETRY value returned to filter out RETRY.Ack messages from the prior retry sequence. This is done to remove fatal condition where a single retry sequence incurs a timeout while the Ack message is in flight. The TIMEOUT counter should be capable of handling worst-case latency for a RETRY.Req sequence to reach the remote side and for the corresponding RETRY.Ack sequence to return.

Certain unpredictable events (e.g., low power transitions, etc.) that interrupt link availability could add a large amount of latency to the RETRY round-trip. To make the TIMEOUT robust to such events, instead of incrementing per link layer clock, TIMEOUT increments whenever the local Tx transmits a flit, protocol, or control. Due to the TIMEOUT protocol, TIMEOUT must force injection of RETRY.Idle flits if it has no real traffic to send, so that the TIMEOUT counter continues to increment.

## 4.2.8.5.3 Remote Retry State Machine (RRSM)

The remote retry state machine is activated at an entity if a flit sent from that entity is received in error by the local receiver, resulting in a link layer retry request (RETRY.Req sequence) from the remote entity. The possible states for this state machine are:

• RETRY\_REMOTE\_NORMAL: This is the initial or default state indicating normal operation.

• RETRY\_LLRACK: This state indicates that a link layer retry request (RETRY.Req sequence) has been received from the remote entity and a RETRY.Ack sequence followed by flits from the retry queue must be (re)sent.

The remote retry state machine transitions are described in Table 4-13.

Table 4-13. Remote Retry State Transition

<table><tr><td>Current Remote Retry State</td><td>Condition</td><td>Next Remote Retry State</td></tr><tr><td>RETRY_REMOTE_NORMAL</td><td>Any flit, other than error free RETRY.Req sequence, is received.</td><td>RETRY_REMOTE_NORMAL</td></tr><tr><td>RETRY_REMOTE_NORMAL</td><td>Error free RETRY.Req sequence is received.</td><td>RETRY_LLRACK</td></tr><tr><td>RETRY_LLRACK</td><td>RETRY.Ack sequence is not sent.</td><td>RETRY_LLRACK</td></tr><tr><td>RETRY_LLRACK</td><td>RETRY.Ack sequence is sent.</td><td>RETRY_REMOTE_NORMAL</td></tr><tr><td>RETRY_LLRACK</td><td>vLSM in Retrain state.</td><td>RETRY_REMOTE_NORMAL</td></tr></table>

Note: To select the priority of sending flits, the following rules apply:

1. Whenever the RRSM state becomes RETRY\_LLRACK, the entity must give priority to sending the Control flit with RETRY.Ack.

2. Except RRSM state of RETRY\_LLRACK, the priority goes to LRSM state of RETRY\_LLRREQ and in that case the entity must send a Control flit with RETRY.Req over all other flits except an all-data flit sequence.

The overall sequence of replay is shown in Figure 4-40.

Figure 4-40. CXL.cachemem Replay Diagram  
![](images/5411a610f061052c623f192ce1d5016b7e53c327dedf7c01d662217f4c6650e7.jpg)

## 4.2.8.6 Interaction with vLSM Retrain State

On detection by the Link Layer of the vLSM transition from Active to Retrain state, the receiver side of the link layer must force a link layer retry on the next flit. Forcing an error will either initiate LLR or cause a current LLR to follow the correct error path. The LLR will ensure that no retryable flits are dropped during the physical layer reinit. Without initiating an LLR it is possible that packets/flits in flight on the physical wires could be lost or the sequence numbers could get mismatched.

Upon detection of a vLSM transition to Retrain, the LLR RRSM needs to be reset to its initial state and any instance of RETRY.Ack sequence needs to be cleared in the link layer and physical layer. The device needs to ensure that it receives a RETRY.Req sequence before it transmits a RETRY.Ack sequence.

## 4.2.8.7 CXL.cachemem Flit CRC

The CXL.cachemem Link Layer uses a 16b CRC for transmission error detection. The 16b CRC is over the 528-bit flit. The assumptions about the type errors is as follows:

• Bit ordering runs down each lane.

• Bit Errors occur randomly or in bursts down a lane, with the majority of the errors being single-bit random errors.

• Random errors can statistically cause multiple bit errors in a single flit, so it is more likely to get 2 errors in a flit than 3 errors, and more likely to get 3 errors in a flit than 4 errors, and so on.

• There is no requirement for primitive polynomial (a polynomial that generates all elements of an extension field from a base field) because there is no fixed payload. Primitive may be the result, but it’s not required.

## 4.2.8.7.1 CRC-16 Polynomial and Detection Properties

The CRC polynomial to be used is 1F053h. The 16b CRC Polynomial has the following properties:

• All single, double, and triple bit errors detected

• Polynomial selection based on best 4-bit error detection characteristics and perfect 1-bit, 2-bit, and 3-bit error detection

## 4.2.8.7.2 CRC-16 Calculation

Below are the 512 bit data masks for use with an XOR tree to produce the 16 CRC bits. Data Mask bits [511:0] for each CRC bit are applied to the flit bits [511:0] and XOR is performed. The resulting CRC bits are included as flit bits [527:512] are defined to be CRC[15:00]. Pseudo code example for CRC bit 15 of this is CRC[15] = XOR (DM[15][511:0] AND Flit[511:0]).

The flit Data Masks for the 16 CRC bits are located below:

<table><tr><td>DM[15] [511:0] =512&#x27;hEF9C_D9F9_C4BB_B83A_3E84_A97C_D7AE_DA13_FAEB_01B8_5B20_4A4C_AE1E_79D9_7753_5D21_DC7F_DD6A_38F0_3E77_F5F5_2A2C_636D_B05C_3978_EA30_CD50_E0D9_9B06_93D4_746B_2431</td></tr><tr><td>DM[14] [511:0] =512&#x27;h9852_B505_26E6_6427_21C6_FDC2_BC79_B71A_079E_8164_76B0_6F6A_F911_4535_CCFA_F3B1_3240_33DF_2488_214C_0F0F_BF3A_52DB_6872_25C4_9F28_ABF8_90B5_5685_DA3E_4E5E_B629</td></tr><tr><td>DM[13] [511:0] =512&#x27;h23B5_837B_57C8_8A29_AE67_D79D_8992_019E_F924_410A_6078_7DF9_D296_DB43_912E_24F9_455F_C485_AAB4_2ED1_F272_F5B1_4A00_0465_2B9A_A5A4_98AC_A883_3044_7ECB_5344_7F25</td></tr><tr><td>DM[12] [511:0] =512&#x27;h7E46_1844_6F5F_FD2E_E9B7_42B2_1367_DADC_8679_213D_6B1C_74B0_4755_1478_BFC4_4F5D_7ED0_3F28_EDAA_291F_0CCC_50F4_C66D_B26E_ACB5_B8E2_8106_B498_0324_ACB1_DDC9_1BA3</td></tr><tr><td>DM[11] [511:0] =512&#x27;h50BF_D5DB_F314_46AD_4A5F_0825_DE1D_377D_B9D7_9126_EEAE_7014_8DB4_F3E5_28B1_7A8F_6317_C2FE_4E25_2AF8_7393_0256_005B_696B_6F22_3641_8DD3_BA95_9A94_C58C_9A8F_A9E0</td></tr><tr><td>DM[10] [511:0] =512&#x27;hA85F_EAED_F98A_2356_A52F_8412_EF0E_9BBE_DCEB_C893_7757_380A_46DA_79F2_9458_BD47_B18B_E17F_2712_957C_39C9_812B_002D_B4B5_B791_1B20_C6E9_DD4A_CD4A_62C6_4D47_D4F0</td></tr><tr><td>DM[09] [511:0] =512&#x27;h542F_F576_FCC5_11AB_5297_C209_7787_4DDF_6E75_E449_BBAB_9C05_236D_3CF9_4A2C_5EA3_D8C5_F0BF_9389_4ABE_1CE4_C095_8016_DA5A_DBC8_8D90_6374_EEA5_66A5_3163_26A3_EA78</td></tr><tr><td>DM[08] [511:0] =512&#x27;h2A17_FABB_7E62_88D5_A94B_E104_BBC3_A6EF_B73A_F224_DDD5_CE02_91B6_9E7C_A516_2F51_EC62_F85F_C9C4_A55F_0E72_604A_C00B_6D2D_6DE4_46C8_31BA_7752_B352_98B1_9351_F53C</td></tr><tr><td>DM[07] [511:0] =512&#x27;h150B_FD5D_BF31_446A_D4A5_F082_5DE1_D377_DB9D_7912_6EEA_E701_48DB_4F3E_528B_17A8_F631_7C2F_E4E2_52AF_8739_3025_6005_B696_B6F2_2364_18DD_3BA9_59A9_4C58_C9A8_FA9E</td></tr><tr><td>DM[06] [511:0] =512&#x27;h8A85_FEAE_DF98_A235_6A52_F841_2EF0_E9BB_EDCE_BC89_3775_7380_A46D_A79F_2945_8BD4_7B18_BE17_F271_2957_C39C_9812_B002_DB4B_5B79_11B2_0C6E_9DD4_ACD4_A62C_64D4_7D4F</td></tr><tr><td>DM[05] [511:0] =512&#x27;hAADE_26AE_AB77_E920_8BAD_D55C_40D6_AECE_0C0C_5FFC_C09A_F38C_FC28_AA16_E3F1_98CB_E1F3_8261_C1C8_AADC_143B_6625_3B6C_DDF9_94C4_62E9_CB67_AE33_CD6C_C0C2_4601_1A96</td></tr><tr><td>DM[04] [511:0] =512&#x27;hD56F_1357_55BB_F490_45D6_EAAE_206B_5767_0606_2FFE_604D_79C6_7E14_550B_71F8_CC65_F0F9_C130_E0E4_556E_0A1D_B312_9DB6_6EFC_CA62_3174_E5B3_D719_E6B6_6061_2300_8D4B</td></tr><tr><td>DM[03] [511:0] =512&#x27;h852B_5052_6E66_4272_1C6F_DC2B_C79B_71A0_79E8_1647_6B06_F6AF_9114_535C_CFAF_3B13_2403_3DF2_4882_14C0_F0FB_F3A5_2DB6_8722_5C49_F28A_BF89_0B55_685D_A3E4_E5EB_6294</td></tr><tr><td>DM[02] [511:0] =512&#x27;hC295_A829_3733_2139_0E37_EE15_E3CD_B8D0_3CF4_0B23_B583_7B57_C88A_29AE_67D7_9D89_9201_9EF9_2441_0A60_787D_F9D2_96DB_4391_2E24_F945_5FC4_85AA_B42E_D1F2_72F5_B14A</td></tr></table>

DM[01][511:0] = 512'h614A\_D414\_9B99\_909C\_871B\_F70A\_F1E6\_DC68\_1E7A\_0591\_DAC1\_BDAB\_E445\_14D7\_33EB\_CEC4\_C900\_CF7C\_ 9220\_8530\_3C3E\_FCE9\_4B6D\_A1C8\_9712\_7CA2\_AFE2\_42D5\_5A17\_68F9\_397A\_D8A5

DM[00][511:0] = 512'hDF39\_B3F3\_8977\_7074\_7D09\_52F9\_AF5D\_B427\_F5D6\_0370\_B640\_9499\_5C3C\_F3B2\_EEA6\_BA43\_B8FF\_BAD4\_ 71E0\_7CEF\_EBEA\_5458\_C6DB\_60B8\_72F1\_D461\_9AA1\_C1B3\_360D\_27A8\_E8D6\_4863

## 4.2.9 Viral

Viral is a containment feature as described in Section 12.4, “CXL Viral Handling.” As such, when the local socket is in a viral state, it is the responsibility of all off-die interfaces to convey this state to the remote side for appropriate handling. The CXL.cachemem link layer conveys viral status information. As soon as the viral status is detected locally, the link layer forces a CRC error on the next outgoing flit. If there is no traffic to send, the transmitter will send an LLCRD flit with a CRC error. It then embeds viral status information in the RETRY.Ack message it generates as part of the defined CRC error recovery flow.

There are two primary benefits to this methodology. First, by using the RETRY.Ack to convey viral status, we do not have to allocate a bit for this in protocol flits. Second, it allows immediate indication of viral and reduces the risk of race conditions between the viral distribution path and the data path. These risks could be particularly exacerbated by the large CXL.cache flit size and the potential limitations in which components (header, slots) allocate dedicated fields for viral indication.

To support MLD components, first introduced in CXL 2.0, a Viral LD-ID Vector is defined in the RETRY.Ack to encode which LD-ID is impacted by the viral state. This allows viral to be indicated to any set of Logical Devices. This vector is applicable only when the primary viral bit is set, and only to links that support multiple LD-ID (referred to as MLD - Multi-Logical Device). Links without LD-ID support (referred to as SLD - Single Logical Device) will treat the vector as Reserved. For MLD, the encoding of all 0s indicates that all LD-ID are in viral and is equivalent to an encoding of all 1s.

## 4.3

## CXL.cachemem Link Layer 256B Flit Mode

## 4.3.1 Introduction

This mode of operation builds on PCIe Flit mode, in which the reliability flows are handled in the Physical Layer. The flit definition in the link layer defines the slot boundary, slot packing rules, and the message flow control. The flit overall has fields that are defined in the physical layer and are shown in this chapter; however, details are not defined in this chapter. The concept of “all Data” as defined in 68B Flit mode does not exist in 256B Flit mode.

## 4.3.2 Flit Overview

There are 2 variations of the 256B flit: Standard, and Latency-Optimized (LOpt). The mode of operation must be in sync with the physical layer. The Standard 256B flit supports either standard messages or Port Based Routing (PBR) messages where PBR messages carry additional ID space (DPID and sometimes SPID) to enable moreadvanced scaling/routing solutions as described in Chapter 3.0.

## Note:

256B flit messages are also referred to as Hierarchy Based Routing (HBR) messages, when comparing to PBR flits/messages. A message default is HBR unless explicitly stated as being PBR.

Figure 4-41 is the Standard 256B flit. The Physical Layer controls 16B of the flit in this mode where the fields are: HDR, CRC, and FEC. All other fields are defined in the link layer.

Figure 4-41. Standard 256B Flit

<table><tr><td rowspan="2"></td><td colspan="2">Bytes</td></tr><tr><td colspan="2">0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15</td></tr><tr><td>Byte 0 &gt;</td><td>2B HDR</td><td>Slot0-14B (H-Slot)</td></tr><tr><td>Byte 16 &gt;</td><td colspan="2">Slot1 - 16B (G-Slot)</td></tr><tr><td>Byte 32 &gt;</td><td colspan="2">Slot2</td></tr><tr><td>Byte 48 &gt;</td><td colspan="2">slot 3</td></tr><tr><td>Byte 64 &gt;</td><td colspan="2">slot 4</td></tr><tr><td>Byte 80 &gt;</td><td colspan="2">slot 5</td></tr><tr><td>Byte 96 &gt;</td><td colspan="2">slot 6</td></tr><tr><td>Byte 112 &gt;</td><td colspan="2">Slot 7</td></tr><tr><td>Byte 128 &gt;</td><td colspan="2">Slot 8</td></tr><tr><td>Byte 144 &gt;</td><td colspan="2">Slot 9</td></tr><tr><td>Byte 160 &gt;</td><td colspan="2">Slot 10</td></tr><tr><td>Byte 176 &gt;</td><td colspan="2">Slot 11</td></tr><tr><td>Byte 192 &gt;</td><td colspan="2">Slot 12</td></tr><tr><td>Byte 208 &gt;</td><td colspan="2">Slot 13</td></tr><tr><td>Byte 224 &gt;</td><td colspan="2">Slot 14</td></tr><tr><td>Byte 240 &gt;</td><td>2B CRD</td><td>8B CRC</td></tr></table>

Figure 4-42 is the latency-optimized flit definition. In this definition, more bytes are allocated to the physical layer to enable less store-and-forward when the transmission is error free. In this flit, 20B are allocated to the Physical Layer, where the fields are: 12B CRC (split across 2 6B CRC codes), 6B FEC, and 2B HDR.

Figure 4-42. Latency-Optimized (LOpt) 256B Flit

<table><tr><td rowspan="2"></td><td colspan="2">Bytes</td></tr><tr><td colspan="2">0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15</td></tr><tr><td colspan="3">Byte 0 &gt; 2B HDR Slot0-14B (H-Slot)</td></tr><tr><td colspan="3">Byte 16 &gt; Slot1 - 16B (G-Slot)</td></tr><tr><td colspan="3">Byte 32 &gt; Slot2</td></tr><tr><td colspan="3">Byte 48 &gt; slot 3</td></tr><tr><td colspan="3">Byte 64 &gt; slot 4</td></tr><tr><td colspan="3">Byte 80 &gt; slot 5</td></tr><tr><td colspan="3">Byte 96 &gt; slot 6</td></tr><tr><td colspan="2">Byte 112 &gt; Slot 7</td><td>6B CRC</td></tr><tr><td colspan="2">Byte 128 &gt; Slot 8 -12B (HS-Slot) -- Last 2B at the bottom</td><td>Slot 7</td></tr><tr><td colspan="3">Byte 144 &gt; Slot 9</td></tr><tr><td colspan="3">Byte 160 &gt; Slot 10</td></tr><tr><td colspan="3">Byte 176 &gt; Slot 11</td></tr><tr><td colspan="3">Byte 192 &gt; Slot 12</td></tr><tr><td colspan="3">Byte 208 &gt; Slot 13</td></tr><tr><td colspan="3">Byte 224 &gt; Slot 14</td></tr><tr><td colspan="2">Byte 240 &gt; 2B CRD Slot 8 - 2B 6B FEC</td><td>6B CRC</td></tr></table>

## Note:

In both flit modes, the flit message packing rules are common, with the exception of Slot 8, which in LOpt 256B flits is a 12B slot with special packing rules. These are a subset of Slot 0 packing rules. This slot format is referred to as the H Subset (HS) format.

PBR packing is a subset of HBR message packing rules. PBR messages are not supported in LOpt 256B Flits, so HS-Slot does not apply.

Some bits of Slot 7 are split across the 128B halves of the flit, and the result is that some messages in Slot 7 cannot be consumed until the CRC for the second half of the flit is checked.

Slot formats are defined by a 4-bit field at the beginning of each slot that carries header information, which is a departure from the 68B formats, where the 3-bit format field is within the flit header. The packing rules are constrained to a subset of messages for upstream and downstream links to match the Transaction Layer requirements. The encodings are non-overlapping between upstream and downstream except when the message(s) in the format are enabled to be sent in both directions. This is a change from the 68B flit definition where the slot format was uniquely defined for upstream and downstream.

The packing rules for the H-slot are a strict subset of the G-slot rules. The subset relationship is defined by the 14B H-slot size where any G-slot messages that extend beyond the 14th byte are not supported in the H-slot format. HS-slot follows the same subset relationship where the cutoff size is 12B.

For the larger PBR message packing, the messages in each slot are a subset of 256B flit message packing rules because of the larger message size required for PBR. PBR flits and messages can be fully symmetric when flowing between switches where the link is not upstream or downstream (also known as “Cross-Link” or “Inter-Switch Link” (ISL)).

For Data and Byte-Enable Slots, a slot-format field is not explicitly included, but is instead known based on prior header messages that must be decoded. This is similar to the “all-data-flit” definition in 68B flit where expected data slots encompass the flit’s entire payload.

Table 4-14 defines the 256B G-Slots for HBR and PBR messages.

Table 4-14. 256B G-Slot Formats (Sheet 1 of 2)

<table><tr><td rowspan="2">Format</td><td rowspan="2">SlotFmt Encoding</td><td colspan="4">HBR</td><td colspan="2">PBR</td></tr><tr><td>Messages</td><td> $Downstream^1$ </td><td> $Upstream^1$ </td><td>Length in Bits (Max 124)</td><td>Messages</td><td>Length in Bits (Max 124)</td></tr><tr><td>G0</td><td>0000b</td><td>H2D Req + H2D Rsp</td><td>X</td><td></td><td>112</td><td>H2D Req</td><td>92</td></tr><tr><td>G1</td><td>0001b</td><td>3 H2D Rsp</td><td>X</td><td></td><td>120</td><td>2 H2D Rsp</td><td>96</td></tr><tr><td>G2</td><td>0010b</td><td>D2H Req + 2 D2H Rsp</td><td></td><td>X</td><td>124</td><td>D2H Req</td><td>96</td></tr><tr><td>G3</td><td>0011b</td><td>4 D2H Rsp</td><td></td><td>X</td><td>96</td><td>3 D2H Rsp</td><td>108</td></tr><tr><td>G4</td><td>0100b</td><td>M2S Req</td><td>X</td><td>D</td><td>100</td><td>M2S Req</td><td>120</td></tr><tr><td>G5</td><td>0101b</td><td>3 M2S BIRsp</td><td>X</td><td>D</td><td>120</td><td>2 M2S BIRsp</td><td>104</td></tr><tr><td>G6</td><td>0110b</td><td>S2M BISnp + S2M NDR</td><td>D</td><td>X</td><td>124</td><td>S2M BISnp</td><td>96</td></tr><tr><td>G7</td><td>0111b</td><td>3 S2M NDR</td><td>D</td><td>X</td><td>120</td><td>2 S2M NDR</td><td>96</td></tr></table>

Table 4-14. 256B G-Slot Formats (Sheet 2 of 2)

<table><tr><td rowspan="2">Format</td><td rowspan="2">SlotFmt Encoding</td><td colspan="4">HBR</td><td colspan="2">PBR</td></tr><tr><td>Messages</td><td>Downstream $^{1}$ </td><td>Upstream $^{1}$ </td><td>Length in Bits (Max 124)</td><td>Messages</td><td>Length in Bits (Max 124)</td></tr><tr><td>G8</td><td>1000b</td><td rowspan="4">RSVD</td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4"></td><td rowspan="4">RSVD</td><td rowspan="4"></td></tr><tr><td>G9</td><td>1001b</td></tr><tr><td>G10</td><td>1010b</td></tr><tr><td>G11</td><td>1011b</td></tr><tr><td>G12</td><td>1100b</td><td>4 H2D DH</td><td>X</td><td></td><td>112</td><td>3 H2D DH</td><td>108</td></tr><tr><td>G13</td><td>1101b</td><td>4 D2H DH</td><td></td><td>X</td><td>96</td><td>3 D2H DH</td><td>108</td></tr><tr><td>G14</td><td>1110b</td><td>M2S RwD</td><td>X</td><td>D</td><td>104</td><td>M2S RwD</td><td>124</td></tr><tr><td>G15</td><td>1111b</td><td>3 S2M DRS</td><td>D</td><td>X</td><td>120</td><td>2 S2M DRS</td><td>96</td></tr></table>

1. D = Supported only for Direct P2P CXL.mem-capable ports.

Table 4-15 captures the H-Slot formats. Notice that “zero extended” is used in PBR messages sent using slot formats H4 and H14 because they do not fit in the slot. This method allows the messages to use this format provided the unsent bits are 0s. The zero-extended method can be avoided by using the G-slot format, but use is allowed for these cases to optimize link efficiency. An example PBR H14, in Figure 4-65, “256B Packing: G14/H14 PBR Messages” on page 242, requires that the bits in Bytes 14 and 15 are all 0s to be able to use the format. This includes CKID[12:8], TC field, and reserved bits within those bytes. Any other field, including CKID[7:0], will be sent normally and can have supported encodings.

Table 4-15. 256B H-Slot Formats (Sheet 1 of 2)

<table><tr><td rowspan="2">Format</td><td rowspan="2">SlotFmt Encoding</td><td colspan="4">HBR</td><td colspan="2">PBR</td></tr><tr><td>Messages</td><td> $Downstream^1$ </td><td> $Upstream^1$ </td><td>Length in Bits (Max 108)</td><td>Messages</td><td>Length in Bits (Max 108)</td></tr><tr><td>H0</td><td>0000b</td><td> $H2D\ Req^2$ </td><td>X</td><td></td><td>72</td><td>H2D Req</td><td>92</td></tr><tr><td>H1</td><td>0001b</td><td> $2 H2D Rsp^2$ </td><td>X</td><td></td><td>80</td><td>2 H2D Rsp</td><td>96</td></tr><tr><td>H2</td><td>0010b</td><td> $D2H\ Req + 1 D2H Rsp^2$ </td><td></td><td>X</td><td>100</td><td>D2H Req</td><td>96</td></tr><tr><td>H3</td><td>0011b</td><td>4 D2H Rsp</td><td></td><td>X</td><td>96</td><td>3 D2H Rsp</td><td>108</td></tr><tr><td>H4</td><td>0100b</td><td>M2S Req</td><td>X</td><td>D</td><td>100</td><td>M2S Req (Zero Extended)</td><td>108 (120)</td></tr><tr><td>H5</td><td>0101b</td><td> $2 M2S\ BIRsp^2$ </td><td>X</td><td>D</td><td>80</td><td>2 M2S BIRsp</td><td>104</td></tr><tr><td>H6</td><td>0110b</td><td> $S2M\ BISnp^2$ </td><td>D</td><td>X</td><td>84</td><td>S2M BISnp</td><td>96</td></tr><tr><td>H7</td><td>0111b</td><td> $2 S2M\ NDR^2$ </td><td>D</td><td>X</td><td>80</td><td>2 S2M NDR</td><td>96</td></tr><tr><td>H8</td><td>1000b</td><td colspan="4">LLCTRL</td><td colspan="2">LLCTRL</td></tr><tr><td>H9</td><td>1001b</td><td rowspan="3">RSVD</td><td></td><td></td><td></td><td rowspan="3">RSVD</td><td></td></tr><tr><td>H10</td><td>1010b</td><td></td><td></td><td></td><td></td></tr><tr><td>H11</td><td>1011b</td><td></td><td></td><td></td><td></td></tr><tr><td>H12</td><td>1100b</td><td> $3 H2D\ DH^2$ </td><td>X</td><td></td><td>84</td><td>3 H2D DH</td><td>108</td></tr></table>

Table 4-15. 256B H-Slot Formats (Sheet 2 of 2)

<table><tr><td rowspan="2">Format</td><td rowspan="2">SlotFmt Encoding</td><td colspan="4">HBR</td><td colspan="2">PBR</td></tr><tr><td>Messages</td><td> $Downstream^1$ </td><td> $Upstream^1$ </td><td>Length in Bits (Max 108)</td><td>Messages</td><td>Length in Bits (Max 108)</td></tr><tr><td>H13</td><td>1101b</td><td>4 D2H DH</td><td></td><td>X</td><td>96</td><td>3 D2H DH</td><td>108</td></tr><tr><td>H14</td><td>1110b</td><td>M2S RwD</td><td>X</td><td>D</td><td>104</td><td>M2S RwD (Zero Extended)</td><td>108 (124)</td></tr><tr><td>H15</td><td>1111b</td><td>2 S2M  $DRS^2$ </td><td>D</td><td>X</td><td>80</td><td>2 S2M DRS</td><td>96</td></tr></table>

1. D = Supported only for Direct P2P CXL.mem-capable ports.  
2. Cases in which the H-Slot is a subset of the corresponding G-slot because not all messages fit into the format.

Table 4-16 captures the HS-Slot formats. The HS-slot format is used only in LOpt 256B flits. Notice that “zero extended” for slot formats are used in HS4 and HS14.

Note: PBR messages never use LOpt 256B flits, and therefore do not use the HS-Slot format.

Table 4-16. 256B HS-Slot Formats

<table><tr><td rowspan="2">Format</td><td rowspan="2">SlotFmt Encoding</td><td colspan="4">HBR</td></tr><tr><td>Messages</td><td> $Downstream^1$ </td><td> $Upstream^1$ </td><td>Length in Bits (Max 92)</td></tr><tr><td>HS0</td><td>0000b</td><td>H2D Req</td><td>X</td><td></td><td>72</td></tr><tr><td>HS1</td><td>0001b</td><td>2 H2D Rsp</td><td>X</td><td></td><td>80</td></tr><tr><td>HS2</td><td>0010b</td><td> $D2H\ \text{Req}^2$ </td><td></td><td>X</td><td>76</td></tr><tr><td>HS3</td><td>0011b</td><td>3 D2H  $Rsp^2$ </td><td></td><td>X</td><td>72</td></tr><tr><td>HS4</td><td>0100b</td><td>M2S Req (Zero Extended)</td><td>X</td><td>D</td><td>92 (100)</td></tr><tr><td>HS5</td><td>0101b</td><td>2 M2S BIRsp</td><td>X</td><td>D</td><td>80</td></tr><tr><td>HS6</td><td>0110b</td><td>S2M BISnp</td><td>D</td><td>X</td><td>84</td></tr><tr><td>HS7</td><td>0111b</td><td>2 S2M NDR</td><td>D</td><td>X</td><td>80</td></tr><tr><td>HS8</td><td>1000b</td><td colspan="4">LLCTRL</td></tr><tr><td>HS9</td><td>1001b</td><td rowspan="3">RSVD</td><td></td><td></td><td></td></tr><tr><td>HS10</td><td>1010b</td><td></td><td></td><td></td></tr><tr><td>HS11</td><td>1011b</td><td></td><td></td><td></td></tr><tr><td>HS12</td><td>1100b</td><td>3 H2D DH</td><td>X</td><td></td><td>84</td></tr><tr><td>HS13</td><td>1101b</td><td>3 D2H  $DH^2$ </td><td></td><td>X</td><td>72</td></tr><tr><td>HS14</td><td>1110b</td><td>M2S RwD (Zero Extended)</td><td>X</td><td>D</td><td>92 (104)</td></tr><tr><td>HS15</td><td>1111b</td><td>2 S2M DRS</td><td>D</td><td>X</td><td>80</td></tr></table>

1. D = Supported only for Direct P2P CXL.mem-capable ports.  
2. Cases in which the HS-Slot is a subset of the corresponding H-slot because not all messages fit into the format.

## 4.3.3 Slot Format Definition

The slot diagrams in this section capture the detailed bit field placement within the slot. Each Diagram is inclusive of G-slot, H-slot, and HS-slot where a subset is created such that H-slot is a subset of G-slot where messages that extend beyond the 14-byte boundary are excluded. Similarly, the HS-slot format is a subset of H-slot and G-slot where messages that extend beyond the 12-byte boundary are excluded.

This G to H to HS subset relationship is captured in Figure 4-43, where the size of each subset is shown.

All messages within the slots are aligned to nibble (4 bit) boundary. This results in some variation in number of reserved bits to align to that boundary.

## Figure 4-43. 256B Packing: Slot and Subset Definition

![](images/29504bcc1467335fd2c310c0b11e6350b7f127629dbbd848d1d8a19ee09e8f7d.jpg)

Slot diagrams in the section include abbreviations for bit field names to allow them to fit into the diagram. In the diagrams, most abbreviations are obvious, but the following abbreviation list ensures clarity:

• Bg = Bogus

• BT11 = BITag[11]

• Ch = ChunkValid

• CID3 = CacheID[3]

• CK12 = CKID[12]

• CQ0 = CQID[0]

• CQ11 = CQID[11]

• DP0 = DPID[0]

• LD0 = LD-ID[0]

• MO3 = MemOpcode[3]

• Op3 = Opcode[3]

• Poi = Poison

• RSVD = Reserved

• RV = Reserved

• SP11 = SPID[11]

• UQ11 = UQID[11]

• Val = Valid

## Figure 4-44. 256B Packing: G0/H0/HS0 HBR Messages

![](images/44058aedb9755d4212afe83bdf4757e2c28e2a0cd71149ca19f480d0e2e44e11.jpg)

H2D Req + H2D Rsp

## Figure 4-45. 256B Packing: G0/H0 PBR Messages

![](images/44fd38c2c18df8bd825422483c8d5ed16aaacc4a05c6417608c7d9b0ae977f5c.jpg)

Figure 4-46. 256B Packing: G1/H1/HS1 HBR Messages  
![](images/f63428de59976e26fc68e70129d03f9fbc7cf35045c440f6f3d38a03da403503.jpg)

![](images/886e76d22205be9384283fc82accab075c45ec94720ec05351ea6f60e5b3505a.jpg)

Figure 4-47. 256B Packing: G1/H1 PBR Messages  
![](images/2c685c440cd9bc7ec3a871ba80f30f8b8cacadaa9d07dfc67661baf4f9d0e13b.jpg)

![](images/91430724d695be283100c058592f5c550a5f0fb8624d50b5a1c814929487ec2d.jpg)

![](images/6ccd3c5856ac7848d1e13fe417cf7a732f59492ad3a3b1e354e06c8a40ebda0c.jpg)

Figure 4-48. 256B Packing: G2/H2/HS2 HBR Messages  
![](images/a02865279f63e921f2918e9885a31c9dca1ca326683cab0029abb279dd3df635.jpg)

## Figure 4-49. 256B Packing: G2/H2 PBR Messages

![](images/664abd623c6d512850151febb22f62c2916f617c095204a5be278582303dbcc5.jpg)

Figure 4-50. 256B Packing: G3/H3/HS3 HBR Messages  
![](images/f56481426a0799bba513d7841be11d8b74923de869f3e629c225b0e53cec58ae.jpg)

Figure 4-51. 256B Packing: G3/H3 PBR Messages  
![](images/cc86bf043e954534bae0203b68615cc078fe658078895162bcd3e0d3dccf61f3.jpg)

Figure 4-52. 256B Packing: G4/H4/HS4 HBR Messages  
![](images/ece8701390d58dfe1be9782a81e7564cc3e8cec56c8100c7f2a3427187665dfb.jpg)

Figure 4-53. 256B Packing: G4/H4 PBR Messages  
![](images/113ac09602d0c0e8f16055382eb2a6f09518eb8d2ca2d66b133c1ddf4013be99.jpg)

Figure 4-54. 256B Packing: G5/H5/HS5 HBR Messages  
![](images/bbe2be20a4a1cbe7bc9aa0be6ac20da48137370010aad23b2e1f2e05592b77e2.jpg)

Figure 4-55. 256B Packing: G5/H5 PBR Messages  
![](images/ab13bc579210327799e415739cdfe281568b86ca6548aa023ce0d4845ab661d2.jpg)

Figure 4-56. 256B Packing: G6/H6/HS6 HBR Messages  
![](images/82f3803cc9eb4c64f045c1b69d4c2fbeccb6bb35479e41f4b17b19c98e905af2.jpg)

![](images/ed0afb8bb8309f9235c0f72764fe26ed38e118625c66d33286789bdd248dd1a9.jpg)

Figure 4-57. 256B Packing: G6/H6 PBR Messages  
![](images/4e6aad81a4a86c284cf6206848256ffae173f0605d6f1feaffb5de5f09400118.jpg)

Figure 4-58. 256B Packing: G7/H7/HS7 HBR Messages  
![](images/3fff572a672408bf213f4b8e3fbcb65785bec59853d497786cf96b470aad8e16.jpg)

![](images/116ce9d5b6f285b11ec0fa466616b94e60b55d7a8c8f053e0bc2b3b12365bdc9.jpg)

Figure 4-59. 256B Packing: G7/H7 PBR Messages  
![](images/ec483992299fa8a8be2d3ed21c2acd31f9cc5f35e36090cfad95d4cf4299518a.jpg)

Figure 4-60. 256B Packing: G12/H12/HS12 HBR Messages  
![](images/0b9836de60d5f87cf394cf7d83d329567ebeb347494812b134b87110807cc18d.jpg)

![](images/9aafe8510b10611da522cbff17f6e59862a955ff23f17aeddc26577884a3df4c.jpg)  
Figure 4-61. 256B Packing: G12/H12 PBR Messages

![](images/f7a08bca6895a0c83a963e08501efd3596be9c208f220e286f91b82fe0d30deb.jpg)

![](images/c5303e17af3495ca7937882cea06cbaa0506ee8a98d17f5668a5bb8196a448a2.jpg)

Figure 4-62. 256B Packing: G13/H13/HS13 HBR Messages  
![](images/bc3a5bbe56afa7ce66622edbc6896316b6e7742fd70c7797db94a9a2167e805d.jpg)

![](images/799b2ebfff4a511d250391ed80dd2db8e81f8abb80a026c84f5e6240978901d7.jpg)

Figure 4-63. 256B Packing: G13/H13 PBR Messages  
![](images/3aa927e3e3180286b2ed15ea1aae4058a0d5a0f86058c60211e8359a18467489.jpg)

Figure 4-64. 256B Packing: G14/H14/HS14 HBR Messages  
![](images/bf5d4bfa1121c198ebe7ebfe723fc8e16395d0bdc0f6055bf9f5f90591a4cf85.jpg)

## Figure 4-65. 256B Packing: G14/H14 PBR Messages

![](images/2fa1ac34d474124515e8c08cbecf23eb32f1a72c95b9b9dba3097a1576fd487f.jpg)  
M2S RwD (last 16 bits H14 implied zero)

![](images/a1eb4a08630dcc69f140aec0c3d6e1b5055c9bceba0429c7715270f62b309cbf.jpg)

## Figure 4-66. 256B Packing: G15/H15/HS15 HBR Messages

<table><tr><td colspan="6">Bit #</td></tr><tr><td></td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td></tr><tr><td>0</td><td colspan="2">MemOp</td><td>Val</td><td colspan="2">SlotFmt=15</td></tr><tr><td>1</td><td colspan="3">Tag[3:0]</td><td>MetaValue</td><td>MetaField</td></tr><tr><td>2</td><td colspan="5">Tag[11:4]</td></tr><tr><td>3</td><td>LD0</td><td>DevLoad</td><td>Poi</td><td colspan="2">Tag[15:12]</td></tr><tr><td>4</td><td colspan="3">RSVD</td><td>TRP</td><td>LD-ID[3:1]</td></tr><tr><td>5</td><td colspan="2">MemOp</td><td>Val</td><td colspan="2">RSVD</td></tr><tr><td>6</td><td colspan="3">Tag[3:0]</td><td>MetaValue</td><td>MetaField</td></tr><tr><td>7</td><td colspan="5">Tag[11:4]</td></tr><tr><td>8</td><td>LD0</td><td>DevLoad</td><td>Poi</td><td colspan="2">Tag[15:12]</td></tr><tr><td>9</td><td colspan="3">RSVD</td><td>TRP</td><td>LD-ID[3:1]</td></tr><tr><td>10</td><td colspan="2">MemOp</td><td>Val</td><td colspan="2">RSVD</td></tr><tr><td>11</td><td colspan="3">Tag[3:0]</td><td>MetaValue</td><td>MetaField</td></tr><tr><td>12</td><td colspan="5">Tag[11:4]</td></tr><tr><td>13</td><td>LD0</td><td>DevLoad</td><td>Poi</td><td colspan="2">Tag[15:12]</td></tr><tr><td>14</td><td colspan="3">RSVD</td><td>TRP</td><td>LD-ID[3:1]</td></tr><tr><td>15</td><td colspan="3">RSVD</td><td colspan="2">RSVD</td></tr></table>

![](images/911061e00320560f35c5d857818ce4d1b35b1e636a9879eae426884e702c342b.jpg)

## Figure 4-67. 256B Packing: G15/H15 PBR Messages

<table><tr><td colspan="6">Bit #</td></tr><tr><td></td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td></tr><tr><td>0</td><td colspan="2">MemOp</td><td>Val</td><td colspan="2">SlotFmt=15</td></tr><tr><td>1</td><td colspan="3">Tag[3:0]</td><td>MetaValue</td><td>MetaField</td></tr><tr><td>2</td><td colspan="5">Tag[11:4]</td></tr><tr><td>3</td><td>DP0</td><td>DevLoad</td><td>Poi</td><td colspan="2">Tag[15:12]</td></tr><tr><td>4</td><td colspan="5">DPID[8:1]</td></tr><tr><td>5</td><td colspan="3">RSVD</td><td>TRP</td><td>DPID[11:9]</td></tr><tr><td>6</td><td colspan="2">MemOp</td><td>Val</td><td colspan="2">RSVD</td></tr><tr><td>7</td><td colspan="3">Tag[3:0]</td><td>MetaValue</td><td>MetaField</td></tr><tr><td>8</td><td colspan="5">Tag[11:4]</td></tr><tr><td>9</td><td>DP0</td><td>DevLoad</td><td>Poi</td><td colspan="2">Tag[15:12]</td></tr><tr><td>10</td><td colspan="5">DPID[8:1]</td></tr><tr><td>11</td><td colspan="3">RSVD</td><td>TRP</td><td>DPID[11:9]</td></tr><tr><td>12</td><td colspan="5">RSVD</td></tr><tr><td>13</td><td rowspan="3" colspan="5">RSVD</td></tr><tr><td>14</td></tr><tr><td>15</td></tr></table>

![](images/d52c6a3f5b2356f977326259d7822cb1409807adf04c55b3265390faac505ec4.jpg)

Figure 4-68. 256B Packing: Implicit Data  
Figure 4-69. 256B Packing: Implicit Trailer RwD  
Figure 4-70. 256B Packing: Implicit Trailer DRS  
![](images/c34eef12f8befb84dd9c5c218706f763a90bb4b8420800b8af74f2a3901718e0.jpg)

![](images/9d5c83ba4e98501e001cc77f088389bffa9b6e974eb3ba52dc4bea315f2eb254.jpg)

Figure 4-71. 256B Packing: Byte-Enable Trailer for D2H Data  
![](images/ab36466c9db42411e1d9ab008c3f41462538195823299618770a7daaa26a8940.jpg)

## 4.3.3.1 Implicit Data Slot Decode

Data and Byte-Enable slots are implicitly known for G-slots based on prior message headers. To simplify decode of the slot format fields, SlotFmt can be used as a quick decode to know if the next 4 G-slots are data slots. Additional G-slots beyond the next 4 may also carry data depending on rollover values, the number of valid Data Headers, and BE bit within headers.

H-slots and HS-slots never carry data, so they always have an explicit 4-bit encoding defining the format.

## IMPLEMENTATION NOTE

The quick decode of the current slot is used to determine whether the next 4 G-slots are data slots. The decode required is different for H/HS-slot compared to G-slots. The H/HS slots comparing SlotFmt[3:2] are equal to 11b, and for G slots reduce the compare to only SlotFmt[3] equal to 1. The difference in decode requirement is because the formats H8/HS8 indicates LLCTRL message where G8 is a reserved encoding.

More generally, the optimization for quick decode can be used to limit the logic levels required to determine whether later slots (by number) are data vs. header slots.

## IMPLEMENTATION NOTE

With Link Layer data path of 64B wide, only 4 slots are processed per clock, which enables a simplified decode to reduce critical paths in the logic to determine whether a G-slot is a data slot vs. a header slot. All further decode is carried over from the previous clock cycle.

Figure 4-72 shows examples where a quick decode of the SlotFmt field can be used to determine which slots are implicit data slots. The Rollover column is the number of data slots carried over from previous flits. Because H-slots never carry data, their decode can proceed without knowledge of prior headers.

Figure 4-72. Header Slot Decode Example

<table><tr><td rowspan="2">Roll-Over</td><td rowspan="2">Current Slot #</td><td rowspan="2">SlotFmt MSB</td><td colspan="15">G-Slots</td></tr><tr><td>H0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td></td><td>0</td><td>0</td><td>1</td><td>S</td><td>D</td><td>D</td><td>D</td><td>D</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td></tr><tr><td></td><td>0</td><td>1</td><td>1</td><td></td><td>S</td><td>D</td><td>D</td><td>D</td><td>D</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td></tr><tr><td></td><td>0</td><td>2</td><td>1</td><td></td><td></td><td>S</td><td>D</td><td>D</td><td>D</td><td>D</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td></tr><tr><td></td><td>1</td><td>0</td><td>1</td><td>S</td><td>R</td><td>D</td><td>D</td><td>D</td><td>D</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td></tr><tr><td></td><td>4</td><td>0</td><td>0</td><td>S</td><td>R</td><td>R</td><td>R</td><td>R</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td><td>?</td></tr></table>

## 4.3.3.2 Trailer Decoder

A trailer is defined to be included with data carrying messages when the TRP or BEP bit is set in the header. The trailer size can vary depending on the link’s capability. The base functionality requires support of the Byte-Enable use case for trailers. The Extended Metadata (EMD) use of trailers is optional. Table 4-17 defines the use cases that are supported for each data-carrying channel.

Table 4-17. Trailer Size and Modes Supported per Channel

<table><tr><td>Channel</td><td>Trailer Use</td><td>Trailer Size Max</td></tr><tr><td>M2S RwD</td><td>Byte-Enables (BE) and/or Extended Metadata (EMD)</td><td>96-bit if Extended Metadata is supported; otherwise, 64-bit for Byte-Enables.</td></tr><tr><td>S2M DRS</td><td>Extended Metadata (EMD)</td><td>96 bits max (32 bits per DRS message) when EMD is enabled; otherwise, 0-bits.</td></tr><tr><td>D2H Data Header (DH)</td><td>Byte-Enables</td><td>64-bit for Byte-Enables.</td></tr><tr><td>Other Channels</td><td>None</td><td>0 bits</td></tr></table>

For RwD and D2H DH messages, the Trailer always follow 4 Data Slots if TRP or BEP is set for the message.

For DRS, the Trailer enables packing of up to 3 trailers together after the first 64B data transfer for Header 0 even when Header 0 does not have an associated trailer. The trailers are tightly packed for each header with TRP bit set. Figure 4-73 illustrates an example case in which the 3 DRS (G15) format is sent where the 1st and 3rd headers have TRP=1 and the 2nd has TRP=0. The trailer comes after the first data transfer (D0) and the valid trailers are tightly packed.

## Note:

The “tightly packed” trailer rule is for future extensibility with larger trailers where a complete set of trailers for a multi-data header will not fit into a single slot and sparse use of TRP=1 with tightly packed trailers enables higher efficiency.

Figure 4-73. DRS Trailer Slot Decode Example  
![](images/6673bbead84ff479497ff3306af9cda27d1de1ed59bed34ba29ec65e5782dbf3.jpg)

## 4.3.4 256B Flit Packing Rules

Rules for 256B flits follow the same basic requirements as 68B flits, in terms of bit order and tightly packed rules. The tightly packed rules apply within groups of up to 4 slots together instead of across the entire flit. The groups are defined as: 0 to 3, 4 to 7, 8 to 11, and 12 to 14. Note that the final group spans only 3 slots.

• The Tx must not inject data headers in H-slots/HS-slots unless the remaining data slots to send is less than or equal to 16.

## Note:

This limits the maximum count of the remaining data to be 36 (16 + 4 (new Data headers) \* 5 (4 Data Slots + 1 Byte Enable slot) = 36):

• The MDH disable control bit is used to restrict the number of valid data header bits to one per slot

• If a Data Header slot format is used (G/H/HS 12 to 15) the first message must have the valid bit set

The maximum message rules are applicable on a rolling 128B group in which the groups are A=”Slot 0 to 3”, B=”Slot 4 to 7”, C=”Slot 8 to 11”, D=”Slot 12 to 14”. Extending these rules to 128B boundary enables the 256B flit slot formats to be fully utilized. The 256B flit slots often have more messages per slot than the legacy 68B flit message rate would allow. Extending to 128B enables the use of these high message count slots while not increasing the message rate per bandwidth.

The definition of rolling is such that the groups combine into 128B rolling groups: AB (Slot 0 to 7), BC (Slot 4 to 11), CD (Slot 8 to 14), and DA (Slot 12 to 14 in current flit and Slot 0 to 3 in the following flit). The maximum message rates apply to each group. The LOpt 256B flit creates one modification to this rule such that Slot 7 is included in groups B and C: B=”Slot 4 to 7” and C=”Slot 7 to 11”. Sub-Group C has 5 slots with this change. Note that this special case is applicable only to the maximum message rate requirement where CD group considers Slot 7 to 14 instead of Slot 8 to 14.

The maximum message rate per 128B group is defined in Table 4-18, and the 68B flit message rate is included for comparison.

## Note:

The term “128B group” is looking at the 128B grouping boundaries of the 256B flit. The actual number of bytes in the combined slots does vary depending on where the alignment is within the 256B flit which has other overhead like CRC, FEC, 2B Hdr.

## Note:

The maximum message count was selected based on a worst-case workload requirement for steady-state message requirement in conjunction with the packing rules to achieve the most-efficient operating point. In some cases, this is 2x from the 68B message rate, which is what would be expected, but that is not true in all cases.

Table 4-18. 128B Group Maximum Message Rates

<table><tr><td>Message Type</td><td>Maximum Message Count per 128B Group</td><td>Maximum Message Count for Each 68B Flit</td></tr><tr><td>D2H Req</td><td>4</td><td>4</td></tr><tr><td>D2H Rsp</td><td>4</td><td>2</td></tr><tr><td>D2H Data Header (DH)</td><td>4</td><td>4</td></tr><tr><td>S2M BISnp</td><td>2</td><td>N/A</td></tr><tr><td>S2M NDR</td><td>6</td><td>2</td></tr><tr><td>S2M DRS-DH</td><td>3</td><td>3</td></tr><tr><td>H2D Req</td><td>2</td><td>2</td></tr><tr><td>H2D Rsp</td><td>6</td><td>4</td></tr><tr><td>H2D Data Header (DH)</td><td>4</td><td>4</td></tr><tr><td>M2S Req</td><td>4</td><td>2</td></tr><tr><td>M2S RwD-DH</td><td>2</td><td>1</td></tr><tr><td>M2S BIRsp</td><td>3</td><td>N/A</td></tr></table>

Other 68B rules that do not apply to 256B flits:

• MDH rule that requires >1 valid header per MDH. In 256B slots, only one format is provided for packing each message type, so this rule is not applicable.

• Rules related to BE do not apply because they are handled with a separate message header bit instead of a flit header bit, and because there are no special constraints placed on the number of messages when the TRP or BEP bit is set.

• 32B transfer rules don’t apply because only 64B transfers are supported.

## IMPLEMENTATION NOTE

Packing choices between H-slot and G-slot can have a direct impact on efficiency in many traffic patterns. Efficiency may be improved if messages that can fully utilize an H-slot (or HS-slot) are prioritized for those slots compared to messages that can better utilize a G-slot.

An example analyzed CXL.mem traffic pattern that sends steady state downstream traffic of MemRd, MemWr, and BIRsp. In this example, MemRd and MemWr can fully utilize an H-slot and do not see a benefit from being packed into a G-slot. The BIRsp packing allows more messages to fit into G-slot (3) compared to an H-slot (2), so prioritizing it for G-slot allows for improvement. In this example, we can see approximately 1.5% bandwidth improvement from prioritizing BIRsp to G-slots as compared to a simple weighted round-robin arbitration.

Prioritizing must be carefully handled to ensure that fairness is provided between each message class.

## 4.3.5

## Credit Return

Table 4-19 defines the 2-byte credit return encoding in the 256B flit.

Table 4-19. Credit Returned Encoding (Sheet 1 of 3)

<table><tr><td rowspan="2">Field</td><td rowspan="2">Encoding (hex)</td><td colspan="5">Definition</td></tr><tr><td>Protocol</td><td>Channel</td><td> $Downstream^1$ </td><td> $Upstream^1$ </td><td>Credit Count</td></tr><tr><td rowspan="25">CRD[4:0]</td><td>00h</td><td colspan="4">No credit return</td><td>0</td></tr><tr><td>01h</td><td colspan="4">No Credit Return and the current flit is an Empty flit as defined in Section 4.3.8.1.</td><td>0</td></tr><tr><td>02h-03h</td><td colspan="5">Reserved</td></tr><tr><td>04h</td><td rowspan="10">Cache</td><td rowspan="5">H2D Request</td><td rowspan="5">X</td><td rowspan="5"></td><td>1</td></tr><tr><td>05h</td><td>4</td></tr><tr><td>06h</td><td>8</td></tr><tr><td>07h</td><td>12</td></tr><tr><td>08h</td><td>16</td></tr><tr><td>09h</td><td rowspan="5">D2H Request</td><td rowspan="5"></td><td rowspan="5">X</td><td>1</td></tr><tr><td>0Ah</td><td>4</td></tr><tr><td>0Bh</td><td>8</td></tr><tr><td>0Ch</td><td>12</td></tr><tr><td>0Dh</td><td>16</td></tr><tr><td>0Eh-13h</td><td colspan="5">Reserved</td></tr><tr><td>14h</td><td rowspan="10">Memory</td><td rowspan="5">M2S Request</td><td rowspan="5">X</td><td rowspan="5">D</td><td>1</td></tr><tr><td>15h</td><td>4</td></tr><tr><td>16h</td><td>8</td></tr><tr><td>17h</td><td>12</td></tr><tr><td>18h</td><td>16</td></tr><tr><td>19h</td><td rowspan="5">S2M BISnp</td><td rowspan="5">D</td><td rowspan="5">X</td><td>1</td></tr><tr><td>1Ah</td><td>4</td></tr><tr><td>1Bh</td><td>8</td></tr><tr><td>1Ch</td><td>12</td></tr><tr><td>1Dh</td><td>16</td></tr><tr><td>1Eh-1Fh</td><td colspan="5">Reserved</td></tr></table>

Table 4-19. Credit Returned Encoding (Sheet 2 of 3)

<table><tr><td rowspan="2">Field</td><td rowspan="2">Encoding (hex)</td><td colspan="5">Definition</td></tr><tr><td>Protocol</td><td>Channel</td><td> $Downstream^1$ </td><td> $Upstream^1$ </td><td>Credit Count</td></tr><tr><td rowspan="24">CRD[9:5]</td><td>00h</td><td colspan="4">No credit return</td><td>0</td></tr><tr><td>01h-03h</td><td colspan="5">Reserved</td></tr><tr><td>04h</td><td rowspan="10">Cache</td><td rowspan="5">H2D Data</td><td rowspan="5">X</td><td rowspan="5"></td><td>1</td></tr><tr><td>05h</td><td>4</td></tr><tr><td>06h</td><td>8</td></tr><tr><td>07h</td><td>12</td></tr><tr><td>08h</td><td>16</td></tr><tr><td>09h</td><td rowspan="5">D2H Data</td><td rowspan="5"></td><td rowspan="5">X</td><td>1</td></tr><tr><td>0Ah</td><td>4</td></tr><tr><td>0Bh</td><td>8</td></tr><tr><td>0Ch</td><td>12</td></tr><tr><td>0Dh</td><td>16</td></tr><tr><td>0Eh-13h</td><td colspan="5">Reserved</td></tr><tr><td>14h</td><td rowspan="10">Memory</td><td rowspan="5">M2S RwD</td><td rowspan="5">X</td><td rowspan="5">D</td><td>1</td></tr><tr><td>15h</td><td>4</td></tr><tr><td>16h</td><td>8</td></tr><tr><td>17h</td><td>12</td></tr><tr><td>18h</td><td>16</td></tr><tr><td>19h</td><td rowspan="5">S2M DRS</td><td rowspan="5">D</td><td rowspan="5">X</td><td>1</td></tr><tr><td>1Ah</td><td>4</td></tr><tr><td>1Bh</td><td>8</td></tr><tr><td>1Ch</td><td>12</td></tr><tr><td>1Dh</td><td>16</td></tr><tr><td>1Eh-1Fh</td><td colspan="5">Reserved</td></tr></table>

Table 4-19. Credit Returned Encoding (Sheet 3 of 3)

<table><tr><td rowspan="2">Field</td><td rowspan="2">Encoding (hex)</td><td colspan="5">Definition</td></tr><tr><td>Protocol</td><td>Channel</td><td> $Downstream^1$ </td><td> $Upstream^1$ </td><td>Credit Count</td></tr><tr><td rowspan="24">CRD[14:10]</td><td>00h</td><td colspan="4">No credit return</td><td>0</td></tr><tr><td>01h-03h</td><td colspan="5">Reserved</td></tr><tr><td>04h</td><td rowspan="10">Cache</td><td rowspan="5">H2D Rsp</td><td rowspan="5">X</td><td rowspan="5"></td><td>1</td></tr><tr><td>05h</td><td>4</td></tr><tr><td>06h</td><td>8</td></tr><tr><td>07h</td><td>12</td></tr><tr><td>08h</td><td>16</td></tr><tr><td>09h</td><td rowspan="5">D2H Rsp</td><td rowspan="5"></td><td rowspan="5">X</td><td>1</td></tr><tr><td>0Ah</td><td>4</td></tr><tr><td>0Bh</td><td>8</td></tr><tr><td>0Ch</td><td>12</td></tr><tr><td>0Dh</td><td>16</td></tr><tr><td>0Eh-13h</td><td colspan="5">Reserved</td></tr><tr><td>14h</td><td rowspan="10">Memory</td><td rowspan="5">M2S BIRsp</td><td rowspan="5">X</td><td rowspan="5">D</td><td>1</td></tr><tr><td>15h</td><td>4</td></tr><tr><td>16h</td><td>8</td></tr><tr><td>17h</td><td>12</td></tr><tr><td>18h</td><td>16</td></tr><tr><td>19h</td><td rowspan="5">S2M NDR</td><td rowspan="5">D</td><td rowspan="5">X</td><td>1</td></tr><tr><td>1Ah</td><td>4</td></tr><tr><td>1Bh</td><td>8</td></tr><tr><td>1Ch</td><td>12</td></tr><tr><td>1Dh</td><td>16</td></tr><tr><td>1Eh-1Fh</td><td colspan="5">Reserved</td></tr><tr><td>CRD[15]</td><td colspan="6">Reserved</td></tr></table>

1. D = Credit channel mapping is applicable only on a Direct P2P CXL.mem link between a device and the switch Downstream Port to which it is attached.

## 4.3.6 Link Layer Control Messages

In 256B Flit mode, control messages are encoded using the H8 format and sometimes using the HS8 format. Figure 4-74 captures the 256B packing for LLCTRL messages. H8 provides 108 bits to be used to encode the control message after accounting for 4-bit slot format encoding. 8 bits are used to encode LLCTRL/SubType, and 4 bits are kept as reserved, with a 96-bit payload. For HS8, it is limited to 2 bytes less, which cuts the available payload to 80 bits. Table 4-20 captures the defined control messages. In almost all cases, the remaining slots after the control message are considered to be reserved (i.e., cleared to all 0s) and do not carry any protocol information. The exception case is IDE.MAC, which allows for protocol messages in the other slots within the flit. For messages that are injected in the HS slot, the slots prior to the HS slot may carry protocol information but the slots after the HS slot are reserved.

Table 4-20. 256B Flit Mode Control Message Details

<table><tr><td>Flit Type</td><td>LLCTRL</td><td>SubType</td><td>SubType Description</td><td>Payload</td><td>Payload Description</td><td>Remaining Slots are Reserved?1</td></tr><tr><td rowspan="6"> $IDE^2$ </td><td rowspan="6">0010b</td><td>0000b</td><td>IDE.Idle</td><td>95:0</td><td>Payload RSVDMessage sent as part of IDE flows to pad sequences with idle flits.See Chapter 11.0 for details on the use of this message.</td><td rowspan="3">Yes</td></tr><tr><td>0001b</td><td>IDE.Start</td><td>95:0</td><td>Payload RSVDMessage sent to begin flit encryption.</td></tr><tr><td>0010b</td><td>IDE.TMAC</td><td>95:0</td><td>MAC Field uses all 96 bits of payload.Truncated MAC Message sent to complete a MAC epoch early. Used only when no protocol messages exist to send.</td></tr><tr><td>0011b</td><td>IDE.MAC</td><td>95:0</td><td>MAC Field uses all 96 bits of payload.This encoding is the standard MAC used at the natural end of the MAC epoch and is sent with other protocol slots encoded within the flit.</td><td>No</td></tr><tr><td>0100b</td><td>IDE.Stop</td><td>95:0</td><td>Payload RSVD.Message used to disable IDE.See Chapter 11.0 for details on the use of this message.</td><td rowspan="2">Yes</td></tr><tr><td>Others</td><td>RSVD</td><td>95:0</td><td>RSVD</td></tr><tr><td rowspan="7"> $In-band Error^3$ </td><td rowspan="7">0011b</td><td rowspan="3">0000b</td><td rowspan="3">Viral</td><td>15:0</td><td>Viral LD-ID Vector[15:0]: Included for MLD links to indicate which LD-ID is impacted by viral. Bit 0 of the vector encodes LD-ID=0, bit 1 is LD-ID=1, etc. Field is treated as Reserved for ports that do not support LD-ID.</td><td rowspan="7">Yes</td></tr><tr><td>79:16</td><td>RSVD</td></tr><tr><td>95:80</td><td>RSVD (these bits do not exist in HS format).</td></tr><tr><td rowspan="3">0001b</td><td rowspan="3">Poison</td><td>3:0</td><td>Poison Message Offset is the encoding of which of the active or upcoming messages will have poison applied. There can be up to 8 active Data carrying messages and up to 4 new data carrying messages where the poison can be applied.0h = Poison the currently active data message1h = Poison the message 1 after the current data message...7h = Poison the message 7 after the current data messageSee Section 4.3.6.3 for additional details.</td></tr><tr><td>79:4</td><td>RSVD</td></tr><tr><td>95:80</td><td>RSVD (these bits do not exist in HS format).</td></tr><tr><td>Others</td><td>RSVD</td><td>95:0</td><td>RSVD</td></tr><tr><td rowspan="3"> $INIT^2$ </td><td rowspan="3">1100b</td><td rowspan="2">1000b</td><td rowspan="2">INIT.Param</td><td>0</td><td>Direct P2P CXL.mem-capable port.Credits for the channels enabled in this feature are not returned unless both sides support it.</td><td rowspan="4">Yes</td></tr><tr><td>95:1</td><td>RSVD</td></tr><tr><td>Others</td><td>RSVD</td><td>95:0</td><td>RSVD</td></tr><tr><td>Reserved</td><td>Others</td><td></td><td>RSVD</td><td>95:0</td><td>RSVD</td></tr></table>

2. Supported only in H-slot.  
1. If yes, all the slots in the current flit after this message are Reserved, If no, the slots after this may carry protocol messages (header or data).  
3. Supported in either H-slot or HS-slot.

Figure 4-74. 256B Packing: H8/HS8 Link Layer Control Message Slot Format  
![](images/e46ff2c7935dbe906c25ac403fc1f43248d4fa906381a6dece580491796e960a.jpg)

After initial link training (from Link Down), the link layer must send and receive the INIT.Param flit before beginning normal operation. After reaching normal operation, the Link Layer will start by returning all possible credits using the standard credit return mechanism. Normal operation is also required before sending other control messages (IDE, In-band Error).

## 4.3.6.2 Viral Injection and Containment

The Viral control flit is injected as soon as possible after the viral condition is observed. For cases in which the error that triggers Viral can impact the current flit, the link layer should signal to the physical layer to stop the currently partially sent CXL.cachemem flit (Flit 0) by injection of a CRC/FEC corruption that ensures a retry condition (note that this does not directly impact CXL.io flits or flits that are being replayed from the Physical Layer retry buffer). Then the Logical Physical Layer will also remove that flit (flit 0) from the retry buffer and replace it with the Viral control flit (flit 1) that must be sent immediately by the link layer. The Link Layer must also resend the flit that was corrupted (flit 0) after the viral flit. Figure 4-75 captures an example of a Link Layer to Logical Physical Layer (LogPhy) with a half-flit interface where CRC is corrupted and Viral is injected. At Cycle “x3”, it is signaled to corrupt the current flit (FlitA). At cycle “x4”, the CRC(bad) is indicated and the link layer starts sending the Viral control. In Cycle “x5”, the retry buffer pointer (WrPtr) is stepped back to ensure the FlitA is removed from the retry buffer and then replaced with the Viral flit sent from the link layer. At Cycle “x6”, the CTRL-Viral flit is also sent with corrupted CRC to ensure the full retry flow (disallowing the single flit retry). Also starting at cycle “x6”, FlitA is resent from the link layer and forwarded on normally through the LogPhy and retry buffer. FlitA is identical to the flit started in Cycle “x2”.

With link IDE enabled this flow works the same and FlitA is retransmitted with the same encryption mask and without altering the integrity state. The control message is not included in link IDE and thus does not impact the IDE requirements.

Figure 4-75. Viral Error Message Injection Standard 256B Flit  
![](images/c2c4c0d1d7bf21b5825f72b0d6f9aa321c642281a2c271065cd2443a0bd7fd04.jpg)

The Error signaling with CRC corruption flow requires special handling for LOpt flits. If the link layer is in the first 128B phase of the flit, the flow is identical to Standard Flit mode. However, if the link layer is in the second phase of the 128B flit (when the first 128B was committed), then the flit corruption is guaranteed only on the second half, but the Physical Layer will remove the entire flit from the retry buffer. The link layer will send the first 128B identically to what was sent before, and then the link layer will inject the Viral control message in Slot 8 (HS-format) and Slots 9-14 are considered RSVD and normal operation continues in the next flit. Any data slots and other message encodings are continued in the next flit. Figure 4-76 captures the unique case for the LOpt flit. The difference from the standard 256B flit is in three areas of this flow. First at Cycle “x4”, the link layer resends FlitA-0 because this half of the flit may have already been consumed. Then at Cycle “x5”, in the second-half of that flit, the link layer injects the control message for Viral (after the final portion of Slot 7). At Cycle “x6”, the second half of the original flit (starting with Slot 8) is repacked in the first half of FlitB following the standard packing rules.

This flow cannot be supported with link IDE, thus any error containment must either be detected sufficiently early to corrupt CRC in the first half of the flit or must be injected in the second half without corrupting the CRC.

Figure 4-76. Viral Error Message Injection LOpt 256B Flit  
![](images/f84ce22d3c2119e9f91f94e01ac40033bd15952ca5d2354db16bf883a6b928d3.jpg)

## 4.3.6.3 Late Poison

Poison can be injected at a point after the header was sent by injecting an Error Control message with the Poison sub-type. The message includes a payload encoding that indicates the data message offset at which the poison applies. It is possible that any one of up to 8 active messages can be targeted. The encoding is an offset that is relative to the data that is yet to be sent, including the currently active data transmission. The poison applies to the entire message payload, just as it does when poison is included in the message header.

If a message is currently active, but not all data slots have been sent, the offset value of zero applies to that message. If a receiver implementation uses “wormhole switching” techniques, where data is forwarded through the on-die fabric before all the data has arrived, then it is possible that data already sent may be consumed. In this case, the only guarantee is that the poison is applied to the remaining data after the poison control message. The following are examples of how this would apply in specific cases.

## Example 1:

• Flit 1 - 1st 3 slots of data Message A in Slots 12 to 14.

• Flit 2 - In-band error poison message in Slot 0 with a poison message offset value of 0.

• Flit 3 - 4th slot of data Message A in Slot 1 and data Message B in Slots 2 to 5.

• The poison control message applies to Message A, but is only guaranteed to be applied to the final data slot of that message. But it may also be applied to the entire message.

## Example 2:

• Flit 1 - 4 slots of data Message A in Slots 11 to 14 where the message header has Byte-Enables Present (BEP) or Trailer Present (TRP) bit set.

• Flit 2 - In-band error poison message in Slot 0 with a poison message offset value of 0.

• Flit 3 - The Trailer (e.g., Byte enables) for data Message A in Slot 1 and data Message B in Slots 2 to 5.

• The poison control message applies to Message A, but is not guaranteed to be applied to any of the data because it was already sent. Note that the use of Trailer in this example could be any supported trailer (e.g., Extended Meta Data and/or Byte-Enables).

To inject poison on data that is scheduled to be sent in the current flit, and no H-slot/ HS-slot exists to interrupt the data transmission, the same CRC corruption flows as described in Section 4.3.6.2, “Viral Injection and Containment,” are used.

## 4.3.6.4 Link Integrity and Data Encryption (IDE)

For the IDE flow, see Chapter 11.0.

## 4.3.7 Credit Return Forcing

To avoid starvation, credit return rules ensure that Credits are sent even when there are no protocol messages pending. In 68B Flit mode, this uses a special control message called LLCRD (its algorithm is described in Section 4.2.8.2). For 256B Flit mode, the same underlying algorithm for forcing is used, but with the following changes:

• Ack forcing is not applicable with 256B flit.

• With 256B flits, CRD is part of standard flit definition, so no special control message is required.

• There is a packing method described in Section 4.3.8. When implementing this algorithm, the end of the flit is tagged as empty if no valid messages or Credit return is included. With this flit packing method, the flit should return a nonzero credit value only if there are other valid messages sent unless the credit forcing algorithm has triggered.

• No requirement to prioritize protocol messages vs. CRD because they are both part of 256B flits.

## 4.3.8 Latency Optimizations

To get the best latency characteristics, the 256B flit is expected to be sent with a link layer implementing 64B or 128B pipeline and the Latency-Optimized flit (which is optional). The basic reasoning for these features is self-evident.

Additional latency optimization is possible sending idle slot scheduling of flits to the ARB/MUX which avoids needing to wait for the next start of flit alignment. There are trade-offs between CXL.io vs. empty slots being scheduled, so overall bandwidth should be considered.

## IMPLEMENTATION NOTE

A case to consider for idle slot scheduling is with a Link Layer pipeline of 64B in which idle slots allow late-arriving messages to be packed later in the flit. By doing this, the Transmitter can avoid stalls by starting the flit with empty slots. An example case of this is with a x4 port in which a message shows and just misses the first 64B of the flit. In this case, it is necessary to wait an additional 192B before sending the message because the ARB/MUX is injecting an empty flit or a flit from CXL.io. In this example, the observed additional latency in x4 is 6 ns (192 bytes/x4 \* 8 bits/byte / 64 GT/s).

## 4.3.8.1 Empty Flit

As part of the latency optimizations described in this chapter, the Link Layer needs to include a way to indicate that the current flit does not have messages or CRD information. The definition of Empty in this context is that the entire flit can be dropped without side effects in the Link Layer:

• No Data Slots are sent

• No Valid bits are set in any protocol slots

• No control message is sent

• No Credits are returned in the CRD field

A special encoding of the CRD field provides this such that CRD[4:0] = 01h as captured in Table 4-19.

When IDE is enabled, the Empty Encoding shall not used as all protocol flits are required to be fully processed.

## 5.0 CXL ARB/MUX

Figure 5-1 shows where the CXL ARB/MUX exists in the Flex Bus layered hierarchy. The ARB/MUX provides dynamic muxing of the CXL.io and CXL.cachemem link layer control and data signals to interface with the Flex Bus physical layer.

Figure 5-1. Flex Bus Layers - CXL ARB/MUX Highlighted

![](images/6a9125c8008deba2291a1ace145527c262370b42fed344d44a25400abf6d508f.jpg)

In the transmit direction, the ARB/MUX arbitrates between requests from the CXL link layers and multiplexes the data. It also processes power state transition requests from the link layers: resolving them to a single request to forward to the physical layer, maintaining virtual link state machines (vLSMs) for each link layer interface, and generating ARB/MUX link management packets (ALMPs) to communicate the power state transition requests across the link on behalf of each link layer. See Section 10.3, Section 10.4, and Section 10.5 for more details on how the ALMPs are utilized in the overall flow for power state transitions. In PCIe\* mode, the ARB/MUX is bypassed, and thus ALMP generation by the ARB/MUX is disabled.

In the receive direction, the ARB/MUX determines the protocol associated with the CXL flit and forwards the flit to the appropriate link layer. It also processes the ALMPs, participating in any required handshakes and updating its vLSMs as appropriate.

For 256B Flit mode, the replay buffer is part of the Physical Layer. ALMPs have a different flit format than in 68B Flit mode, and are protected by forward error correction (FEC) and cyclic redundancy check (CRC). They must also be allocated to the replay buffer in the Physical Layer and follow the replay sequence protocols. Hence, they are guaranteed to be delivered to the remote ARB/MUX error free.

## 5.1 vLSM States

The ARB/MUX maintains vLSMs for each CXL link layer it interfaces with, transitioning the state based on power state transition requests it receives from the local link layer or from the remote ARB/MUX on behalf of a remote link layer. Table 5-1 lists the different possible states for the vLSMs. PM States and Retrain are virtual states that can differ across interfaces (CXL.io, CXL.cache, and CXL.mem); however, all other states such as LinkReset, LinkDisable, and LinkError are forwarded to the Link Layer and are therefore synchronized across interfaces.

Table 5-1. vLSM States Maintained per Link Layer Interface

<table><tr><td>vLSM State</td><td>Description</td></tr><tr><td>Reset</td><td>Power-on default state during which initialization occurs</td></tr><tr><td>Active</td><td>Normal operational state</td></tr><tr><td>Active.PMNAK</td><td>Substate of Active to indicate unsuccessful ALMP negotiation of PM entry. This is not a state requested by the Link Layer. It is applicable only for Upstream Ports. It is not applicable for 68B Flit mode.</td></tr><tr><td>L1.0</td><td>Power savings state, from which the link can enter Active via Retrain (maps to PCIe L1)</td></tr><tr><td>L1.1</td><td>Power savings state, from which the link can enter Active via Retrain (reserved for future use)</td></tr><tr><td>L1.2</td><td>Power savings state, from which the link can enter Active via Retrain (reserved for future use)</td></tr><tr><td>L1.3</td><td>Power savings state, from which the link can enter Active via Retrain (reserved for future use)</td></tr><tr><td>DAPM</td><td>Deepest Allowable PM State (not a resolved state; a request that resolves to an L1 substate)</td></tr><tr><td>SLEEP_L2</td><td>Power savings state, from which the link must go through Reset to reach Active</td></tr><tr><td>LinkReset</td><td>Reset propagation state resulting from software-initiated or hardware-initiated reset</td></tr><tr><td>LinkError</td><td>Link Error state due to hardware-detected errors that cannot be corrected through link recovery (e.g., uncorrectable internal errors or surprise link down)</td></tr><tr><td>LinkDisable</td><td>Software-controlled link disable state</td></tr><tr><td>Retrain</td><td>Transitory state that transitions to Active</td></tr></table>

Note: When the Physical Layer LTSSM enters Hot Reset or Disabled state, that state is communicated to all link layers as LinkReset or LinkDisable, respectively. No ALMPs are exchanged, regardless of who requested them, for these transitions. LinkError must take the LTSSM to Detect or Disabled. For example, it is permitted to map CXL.io Downstream Port Containment to LinkError (when the LTSSM is in Disabled state).

The ARB/MUX looks at the state of each vLSM to resolve to a single state request to forward to the physical layer as specified in Table 5-2. For example, if the current vLSM[0] state is L1.0 (row = L1.0) and the current vLSM[1] state is Active (column = Active), then the resolved request from the ARB/MUX to the Physical layer will be Active.

Table 5-2. ARB/MUX Multiple vLSM Resolution Table

<table><tr><td>Resolved Request from ARB/MUX to Flex Bus Physical Layer (Row = current vLSM[0] state; Column = current vLSM[1] state)</td><td>Reset</td><td>Active</td><td>L1.0</td><td>L1.1 (reserved for future use)</td><td>L1.2 (reserved for future use)</td><td>L1.3 (reserved for future use)</td><td>SLEEP_L2</td></tr><tr><td>Reset</td><td>RESET</td><td>Active</td><td>L1.0</td><td>L1.1 or lower</td><td>L1.2 or lower</td><td>L1.3 or lower</td><td>SLEEP_L2</td></tr><tr><td>Active</td><td>Active</td><td>Active</td><td>Active</td><td>Active</td><td>Active</td><td>Active</td><td>Active</td></tr><tr><td>L1.0</td><td>L1.0</td><td>Active</td><td>L1.0</td><td>L1.0</td><td>L1.0</td><td>L1.0</td><td>L1.0</td></tr><tr><td>L1.1 (reserved for future use)</td><td>L1.1 or lower</td><td>Active</td><td>L1.0</td><td>L1.1 or lower</td><td>L1.1 or lower</td><td>L1.1 or lower</td><td>L1.1 or lower</td></tr><tr><td>L1.2 (reserved for future use)</td><td>L1.2 or lower</td><td>Active</td><td>L1.0</td><td>L1.1 or lower</td><td>L1.2 or lower</td><td>L1.2 or lower</td><td>L1.2 or lower</td></tr><tr><td>L1.3 (reserved for future use)</td><td>L1.3 or lower</td><td>Active</td><td>L1.0</td><td>L1.1 or lower</td><td>L1.2 or lower</td><td>L1.3 or lower</td><td>L1.3 or lower</td></tr><tr><td>SLEEP_L2</td><td>SLEEP_L2</td><td>Active</td><td>L1.0</td><td>L1.1 or lower</td><td>L1.2 or lower</td><td>L1.3 or lower</td><td>SLEEP_L2</td></tr></table>

Based on the requested state from one or more of the Link Layers, ARB/MUX wil change the state request to the physical layer for the desired link state.

For implementations in which the Link Layers support directing the ARB/MUX to LinkReset or LinkError or LinkDisable, the ARB/MUX must unconditionally propagate these requests from the requesting Link Layer to the Physical Layer; this takes priority over Table 5-2.

Table 5-3 describes the conditions under which a vLSM transitions from one state to the next. A transition to the next state occurs after all the steps in the trigger conditions column are complete. Some of the trigger conditions are sequential and indicate a series of actions from multiple sources. For example, on the transition from Active to L1.x state on an Upstream Port, the state transition will not occur until the vLSM has received a request to enter L1.x from the Link Layer followed by the vLSM sending a Request ALMP{L1.x} to the remote vLSM. Next, the vLSM must wait to receive a Status ALMP{L1.x} from the remote vLSM. Once all these conditions are met in sequence, the vLSM will transition to the L1.x state as requested. Certain trigger conditions are applicable only when operating in 68B Flit mode, and these are highlighted in the table “For 68B Flit mode only”.

Table 5-3. ARB/MUX State Transition Table (Sheet 1 of 2)

<table><tr><td>Current vLSM State</td><td>Next State</td><td>Upstream Port Trigger Condition</td><td>Downstream Port Trigger Condition</td></tr><tr><td rowspan="3">Active</td><td>L1.x</td><td>Upon receiving a Request to enter L1.x from Link Layer, the ARB/MUX must initiate a Request ALMP{L1.x} and receive a Status ALMP{L1.x} from the remote vLSM</td><td>Upon receiving a Request to enter L1.x from Link Layer and receiving a Request ALMP{L1.x} from the Remote vLSM, the ARB/MUX must send Status ALMP{L1.x} to the remote vLSM</td></tr><tr><td>L2</td><td>Upon receiving a Request to enter L2 from Link Layer the ARB/MUX must initiate a Request ALMP{L2} and receive a Status ALMP{L2} from the remote vLSM</td><td>Upon receiving a Request to enter L2 from Link Layer and receiving a Request ALMP{L2} from the Remote vLSM the ARB/MUX must send Status ALMP{L2} to the remote vLSM</td></tr><tr><td>Active.PMNAK</td><td>For 256B Flit mode: Upon receiving a PMNAK ALMP from the Downstream Port ARB/MUX.This arc is not applicable for 68B Flit mode.</td><td>N/A</td></tr><tr><td>Active.PMNAK</td><td>Active</td><td>For 256B Flit mode: Upon receiving a request to enter Active from the Link Layer (see Section 5.1.2.4.2.2).This arc is not applicable for 68B Flit mode.</td><td>N/A</td></tr><tr><td>L1.x</td><td>Retrain</td><td>Upon receiving an ALMP Active request from remote ARB/MUX</td><td>Upon receiving an ALMP Active request from remote ARB/MUX</td></tr><tr><td>Active</td><td>Retrain</td><td>For 68B Flit mode only: Any of the following two conditions are met:1) Physical Layer LTSSM enters Recovery.2) Physical Layer transitions from Recovery to L0 and State Status ALMP synchronization for Recovery exit resolves to Retrain (see Section 5.1.2.3).For 256B Flit mode, this arc is not applicable since the replay buffer is moved to logPHY, there is no reason to expose Active to Retrain arc to protocol layer vLSMs.</td><td>For 68B Flit mode only: Physical Layer LTSSM enters Recovery.For 256B Flit mode, this arc is not applicable since the replay buffer is moved to logPHY, there is no reason to expose Active to Retrain arc to protocol layer vLSMs.</td></tr><tr><td>Retrain</td><td>Active</td><td>Link Layer is requesting Active and any of the following conditions are met:1) For 68B Flit mode only: Physical Layer transitions from Recovery to L0 and State Status ALMP synchronization for Recovery exit resolves to Active.2) For 68B Flit mode only: Physical Layer transitions from Recovery to L0 and State Status ALMP synchronization for Recovery exit does not resolve to Active. Entry to Active ALMP exchange protocol is complete (see Section 5.1.2.2).3) Physical Layer has been in L0. Entry to Active ALMP exchange protocol is complete (see Section 5.1.2.2).</td><td>Link Layer is requesting Active and any of the following conditions are met:1) For 68B Flit mode only: Physical Layer transitions from Recovery to L0 and State Status ALMP synchronization for Recovery exit resolves to Active.2) For 68B Flit mode only: Physical Layer transitions from Recovery to L0 and State Status ALMP synchronization for Recovery exit does not resolve to Active. Entry to Active ALMP exchange protocol is complete (see Section 5.1,2.2).3) Physical Layer has been in L0. Entry to Active ALMP exchange protocol is complete (see Section 5.1.2.2).</td></tr><tr><td>Retrain</td><td>Reset</td><td>For 68B Flit mode: Physical Layer transitions from Recovery to L0 and State Status ALMP synchronization for Recovery exit resolves to Reset (see Section 5.1.2.3).For 256B Flit mode, this arc is N/A.</td><td>N/A</td></tr><tr><td>ANY (Except Disable/LinkError)</td><td>LinkReset</td><td>Physical Layer LTSSM in Hot Reset</td><td>Physical Layer LTSSM in Hot Reset</td></tr></table>

Table 5-3. ARB/MUX State Transition Table (Sheet 2 of 2)

<table><tr><td>Current vLSM State</td><td>Next State</td><td>Upstream Port Trigger Condition</td><td>Downstream Port Trigger Condition</td></tr><tr><td>ANY (Except LinkError)</td><td>Disabled</td><td>Physical Layer LTSSM in Disabled state</td><td>Physical Layer LTSSM in Disabled state</td></tr><tr><td>ANY</td><td>LinkError</td><td>Directed to enter LinkError from Link Layer or indication of LinkError from Physical Layer</td><td>Directed to enter LinkError from Link Layer or indication of LinkError from Physical Layer</td></tr><tr><td>L2</td><td>Reset</td><td>Implementation Specific. Refer to rule 3 in Section 5.1.1.</td><td>Implementation Specific. Refer to rule 3 in Section 5.1.1.</td></tr><tr><td>Disabled</td><td>Reset</td><td>Implementation Specific. Refer to rule 3 in Section 5.1.1.</td><td>Implementation Specific. Refer to rule 3 in Section 5.1.1.</td></tr><tr><td>LinkError</td><td>Reset</td><td>Implementation Specific. Refer to rule 3 in Section 5.1.1.</td><td>Implementation Specific. Refer to rule 3 in Section 5.1.1.</td></tr><tr><td>LinkReset</td><td>Reset</td><td>Implementation Specific. Refer to rule 3 in Section 5.1.1.</td><td>Implementation Specific. Refer to rule 3 in Section 5.1.1.</td></tr><tr><td>Reset</td><td>Active</td><td>Any of the following conditions are met:1) Link Layer is asking for Active and Entry to Active ALMP exchange protocol is complete (see Section 5.1.2.2).2) For 68B Flit mode only: Physical Layer transitions from Recovery to L0 and State Status ALMP synchronization for Recovery exit resolves to Active (see Section 5.1.2.3).</td><td>Any of the following conditions are met:1) Link Layer is asking for Active and Entry to Active ALMP exchange protocol is complete (see Section 5.1.2.2).2) For 68B Flit mode only: Physical Layer transitions from Recovery to L0 and State Status ALMP synchronization for Recovery exit resolves to Active (see Section 5.1.2.3).</td></tr></table>

## 5.1.1 Additional Rules for Local vLSM Transitions

1. For 68B Flit mode, if any Link Layer requests entry into Retrain to the ARB/MUX, the ARB/MUX must forward the request to the Physical Layer to initiate LTSSM transition to Recovery. In accordance with the Active to Retrain transition trigger condition, after the LTSSM is in Recovery, the ARB/MUX should reflect Retrain to all vLSMs that are in Active state. For 256B Flit mode, there is no Active to Retrain arc in the ARB/MUX vLSM because Physical Layer LTSSM transitions to Recovery do not impact vLSM state.

## Note:

For 256B Flit mode: Not exposing the Physical Layer LTSSM transition to Recovery to the Link Layer vLSMs allows for optimizations in which the Rx Retry buffer can drain while the LTSSM is in Recovery. It also avoids corner cases in which the vLSMs become out of sync with the remote Link partner. To handle error conditions such as UpdateFC DLLP timeouts, implementations must have a sideband mechanism from the Link Layers to the Physical Layer for triggering the LTSSM transition to Recovery.

2. Once a vLSM is in Retrain state, it is expected that the corresponding Link Layer will eventually request ARB/MUX for a transition to Active.

3. If the LTSSM moves to Detect, each vLSM must eventually transition to Reset.

## 5.1.2 Rules for vLSM State Transitions across Link

This section refers to vLSM state transitions.

## 5.1.2.1 General Rules

• The link cannot operate for any other protocols if the CXL.io protocol is down (CXL.io operation is a minimum requirement)

## 5.1.2.2 Entry to Active Exchange Protocol

The ALMP protocol required for the entry to active consists of 4 ALMP exchanges between the local and remote vLSMs as seen in Figure 5-2. Entry to Active begins with an Active State Request ALMP sent to the remote vLSM which responds with an Active State Status ALMP. The only valid response to an Active State Request is an Active State Status once the corresponding Link Layer is ready to receive protocol flits. The remote vLSM must also send an Active State Request ALMP to the local vLSM which responds with an Active State Status ALMP.

During initial link training, the Upstream Port (UP in Figure 5-2) must wait for a nonphysical layer flit (i.e., a flit that was not generated by the physical layer of the Downstream Port (DP in Figure 5-2)) before transmitting any ALMPs (see Section 6.4.1). Thus, during initial link training, the first ALMP is always sent from the Downstream Port to the Upstream Port. If additional Active exchange handshakes subsequently occur (e.g., as part of PM exit), the Active request ALMP can be initiated from either side.

Once an Active State Status ALMP has been sent and received by a vLSM, the vLSM transitions to Active State.

## Figure 5-2. Entry to Active Protocol Exchange

<table><tr><td>vLSM</td><td>DP</td><td>CHANNEL</td><td>UP</td><td>vLSM</td></tr><tr><td>Status = Reset</td><td>LTSSM</td><td>vLSM[0]</td><td></td><td>Status = Reset</td></tr><tr><td>Status = Active</td><td>State_REQ ALMP {ACTIVE} vLSM[0]</td><td>STATE_STS ALMP {ACTIVE} vLSM[0]</td><td>STATE_REQ ALMP {ACTIVE} vLSM[0]</td><td>Status = Active</td></tr></table>

## 5.1.2.3 Status Synchronization Protocol

For 256B Flit mode, since the retry buffer is in the physical layer, all ALMPs are guaranteed to be delivered error free to the remote ARB/MUX. Additionally, all ALMPs are guaranteed to get a response. Therefore, there is no scenario where the Upstream Port and Downstream Port vLSMs can get out of sync.

Status Synchronization Protocol is only applicable for 68B Flit mode. The following description and rules are applicable for 68B Flit mode.

After the highest negotiated speed of operation is reached during initial link training, all subsequent LTSSM Recovery transitions must be signaled to the ARB/MUX. vLSM Status Synchronization Protocol must be performed after Recovery exit. A Link Layer cannot conduct any other communication on the link coming out of LTSSM recovery until Status Synchronization Protocol is complete for the corresponding vLSM. Figure 5-3 shows an example of Status Synchronization Protocol.

The Status Synchronization Protocol completion requires the following events in the order listed:

1. Status Exchange: Transmit a State Status ALMP, and receive an error free State Status ALMP. The state indicated in the transmitted State Status ALMP is a snapshot of the vLSM state. Refer to Section 5.1.2.3.1.

2. A corresponding State Status Resolution based on the sent and received State Status ALMPs during the synchronization exchange. See Table 5-4 for determining the resolved vLSM state.

3. New State Request and Status ALMP exchanges when applicable. This occurs if the resolved vLSM state is not the same as the Link Layer requested state.

## 5.1.2.3.1 vLSM Snapshot Rule

A STATUS\_EXCHANGE\_PENDING variable is used to determine when a snapshot of the vLSM can be taken. The following rules apply:

• Snapshot of the vLSM is taken before entry to LTSSM Recovery if the STATUS\_EXCHANGE\_PENDING variable is cleared for that vLSM

• STATUS\_EXCHANGE\_PENDING variable is set for a vLSM once a snapshot is taken

• STATUS\_EXCHANGE\_PENDING variable is cleared on reset or on completion of Status Exchange (i.e., Transmit a State Status ALMP, and receive an error free State Status ALMP)

This is to account for situations where a corrupted State Status ALMP during Status Exchange can lead to additional LTSSM transitions through Recovery. See Figure 5-16 for an example of this flow.

Figure 5-3. Example Status Exchange  
![](images/c82a49ef9e94a608157b961763df90e5f17ea61141516e6839e9d3d0521de82b.jpg)

<table><tr><td>No.</td><td>Sent Status ALMP</td><td>Received Status ALMP</td><td>Resolved vLSM State</td></tr><tr><td>1.</td><td>Reset</td><td>Reset</td><td>Reset</td></tr><tr><td>2.</td><td>Reset</td><td>Active</td><td>Active</td></tr><tr><td>3.</td><td>Reset</td><td>L2</td><td>Reset</td></tr><tr><td>4.</td><td>Active</td><td>Reset</td><td>Active</td></tr><tr><td>5.</td><td>Active</td><td>Active</td><td>Active</td></tr><tr><td>6.</td><td>Active</td><td>Retrain</td><td>Active</td></tr><tr><td>7.</td><td>Active</td><td>L1.x</td><td>Retrain</td></tr><tr><td>8.</td><td>Active</td><td>L2</td><td>Reset</td></tr></table>

Table 5-4. vLSM State Resolution after Status Exchange (Sheet 2 of 2)

<table><tr><td>No.</td><td>Sent Status ALMP</td><td>Received Status ALMP</td><td>Resolved vLSM State</td></tr><tr><td>9.</td><td>Retrain</td><td>Active</td><td>Active</td></tr><tr><td>10.</td><td>Retrain</td><td>Retrain</td><td>Retrain</td></tr><tr><td>11.</td><td>Retrain</td><td>L1.x</td><td>Retrain</td></tr><tr><td>12.</td><td>L1.x</td><td>Active</td><td>L1.x</td></tr><tr><td>13.</td><td>L1.x</td><td>Retrain</td><td>L1.x</td></tr><tr><td>14.</td><td>L1.x</td><td>L1.x</td><td>L1.x</td></tr><tr><td>15.</td><td>L2</td><td>Active</td><td>L2</td></tr><tr><td>16.</td><td>L2</td><td>Reset</td><td>L2</td></tr><tr><td>17.</td><td>L2</td><td>L2</td><td>L2</td></tr></table>

## 5.1.2.3.2 Notes on State Resolution after Status Exchange (Table 5-4)

• For the rows where the resolved state is Active, the corresponding ARB/MUX must ensure that protocol flits received immediately after the State Status ALMP from remote ARB/MUX can be serviced by the Link Layer of the corresponding vLSM. One way to guarantee this is to ensure that for these cases the Link Layer receiver is ready before sending the State Status ALMP during Status Exchange.

• Rows 7 and 11 will result in L1 exit flow following state resolution. The corresponding ARB/MUX must initiate a transition to Active through new State Request ALMPs. Once both the Upstream Port VLSM and Downstream Port vLSM are in Active, the Link Layers can redo PM entry negotiation if required. Similarly, for row 10 if reached during PM negotiation, it is required for both vLSMs to initiate Active request ALMPs.

• When supported, rows 3 and 8 will result in L2 exit flow following state resolution. Since the LTSSM will eventually move to Detect, each vLSM will eventually transition to Reset state.

• Rows 7 and 8 are applicable only for Upstream Ports. Since entry into PM is always initiated by the Upstream Port, and it cannot transition its vLSM to PM unless the Downstream Port has done so, there is no case where these rows can apply for Downstream Ports.

• Behavior is undefined and implementation specific for combinations not captured in Table 5-4.

## 5.1.2.4 State Request ALMP

The following rules apply for sending a State Request ALMP. A State Request ALMP is sent to request a state change to Active or PM. For PM, the request can only be initiated by the ARB/MUX on the Upstream Port.

## 5.1.2.4.1 For Entry into Active

• All Recovery state operations must complete before the entry to Active sequence starts. For 68B Flit mode, this includes the completion of Status Synchronization Protocol after LTSSM transitions from Recovery to L0.

• An ALMP State Request is sent to initiate the entry into Active State.

• A vLSM must send a Request and receive a Status before the transmitter is considered active. This is not equivalent to vLSM Active state.

• Protocol layer flits must only be transmitted once the vLSM has reached Active state.

Figure 5-4 shows an example of entry into the Active state. The flows in Figure 5-4 show four independent actions (ALMP handshakes) that may not necessarily occur in the order or small timeframe shown. The vLSM transmitter and receiver may become active independent of one another. Both transmitter and receiver must be active before the vLSM state is Active. The transmitter becomes active after a vLSM has transmitted a Request ALMP{Active} and received a Status ALMP{Active}. The receiver becomes active after a vLSM receives a Request ALMP{Active} and sends a Status ALMP{Active} in response.

Please refer to Section 5.1.2.2 for rules regarding the Active State Request/Status handshake protocol.

Figure 5-4. CXL Entry to Active Example Flow  
![](images/38c48e38a268d5b3bf2b30893592111a904777e5f130312343868bee050d9020.jpg)

## 5.1.2.4.2 For Entry into PM State (L1/L2)

• An ALMP State Request is sent to initiate the entry into PM States. Only Upstream Ports can initiate entry into PM states.

• For Upstream Ports, a vLSM must send a Request and receive a Status before the PM negotiation is considered complete for the corresponding vLSM.

Figure 5-5 shows an example of Entry to PM State (L1) initiated by the Upstream Port (UP in the figure) ARB/MUX. Each vLSM will be ready to enter L1 State once the vLSM has sent a Request ALMP{L1} and received a Status ALMP{L1} in return or the vLSM has received a Request ALMP{L1} and sent a Status ALMP{L1} in return. The vLSMs operate independently and actions may not complete in the order or within the timeframe shown. Once all vLSMs are ready to enter PM State (L1), the Channel will complete the EIOS exchange and enter L1.

Figure 5-5. CXL Entry to PM State Example  
![](images/b1a2b9696cc91f00431fdb2935a50c729c614f8e4e119afe0bb03bc47b81f18e.jpg)

## 5.1.2.4.2.1 PM Retry and Reject Scenarios for 68B Flit Mode

This section is applicable for 68B Flit mode only. If PM entry is not accepted by the Downstream Port, it must not respond to the PM State Request. In this scenario:

• The Upstream Port is permitted to retry entry into PM with another PM State Request after a 1-ms (not including time spent in recovery states) timeout, when waiting for a response for a PM State Request. Upstream Port must not expect a PM State Status response for every PM State Request ALMP. Even if the Upstream Port has sent multiple PM State Requests because of PM retries, if it receives a single PM State Status ALMP, it must move the corresponding vLSM to the PM state indicated in the ALMP. For a Downstream Port, if the vLSM is Active and it has received multiple PM State Request ALMPs for that vLSM, it is permitted to treat the requests as a single PM request and respond with a single PM State Status only if the vLSM transitions into the PM state. Figure 5-6 shows an example of this flow.

Figure 5-6. Successful PM Entry following PM Retry  
![](images/13f457dbaef8ef103831df90702b874db6d5d6b2d3f42a34e36153b968be6845.jpg)

• The Upstream Port is also permitted to abort entry into PM by sending an Active State Request ALMP for the corresponding vLSM. Two scenarios are possible in this case:

Downstream Port receives the Active State Request before the commit point of PM acceptance. The Downstream Port must abort PM entry and respond with Active State Status ALMP. The Upstream Port can begin flit transfer toward the Downstream Port once Upstream Port receives Active State Status ALMP. Since the vLSMs are already in Active state and flit transfer was already allowed from the Downstream Port to the Upstream Port direction during this flow, there is no Active State Request ALMP from the Downstream Port-to-Upstream Port direction. Figure 5-7 shows an example of this flow.

Figure 5-7. PM Abort before Downstream Port PM Acceptance  
![](images/fbfde3ba96ebd40706d13616dfdc6d1dfe18a677804bf3a8582341104efdf920.jpg)

— Downstream Port receives the Active State Request after the commit point of PM acceptance or after its vLSM is in a PM state. The Downstream Port must finish PM entry and send PM State Status ALMP (if not already done so). The Upstream Port must treat the received PM State Status ALMP as an unexpected ALMP and trigger link Recovery. Figure 5-8 shows an example of this flow.

Figure 5-8. PM Abort after Downstream Port PM Acceptance  
![](images/758c8d75b0b1b080a09f5e808ef713b4c36770ab1c2a98eeb751b8543038336c.jpg)

## 5.1.2.4.2.2 PM Retry and Reject Scenario for 256B Flit Mode

This section is applicable for 256B Flit mode only. Upon receiving a PM Request ALMP, the Downstream Port must respond to it with either a PM Status ALMP or an Active.PMNAK Status ALMP.

It is strongly recommended for the Downstream Port ARB/MUX to send the response ALMP to the Physical Layer within 10 us of receiving the request ALMP from the Physical Layer (the time is counted only during the L0 state of the physical LTSSM, excluding the time spent in the Downstream Port’s Rx Retry buffer for the request, or the time spent in the Downstream Port’s Tx Retry buffer for the response). If the Downstream Port does not meet the conditions to accept PM entry within that time window, it must respond with an Active.PMNAK Status ALMP.

The Downstream Port ARB/MUX must wait for at least 1 us after receiving the PM Request ALMP from the Physical Layer before deciding whether to schedule an Active.PMNAK Status ALMP.

## Note:

There is no difference between a PM Request ALMP for PCI\*-PM vs. ASPM. For both cases on the CXL.io Downstream Port, idle time with respect to lack of TLP flow triggers the Link Layer to request L1 to ARB/MUX. Waiting for at least 1 us on the Downstream Port, the ARB/MUX provides sufficient time for the PCI-PM-related CSR completion from the Upstream Port to the Downstream Port for the write to the non-D0 state to exit the Downstream Port’s CXL.io Link Layer, and reduces the likelihood of returning an Active.PMNAK Status ALMP.

Upon receiving an Active.PMNAK Status ALMP, the Upstream Port must transition the corresponding vLSM to Active.PMNAK state. The Upstream port must continue to receive and process flits while the vLSM state is Active or Active.PMNAK. If PMTimeout (see Section 8.2.5.1) is enabled and a response is not received for a PM Request ALMP within the programmed time window, the ARB/MUX must treat this as an uncorrectable internal error and escalate accordingly.

For Upstream Ports, after the Link Layer requests PM entry, the Link Layer must not change this request until it observes the vLSM status change to either the requested state or Active.PMNAK or one of the non-virtual states (LinkError, LinkReset, LinkDisable, or Reset). If Active.PMNAK is observed, the Link Layer must request Active to the ARB/MUX and wait for the vLSM to transition to Active before transmitting flits or re-requesting PM entry (if PM entry conditions are met).

The PM handshakes are reset by any events that cause physical layer LTSSM transitions that result in vLSM states of LinkError, LinkReset, LinkDisable, or Reset; these can occur at any time. Because these are Link down events, no response will be received for any outstanding Request ALMPs.

Figure 5-9. Example of a PMNAK Flow  
![](images/c5a80be422cb13f07c121b695f687cb1a7c2c24d8afba4d4b604a3b0e0ba7dac.jpg)

## 5.1.2.5 L0p Support

256B Flit mode supports L0p as defined in PCIe Base Specification; however, instead of using Link Management DLLPs, the ARB/MUX ALMPs are used to negotiate the L0p width with the Link partner. PCIe rules related to DLLP transmission, corruption, and consequent abandonment of L0p handshakes do not apply to CXL. This section defines the additional rules that are required when ALMPs are used for negotiation of L0p width.

When L0p is enabled, the ARB/MUX must aggregate the requested link width indications from the CXL.io and CXL.cachemem Link Layers to determine the L0p width for the physical link. The Link Layers must also indicate to the ARB/MUX whether the L0p request is a priority request (e.g., such as in the case of thermal throttling). The aggregated width must be greater than or equal to the larger link width that is requested by the Link Layers if it is not a priority request. The aggregated width can be greater if the ARB/MUX decides that the two protocol layers combined require a larger width than the width requested by each protocol layer. For example, if CXL.io is requesting a width of x2, and CXL.cachemem is requesting a width of x2, the ARB/MUX is permitted to request and negotiate x4 with the remote Link partner. The specific algorithm for aggregation is implementation specific.

In the case of a priority request from either Link Layer, the aggregated width is the lowest link width that is priority requested by the Link Layers. The ARB/MUX uses L0p ALMP handshakes to negotiate the L0p link width changes with its Link partner.

The following sequence is followed for L0p width changes:

1. Each Link Layer indicates its minimum required link width to the ARB/MUX. It also indicates whether the request is a priority request.

2. If the ARB/MUX determines that the aggregated L0p width is different from the current width of the physical link, the ARB/MUX must initiate an L0p width change request to the remote ARB/MUX using the L0p request ALMP. It also indicates whether the request is a priority request in the ALMP.

3. The ARB/MUX must ensure that there is only one outstanding L0p request at a time to the remote Link partner.

4. The ARB/MUX must respond with an L0p ACK or an L0p NAK to any outstanding L0p request ALMP within 1 us. (The time is counted only during the L0 state of the physical LTSSM. Time is measured from the receipt of the request ALMP from the Physical Layer to the scheduling of the response ALMP from the ARB/MUX to the Physical Layer. The time does not include the time spent by the ALMPs in the RX or TX Retry buffers.)

5. Whether to send an L0p ACK or an L0p NAK response must be determined using the L0p resolution rules from PCIe Base Specification.

6. If PMTimeout (see Section 8.2.5.1) is enabled and a response is not received for an L0p Request ALMP within the programmed time window, the ARB/MUX must treat this as an uncorrectable internal error and escalate accordingly.

7. Once the L0p ALMP handshake is complete, the ARB/MUX must direct the Physical Layer to take the necessary steps for downsizing or upsizing the link, as follows:

a. Downsizing: If the ARB/MUX receives an L0p ACK in response to its L0p request to downsize, the ARB/MUX notifies the Physical Layer to start the flow for transitioning to the corresponding L0p width at the earliest opportunity. If the ARB/MUX sends an L0p ACK in response to an L0p request, the ARB/MUX notifies the Physical Layer to participate in the flow for transitioning to the corresponding L0p width once it has been initiated by the remote partner. After a successful L0p width change, the corresponding width must be reflected back to the Link Layers.

b. Upsizing: If the ARB/MUX receives an L0p ACK in response to its L0p request to upsize, the ARB/MUX notifies the Physical Layer to immediately begin the upsizing process. If the ARB/MUX sends an L0p ACK in response to an L0p request, the ARB/MUX notifies the Physical Layer of the new width and an indication to wait for upsizing process from the remote Link partner. After a successful L0p width change, the corresponding width must be reflected back to the Link Layers.

If the Link has not reached the negotiated L0p width 24 ms after the L0p ACK was sent or received, the ARB/MUX must trigger the Physical Layer to transition the LTSSM to Recovery.

The L0p ALMP handshakes can happen concurrently with vLSM ALMP handshakes. L0p width changes do not affect vLSM states.

In 256B Flit mode, the PCIe-defined PM and Link Management DLLPs are not applicable for CXL.io and must not be used.

Similar to PCIe, the Physical Layer’s entry to Recovery or link down conditions restores the link to its maximum configured width and any Physical Layer states related to L0p are reset as if no width change was made. The ARB/MUX must finish any outstanding L0p handshakes before requesting the Physical Layer to enter a PM state. If the ARB/ MUX is waiting for an L0p ACK or NAK from the remote ARB/MUX when the link enters Recovery, after exit from Recovery, the ARB/MUX must continue to wait for the L0p response, discard that response, and then, if desired, reinitiate the L0p handshake.

## 5.1.2.6 State Status ALMP

## 5.1.2.6.1 When State Request ALMP Is Received

A State Status ALMP is sent after a valid State Request ALMP is received for Active State (if the current vLSM state is already in Active, or if the current vLSM state is not Active and the request is following the entry into Active protocol) or PM States (when entry to the PM state is accepted). For 68B Flit mode, no State Status ALMP is sent if the PM state is not accepted. For 256B Flit mode, an Active.PMNAK State Status ALMP must be sent if the PM state is not accepted.

## 5.1.2.6.2 Recovery State (68B Flit Mode Only)

The rules in this section apply only for 68B Flit mode. For 256B Flit mode, physical layer Recovery does not trigger the Status Synchronization protocol.

• The vLSM will trigger link Recovery if a State Status ALMP is received without a State Request first being sent by the vLSM except when the State Status ALMP is received for synchronization purposes (i.e., after the link exits Recovery).

Figure 5-10 shows a general example of Recovery exit. Please refer to Section 5.1.2.3 for details on the status synchronization protocol.

Figure 5-10. CXL Recovery Exit Example Flow  
![](images/ffcad6f2f96abf4e950cb740ee648b05b213c7b42dae58fc5fee8ca942c58282.jpg)

On Exit from Recovery, the vLSMs on either side of the channel will send a Status ALMP to synchronize the vLSMs. The Status ALMPs for synchronization may trigger a State Request ALMP if the resolved state and the Link Layer requested state are not the same, as seen in Figure 5-11. Refer to Section 5.1.2.3 for the rules that apply during state synchronization. The ALMP for synchronization may trigger a re-entry to recovery in the case of unexpected ALMPs. This is explained using the example of initial link training flows in Section 5.1.3.1. If the resolved states from both vLSMs are the same as the Link Layer requested state, the vLSMs are considered to be synchronized and will continue normal operation.

Figure 5-11 shows an example of the exit from a PM State (L1) through Recovery. The Downstream Port (DP in the figure) vLSM[0] in L1 state receives the Active Request, and the link enters Recovery. After the exit from recovery, each vLSM sends Status ALMP{L1} to synchronize the vLSMs. Because the resolved state after synchronization is not equal to the requested state, Request ALMP{Active} and Status ALMP{Active} handshakes are completed to enter Active State.

Figure 5-11. CXL Exit from PM State Example  
![](images/14d8794a555508f3d9e4c038b86576b1cc839fe6f97d2acfe0410c9978df253a.jpg)

## 5.1.2.7 Unexpected ALMPs (68B Flit Mode Only)

Unexpected ALMPs are applicable only for 68B Flit mode. For 256B Flit mode, there are no scenarios that lead to unexpected ALMPs.

The following situations describe circumstances where an unexpected ALMP will trigger link recovery:

• When performing the Status Synchronization Protocol after exit from recovery, any ALMP other than a Status ALMP is considered an unexpected ALMP and will trigger recovery.

• When an Active Request ALMP has been sent, receipt of any ALMP other than an Active State Status ALMP or an Active Request ALMP is considered an unexpected ALMP and will trigger recovery.

• As outlined in Section 5.1.2.6.2, a State Status ALMP received without a State Request ALMP first being sent is an unexpected ALMP except during the Status Synchronization Protocol.

## 5.1.3 Applications of the vLSM State Transition Rules for 68B Flit Mode

## 5.1.3.1 Initial Link Training

As the link trains from 2.5 GT/s speed to the highest supported speed (8.0 GT/s or higher for CXL), the LTSSM may go through several Recovery to L0 to Recovery transitions. Implementations are not required to expose ARB/MUX to all of these Recovery transitions. Depending on whether these initial Recovery transitions are hidden from the ARB/MUX, there are four possible scenarios for the initial ALMP handshakes. In all cases, the vLSM state transition rules guarantee that the situation will resolve itself with the vLSMs reaching Active state. These scenarios are presented in the following figures. Note that the figures are illustrative examples, and implementations must follow the rules outlined in the previous sections. Only one vLSM handshake is shown in the figures, but the similar handshakes can occur for the second vLSM as well. Figure 5-12 shows an example of the scenario where both the Upstream Port and Downstream Port (UP and DP in the figure, respectively) are hiding the initial recovery transitions from ARB/MUX. Since neither of them saw a notification of recovery entry, they proceed with the exchange of Active request and status ALMPs to transition into the Active state. Note that the first ALMP (Active request ALMP) is sent from the Downstream Port to the Upstream Port.

Figure 5-12. Both Upstream Port and Downstream Port Hide Recovery Transitions from ARB/MUX

![](images/9bc58729cdca65d9a0f32d945cb26b7cdd7336b6c6deffe66f2c9b3ecb7549a9.jpg)

Figure 5-13 shows an example where both the Upstream Port and Downstream Port (UP and DP in the figure, respectively) notify the ARB/MUX of at least one recovery transition during initial link training. In this case, first state status synchronization ALMPs are exchanged (indicating Reset state), followed by regular exchange of Active request and status ALMPs (not explicitly shown). Note that the first ALMP (Reset status) is sent from the Downstream Port to the Upstream Port.

Figure 5-13. Both Upstream Port and Downstream Port Notify ARB/MUX of Recovery Transitions  
![](images/01c097f9879ce4f17ac5478b5073d558940890da2025c73b507e8ac4bd982fd6.jpg)

Figure 5-14 shows an example of the scenario where the Downstream Port (DP in the figure) hides initial recovery transitions from the ARB/MUX, but the Upstream Port (UP in the figure) does not. In this case, the Downstream Port ARB/MUX has not seen recovery transition, so it begins by sending an Active state request ALMP to the Upstream Port. The Upstream Port interprets this as an unexpected ALMP, which triggers link recovery (which must now be communicated to the ARB/MUX because it is after reaching operation at the highest supported link speed). State status synchronization with state=Reset is performed, followed by regular Active request and status handshakes (not explicitly shown).

Figure 5-14. Downstream Port Hides Initial Recovery, Upstream Port Does Not  
![](images/9f9f443f580428054283f05c3dba8094fdbb7c47ead90a1570858da00245583d.jpg)

Figure 5-15 shows an example of the scenario where the Upstream Port (UP in the figure) hides initial recovery transitions, but the Downstream Port (DP in the figure) does not. In this case, the Downstream Port first sends a Reset status ALMP. This will cause the Upstream Port to trigger link recovery as a result of the rules in Section 5.1.2.4.2.1 (which must now be communicated to the ARB/MUX because it is after reaching operation at the highest supported link speed). State status synchronization with state=Reset is performed, followed by regular Active request and status handshakes (not explicitly shown).

Figure 5-15. Upstream Port Hides Initial Recovery, Downstream Port Does Not

![](images/e7526637b19acf5e21467fbb3c88bbf2c75c81d5b1e6b7fd7644d1c3b7756b29.jpg)

## 5.1.3.2 Status Exchange Snapshot Example

Figure 5-16 shows an example case where a State Status ALMP during Status Exchange gets corrupted for vLSM[1] on the Upstream Port (UP in the figure). A corrupted ALMP is when the lower four DWORDs don’t match for a received ALMP; it indicates a bit error on the lower four DWORDs of the ALMP during transmission. The ARB/MUX triggers LTSSM Recovery as a result. When the recovery entry notification is received for the second Recovery entry, the snapshot of vLSM[1] on the Upstream Port is still Active since the status exchanges had not successfully completed.

Figure 5-16. Snapshot Example during Status Synchronization  
![](images/b1a604b92f13153d9cbfdb9381c2cd04c6612545becad65b83795c3c7c23f0b6.jpg)

## 5.1.3.3 L1 Abort Example

Figure 5-17 shows an example of a scenario that could arise during L1 transition of the physical link. It begins with successful L1 entry by both vLSMs through corresponding PM request and status ALMP handshakes. The ARB/MUX even requests the Physical Layer to take the LTSSM to L1 for both the Upstream Port and Downstream Port (UP and DP in Figure 5-17, respectively). However, there is a race and one of the vLSMs requests Active before EIOS is received by the Downstream Port Physical Layer. This causes the ARB/MUX to remove the request for L1 entry (L1 abort), while sending an Active request ALMP to the Upstream Port. When EIOS is eventually received by the physical layer, since the ARB/MUX on the Downstream Port side is not requesting L1 (and there is no support for L0s in CXL), the Physical Layer must take the LTSSM to Recovery to resolve this condition. On Recovery exit, both the Upstream Port and Downstream Port ARB/MUX send their corresponding vLSM state status as part of the synchronization protocol. For vLSM[1], since the resolved state status (Retrain) is not the same as desired state status (Active), another Active request ALMP must be sent by the Downstream Port to the Upstream Port. Similarly, on the Upstream Port side, the received state status (L1) is not the same as the desired state status (Active since the vLSM moving to Retrain will trigger the Upstream Port link layer to request Active), the Upstream Port ARB/MUX will initiate an Active request ALMP to the Downstream Port. After the Active state status ALMP has been sent and received, the corresponding ARB/ MUX will move the vLSM to Active, and the protocol level flit transfer can begin.

Figure 5-17. L1 Abort Example  
![](images/5520de115ca9472d4f01c64befa6225592345023517864933adfa9cee5a4be23.jpg)

## 5.2 ARB/MUX Link Management Packets

The ARB/MUX uses ALMPs to communicate virtual link state transition requests and responses associated with each link layer to the remote ARB/MUX.

An ALMP is a 1-DWORD packet with the format shown in Figure 5-18. For 68B Flit mode, this 1-DWORD packet is replicated four times on the lower 16 bytes of a 528-bit flit to provide data integrity protection; the flit is zero-padded on the upper bits. If the ARB/MUX detects an error in the ALMP, it initiates a retrain of the link.

Figure 5-18. ARB/MUX Link Management Packet Format

<table><tr><td colspan="8">Byte 0</td><td colspan="7">Byte 1</td><td colspan="7">Byte 2</td><td colspan="7">Byte 3</td><td></td><td></td><td></td></tr><tr><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td colspan="8">Reserved</td><td colspan="7">Message</td><td colspan="16">Message Specific</td><td></td></tr></table>

For 256B Flit mode, Bytes 0, 1, 2, and 3 of the ALMP are placed on Bytes 2, 3, 4, and 5 of the 256B flit, respectively (as defined in Section 6.2.3.1). There is no replication since the ALMP is now protected through CRC and FEC. Figure 5-19 shows the ALMP byte positions in the Standard 256B flit. Figure 5-20 shows the ALMP byte positions in the Latency-Optimized 256B flit. See Section 6.2.3.1 for definitions of the FlitHdr, CRC, and FEC bytes.

Figure 5-19. ALMP Byte Positions in Standard 256B Flit

<table><tr><td>FlitHdr(2 bytes)</td><td>ALMPByte 0</td><td>ALMPByte 1</td><td>ALMPByte 2</td><td>ALMPByte 3</td><td colspan="2">122 bytes of 00h</td></tr><tr><td colspan="5">114 bytes of 00h</td><td>CRC (8 bytes)</td><td>FEC (6 bytes)</td></tr></table>

Figure 5-20. ALMP Byte Positions in Latency-Optimized 256B Flit

<table><tr><td>FlitHdr(2 bytes)</td><td>ALMPByte 0</td><td>ALMPByte 1</td><td>ALMPByte 2</td><td>ALMPByte 3</td><td colspan="2">116 bytes of 00h</td><td>CRC (6 bytes)</td></tr><tr><td colspan="6">116 bytes of 00h</td><td>FEC (6 bytes)</td><td>CRC (6 bytes)</td></tr></table>

For 256B Flit mode, there are two categories of ALMPs: the vLSM ALMPs and the L0p Negotiation ALMPs. For 68B Flit mode, only vLSM ALMPs are applicable. Byte 1 of the ALMP is shown in Table 5-5.

ALMP Byte 1 Encoding

<table><tr><td>Byte 1 Bits</td><td>Description</td></tr><tr><td>7:0</td><td>Message Encoding0000 0001b = L0p Negotiation ALMP (for 256B Flit mode; reserved for 68B Flit mode)0000 1000b = vLSM ALMP is encoded in Bytes 2 and 3All other encodings are reserved</td></tr></table>

Bytes 2 and 3 for vLSM ALMPs are shown in Table 5-6. Bytes 2 and 3 for L0p Negotiation ALMPs are shown in Table 5-7.

ALMP Byte 2 and 3 Encodings for vLSM ALMP

<table><tr><td>Byte 2 Bits</td><td>Description</td></tr><tr><td>3:0</td><td>vLSM State EncodingNote:Rx should treat this as reserved for L0p ALMP.0000b = Reset (for Status ALMP)0000b = Reserved (for Request ALMP)0001b = Active0010b = Reserved (for Request ALMP)0010b = Active.PMNAK (for Status ALMP for 256B Flit mode; reserved for 68B Flit mode)0011b = DAPM (for Request ALMP)0011b = Reserved (for Status ALMP)0100b = IDLE_L1.0 (maps to PCIe L1)0101b = IDLE_L1.1 (reserved for future use)0110b = IDLE_L1.2 (reserved for future use)0111b = IDLE_L1.3 (reserved for future use)1000b = L21011b = Retrain (for Status ALMP only)1011b = Reserved (for Request ALMP)All other encodings are reserved</td></tr><tr><td>6:4</td><td>Reserved</td></tr><tr><td>7</td><td>Request/Status Type0 = vLSM Status ALMP1 = vLSM Request ALMP</td></tr><tr><td>Byte 3 Bits</td><td>Description</td></tr><tr><td>3:0</td><td>Virtual LSM Instance Number:Indicates the targeted vLSM interface when there are multiple vLSMs present.0001b = ALMP for CXL.io0010b = ALMP for CXL.cache and CXL.memAll other encodings are reserved</td></tr><tr><td>7:4</td><td>Reserved</td></tr></table>

ALMP Byte 2 and 3 Encodings for L0p Negotiation ALMP (Sheet 1 of 2)

<table><tr><td>Byte 2 Bits</td><td>Description</td></tr><tr><td>5:0</td><td>Reserved</td></tr><tr><td>6</td><td>0 = Not an L0p.Priority Request1 = L0p.Priority Request</td></tr><tr><td>7</td><td>Request/Status Type0 = L0p Response ALMP1 = L0p Request ALMP</td></tr></table>

ALMP Byte 2 and 3 Encodings for L0p Negotiation ALMP (Sheet 2 of 2)

<table><tr><td>Byte 3 Bits</td><td>Description</td></tr><tr><td>3:0</td><td>0100b = ALMP for L0p (for 256B Flit mode; reserved for 68B Flit mode)All other encodings are reserved</td></tr><tr><td>7:4</td><td>L0p WidthNote:Encodings 0000b to 0100b are requests for L0p Request ALMP, and imply an ACK for L0p Response ALMP.0000b = x160001b = x80010b = x40011b = x20100b = x11000b = Reserved for L0p Request ALMP1000b = L0p NAK for L0p Response ALMPAll other encodings are reservedIf the width encoding in an ACK does not match the requested L0p width, the ARB/MUX must consider it a NAK. It is permitted to resend an L0p request, if the conditions of entry are still met.</td></tr></table>

For vLSM ALMPs, the message code used in Byte 1 of the ALMP is 0000 1000b. These ALMPs can be request or status type. The local ARB/MUX initiates transition of a remote vLSM using a request ALMP. After receiving a request ALMP, the local ARB/MUX processes the transition request and returns a status ALMP. For 68B Flit mode, if the transition request is not accepted, a status ALMP is not sent and both local and remote vLSMs remain in their current state. For 256B Flit mode, if the PM transition request is not accepted, an Active.PMNAK Status ALMP is sent.

For L0p Negotiation ALMPs, the message code used in Byte 1 of the ALMP is 0000 0001b. These ALMPs can be of request or response type. See Section 5.1.2.5 for L0p negotiation flow.

## 5.2.1 ARB/MUX Bypass Feature

The ARB/MUX must disable generation of ALMPs when the Flex Bus link is operating in PCIe mode. Determination of the bypass condition can be via hwinit or during link training.

## Arbitration and Data Multiplexing/Demultiplexing

The ARB/MUX is responsible for arbitrating between requests from the CXL link layers and multiplexing the data based on the arbitration results. The arbitration policy is implementation specific as long as it satisfies the timing requirements of the higherlevel protocols being transferred over the Flex Bus link. Additionally, there must be a way to program the relative arbitration weightages associated with the CXL.io and CXL.cache + CXL.mem link layers as they arbitrate to transmit traffic over the Flex Bus link. See Section 8.2.5 for more details. Interleaving of traffic between different CXL protocols is done at the 528-bit flit boundary for 68B Flit mode, and at the 256B flit boundary for 256B Flit mode.

## 6.0 Flex Bus Physical Layer

## 6.1 Overview

## Figure 6-1. Flex Bus Layers - Physical Layer Highlighted

![](images/e0e9b889c3b2698e22667af01fe0279e3804e92d9fb5d26401b3d31c406f5410.jpg)

The figure above shows where the Flex Bus physical layer exists in the Flex Bus layered hierarchy. On the transmitter side, the Flex Bus physical layer prepares data received from either the PCIe\* link layer or the CXL ARB/MUX for transmission across the Flex Bus link. On the receiver side, the Flex Bus physical layer deserializes the data received on the Flex Bus link and converts it to the appropriate format to forward to the PCIe link layer or the ARB/MUX. The Flex Bus physical layer consists of a logical sub-block, aka the logical PHY, and an electrical sub-block. The logical PHY operates in PCIe mode during initial link training and switches over to CXL mode, if appropriate, depending on the results of alternate protocol negotiation, during recovery after training to 2.5 GT/s. The electrical sub-block follows PCIe Base Specification.

In CXL mode, normal operation occurs at native link width and 32 GT/s or 64 GT/s link speed. Bifurcation (aka link subdivision) into x8 and x4 widths is supported in CXL mode. Degraded modes of operation include 8 GT/s or 16 GT/s or 32 GT/s link speed and smaller link widths of x2 and x1. Table 6-1 summarizes the supported CXL combinations. In PCIe mode, the link supports all widths and speeds defined in PCIe Base Specification, as well as the ability to bifurcate.

Flex Bus.CXL Link Speeds and Widths for Normal and Degraded Mode

<table><tr><td>Link Speed</td><td>Native Width</td><td>Degraded Modes Supported</td></tr><tr><td rowspan="3">32 GT/s</td><td>x16</td><td>x16 at 16 GT/s or 8 GT/s;x8, x4, x2, or x1 at 32 GT/s or 16 GT/s or 8 GT/s</td></tr><tr><td>x8</td><td>x8 at 16 GT/s or 8 GT/s;x4, x2, or x1 at 32 GT/s or 16 GT/s or 8 GT/s</td></tr><tr><td>x4</td><td>x4 at 16 GT/s or 8 GT/s;x2 or x1 at 32 GT/s or 16 GT/s or 8 GT/s</td></tr><tr><td rowspan="3">64 GT/s</td><td>x16</td><td>x16 at 32 GT/s or 16 GT/s or 8 GT/s;x8, x4, x2, or x1 at 64 GT/s or 32 GT/s or 16 GT/s or 8 GT/s</td></tr><tr><td>x8</td><td>x8 at 32 GT/s or at 16 GT/s or 8 GT/s;x4, x2, or x1 at 64GT/s or 32 GT/s or 16 GT/s or 8 GT/s</td></tr><tr><td>x4</td><td>x4 at 32 GT/s or at 16 GT/s or 8 GT/s;x2 or x1 at 64 GT/s or 32 GT/s or 16 GT/s or 8 GT/s</td></tr></table>

This chapter focuses on the details of the logical PHY. The Flex Bus logical PHY is based on the PCIe logical PHY; PCIe mode follows PCIe Base Specification exactly while Flex Bus.CXL mode has deltas from PCIe that affect link training and framing. Please refer to the “Physical Layer Logical Block” chapter of PCIe Base Specification for details on PCIe mode. The Flex Bus.CXL deltas are described in this chapter.

## Flex Bus.CXL Framing and Packet Layout

The Flex Bus.CXL framing and packet layout is described in this section for x16, x8, x4, x2, and x1 link widths.

## 6.2.1 Ordered Set Blocks and Data Blocks

Flex Bus.CXL uses the PCIe concept of Ordered Set blocks and data blocks. Each block spans 128 bits per lane and potentially two bits of Sync Header per lane.

Ordered Set blocks are used for training, entering and exiting Electrical Idle, transitions to data blocks, and clock tolerance compensation; they are the same as defined in PCIe Base Specification. A 2-bit Sync Header with value 01b is inserted before each 128 bits transmitted per lane in an Ordered Set block when 128b/130b encoding is used; in the Sync Header bypass latency-optimized mode, there is no Sync Header. Additionally, as per PCIe Base Specification, there is no Sync Header when 1b/1b encoding is used.

Data blocks are used for transmission of the flits received from the CXL ARB/MUX. In 68B Flit mode, a 16-bit Protocol ID field is associated with each 528-bit flit payload (512 bits of payload + 16 bits of CRC) received from the link layer, which is striped across the lanes on an 8-bit granularity; the placement of the Protocol ID depends on the width. A 2-bit Sync Header with value 10b is inserted before every 128 bits transmitted per lane in a data block when 128b/130b encoding is used; in the latencyoptimized Sync Header Bypass mode, there is no Sync Header. A 528-bit flit may traverse the boundary between data blocks. In 256B Flit mode, the flits are 256 bytes, which includes the Protocol ID information in the Flit Type field.

Transitions between Ordered Set blocks and data blocks are indicated in a couple of ways, only a subset of which may be applicable depending on the data rate and CXL mode. One way is via the 2-bit Sync Header of 01b for Ordered Set blocks and 10b for data blocks. The second way is via the use of Start of Data Stream (SDS) Ordered Sets and End of Data Stream (EDS) tokens. Unlike PCIe where the EDS token is explicit, Flex Bus.CXL encodes the EDS indication in the Protocol ID value in 68B Flit mode; the latter is referred to as an “implied EDS token.” In 256B Flit mode, transitions from Data Blocks to Ordered Set Blocks are permitted to occur at only fixed locations as specified in PCIe Base Specification for PCIe Flit mode.

## 6.2.2 68B Flit Mode

Selection of 68B Flit mode vs. 256B Flit mode occurs during PCIe link training. The following subsections describe the physical layer framing and packet layout for 68B Flit mode. See Section 6.2.3 for 256B Flit mode.

## 6.2.2.1 Protocol ID[15:0]

The 16-bit Protocol ID field specifies whether the transmitted flit is CXL.io, CXL.cachemem, or some other payload. Table 6-2 provides a list of valid 16-bit Protocol ID encodings. Encodings that include an implied EDS token signify that the next block after the block in which the current flit ends is an Ordered Set block. Implied EDS tokens can only occur with the last flit transmitted in a data block.

Flex Bus.CXL Protocol IDs

<table><tr><td>Protocol ID[15:0]</td><td>Description</td></tr><tr><td>FFFFh</td><td>CXL.io</td></tr><tr><td>D2D2h</td><td>CXL.io with Implied EDS Token</td></tr><tr><td>5555h</td><td>CXL.cachemem</td></tr><tr><td>8787h</td><td>CXL.cachemem with Implied EDS Token</td></tr><tr><td>9999h</td><td>NULL Flit: Null flit generated by the Physical Layer</td></tr><tr><td>4B4Bh</td><td>NULL flit with Implied EDS Token: Variable length flit containing NULLs that ends exactly at the data block boundary that precedes the Ordered Set block (generated by the Physical Layer)</td></tr><tr><td>CCCCh</td><td>CXL ARB/MUX Link Management Packets (ALMPs)</td></tr><tr><td>1E1Eh</td><td>CXL ARB/MUX Link Management Packets (ALMPs) with Implied EDS Token</td></tr><tr><td>All other encodings</td><td>Reserved</td></tr></table>

NULL flits are inserted into the data stream by the physical layer when there are no valid flits available from the link layer. A NULL flit transferred with an implied EDS token ends exactly at the data block boundary that precedes the Ordered Set block; these are variable length flits, up to 528 bits, intended to facilitate transition to Ordered Set blocks as quickly as possible. When 128b/130b encoding is used, the variable length NULL flit ends on the first block boundary encountered after the 16-bit Protocol ID has been transmitted, and the Ordered Set is transmitted in the next block. Because Ordered Set blocks are inserted at fixed block intervals that align to the flit boundary when Sync Headers are disabled (as described in Section 6.8.1), variable length NULL flits will always contain a fixed 528-bit payload when Sync Headers are disabled. See Section 6.8.1 for examples of NULL flit with implied EDS usage scenarios. A NULL flit is composed of an all 0s payload.

An 8-bit encoding with a hamming distance of four is replicated to create the 16-bit encoding for error protection against bit flips. A correctable Protocol ID framing error is logged but no further error handling action is required if only one 8-bit encoding group looks incorrect; the correct 8-bit encoding group is used for normal processing. If both 8-bit encoding groups are incorrect, an uncorrectable Protocol ID framing error is logged, the flit is dropped, and the physical layer enters into recovery to retrain the link.

The physical layer is responsible for dropping any flits it receives with invalid Protocol IDs. This includes dropping any flits with unexpected Protocol IDs that correspond to Flex Bus-defined protocols that have not been enabled during negotiation; Protocol IDs associated with flits generated by physical layer or by the ARB/MUX must not be treated as unexpected. When a flit is dropped due to an unexpected Protocol ID, the physical layer logs an unexpected protocol ID error in the Flex Bus DVSEC Port Status register.

See Section 6.2.2.8 for additional details regarding Protocol ID error detection and handling.

## 6.2.2.2 x16 Packet Layout

Figure 6-2 shows the x16 packet layout. First, the 16 bits of Protocol ID are transferred, split on an 8-bit granularity across consecutive lanes; this is followed by transfer of the 528-bit flit, striped across the lanes on an 8-bit granularity. Depending on the symbol time, as labeled on the leftmost column in the figure, the Protocol ID plus flit transfer may start on Lane 0, Lane 4, Lane 8, or Lane 12. The pattern of transfer repeats after every 17 symbol times. The two-bit Sync Header shown in the figure, inserted after every 128 bits transferred per lane, is not present for the latencyoptimized mode where Sync Header bypass is negotiated.

Figure 6-2. Flex Bus x16 Packet Layout

<table><tr><td></td><td>L0</td><td>L1</td><td>L2</td><td>L3</td><td>L4</td><td>L5</td><td>L6</td><td>L7</td><td>L8</td><td>L9</td><td>L10</td><td>L11</td><td>L12</td><td>L13</td><td>L14</td><td>L15</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>ProtID[7.0]</td><td>ProtID[15.8]</td><td>Flit[7.0]</td><td>Flit[15.8]</td><td>Flit[23.16]</td><td>Flit[31.24]</td><td>Flit[39.32]</td><td>Flit[47.40]</td><td>Flit[55.48]</td><td>Flit[63.56]</td><td>Flit[71.64]</td><td>Flit[79.72]</td><td>Flit[87.80]</td><td>Flit[95.88]</td><td>Flit[103.96]</td><td>Flit[111.104]</td></tr><tr><td>Symbol1</td><td>Flit[119.112]</td><td>Flit[127.120]</td><td>Flit[135.128]</td><td>Flit[143.136]</td><td>Flit[151.144]</td><td>Flit[159.152]</td><td>Flit[167.160]</td><td>Flit[175.168]</td><td>Flit[183.176]</td><td>Flit[191.184]</td><td>Flit[199.192]</td><td>Flit[207.200]</td><td>Flit[215.208]</td><td>Flit[223.216]</td><td>Flit[231.224]</td><td>Flit[239.232]</td></tr><tr><td>Symbol2</td><td>Flit[247.240]</td><td>Flit[255.248]</td><td>Flit[263.256]</td><td>Flit[271.264]</td><td>Flit[279.272]</td><td>Flit[287.280]</td><td>Flit[295.288]</td><td>Flit[303.296]</td><td>Flit[311.304]</td><td>Flit[319.312]</td><td>Flit[327.320]</td><td>Flit[335.328]</td><td>Flit[343.336]</td><td>Flit[351.344]</td><td>Flit[359.352]</td><td>Flit[367.360]</td></tr><tr><td>Symbol3</td><td>Flit[375.368]</td><td>Flit[383.376]</td><td>Flit[391.384]</td><td>Flit[399.392]</td><td>Flit[407.400]</td><td>Flit[415.408]</td><td>Flit[423.416]</td><td>Flit[431.424]</td><td>Flit[439.432]</td><td>Flit[447.440]</td><td>Flit[455.448]</td><td>Flit[463.456]</td><td>Flit[471.464]</td><td>Flit[479.472]</td><td>Flit[487.480]</td><td>Flit[495.488]</td></tr><tr><td>Symbol4</td><td>Flit[503.496]</td><td>Flit[511.504]</td><td>Flit[519.512]</td><td>Flit[527.520]</td><td>ProtID[7.0]</td><td>ProtID[15.8]</td><td>Flit[7.0]</td><td>Flit[15.8]</td><td>Flit[23.16]</td><td>Flit[31.24]</td><td>Flit[39.32]</td><td>Flit[47.40]</td><td>Flit[55.48]</td><td>Flit[63.56]</td><td>Flit[7l.64]</td><td>Flit[79.72]</td></tr><tr><td>Symbol5</td><td>Flit[87.80]</td><td>Flit[95.88]</td><td>Flit[103.96]</td><td>Flit[111.104]</td><td>Flit[119.112]</td><td>Flit[127.120]</td><td>Flit[135.128]</td><td>Flit[143.136]</td><td>Flit[151.144]</td><td>Flit[159.152]</td><td>Flit[167.160]</td><td>Flit[175.168]</td><td>Flit(183.176)</td><td>Flit[191.184]</td><td>Flit[199.192]</td><td>Flit[207.200]</td></tr><tr><td>Symbol6</td><td>Flit[215.208]</td><td>Flit[223.216]</td><td>Flit[231.224]</td><td>Flit[239.232]</td><td>Flit[247.240]</td><td>Flit[255.248]</td><td>Flit[263.256]</td><td>Flit[271.264]</td><td>Flit[279.272]</td><td>Flit[287.280]</td><td>Flit[295.288]</td><td>Flit[303.296]</td><td>Flit311.304]</td><td>Flit[319.312]</td><td>Flit[327.320]</td><td>Flit[335.328]</td></tr><tr><td>Symbol7</td><td>Flit[343.336]</td><td>Flit[351.344]</td><td>Flit[359.352]</td><td>Flit[367.360]</td><td>Flit[375.368]</td><td>Flit[383.376]</td><td>Flit[391.384]</td><td>Flit[399.392]</td><td>Flit[407.400]</td><td>Flit[415.408]</td><td>Flit[423.416]</td><td>Flit[431.424]</td><td>Flit439.432]</td><td>Flit[447.440]</td><td>Flit[455.448]</td><td>Flit[463.456]</td></tr><tr><td>Symbol8</td><td>Flit[471.464]</td><td>Flit[479.472]</td><td>Flit[487.480]</td><td>Flit[495.488]</td><td>Flit[503.496]</td><td>Flit[511.504]</td><td>Flit[519.512]</td><td>Flit[527.520]</td><td>ProtID[7.0]</td><td>ProtID[15.8]</td><td>Flit[7.0]</td><td>Flit[15.8]</td><td>Flit[23.16]</td><td>Flit[31. 24]</td><td>Flit[39.32]</td><td>Flit[47.40]</td></tr><tr><td>Symbol9</td><td>Flit[55.48]</td><td>Flit[63.56]</td><td>Flit[71.64]</td><td>Flit[79.72]</td><td>Flit[87.80]</td><td>Flit[95.88]</td><td>Flit[103.96]</td><td>Flit[111.104]</td><td>Flit[119.112]</td><td>Flit[127.120]</td><td>Flit[135.128]</td><td>Flit[143.136]</td><td>Flit[151.44]</td><td>Flit[159.152]</td><td>Flit[167.160]</td><td>Flit[175.168]</td></tr><tr><td>Symbol10</td><td>Flit[183.176]</td><td>Flit[191.184]</td><td>Flit[199.192]</td><td>Flit[207.200]</td><td>Flit[215.208]</td><td>Flit[223.216]</td><td>Flit[231.224]</td><td>Flit[239.232]</td><td>Flit[247.240]</td><td>Flit[255.248]</td><td>Flit[263.256]</td><td>Flit[271.264]</td><td>Flit279.272]</td><td>Flit[287.280]</td><td>Flit[295.288]</td><td>Flit[303.296]</td></tr><tr><td>Symbol11</td><td>Flit[311.304]</td><td>Flit[319.312]</td><td>Flit[327.320]</td><td>Flit[335.328]</td><td>Flit[343.336]</td><td>Flit[351.344]</td><td>Flit[359.352]</td><td>Flit[367.360]</td><td>Flit[375.368]</td><td>Flit[383.376]</td><td>Flit[391.384]</td><td>Flit[399.392]</td><td>Flit407.400]</td><td>Flit[415.408]</td><td>Flit[423.416]</td><td>Flit[431.424]</td></tr><tr><td>Symbol12</td><td>Flit[439.432]</td><td>Flit[447.440]</td><td>Flit[455.448]</td><td>Flit[463.456]</td><td>Flit[471.464]</td><td>Flit[479.472]</td><td>Flit[487.480]</td><td>Flit[495.488]</td><td>Flit[503.496]</td><td>Flit[511.504]</td><td>Flit[519.512]</td><td>Flit[527.520]</td><td>ProtID [7.0]</td><td>ProtID [15.8]</td><td>Flit[7.0]</td><td>Flit[15.8]</td></tr><tr><td>Symbol13</td><td>Flit[23.16]</td><td>Flit[31.24]</td><td>Flit[39.32]</td><td>Flit[47.40]</td><td>Flit[55.48]</td><td>Flit[63.56]</td><td>Flit[71.64]</td><td>Flit[79.72]</td><td>Flit[87.80]</td><td>Flit[95.88 ]</td><td>Flit[103.96]</td><td>Flit[111.104]</td><td>Flit[119.112]</td><td>Flit[127.120]</td><td>Flit[135.128]</td><td>Flit[143.136]</td></tr><tr><td>Symbol14</td><td>Flit[151.144]</td><td>Flit[159.152]</td><td>Flit[167.160]</td><td>Flit[175.168]</td><td>Flit[183.176]</td><td>Flit[191.184]</td><td>Flit[199.192]</td><td>Flit[207.200]</td><td>Flit215.208]</td><td>Flit[223.216]</td><td>Flit[231.224]</td><td>Flit[239.232]</td><td>Flit247.240]</td><td>Flit[255.248]</td><td>Flit[263.256]</td><td>Flit[271.264]</td></tr><tr><td>Symbol15</td><td>Flit[279.272]</td><td>Flit[287.280]</td><td>Flit[295.288]</td><td>Flit[303.296]</td><td>Flit[311.304]</td><td>Flit[319.312]</td><td>Flit[327.320]</td><td>Flit[335.328]</td><td>Flit343.336]</td><td>Flit[351.344]</td><td>Flit[359.352]</td><td>Flit[367.360]</td><td>Flit[375.368]</td><td>Flit[383.376]</td><td>Flit[391.384]</td><td>Flit[399.392]</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>Flit[407.400]</td><td>Flit[415.408]</td><td>Flit[423.416]</td><td>Flit[431.424]</td><td>Flit[439.432]</td><td>Flit[447.440]</td><td>Flit[455.448]</td><td>Flit[463.456]</td><td>Flit471.464]</td><td>Flit[479.472]</td><td>Flit[487.480]</td><td>Flit[495.488]</td><td>Flit[503.496]</td><td>Flit[511.504]</td><td>Flit[519.512]</td><td>Flit[527.520]</td></tr><tr><td>Symbol1</td><td>ProtID [7.0]</td><td>ProtID [15.8]</td><td>Flit[7.0]</td><td>Flit[15.8]</td><td>Flit[23.16]</td><td>Flit[31.24]</td><td>Flit[39.32]</td><td>Flit[47.40]</td><td>Flit[55.48]</td><td>Flit[63.56]</td><td>Flit[71.64]</td><td>Flit[79. 72]</td><td>Flit[87.80]</td><td>Flit[95.88]</td><td>Flit[103.96]</td><td>Flit[111.104]</td></tr></table>

Figure 6-3 provides an example where CXL.io and CXL.cachemem traffic is interleaved with an interleave granularity of two flits on a x16 link. The upper part of the figure shows what the CXL.io stream looks like before mapping to the Flex Bus lanes and before interleaving with CXL.cachemem traffic; the framing rules follow the x16 framing rules specified in PCIe Base Specification, as specified in Section 4.1. The lower part of the figure shows the final result when the two streams are interleaved on the Flex Bus lanes. For CXL.io flits, after transferring the 16-bit Protocol ID, 512 bits are used to transfer CXL.io traffic and 16 bits are unused. For CXL.cachemem flits, after transferring the 16-bit Protocol ID, 528 bits are used to transfer a CXL.cachemem flit. See Chapter 4.0 for more details on the flit format. As this example illustrates, the PCIe TLPs and DLLPs encapsulated within the CXL.io stream may be interrupted by nonrelated CXL traffic if they cross a flit boundary.

Figure 6-3. Flex Bus x16 Protocol Interleaving Example

<table><tr><td></td><td>L0</td><td>L1</td><td>L2</td><td>L3</td><td>L4</td><td>L5</td><td>L6</td><td>L7</td><td>L8</td><td>L9</td><td>L10</td><td>L11</td><td>L12</td><td>L13</td><td>L14</td><td>L15</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td colspan="4">PCIe STP Token</td><td colspan="4">PCIe TLP Header DW0</td><td colspan="4">PCIe TLP Header DW1</td><td colspan="4">PCIe TLP Header DW2</td></tr><tr><td>Symbol1</td><td colspan="4">PCIe TLP Data Payload DW0</td><td colspan="4">PCIe TLP Data Payload DW1</td><td colspan="4">PCIe TLP Data Payload DW2</td><td colspan="4">PCIe TLP LCRC</td></tr><tr><td>Symbol2</td><td colspan="2">PCIe SDP Token</td><td colspan="4">PCIe DLLP Payload</td><td colspan="2">PCIe DLLP CRC</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td></tr><tr><td>Symbol3</td><td colspan="4">PCIe STP Token</td><td colspan="4">PCIe TLP Header DW0</td><td colspan="4">PCIe TLP Header DW1</td><td colspan="4">PCIe TLP Header DW2</td></tr><tr><td>Symbol4</td><td colspan="4">PCIe TLP Data Payload DW0</td><td colspan="4">PCIe TLP Data Payload DW1</td><td colspan="4">PCIe TLP Data Payload DW2</td><td colspan="4">PCIe TLP Data Payload DW3</td></tr><tr><td>Symbol5</td><td colspan="4">PCIe TLP Data Payload DW4</td><td colspan="4">PCIe TLP Data Payload DW5</td><td colspan="4">PCIe TLP Data Payload DW6</td><td colspan="4">PCIe TLP Data Payload DW7</td></tr><tr><td>Symbol6</td><td colspan="4">PCIe TLP Data Payload DW8</td><td colspan="4">PCIe TLP LCRC</td><td colspan="2">PCIe SDP Token</td><td colspan="4">PCIe DLLP Payload</td><td colspan="2">PCIe DLLP CRC</td></tr><tr><td>Symbol7</td><td colspan="4">PCIe STP Token</td><td colspan="4">PCIe TLP Header DW0</td><td colspan="4">PCIe TLP Header DW1</td><td colspan="4">PCIe TLP Header DW2</td></tr><tr><td>Symbol8</td><td colspan="4">PCIe TLP Data Payload DW0</td><td colspan="4">PCIe TLP Data Payload DW1</td><td colspan="4">PCIe TLP Data Payload DW2</td><td colspan="4">PCIe TLP LCRC</td></tr></table>

<table><tr><td></td><td>L0</td><td>L1</td><td>L2</td><td>L3</td><td>L4</td><td>L5</td><td>L6</td><td>L7</td><td>L8</td><td>L9</td><td>L10</td><td>L11</td><td>L12</td><td>L13</td><td>L14</td><td>L15</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>ProtID[7:0]=CXLio</td><td>ProtID[15:8]=CXLio</td><td colspan="4">PCIe STP Token</td><td colspan="4">PCIe TLP Header DW0</td><td colspan="4">PCIe TLP Header DW1</td><td colspan="2">PCIe TLP Header DW2[15:0]</td></tr><tr><td>Symbol1</td><td colspan="2">PCIe TLP Header DW2[31:16]</td><td colspan="4">PCIe TLP Data Payload DW0</td><td colspan="4">PCIe TLP Data Payload DW1</td><td colspan="4">PCIe TLP Data Payload DW2</td><td colspan="2">PCIe TLP LCRC</td></tr><tr><td>Symbol2</td><td colspan="2">PCIe TLP LCRC</td><td colspan="2">PCIe SDP Token</td><td colspan="4">PCIe DLLP Payload</td><td colspan="2">PCIe DLLP CRC</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td></tr><tr><td>Symbol3</td><td>PCIe IDL</td><td>PCIe IDL</td><td colspan="4">PCIe STP Token</td><td colspan="4">PCIe TLP Header DW0</td><td colspan="4">PCIe TLP Header DW1</td><td colspan="2">PCIe TLP Header DW2[15:0]</td></tr><tr><td>Symbol4</td><td colspan="2">PCIe TLP Header DW2[31:16]</td><td>Reserved</td><td>Reserved</td><td>ProtID[7:0]=CXLio</td><td>ProtID[15:8]=CXLio</td><td colspan="4">PCIe TLP Data Payload DW0</td><td colspan="4">PCIe TLP Data Payload DW1</td><td colspan="2">PCIe TLP Data Payload DW2[15:0]</td></tr><tr><td>Symbol5</td><td colspan="2">PCIe TLP Data Payload DW2[31:16]</td><td colspan="4">PCIe TLP Data Payload DW3</td><td colspan="4">PCIe TLP Data Payload DW4</td><td colspan="4">PCIe TLP Data Payload DW5</td><td colspan="2">PCIe TLP Data Payload DW6[15:0]</td></tr><tr><td>Symbol6</td><td colspan="2">PCIe TLP Data Payload DW6[31:16]</td><td colspan="4">PCIe TLP Data Payload DW7</td><td colspan="4">PCIe TLP Data Payload DW8</td><td colspan="4">PCIe TLP LCRC</td><td colspan="2">PCIe SDP Token</td></tr><tr><td>Symbol7</td><td colspan="4">PCIe DLLP Payload</td><td colspan="2">PCIe DLLP CRC</td><td colspan="4">PCIe STP Token</td><td colspan="4">PCIe TLP Header DW0</td><td colspan="2">PCIe TLP Header DW1[15:0]</td></tr><tr><td>Symbol8</td><td colspan="2">PCIe TLP Header DW1[31:16]</td><td colspan="4">PCIe TLP Header DW2</td><td>Reserved</td><td>Reserved</td><td>ProtID[7:0]=CXL camem</td><td>ProtID[15:8]=CXL camem</td><td>Flt[7:0]</td><td>Flt[15:8]</td><td>Flt[23:16]</td><td>Flt[31:24]</td><td>Flt[39:32]</td><td>Flt[47:40]</td></tr><tr><td>Symbol9</td><td>Flt[55:48]</td><td>Flt[63:56]</td><td>Flt[71:64]</td><td>Flt[79:72]</td><td>Flt[87:80]</td><td>Flt[95:88]</td><td>Flt[103:96]</td><td>Flt[111:104]</td><td>Flt[119:112]</td><td>Flt[127:120]</td><td>Flt[135:128]</td><td>Flt[143:136]</td><td>Flt[151:144]</td><td>Flt[159:152]</td><td>Flt[167:160]</td><td>Flt[175:168]</td></tr><tr><td>Symbol10</td><td>Flt[183:176]</td><td>Flt[191:184]</td><td>Flt[199:192]</td><td>Flt[207:200]</td><td>Flt[215:208]</td><td>Flt[223:216]</td><td>Flt[231:224]</td><td>Flt[239:232]</td><td>Flt[247:240]</td><td>Flt[255:248]</td><td>Flt[263:256]</td><td>Flt[271:264]</td><td>Flt[279:272]</td><td>Flt[287:280]</td><td>Flt[295:288]</td><td>Flt[303:296]</td></tr><tr><td>Symbol11</td><td>Flt[311:304]</td><td>Flt[319:312]</td><td>Flt[327:320]</td><td>Flt[335:328]</td><td>Flt[343:336]</td><td>Flt[351:344]</td><td>Flt[359:352]</td><td>Flt[367:360]</td><td>Flt[375:368]</td><td>Flt[383:376]</td><td>Flt[391:384]</td><td>Flt[399:392]</td><td>Flt[407:400]</td><td>Flt[415:408]</td><td>Flt[423:416]</td><td>Flt[431:424]</td></tr><tr><td>Symbol12</td><td>Flt[439:432]</td><td>Flt[447:440]</td><td>Flt[455:448]</td><td>Flt[463:456]</td><td>Flt[471:464]</td><td>Flt[479:472]</td><td>Flt[487:480]</td><td>Flt[495:488]</td><td>Flt[503:496]</td><td>Flt[511:504]</td><td>CRC</td><td>CRC</td><td>ProtID[7:0]=CXL camem</td><td>ProtID[15:8]=CXL camem</td><td>Flt[7:0]</td><td>Flt[15:8]</td></tr><tr><td>Symbol13</td><td>Flt[23:16]</td><td>Flt[31:24]</td><td>Flt[39:32]</td><td>Flt[47:40]</td><td>Flt[55:48]</td><td>Flt[63:56]</td><td>Flt[71:64]</td><td>Flt[79:72]</td><td>Flt[87:80]</td><td>Flt[95:88]</td><td>Flt[103:96]</td><td>Flt[111:104]</td><td>Flt[119:112]</td><td>Flt[ 127:120]</td><td>Flt[135:128]</td><td>Flt[143:136]</td></tr><tr><td>Symbol14</td><td>Flt[151:144]</td><td>Flt[159:152]</td><td>Flt[167:160]</td><td>Flt[175:168]</td><td>Flt[183:176]</td><td>Flt[191:184]</td><td>Flt[199:192]</td><td>Flt[207:200]</td><td>Flt[215:208]</td><td>Flt[223:216]</td><td>Flt[231:224]</td><td>Flt[239:232]</td><td>Flt247:240]</td><td>Flt[255:248]</td><td>Flt[263:256]</td><td>Flt[271:264]</td></tr><tr><td>Symbol15</td><td>Flt[279:272]</td><td>Flt[287:280]</td><td>Flt[295:288]</td><td>Flt[303:296]</td><td>Flt[311:304]</td><td>Flt[319:312]</td><td>Flt[327:320]</td><td>Flt[335:328]</td><td>Flt[343:336]</td><td>Flt[351:344]</td><td>Flt[359:352]</td><td>Flt[367:360]</td><td>Flt375:368]</td><td>Flt[383:376]</td><td>Flt[391:384]</td><td>Flt[399:392]</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>Flt[407:400]</td><td>Flt[415:408]</td><td>Flt[423:416]</td><td>Flt[431:424]</td><td>Flt[439:432]</td><td>Flt[447:440]</td><td>Flt[455:448]</td><td>Flt[463:456]</td><td>Flt[471:464]</td><td>Flt[479:472]</td><td>Flt[487:480]</td><td>Flt[495:488]</td><td>Flt503:496]</td><td>Flt[511:504]</td><td>CRC</td><td>CRC</td></tr><tr><td>Symbol1</td><td>ProtID[7:0]=CXLio</td><td>ProtID[15:8]=CXLio</td><td colspan="4">PCIe TLP Data Payload DW0</td><td colspan="4">PCIe TLP Data Payload DW1</td><td colspan="4">PCIe TLP Data Payload DW2</td><td colspan="2">PCIe TLP LCRC[15:0]</td></tr></table>

## 6.2.2.3 x8 Packet Layout

Figure 6-4 shows the x8 packet layout. 16 bits of Protocol ID followed by a 528-bit flit are striped across the lanes on an 8-bit granularity. Depending on the symbol time, the Protocol ID plus flit transfer may start on Lane 0 or Lane 4. The pattern of transfer repeats after every 17 symbol times. The two-bit Sync Header shown in the figure is not present for the Sync Header bypass latency-optimized mode.

Figure 6-4. Flex Bus x8 Packet Layout

<table><tr><td></td><td>L0</td><td>L1</td><td>L2</td><td>L3</td><td>L4</td><td>L5</td><td>L6</td><td>L7</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>ProtID[7:0]</td><td>ProtID[15:8]</td><td>Flit[7:0]</td><td>Flit[15:8]</td><td>Flit[23:16]</td><td>Flit[31:24]</td><td>Flit[39:32]</td><td>Flit[47:40]</td></tr><tr><td>Symbol1</td><td>Flit[55:48]</td><td>Flit[63:56]</td><td>Flit[71:64]</td><td>Flit[79:72]</td><td>Flit[87:80]</td><td>Flit[95:88]</td><td>Flit[103:96]</td><td>Flit[111:104]</td></tr><tr><td>Symbol2</td><td>Flit[119:112]</td><td>Flit[127:120]</td><td>Flit[135:128]</td><td>Flit[143:136]</td><td>Flit[151:144]</td><td>Flit[159:152]</td><td>Flit[167:160]</td><td>Flit[175:168]</td></tr><tr><td>Symbol3</td><td>Flit[183:176]</td><td>Flit[191:184]</td><td>Flit[199:192]</td><td>Flit[207:200]</td><td>Flit[215:208]</td><td>Flit[223:216]</td><td>Flit[231:224]</td><td>Flit[239:232]</td></tr><tr><td>Symbol4</td><td>Flit[247:240]</td><td>Flit[255:248]</td><td>Flit[263:256]</td><td>Flit[271:264]</td><td>Flit[279:272]</td><td>Flit[287:280]</td><td>Flit[295:288]</td><td>Flit[303:296]</td></tr><tr><td>Symbol5</td><td>Flit[311:304]</td><td>Flit[319:312]</td><td>Flit[327:320]</td><td>Flit[335:328]</td><td>Flit[343:336]</td><td>Flit[351:344]</td><td>Flit[359:352]</td><td>Flit[367:360]</td></tr><tr><td>Symbol6</td><td>Flit[375:368]</td><td>Flit[383:376]</td><td>Flit[391:384]</td><td>Flit[399:392]</td><td>Flit[407:400]</td><td>Flit[415:408]</td><td>Flit[423:416]</td><td>Flit[431:424]</td></tr><tr><td>Symbol7</td><td>Flit[439:432]</td><td>Flit[447:440]</td><td>Flit[455:448]</td><td>Flit[463:456]</td><td>Flit[471:464]</td><td>Flit[479:472]</td><td>Flit[487:480]</td><td>Flit[495:488]</td></tr><tr><td>Symbol8</td><td>Flit[503:496]</td><td>Flit[511:504]</td><td>Flit[519:512]</td><td>Flit[527:520]</td><td>ProtID[7:0]</td><td>ProtID[15:8]</td><td>Flit[7:0]</td><td>Flit[15:8]</td></tr><tr><td>Symbol9</td><td>Flit[23:16]</td><td>Flit[31:24]</td><td>Flit[39:32]</td><td>Flit[47:40]</td><td>Flit[55:48]</td><td>Flit[63:56]</td><td>Flit[71:64]</td><td>Flit[79:72]</td></tr><tr><td>Symbol10</td><td>Flit[87:80]</td><td>Flit[95:88]</td><td>Flit[103:96]</td><td>Flit[111:104]</td><td>Flit[119:112]</td><td>Flit[127:120]</td><td>Flit[135:128]</td><td>Flit[143:136]</td></tr><tr><td>Symbol11</td><td>Flit[151:144]</td><td>Flit[159:152]</td><td>Flit[167:160]</td><td>Flit[175:168]</td><td>Flit[183:176]</td><td>Flit[191:184]</td><td>Flit[199:192]</td><td>Flit[207:200]</td></tr><tr><td>Symbol12</td><td>Flit[215:208]</td><td>Flit[223:216]</td><td>Flit[231:224]</td><td>Flit[239:232]</td><td>Flit[247:240]</td><td>Flit[255:248]</td><td>Flit[263:256]</td><td>Flit[271:264]</td></tr><tr><td>Symbol13</td><td>Flit[279:272]</td><td>Flit[287:280]</td><td>Flit[295:288]</td><td>Flit[303:296]</td><td>Flit[311:304]</td><td>Flit[319:312]</td><td>Flit[327:320]</td><td>Flit[335:328]</td></tr><tr><td>Symbol14</td><td>Flit[343:336]</td><td>Flit[351:344]</td><td>Flit[359:352]</td><td>Flit[367:360]</td><td>Flit[375:368]</td><td>Flit[383:376]</td><td>Flit[391:384]</td><td>Flit[399:392]</td></tr><tr><td>Symbol15</td><td>Flit[407:400]</td><td>Flit[415:408]</td><td>Flit[423:416]</td><td>Flit[431:424]</td><td>Flit[439:432]</td><td>Flit[447:440]</td><td>Flit[455:448]</td><td>Flit[463:456]</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>Flit[471:464]</td><td>Flit[479:472]</td><td>Flit[487:480]</td><td>Flit[495:488]</td><td>Flit[503:496]</td><td>Flit[511:504]</td><td>Flit[519:512]</td><td>Flit[527:520]</td></tr><tr><td>Symbol1</td><td>ProtID[7:0]</td><td>ProtID[15:8]</td><td>Flit[7:0]</td><td>Flit[15:8]</td><td>Flit[23:16]</td><td>Flit[31:24]</td><td>Flit[39:32]</td><td>Flit[47:40]</td></tr></table>

Figure 6-5 illustrates how CXL.io and CXL.cachemem traffic is interleaved on a x8 Flex Bus link. The same traffic from the x16 example in Figure 6-3 is mapped to a x8 link.

Figure 6-5. Flex Bus x8 Protocol Interleaving Example

<table><tr><td></td><td>L0</td><td>L1</td><td>L2</td><td>L3</td><td>L4</td><td>L5</td><td>L6</td><td>L7</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>ProtID[7:0]=CXL.io</td><td>ProtID[15:8]=CXL.io</td><td colspan="4">PCIe STPToken</td><td colspan="2">PCIe TLP Header DW0[15:0]</td></tr><tr><td>Symbol1</td><td colspan="2">PCIe TLP Header DW0[31:16]</td><td colspan="4">PCIe TLP Header DW1</td><td colspan="2">PCIe TLP Header DW2[15:0]</td></tr><tr><td>Symbol2</td><td colspan="2">PCIe TLP Header DW2[31:16]</td><td colspan="4">PCIe TLP Data Payload DW0</td><td colspan="2">PCIe TLP Data Payload DW1[15:0]</td></tr><tr><td>Symbol3</td><td colspan="2">PCIe TLP Data Payload DW1[31:16]</td><td colspan="4">PCIe TLP Data Payload DW2</td><td colspan="2">PCIe TLP LCRC</td></tr><tr><td>Symbol4</td><td colspan="2">PCIe TLP LCRC</td><td colspan="2">PCIe SDP Token</td><td colspan="4">PCIe DLLP Payload</td></tr><tr><td>Symbol5</td><td colspan="2">PCIe DLLP CRC</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td></tr><tr><td>Symbol6</td><td>PCIe IDL</td><td>PCIe IDL</td><td colspan="4">PCIe STPToken</td><td colspan="2">PCIe TLP Header DW0[15:0]</td></tr><tr><td>Symbol7</td><td colspan="2">PCIe TLP Header DW0[31:16]</td><td colspan="4">PCIe TLP Header DW1</td><td colspan="2">PCIe TLP Header DW2[15:0]</td></tr><tr><td>Symbol8</td><td colspan="2">PCIe TLP Header DW2[31:16]</td><td>Reserved</td><td>Reserved</td><td>ProtID[7:0]=CXL.io</td><td>ProtID[15:8]=CXL.io</td><td colspan="2">PCIe TLP Data Payload DW0[15:0]</td></tr><tr><td>Symbol9</td><td colspan="2">PCIe TLP Data Payload DW0[31:16]</td><td colspan="4">PCIe TLP Data Payload DW1</td><td colspan="2">PCIe TLP Data Payload DW2[15:0]</td></tr><tr><td>Symbol10</td><td colspan="2">PCIe TLP Data Payload DW2[31:16]</td><td colspan="4">PCIe TLP Data Payload DW3</td><td colspan="2">PCIe TLP Data Payload DW4[15:0]</td></tr><tr><td>Symbol11</td><td colspan="2">PCIe TLP Data Payload DW4[31:16]</td><td colspan="4">PCIe TLP Data Payload DW5</td><td colspan="2">PCIe TLP Data Payload DW6[15:0]</td></tr><tr><td>Symbol12</td><td colspan="2">PCIe TLP Data Payload DW6[31:16]</td><td colspan="4">PCIe TLP Data Payload DW7</td><td colspan="2">PCIe TLP Data Payload DW8[15:0]</td></tr><tr><td>Symbol13</td><td colspan="2">PCIe TLP Data Payload DW8[31:16]</td><td colspan="4">PCIe TLP LCRC</td><td colspan="2">PCIe SDP Token</td></tr><tr><td>Symbol14</td><td colspan="4">PCIe DLLP Payload</td><td colspan="2">PCIe DLLP CRC</td><td colspan="2">PCIe STPToken[15:0]</td></tr><tr><td>Symbol15</td><td colspan="2">PCIe STPToken[31:16]</td><td colspan="4">PCIe TLP Header DW0</td><td colspan="2">PCIe TLP Header DW1[15:0]</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td colspan="2">PCIe TLP Header DW1[31:16]</td><td colspan="4">PCIe TLP Header DW2</td><td>Reserved</td><td>Reserved</td></tr><tr><td>Symbol1</td><td>ProtID[7:0]=CXL.camem</td><td>ProtID[15:8]=CXL.camem</td><td>Flit[7:0]</td><td>Flit[15:8]</td><td>Flit[23:16]</td><td>Flit[31:24]</td><td>Flit[39:32]</td><td>Flit[47:40]</td></tr><tr><td>Symbol2</td><td>Flit[55:48]</td><td>Flit[63:56]</td><td>Flit[71:64]</td><td>Flit[79:72]</td><td>Flit[87:80]</td><td>Flit[95:88]</td><td>Flit[103:96]</td><td>Flit[111:104]</td></tr><tr><td>Symbol3</td><td>Flit[119:112]</td><td>Flit[127:120]</td><td>Flit[135:128]</td><td>Flit[143:136]</td><td>Flit[151:144]</td><td>Flit[159:152]</td><td>Flit[167:160]</td><td>Flit[175:168]</td></tr><tr><td>Symbol4</td><td>Flit[183:176]</td><td>Flit[191:184]</td><td>Flit[199:192]</td><td>Flit[207:200]</td><td>Flit[215:208]</td><td>Flit[223:216]</td><td>Flit[231:224]</td><td>Flit[239:232]</td></tr><tr><td>Symbol5</td><td>Flit[247:240]</td><td>Flit[255:248]</td><td>Flit[263:256]</td><td>Flit[271:264]</td><td>Flit[279:272]</td><td>Flit[287:280]</td><td>Flit[295:288]</td><td>Flit[303:296]</td></tr><tr><td>Symbol6</td><td>Flit[311:304]</td><td>Flit[319:312]</td><td>Flit[327:320]</td><td>Flit[335:328]</td><td>Flit[343:336]</td><td>Flit[351:344]</td><td>Flit[359:352]</td><td>Flit[367:360]</td></tr><tr><td>Symbol7</td><td>Flit[375:368]</td><td>Flit[383:376]</td><td>Flit[391:384]</td><td>Flit[399:392]</td><td>Flit[407:400]</td><td>Flit[415:408]</td><td>Flit[423:416]</td><td>Flit[431:424]</td></tr><tr><td>Symbol8</td><td>Flit[439:432]</td><td>Flit[447:440]</td><td>Flit[455:448]</td><td>Flit[463:456]</td><td>Flit[471:464]</td><td>Flit[479:472]</td><td>Flit[487:480]</td><td>Flit[495:488]</td></tr><tr><td>Symbol9</td><td>Flit[503:496]</td><td>Flit[511:504]</td><td>CRC</td><td>CRC</td><td>ProtID[7:0]=CXL.camem</td><td>ProtID[15:8]=CXL.camem</td><td>Flit[7:0]</td><td>Flit[15:8]</td></tr><tr><td>Symbol10</td><td>Flit[23:16]</td><td>Flit[31:24]</td><td>Flit[39:32]</td><td>Flit[47:40]</td><td>Flit[55:48]</td><td>Flit[63:56]</td><td>Flit[71:64]</td><td>Flit[79:72]</td></tr><tr><td>Symbol11</td><td>Flit[87:80]</td><td>Flit[95:88]</td><td>Flit[103:96]</td><td>Flit[111:104]</td><td>Flit[119:112]</td><td>Flit[127:120]</td><td>Flit[135:128]</td><td>Flit[143:136]</td></tr><tr><td>Symbol12</td><td>Flit[151:144]</td><td>Flit[159:152]</td><td>Flit[167:160]</td><td>Flit[175:168]</td><td>Flit[183:176]</td><td>Flit[191:184]</td><td>Flit[199:192]</td><td>Flit[207:200]</td></tr><tr><td>Symbol13</td><td>Flit[215:208]</td><td>Flit[223:216]</td><td>Flit[231:224]</td><td>Flit[239:232]</td><td>Flit[247:240]</td><td>Flit[255:248]</td><td>Flit[263:256]</td><td>Flit[271:264]</td></tr><tr><td>Symbol14</td><td>Flit[279:272]</td><td>Flit[287:280]</td><td>Flit[295:288]</td><td>Flit[303:296]</td><td>Flit[311:304]</td><td>Flit[319:312]</td><td>Flit[327:320]</td><td>Flit[335:328]</td></tr><tr><td>Symbol15</td><td>Flit[343:336]</td><td>Flit[351:344]</td><td>Flit[359:352]</td><td>Flit[367:360]</td><td>Flit[375:368]</td><td>Flit[383:376]</td><td>Flit[391:384]</td><td>Flit[399:392]</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>Flit[407:400]</td><td>Flit[415:408]</td><td>Flit[423:416]</td><td>Flit[431:424]</td><td>Flit[439:432]</td><td>Flit[447:440]</td><td>Flit[455:448]</td><td>Flit[463:456]</td></tr><tr><td>Symbol1</td><td>Flit[471:464]</td><td>Flit[479:472]</td><td>Flit[487:480]</td><td>Flit[495:488]</td><td>Flit[503:496]</td><td>Flit[511:504]</td><td>CRC</td><td>CRC</td></tr><tr><td>Symbol2</td><td>ProtID[7:0]=CXL.io</td><td>ProtID[15:8]=CXL.io</td><td colspan="4">PCIe TLP Data Payload DW0</td><td colspan="2">PCIe TLP Data Payload DW1[15:0]</td></tr><tr><td>Symbol3</td><td colspan="2">PCIe TLP Data Payload DW1[31:16]</td><td colspan="4">PCIe TLP Data Payload DW2</td><td colspan="2">PCIe TLP LCRC[15:0]</td></tr></table>

## 6.2.2.4 x4 Packet Layout

Figure 6-6 shows the x4 packet layout. 16 bits of Protocol ID followed by a 528-bit flit are striped across the lanes on an 8-bit granularity. The Protocol ID plus flit transfer always starts on Lane 0; the entire transfer takes 17 symbol times. The two-bit Sync Header shown in the figure is not present for Latency-optimized Sync Header Bypass mode.

Figure 6-6. Flex Bus x4 Packet Layout

<table><tr><td></td><td>L0</td><td>L1</td><td>L2</td><td>L3</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>ProtID[7:0]</td><td>ProtID[15:8]</td><td>Flit[7:0]</td><td>Flit[15:8]</td></tr><tr><td>Symbol1</td><td>Flit[23:16]</td><td>Flit[31:24]</td><td>Flit[39:32]</td><td>Flit[47:40]</td></tr><tr><td>Symbol2</td><td>Flit[55:48]</td><td>Flit[63:56]</td><td>Flit[71:64]</td><td>Flit[79:72]</td></tr><tr><td>Symbol3</td><td>Flit[87:80]</td><td>Flit[95:88]</td><td>Flit[103:96]</td><td>Flit[111:104]</td></tr><tr><td>Symbol4</td><td>Flit[119:112]</td><td>Flit[127:120]</td><td>Flit[135:128]</td><td>Flit[143:136]</td></tr><tr><td>Symbol5</td><td>Flit[151:144]</td><td>Flit[159:152]</td><td>Flit[167:160]</td><td>Flit[175:168]</td></tr><tr><td>Symbol6</td><td>Flit[183:176]</td><td>Flit[191:184]</td><td>Flit[199:192]</td><td>Flit[207:200]</td></tr><tr><td>Symbol7</td><td>Flit[215:208]</td><td>Flit[223:216]</td><td>Flit[231:224]</td><td>Flit[239:232]</td></tr><tr><td>Symbol8</td><td>Flit[247:240]</td><td>Flit[255:248]</td><td>Flit[263:256]</td><td>Flit[271:264]</td></tr><tr><td>Symbol9</td><td>Flit[279:272]</td><td>Flit[287:280]</td><td>Flit[295:288]</td><td>Flit[303:296]</td></tr><tr><td>Symbol 10</td><td>Flit[311:304]</td><td>Flit[319:312]</td><td>Flit[327:320]</td><td>Flit[335:328]</td></tr><tr><td>Symbol 11</td><td>Flit[343:336]</td><td>Flit[351:344]</td><td>Flit[359:352]</td><td>Flit[367:360]</td></tr><tr><td>Symbol 12</td><td>Flit[375:368]</td><td>Flit[383:376]</td><td>Flit[391:384]</td><td>Flit[399:392]</td></tr><tr><td>Symbol 13</td><td>Flit[407:400]</td><td>Flit[415:408]</td><td>Flit[423:416]</td><td>Flit[431:424]</td></tr><tr><td>Symbol 14</td><td>Flit[439:432]</td><td>Flit[447:440]</td><td>Flit[455:448]</td><td>Flit[463:456]</td></tr><tr><td>Symbol 15</td><td>Flit[471:464]</td><td>Flit[479:472]</td><td>Flit[487:480]</td><td>Flit[495:488]</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>Flit[503:496]</td><td>Flit[511:504]</td><td>Flit[519:512]</td><td>Flit[527:520]</td></tr><tr><td>Symbol1</td><td>ProtID[7:0]</td><td>ProtID[15:8]</td><td>Flit[7:0]</td><td>Flit[15:8]</td></tr></table>

## 6.2.2.5 x2 Packet Layout

The x2 packet layout looks similar to the x4 packet layout in that the Protocol ID aligns to Lane 0. 16 bits of Protocol ID followed by a 528-bit flit are striped across two lanes on an 8-bit granularity, taking 34 symbol times to complete the transfer.

## 6.2.2.6 x1 Packet Layout

The x1 packet layout is used only in degraded mode. The 16 bits of Protocol ID followed by 528-bit flit are transferred on a single lane, taking 68 symbol times to complete the transfer.

## 6.2.2.7 Special Case: CXL.io — When a TLP Ends on a Flit Boundary

For CXL.io traffic, if a TLP ends on a flit boundary and there is no additional CXL.io traffic to send, the receiver still requires a subsequent EDB indication if it is a nullified TLP or all IDLE flit or a DLLP to confirm it is a good TLP before processing the TLP. Figure 6-7 illustrates a scenario where the first CXL.io flit encapsulates a TLP that ends at the flit boundary, and the transmitter has no more TLPs or DLLPs to send. To ensure that the transmitted TLP that ended on the flit boundary is processed by the receiver, a subsequent CXL.io flit containing PCIe IDLE tokens is transmitted. The Link Layer generates the subsequent CXL.io flit.

Figure 6-7. CXL.io TLP Ending on Flit Boundary Example

<table><tr><td></td><td>L0</td><td>L1</td><td>L2</td><td>L3</td><td>L4</td><td>L5</td><td>L6</td><td>L7</td><td>L8</td><td>L9</td><td>L10</td><td>L11</td><td>L12</td><td>L13</td><td>L14</td><td>L15</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>ProtID(7.0)=CXLio</td><td>ProtID[15.8]=CXLio</td><td colspan="4">PCIe STP Token</td><td colspan="4">PCIe TLP Header DW0</td><td colspan="4">PCIe TLP Header DW1</td><td colspan="2">PCIe TLP Header DW2[15.0]</td></tr><tr><td>Symbol1</td><td colspan="2">PCIe TLP Header DW2[31:16]</td><td colspan="4">PCIe TLP Data Payload DW0</td><td colspan="4">PCIe TLP Data Payload DW1</td><td colspan="4">PCIe TLP Data Payload DW2</td><td colspan="2">PCIe TLP Data Payload DW3[31:16]</td></tr><tr><td>Symbol2</td><td colspan="2">PCIe TLP Data Payload DW3[31:16]</td><td colspan="4">PCIe TLP Data Payload DW4</td><td colspan="4">PCIe TLP Data Payload DW5</td><td colspan="4">PCIe TLP Data Payload DW6</td><td colspan="2">PCIe TLP Header DW7[15.0]</td></tr><tr><td>Symbol3</td><td colspan="2">PCIe TLP Header DW7[31:16]</td><td colspan="4">PCIe TLP Data Payload DW8</td><td colspan="4">PCIe TLP Data Payload DW9</td><td colspan="4">PCIe TLP Data Payload DW10</td><td colspan="2">PCIe TLP LCRC[15:0]</td></tr><tr><td>Symbol4</td><td colspan="2">PCIe TLP LCRC[31:16]</td><td>Reserved</td><td>Reserved</td><td>ProtID[7.0]=CXLio</td><td>ProtID[15.8]=CXLio</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td></tr><tr><td>Symbol5</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td></tr><tr><td>Symbol6</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td></tr><tr><td>Symbol7</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td></tr><tr><td>Symbol8</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>PCIe IDL</td><td>Reserved</td><td>Reserved</td><td>ProtID[7.0]=CXL camem</td><td>ProtID[15.8]=CXL camem</td><td>Flit[7:0]</td><td>Flit[15:8]</td><td>Flit[23:16]</td><td>Flit[31:24]</td><td>Flit[39:32]</td><td>Flit[47:40]</td></tr><tr><td>Symbol9</td><td>Flit[55:48]</td><td>Flit[63:56]</td><td>Flit[71:64]</td><td>Flit[79:72]</td><td>Flit[87:80]</td><td>Flit[95:88]</td><td>Flit[103:96]</td><td>Flit[111:104]</td><td>Flit[119:112]</td><td>Flit[127:120]</td><td>Flit[135:128]</td><td>Flit[143:136]</td><td>Flit[151:144]</td><td>Flit[159:152]</td><td>Flit[167:160]</td><td>Flit[175:168]</td></tr><tr><td>Symbol10</td><td>Flit[183:176]</td><td>Flit[191:184]</td><td>Flit[199:192]</td><td>Flit[207:200]</td><td>Flit[215:208]</td><td>Flit[223:216]</td><td>Flit[231:224]</td><td>Flit[239:232]</td><td>Flit[247:240]</td><td>Flit[255:248]</td><td>Flit[263:256]</td><td>Flit[271:264]</td><td>Flit[279:272]</td><td>Flit[287:280]</td><td>Flit[295:288]</td><td>Flit[303:296]</td></tr><tr><td>Symbol11</td><td>Flit[311:304]</td><td>Flit[319:312]</td><td>Flit[327:320]</td><td>Flit[335:328]</td><td>Flit[343:336]</td><td>Flit[351:344]</td><td>Flit[359:352]</td><td>Flit[367:360]</td><td>Flit[375:368]</td><td>Flit[383:376]</td><td>Flit[391:384]</td><td>Flit[399:392]</td><td>Flit[407:400]</td><td>Flit[415:408]</td><td>Flit[423:416]</td><td>Flit[431:424]</td></tr><tr><td>Symbol12</td><td>Flit[439:432]</td><td>Flit[447:440]</td><td>Flit[455:448]</td><td>Flit[463:456]</td><td>Flit[471:464]</td><td>Flit[479:472]</td><td>Flit[487:480]</td><td>Flit[495:488]</td><td>Flit[503:496]</td><td>Flit[511:504]</td><td>CRC</td><td>CRC</td><td>ProtID[7.0]=CXL camem</td><td>ProtID[15.8]=CXL camem</td><td>Flit[7.0]</td><td>Flit[15:8]</td></tr><tr><td>Symbol13</td><td>Flit[23:16]</td><td>Flit[31:24]</td><td>Flit[39:32]</td><td>Flit[47:40]</td><td>Flit[55:48]</td><td>Flit[63:56]</td><td>Flit[71:64]</td><td>Flit[79:72]</td><td>Flit[87:80]</td><td>Flit[95:88]</td><td>Flit[103:96]</td><td>Flit[111:104]</td><td>Flit[119:112]</td><td>Flit[ 127:120]</td><td>Flit[135:128]</td><td>Flit[143:136]</td></tr><tr><td>Symbol14</td><td>Flit[151:144]</td><td>Flit[159:152]</td><td>Flit[167:160]</td><td>Flit[175:168]</td><td>Flit[183:176]</td><td>Flit[191:184]</td><td>Flit[199:192]</td><td>Flit[207:200]</td><td>Flit[215:208]</td><td>Flit[223:216]</td><td>Flit[231:224]</td><td>Flit[239:232]</td><td>Flit247:240]</td><td>Flit[255:248]</td><td>Flit[263:256]</td><td>Flit[271:264]</td></tr><tr><td>Symbol15</td><td>Flit[279:272]</td><td>Flit[287:280]</td><td>Flit[295:288]</td><td>Flit[303:296]</td><td>Flit[311:304]</td><td>Flit[319:312]</td><td>Flit[327:320]</td><td>Flit[335:328]</td><td>Flit[343:336]</td><td>Flit[351:344]</td><td>Flit[359:352]</td><td>Flit[367:360]</td><td>Flit375:368]</td><td>Flit[383:376]</td><td>Flit[391:384]</td><td>Flit[399:392]</td></tr><tr><td rowspan="2">Sync Hdr</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Symbol0</td><td>Flit[407:400]</td><td>Flit[415:408]</td><td>Flit[423:416]</td><td>Flit[431:424]</td><td>Flit[439:432]</td><td>Flit[447:440]</td><td>Flit[455:448]</td><td>Flit[463:456]</td><td>Flit[471:464]</td><td>Flit[479:472]</td><td>Flit[487:480]</td><td>Flit[495:488]</td><td>Flit [503:496]</td><td>Flit[511:504]</td><td>CRC</td><td>CRC</td></tr></table>

## 6.2.2.8 Framing Errors

The physical layer is responsible for detecting framing errors and, subsequently, for initiating entry into recovery to retrain the link.

The following are framing errors detected by the physical layer:

• Sync Header errors

• Protocol ID framing errors

• EDS insertion errors

• PCIe framing errors located within the 528-bit CXL.io flit

Protocol ID framing errors are described in Section 6.2.2 and summarized in Table 6-3. A Protocol ID with a value that is defined in the CXL specification is considered a valid Protocol ID. A valid Protocol ID is either expected or unexpected. An expected Protocol ID is one that corresponds to a protocol that was enabled during negotiation. An unexpected Protocol ID is one that corresponds to a protocol that was not enabled during negotiation. A Protocol ID with a value that is not defined in the CXL specification is considered an invalid Protocol ID. Whenever a flit is dropped by the physical layer due to either an Unexpected Protocol ID Framing Error or an

Uncorrectable Protocol ID Framing Error, the physical layer enters LTSSM recovery to retrain the link and notifies the link layers to enter recovery and, if applicable, to initiate link level retry.

Table 6-3.

Protocol ID Framing Errors

<table><tr><td>Protocol ID[7:0]</td><td>Protocol ID[15:8]</td><td>Expected Action</td></tr><tr><td>Invalid</td><td>Valid &amp; Expected</td><td>Process normally using Protocol ID[15:8];Log as CXL_Correctable_Protocol_ID_Framing_Error in DVSEC Flex Bus Port Status register.</td></tr><tr><td>Valid &amp; Expected</td><td>Invalid</td><td>Process normally using Protocol ID[7:0];Log as CXL_Correctable_Protocol_ID_Framing_Error in DVSEC Flex Bus Port Status register.</td></tr><tr><td>Valid &amp; Unexpected</td><td>Valid &amp; Unexpected &amp; Equal to Protocol ID[7:0]</td><td>Drop flit and log asCXL_Unexpected_Protocol_ID_Dropped in DVSEC Flex Bus Port Status register; enter LTSSM recovery to retrain the link; notify link layers to enter recovery and, if applicable, initiate link level retry</td></tr><tr><td>Invalid</td><td>Valid &amp; Unexpected</td><td>Drop flit and log asCXL_Unexpected_Protocol_ID_Dropped in DVSEC Flex Bus Port Status register; enter LTSSM recovery to retrain the link; notify link layers to enter recovery and, if applicable, initiate link level retry</td></tr><tr><td>Valid &amp; Unexpected</td><td>Invalid</td><td>Drop flit and log asCXL_Unexpected_Protocol_ID_Dropped in DVSEC Flex Bus Port Status register; enter LTSSM recovery to retrain the link; notify link layers to enter recovery and, if applicable, initiate link level retry</td></tr><tr><td>Valid</td><td>Valid &amp; Not Equal to Protocol ID[7:0]</td><td>Drop flit and log asCXL_Uncorrectable_Protocol_ID_Framing_Error in DVSEC Flex Bus Port Status register; enter LTSSM recovery to retrain the link; notify link layers to enter recovery and, if applicable, initiate link level retry</td></tr><tr><td>Invalid</td><td>Invalid</td><td>Drop flit and log asCXL_Uncorrectable_Protocol_ID_Framing_Error in DVSEC Flex Bus Port Status register; enter LTSSM recovery to retrain the link; notify link layers to enter recovery and, if applicable, initiate link level retry</td></tr></table>

## 6.2.3 256B Flit Mode

256B Flit mode operation relies on support of PCIe Base Specification. Selection of 68B Flit mode or 256B Flit mode occurs during PCIe link training. Table 6-4 specifies the scenarios in which the link operates in 68B Flit mode and 256B Flit mode. CXL mode is supported at PCIe link rates of 8 GT/s or higher; CXL mode is not supported at 2.5 GT/ s or 5 GT/s link rates, regardless of whether PCIe Flit mode is negotiated. If PCIe Flit mode is selected during training, as described in PCIe Base Specification, and the link speed is 8 GT/s or higher, 256B Flit mode is used. If PCIe Flit mode is not selected during training and the link speed is 8 GT/s or higher, 68B Flit mode is used.

256B Flit Mode vs. 68B Flit Mode Operation

<table><tr><td>Data Rate</td><td>PCIe Flit Mode</td><td>Encoding</td><td>CXL Flit Mode</td></tr><tr><td>2.5 GT/s, 5 GT/s</td><td>No</td><td>8b/10b</td><td>CXL is not supported</td></tr><tr><td>2.5 GT/s, 5 GT/s</td><td>Yes</td><td>8b/10b</td><td>CXL is not supported</td></tr><tr><td>8 GT/s, 16 GT/s, 32 GT/s</td><td>No</td><td>128b/130b</td><td>68B flits</td></tr><tr><td>8 GT/s, 16 GT/s, 32 GT/s</td><td>Yes</td><td>128b/130b</td><td>256B flits</td></tr><tr><td>64 GT/s</td><td>Yes</td><td>1b/1b</td><td>256B flits</td></tr></table>

## 6.2.3.1 256B Flit Format

The 256B flit leverages several elements from the PCIe flit. There are two variants of the 256B flit:

• Standard 256B flit

• Latency-optimized 256B flit with 128-byte flit halves

## 6.2.3.1.1 Standard 256B Flit

The standard 256B flit format is shown in Figure 6-8. The 256-byte flit includes 2 bytes of Flit Header information as specified in Table 6-5. There are 240 bytes of Flit Data, for which the format differs depending on whether the flit carries CXL.io payload, CXL.cachemem payload, or ALMP payload, or whether an IDLE flit is being transmitted. For CXL.io, the Flit Data includes TLP payload and a 4-byte DLLP payload as specified in PCIe Base Specification; the DLLP payload is located at the end of the Flit Data as shown in Figure 6-9. For CXL.cachemem, the Flit Data format is specified in Chapter 4.0. The 8 bytes of CRC protects the Flit Header and Flit Data and is calculated as specified in PCIe Base Specification. The 6 bytes of FEC protects the Flit Header, Flit Data, and CRC, and is calculated as specified in PCIe Base Specification. The application of flit bits to the PCIe physical lanes is shown in Figure 6-10.

Figure 6-8. Standard 256B Flit

<table><tr><td>FlitHdr (2 bytes)</td><td colspan="3">FlitData (126 bytes)</td></tr><tr><td colspan="2">FlitData (114 bytes)</td><td>CRC (8 bytes)</td><td>FEC (6 bytes)</td></tr></table>

Figure 6-9. CXL.io Standard 256B Flit

<table><tr><td>FlitHdr (2 bytes)</td><td colspan="4">FlitData (126 bytes)</td></tr><tr><td colspan="2">FlitData (110 bytes)</td><td>DLLP (4 bytes)</td><td>CRC (8 bytes)</td><td>FEC (6 bytes)</td></tr></table>

The 2 bytes of Flit Header as defined in Table 6-5 are transmitted as the first two bytes of the flit. The 2-bit Flit Type field indicates whether the flit carries CXL.io traffic, CXL.cachemem traffic, ALMPs, IDLE flits, Empty flits, or NOP flits. Please refer to Section 6.2.3.1.1.1 for more details. The Prior Flit Type definition is as defined in PCIe Base Specification; it enables the receiver to know that the prior flit was an NOP flit or IDLE flit, and thus does not require replay (i.e., can be discarded) if it has a CRC error. The Type of DLLP Payload definition is as defined in PCIe Base Specification for CXL.io flits; otherwise, this bit is reserved. The Replay Command[1:0] and Flit Sequence Number[9:0] definitions are as defined in PCIe Base Specification.

Table 6-5. 256B Flit Header

<table><tr><td>Flit Header Field</td><td>Flit Header Bit Location</td><td>Description</td></tr><tr><td>Flit Type[1:0]</td><td>[7:6]</td><td>00b = Physical Layer IDLE flit or Physical Layer NOP flit or CXL.io NOP flit01b = CXL.io Payload flit10b = CXL.cachemem Payload flit or CXL.cachemem-generated Empty flit11b = ALMPPlease refer toTable 6-6for more details.</td></tr><tr><td>Prior Flit Type</td><td>[5]</td><td>0 = Prior flit was a NOP or IDLE flit (not allocated into Replay buffer)1 = Prior flit was a Payload flit or Empty flit (allocated into Replay buffer)</td></tr><tr><td>Type of DLLP Payload</td><td>[4]</td><td>If (Flit Type = (CXL.io Payload or CXL.io NOP): Use as defined in PCIe Base SpecificationIf (Flit Type != (CXL.io Payload or CXL.io NOP)): Reserved</td></tr><tr><td>Replay Command[1:0]</td><td>[3:2]</td><td>Same as defined in PCIe Base Specification.</td></tr><tr><td>Flit Sequence Number[9:0]</td><td>{[1:0], [15:8]}</td><td>10-bit Sequence Number as defined in PCIe Base Specification.</td></tr></table>

## 6.2.3.1.1.1 256B Flit Type

Table 6-6 specifies the different flit payloads that are associated with each Flit Type encoding.

Table 6-6. Flit Type[1:0]

<table><tr><td>Encoding</td><td>Flit Payload</td><td>Source</td><td>Description</td><td>Allocated to Retry Buffer?</td></tr><tr><td rowspan="3">00b</td><td>Physical Layer NOP</td><td rowspan="2">Physical Layer</td><td>Physical Layer generated (and sunk) flit with no valid payload; inserted in the data stream when its Tx retry buffer is full and it is backpressuring the upper layer or when no other flits from upper layers are available to transmit.</td><td>No</td></tr><tr><td>IDLE</td><td>Physical Layer generated (and consumed) all 0s payload flit used to facilitate LTSSM transitions as described in PCIe Base Specification.</td><td>No</td></tr><tr><td>CXL.io NOP</td><td rowspan="2">CXL.io Link Layer</td><td>Valid CXL.io DLLP payload (no TLP payload); periodically inserted by the CXL.io link layer to satisfy the PCIe Base Specification requirement for a credit update interval if no other CXL.io flits are available to transmit.</td><td>No</td></tr><tr><td>01b</td><td>CXL.io Payload</td><td>Valid CXL.io TLP and valid DLLP payload.</td><td>Yes</td></tr><tr><td rowspan="2">10b</td><td>CXL.cachemem Payload</td><td rowspan="2">CXL.cachemem Link Layer</td><td>Valid CXL.cachemem slot and/or CXL.cachemem credit payload.</td><td>Yes</td></tr><tr><td>CXL.cachemem Empty</td><td>No valid CXL.cachemem payload; generated when CXL.cachemem link layer speculatively arbitrates to transfer a flit to reduce idle to valid transition time but no valid CXL.cachemem payload arrives in time to use any slots in the flit.</td><td>Yes, allocate only to the Tx Retry Buffer</td></tr><tr><td>11b</td><td>ALMP</td><td>ARB/MUX</td><td>ARB/MUX Link Management Packet.</td><td>Yes</td></tr></table>

Prior to the Sequence Number Handshake upon each entry to L0, as described in PCIe Base Specification, a Flit Type encoding of 00b indicates an IDLE flit. These IDLE flits contain all zeros payload and are generated and consumed by the Physical Layer.

During and after the Sequence Number Handshake in L0, a Flit Type encoding of 00b indicates either a Physical Layer NOP flit or a CXL.io NOP flit. The Physical Layer must insert NOP flits when it backpressures the upper layers due to its Tx retry buffer filling up; it is also required to insert NOP flits when traffic is not generated by the upper layers. These NOP flits must not be allocated into the transmit retry buffer or receive retry buffer. Physical Layer NOP flits carry 0s in the bit positions that correspond to the bit positions in CXL.io flits that are used to carry DLLP payload; the remaining bits in Physical Layer NOP flits are reserved.

CXL.io NOP flits are generated by the CXL.io Link Layer and carry only valid DLLP payload. When a Flit Type of 00b is decoded, the Physical Layer must always check for valid DLLP payload. CXL.io NOP flits must not be allocated into the transmit retry buffer or into the receive retry buffer.

A Flit Type encoding of 01b indicates CXL.io Payload traffic; these flits can encapsulate both valid TLP payload and valid DLLP payload.

A Flit Type encoding of 10b indicates either a flit with valid CXL.cachemem Payload flit or a CXL.cachemem Empty flit; this enables CXL.cachemem to minimize idle to valid traffic transitions by arbitrating for use of the ARB/MUX transmit data path even while it does not have valid traffic to send so that it can potentially fill later slots in the flit with late arriving traffic, instead of requiring CXL.cachemem to wait until the next 256-byte flit boundary to begin transmitting valid traffic. CXL.cachemem Empty flits are retryable and must be allocated in the transmit retry buffer. The Physical Layer must decode the Link Layer CRD[4:0] bits to determine whether the flit carries valid payload or whether the flit is an empty CXL.cachemem Empty flit. See Table 4-19 in Chapter 4.0 for more details.

A Flit Type encoding of 11b indicates an ALMP.

Figure 6-10 shows how the flit is mapped to the physical lanes on the link. The flit is striped across the lanes on an 8-bit granularity starting with 16-bit Flit Header, followed by the 240 bytes of Flit Data, the 8-byte CRC, and finally the 6-byte FEC (3-way interleaved ECC described in PCIe Base Specification).

Figure 6-10. Standard 256B Flit Applied to Physical Lanes (x16)

<table><tr><td></td><td>L0</td><td>L1</td><td>L2</td><td>L3</td><td>L4</td><td>L5</td><td>L6</td><td>L7</td><td>L8</td><td>L9</td><td>L10</td><td>L11</td><td>L12</td><td>L13</td><td>L14</td><td>L15</td></tr><tr><td>Symbol0</td><td>FltIDhr[7:0]</td><td>FltIDhr[15:8]</td><td>FltID[7:0]</td><td>FltID[15:8]</td><td>FltID[23:16]</td><td>FltID[31:24]</td><td>FltID[39:32]</td><td>FltID[47:40]</td><td>FltID[55:48]</td><td>FltID[63:56]</td><td>FltID[71:64]</td><td>FltID[79:72]</td><td>FltID[87:80]</td><td>FltID[95:88]</td><td>FltID[103:96]</td><td>FltID[111:104]</td></tr><tr><td>Symbol1</td><td>FltID[119:112]</td><td>FltID[127:120]</td><td>FltID[135:128]</td><td>FltID[143:136]</td><td>FltID[151:144]</td><td>FltID[159:152]</td><td>FltID[167:160]</td><td>FltID[175:168]</td><td>FltID[183:176]</td><td>FltID[191:184]</td><td>FltID[199:192]</td><td>FltID[207:200]</td><td>FltID[215:208]</td><td>FltID[223:216]</td><td>FltID[231:224]</td><td>FltID[239:232]</td></tr><tr><td>Symbol2</td><td>FltID[247:240]</td><td>FltID[255:248]</td><td>FltID[263:256]</td><td>FltID[271:264]</td><td>FltID[279:272]</td><td>FltID[287:280]</td><td>FltID[295:288]</td><td>FltID[303:296]</td><td>FltID[311:304]</td><td>FltID[319:312]</td><td>FltID[327:320]</td><td>FltID[335:328]</td><td>FltID[243:336]</td><td>FltID[351:344]</td><td>FltID[359:352]</td><td>FltID[367:360]</td></tr><tr><td>Symbol3</td><td>FltID[375:368]</td><td>FltID[383:376]</td><td>FltID[391:384]</td><td>FltID[399:392]</td><td>FltID[407:400]</td><td>FltID[415:408]</td><td>FltID[423:416]</td><td>FltID[431:424]</td><td>FltID[439:432]</td><td>FltID[447:440]</td><td>FltID[455:448]</td><td>FltID[463:456]</td><td>FltID[471:464]</td><td>FltID[479:472]</td><td>FltID[487:480]</td><td>FltID[495:488]</td></tr><tr><td>Symbol4</td><td>FltID[503:496]</td><td>FltID[511:504]</td><td>FltID[519:512]</td><td>FltID[527:520]</td><td>FltID[535:528]</td><td>FltID[543:536]</td><td>FltID[551:544]</td><td>FltID[559:552]</td><td>FltID[567:560]</td><td>FltID[575:568]</td><td>FltID[583:576]</td><td>FltID[591:584]</td><td>FltID[599:592]</td><td>FltID[607:600]</td><td>FltID[615:608]</td><td>FltID[623:616]</td></tr><tr><td>Symbol5</td><td>FltID[631:624]</td><td>FltID[639:632]</td><td>FltID[647:640]</td><td>FltID[655:648]</td><td>FltID[663:656]</td><td>FltID[671:664]</td><td>FltID[679:672]</td><td>FltID[687:680]</td><td>FltID[695:688]</td><td>FltID[703:696]</td><td>FltID[711:704]</td><td>FltID[719:712]</td><td>FltID[727:720]</td><td>FltID[735:728]</td><td>FltID[743:736]</td><td>FltID[751:744]</td></tr><tr><td>Symbol6</td><td>FltID[759:752]</td><td>FltID[767:760]</td><td>FltID[775:768]</td><td>FltID[783:776]</td><td>FltID[791:784]</td><td>FltID[799:792]</td><td>FltID[807:800]</td><td>FltID[815:808]</td><td>FltID[823:816]</td><td>FltID[831:824]</td><td>FltID[839:832]</td><td>FltID[847:840]</td><td>FltID[855:848]</td><td>FltID[863:856]</td><td>FltID[871:864]</td><td>FltID[879:872]</td></tr><tr><td>Symbol7</td><td>FltID[887:880]</td><td>FltID[895:888]</td><td>FltID[903:896]</td><td>FltID[911:904]</td><td>FltID[919:912]</td><td>FltID[927:920]</td><td>FltID[935:928]</td><td>FltID[943:936]</td><td>FltID[951:944]</td><td>FltID[959:952]</td><td>FltID[967:960]</td><td>FltID[975:968]</td><td>FltID[983:976]</td><td>FltID[991:984]</td><td>FltID[999:992]</td><td>FltID[1007:1000]</td></tr><tr><td>Symbol8</td><td>FltID[1015:1008]</td><td>FltID[1023:1016]</td><td>FltID[1031:1024]</td><td>FltID[1039:1032]</td><td>FltID[1047:1040]</td><td>FltID[1055:1048]</td><td>FltID[1063:1056]</td><td>FltID[1071:1064]</td><td>FltID[1079:1072]</td><td>FltID[1087:1080]</td><td>FltID[1095:1088]</td><td>FltID[1103:1096]</td><td>FltID[1111:1104]</td><td>FltID[1119:1112]</td><td>FltID[1127:1120]</td><td>FltID[1135:1128]</td></tr><tr><td>Symbol9</td><td>FltID[1143:1136]</td><td>FltID[1151:1144]</td><td>FltID[1159:1152]</td><td>FltID[1167:1160]</td><td>FltID[1175:1168]</td><td>FltID[1183:1176]</td><td>FltID[1191:1184]</td><td>FltID[1199:1192]</td><td>FltID[1207:1200]</td><td>FltID[1215:1208]</td><td>FltID[1223:1216]</td><td>FltID[1231:1224]</td><td>FltID[1239:1232]</td><td>FltID[1247:1240]</td><td>FltID[1255:1248]</td><td>FltID[1263:1256]</td></tr><tr><td>Symbol10</td><td>FltID[1271:1264]</td><td>FltID[1279:1272]</td><td>FltID[1287:1280]</td><td>FltID[1295:1288]</td><td>FltID[1303:1296]</td><td>FltID[1311:1304]</td><td>FltID[1319:1312]</td><td>FltID[1327:1320]</td><td>FltID[1335:1328]</td><td>FltID[1343:1336]</td><td>FltID[1351:1344]</td><td>FltID[1359:1352]</td><td>FltID[1367:1360]</td><td>FltID[1375:1368]</td><td>FltID[1383:1376]</td><td>FltID[1391:1384]</td></tr><tr><td>Symbol11</td><td>FltID[1399:1392]</td><td>FltID[1407:1400]</td><td>FltID[1415:1408]</td><td>FltID[1423:1416]</td><td>FltID[1431:1424]</td><td>FltID[1439:1432]</td><td>FltID[1447:1440]</td><td>FltID[1455:1448]</td><td>FltID[1463:1456]</td><td>FltID[1471:1464]</td><td>FltID[1479:1472]</td><td>FltID[1487:1480]</td><td>FltID[1495:1488]</td><td>FltID[1503:1496]</td><td>FltID[1511:1504]</td><td>FltID[1519:1512]</td></tr><tr><td>Symbol12</td><td>FltID[1527:1520]</td><td>FltID[1535:1528]</td><td>FltID[1543:1536]</td><td>FltID[1551:1544]</td><td>FltID[1559:1552]</td><td>FltID[1567:1560]</td><td>FltID[1575:1568]</td><td>FltID[1583:1576]</td><td>FltID[1591:1584]</td><td>FltID[1599:1592]</td><td>FltID[1607:1600]</td><td>FltID[1615:1608]</td><td>FltID[1623:1616]</td><td>FltID[1631:1624]</td><td>FltID[1639:1632]</td><td>FltID[1647:1640]</td></tr><tr><td>Symbol13</td><td>FltID[1655:1648]</td><td>FltID[1663:1656]</td><td>FltID[1671:1664]</td><td>FltID[1679:1672]</td><td>FltID[1687:1680]</td><td>FltID[1695:1688]</td><td>FltID[1703:1696]</td><td>FltID[1711:1704]</td><td>FltID[1719:1712]</td><td>FltID[1727:1720]</td><td>FltID[1735:1728]</td><td>FltID[1743:1736]</td><td>FltID[1751:1744]</td><td>FltID[1759:1752]</td><td>FltID[1767:1760]</td><td>FltID[1775:1768]</td></tr><tr><td>Symbol14</td><td>FltID[1783:1776]</td><td>FltID[1791:1784]</td><td>FltID[1799:1792]</td><td>FltID[1807:1800]</td><td>FltID[1815:1808]</td><td>FltID[1823:1816]</td><td>FltID[1839:1832]</td><td>FltID[1847:1840]</td><td>FltID[1855:1848]</td><td>FltID[1855:1848]</td><td>FltID[1863:1856]</td><td>FltID[1871:1864]</td><td>FltID[1879:1872]</td><td>FltID[1887:1880]</td><td>FltID[1895:1888]</td><td>FltID[1903:1896]</td></tr><tr><td>Symbol15</td><td>FltID[1911:1904]</td><td>FltID[1919:1912]</td><td>CRCO</td><td>CRC1</td><td>CRC2</td><td>CRC3</td><td>CRC4</td><td>CRC5</td><td>CRC6</td><td>CRC7</td><td>ECC 0A</td><td>ECC 0B</td><td>ECC 0C</td><td>ECC 1A</td><td>ECC 1B</td><td>ECC 2B</td></tr></table>

## 6.2.3.1.2 Latency-Optimized 256B Flit with 128-Byte Flit Halves

Figure 6-11 shows the latency-optimized 256B flit format. This latency-optimized flit format is optionally supported by components that support 256B flits. The decision to operate in standard 256B flit format or the latency-optimized 256B flit format occurs once during CXL alternate protocol negotiation; dynamic switching between the two formats is not supported.

Figure 6-11. Latency-Optimized 256B Flit

<table><tr><td>FlitHdr (2 bytes)</td><td colspan="2">FlitData (120 bytes)</td><td>CRC (6 bytes)</td></tr><tr><td colspan="2">FlitData (116 bytes)</td><td>FEC (6 bytes)</td><td>CRC (6 bytes)</td></tr></table>

The latency-optimized flit format organizes the 256-byte flit into 128-byte flit halves. The even flit half consists of the 2-byte Flit Header, 120 bytes of Flit Data, and 6 bytes of CRC that protects the even 128-byte flit half. The odd flit half consists of 116 bytes of Flit Data, 6 bytes of FEC that protects the entire 256 bytes of the flit, and 6 bytes of CRC that protects the 128-byte odd flit half excluding the 6-byte FEC. The benefit of the latency-optimized flit format is reduction of flit accumulation latency. Because each 128-byte flit half is independently protected by CRC, the first half of the flit can be consumed by the receiver if CRC passes without waiting for the second half to be received for FEC decode. The flit accumulation latency savings increases for smaller link widths; for x4 link widths the round trip flit accumulation latency is 8 ns at 64 GT/s link speed. Similarly, the odd flit half can be consumed if CRC passes, without having to wait for the more-complex FEC decode operation to first complete. If CRC fails for either flit half, FEC decode and correct is applied to the entire 256-byte flit. Subsequently, each flit half is consumed if CRC passes, if the flit half was not already previously consumed, and if all data previous to the flit half has been consumed.

## Note:

For CXL.io, due to the potential of a Flit Marker, the last TLP of the first 128-byte flit half is not permitted to be consumed until the entire flit is successfully received. Additionally, the CXL.io Transaction Layer must wait until the second half of the flit is successfully received before responding to a PTM request that was received in the first half of the flit so that it responds with the correct master timestamp.

Note that flits are still retried on a 256-byte granularity even with the latency-optimized 256-byte flit. If either flit half fails CRC after FEC decode and correct, the receiver requests a retry of the entire 256-byte flit. The receiver is responsible for tracking whether it has previously consumed either half during a retry and must drop any flit halves that have been previously consumed.

The following error scenario example illustrates how latency-optimized flits are processed. The even flit half passes CRC check prior to FEC decode and is consumed. The odd flit half fails CRC check. The FEC decode and correct is applied to the 256-byte flit; subsequently, the even flit half now fails CRC and the odd flit half passes. In this scenario, the FEC correction is suspect since a previously passing CRC check now fails. The receiver requests a retry of the 256-byte flit, and the odd flit half is consumed from the retransmitted flit, assuming it passes FEC and CRC checks. Note that even though the even flit half failed CRC post-FEC correction in the original flit, the receiver must not re-consume the even flit half from the retransmitted flit. The expectation is that this scenario occurs most likely due to multiple errors in the odd flit half exceeding FEC correction capability, thus causing additional errors to be injected due to FEC correction.

Table 6-7 summarizes processing steps for different CRC scenarios, depending on results of the CRC check for the even flit half and the odd flit half on the original flit, the post-FEC corrected flit, and the retransmitted flit.

Table 6-7. Latency-Optimized Flit Processing for CRC Scenarios (Sheet 1 of 2)

<table><tr><td colspan="3">Original Flit</td><td colspan="3">Post-FEC Corrected Flit</td><td colspan="3">Retransmitted Flit</td></tr><tr><td>Even CRC</td><td>Odd CRC</td><td>Action</td><td>Even CRC</td><td>Odd CRC</td><td>Subsequent Action</td><td>Even CRC</td><td>Odd CRC</td><td>Subsequent Action</td></tr><tr><td>Pass</td><td>Pass</td><td>Consume Flit</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td rowspan="8">Pass</td><td rowspan="8">Fail</td><td rowspan="8">Permitted to consume even flit half; perform FEC decode and correct</td><td>Pass</td><td>Pass</td><td>Consume even flit half if not previously consumed (must drop even flit half if previously consumed); Consume odd flit half</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td rowspan="3">Pass</td><td rowspan="3">Fail</td><td rowspan="3">Permitted to consume even flit half if not previously consumed; Request Retry</td><td>Pass</td><td>Pass</td><td>Consume even flit half if not previously consumed (must drop even flit half if previously consumed); Consume odd flit half</td></tr><tr><td>Pass</td><td>Fail</td><td>Permitted to consume even flit half if not previously consumed (must drop even flit half if previously consumed); perform FEC decode and correct</td></tr><tr><td>Fail</td><td>Pass/Fail</td><td>Perform FEC decode and correct and evaluate next steps</td></tr><tr><td rowspan="4">Fail</td><td rowspan="4">Pass/Fail</td><td rowspan="4">Request Retry; Log error for even flit half if previously  $consumed^1$ </td><td>Pass</td><td>Pass</td><td>Consume even flit half if not previously consumed (must drop even flit half if previously consumed); Consume odd flit half</td></tr><tr><td>Pass</td><td>Fail</td><td>Permitted to consume even flit half if not previously consumed (must drop even flit half if previously consumed); perform FEC decode and correct</td></tr><tr><td>Fail</td><td>Pass</td><td>Perform FEC decode and correct and evaluate next steps</td></tr><tr><td>Fail</td><td>Fail</td><td>Perform FEC decode and correct and evaluate next steps</td></tr><tr><td rowspan="8">Fail</td><td rowspan="8">Pass</td><td rowspan="8">Perform FEC decode and correct</td><td>Pass</td><td>Pass</td><td>Consume flit</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td rowspan="4">Pass</td><td rowspan="4">Fail</td><td rowspan="4">Permitted to consume even flit half; Request Retry</td><td>Pass</td><td>Pass</td><td>Consume even flit half if not previously consumed (must drop even flit half if previously consumed); Consume odd flit half</td></tr><tr><td>Pass</td><td>Fail</td><td>Permitted to consume even flit half if not previously consumed; Perform FEC decode and correct and evaluate next steps</td></tr><tr><td>Fail</td><td>Pass</td><td>Perform FEC decode and correct and evaluate next steps</td></tr><tr><td>Fail</td><td>Fail</td><td>Perform FEC decode and correct and evaluate next steps</td></tr><tr><td rowspan="3">Fail</td><td rowspan="3">Pass/Fail</td><td rowspan="3">Request Retry</td><td>Pass</td><td>Pass</td><td>Consume flit</td></tr><tr><td>Pass</td><td>Fail</td><td>Permitted to consume even flit half; Perform FEC decode and correct and evaluate next steps</td></tr><tr><td>Fail</td><td>Pass/Fail</td><td>Perform FEC decode and correct and evaluate next steps</td></tr></table>

Table 6-7. Latency-Optimized Flit Processing for CRC Scenarios (Sheet 2 of 2)

<table><tr><td colspan="3">Original Flit</td><td colspan="3">Post-FEC Corrected Flit</td><td colspan="3">Retransmitted Flit</td></tr><tr><td>Even CRC</td><td>Odd CRC</td><td>Action</td><td>Even CRC</td><td>Odd CRC</td><td>Subsequent Action</td><td>Even CRC</td><td>Odd CRC</td><td>Subsequent Action</td></tr><tr><td rowspan="8">Fail</td><td rowspan="8">Fail</td><td rowspan="8">Perform FEC decode and correct</td><td>Pass</td><td>Pass</td><td>Consume flit</td><td>N/A</td><td>N/A</td><td>N/A</td></tr><tr><td rowspan="4">Pass</td><td rowspan="4">Fail</td><td rowspan="4">Permitted to consume even flit half; Request Retry</td><td>Pass</td><td>Pass</td><td>Consume even flit half if not previously consumed (must drop even flit half if previously consumed); Consume odd flit half</td></tr><tr><td>Pass</td><td>Fail</td><td>Permitted to consume even flit half if not previously consumed; Perform FEC decode and correct and evaluate next steps</td></tr><tr><td>Fail</td><td>Pass</td><td>Perform FEC decode and correct and evaluate next steps</td></tr><tr><td>Fail</td><td>Fail</td><td>Perform FEC decode and correct and evaluate next steps</td></tr><tr><td rowspan="3">Fail</td><td rowspan="3">Pass/Fail</td><td rowspan="3">Request Retry</td><td>Pass</td><td>Pass</td><td>Consume flit</td></tr><tr><td>Pass</td><td>Fail</td><td>Permitted to consume even flit half; Perform FEC decode and correct and evaluate next steps</td></tr><tr><td>Fail</td><td>Pass/Fail</td><td>Perform FEC decode and correct and evaluate next steps</td></tr></table>

1. The receiver must not consume the FEC-corrected odd flit half that passes CRC because the FEC correction operation is potentially suspect in this particular scenario.

For CXL.io, the Flit Data includes TLP and DLLP payload; the 4-bytes of DLLP are transferred just before the FEC in the flit as shown in Figure 6-12.

Figure 6-12. CXL.io Latency-Optimized 256B Flit

<table><tr><td>FlitHdr (2 bytes)</td><td colspan="3">FlitData (120 bytes)</td><td>CRC (6 bytes)</td></tr><tr><td colspan="2">FlitData (112 bytes)</td><td>DLLP (4 bytes)</td><td>FEC (6 bytes)</td><td>CRC (6 bytes)</td></tr></table>

## 6.2.3.1.2.1 Latency-Optimized Flit 6-Byte CRC Calculation

The 6-Byte CRC is chosen to optimize the data path as well as allow reuse of the 8-Byte CRC logic from PCIe to save area. The CRC for the even flit half is calculated independent of the calculation for the odd flit half.

A (130, 136) Reed-Solomon code is used, where six bytes of CRC are generated over a 130-byte message to generate a 136-byte codeword. For the even flit half, bytes 0 to 121 of the message are the 122 non-CRC bytes of the flit (with byte 0 of flit mapping to byte 0 of the message, byte 1 of the flit mapping to byte 1 of the message and so on), whereas bytes 122 to 129 are zero (these are not sent on the link, but both transmitter and receiver must zero pad the remaining bytes before computing CRC). For the odd flit half, bytes 0 to 115 of the message are the 116 non-CRC and non-FEC bytes of the flit (with byte 128 of the flit mapping to byte 0 of the message, byte 129 of the flit mapping to byte 1 of the message and so on), whereas bytes 116 to 129 of the message are zero.

The CRC generator polynomial defined over $\mathsf { G F } ( 2 ^ { 8 } ) , \mathsf { i s ~ } \mathsf { g } ( \mathbf { x } ) = ( \mathbf { x } + \alpha ) ( \mathbf { x } + \alpha ^ { 2 } ) . . . ( \mathbf { x } + \alpha ^ { 6 } )$ where is the root of the primitive polynomial of degree 8: . Thus,α x<sup>8</sup> x<sup>5</sup> x<sup>3</sup> + + + +x 1 $\operatorname { g } ( \mathbf { x } ) = \mathbf { x } ^ { 6 } + \alpha ^ { 1 4 7 } \mathbf { x } ^ { 5 } + \alpha ^ { 1 0 7 } \mathbf { x } ^ { 4 } + { \dot { \alpha } } ^ { 2 5 0 } \mathbf { x } ^ { 3 } + \alpha ^ { 1 \dot { 1 } 4 } \mathbf { x } ^ { \dot { 2 } } + \alpha ^ { 1 6 1 } \mathbf { x } + \alpha ^ { 2 1 }$

When reusing the PCIe logic of 8B CRC generation, the first step is to generate the 8- Byte CRC from the PCIe logic. The flit bytes must be mapped to a specific location within the 242 bytes of input to the PCIe logic of 8B CRC generation.

Table 6-8. Byte Mapping for Input to PCIe 8B CRC Generation

<table><tr><td>PCIe CRC Input Bytes</td><td>Even Flit Half Mapping</td><td>Odd Flit Half Mapping</td></tr><tr><td>Byte 0 to Byte 113</td><td>00h for all bytes</td><td>00h for all bytes</td></tr><tr><td>Byte 114 to Byte 229</td><td>Byte 0 to Byte 115 of the flit</td><td>Byte 128 to Byte 243 of the flit</td></tr><tr><td>Byte 230 to Byte 235</td><td>Byte 116 to Byte 121 of the flit</td><td>00h for all bytes</td></tr><tr><td>Byte 236 to Byte 241</td><td>00h for all bytes</td><td>00h for all bytes</td></tr></table>

If the polynomial form of the result is: $\mathbf { r } ^ { \prime } ( \mathbf { x } ) = \mathbf { r } _ { 7 } \mathbf { x } ^ { 7 } + \mathbf { r } _ { 6 } \mathbf { x } ^ { 6 } + \mathbf { r } _ { 5 } \mathbf { x } ^ { 5 } + \mathbf { r } _ { 4 } \mathbf { x } ^ { 4 } + \mathbf { r } _ { 3 } \mathbf { x } ^ { 3 } + \mathbf { r } _ { 2 } \mathbf { x } ^ { 2 } + \mathbf { r } _ { 1 } \mathbf { x } + \mathbf { r } _ { 0 }$ then the 6-Byte CRC can be computed using the following (equation shows the polynomial form of the 6-Byte CRC):

$$
\begin{array}{r} \mathbf {r} (\mathbf {x}) = (r _ {5} + \alpha^ {1 4 7} r _ {6} + \alpha^ {9 0} r _ {7}) \mathbf {x} ^ {5} + (r _ {4} + \alpha^ {1 0 7} r _ {6} + \alpha^ {2 0 2} r _ {7}) \mathbf {x} ^ {4} + \\ (r _ {3} + \alpha^ {2 5 0} r _ {6} + \alpha^ {4 1} r _ {7}) \mathbf {x} ^ {3} + (r _ {2} + \alpha^ {1 1 4} r _ {6} + \alpha^ {6 3} r _ {7}) \mathbf {x} ^ {2} + \\ (r _ {1} + \alpha^ {1 6 1} r _ {6} + \alpha^ {1 4 7} r _ {7}) \mathbf {x} + (r _ {0} + \alpha^ {2 1} r _ {6} + \alpha^ {1 6 8} r _ {7}) \end{array}
$$

Figure 6-13 shows the two concepts of computing the 6-Byte CRC.  
Figure 6-13. Different Methods for Generating 6-Byte CRC  
![](images/a2737c23b796c6bf80fe9bc22447aa35a27305d0a54b370ed16fc5fa6193fa30.jpg)  
The following are provided as attachments to the CXL specification:

• 6B CRC generator matrix (see PCIe Base Specification for the 8B CRC generator matrix).

• 6B CRC Register Transfer Level (RTL) code (see PCIe Base Specification for the 8B CRC RTL code). A single module with 122 bytes of input and 128 bytes of output is provided and can be used for both the even flit half and the odd flit half (by assigning bytes 116 to 121 of the input to be 00h for the odd flit half).

• 8B CRC to 6B CRC converter RTL code. A single module with 122 bytes of input and 128 bytes of output is provided and can be used for both the even flit half and the odd flit half (by assigning bytes 116 to 121 of the input to be 00h for the odd flit half).

## 6.2.3.2 CRC Corruption for Containment with 256B Flits

CXL has multiple scenarios that require CRC to be intentionally corrupted during transmission of a 256B Flit to force the receiver to reject the Flit and initiate a replay. During the subsequent replay, the transmitter has the opportunity to inject additional information about the Flit. These scenarios include viral containment and late poison and nullify scenarios.

To corrupt the CRC in these scenarios, the transmitter must invert all the bits of the CRC field during transmission. FEC generation must be done using the corrupted CRC. For latency-optimized 256B Flits, the transmitter must invert the CRC bits associated with either the even flit half or the odd flit half.

## 6.2.3.2.1 CXL.cachemem Viral Injection and Late Poison for 256B Flits

See Chapter 4.0 for details on CXL.cachemem viral injection and late poison scenarios. Section 4.3.6.2 describes the viral injection flow. Section 4.3.6.3 describes the late poison injection flow.

## 6.2.3.2.2 Late Nullify or Poison for CXL.io

The PCIe specification defines a Flit Marker that is used to nullify or poison the last TLP in the flit. Because the Flit Header is forwarded at the beginning of a flit transmission, a transmitter may not know sufficiently early whether a Flit Marker is required to nullify or poison the last TLP. If the transmitter realizes after the Flit Header has been forwarded that a TLP must be poisoned or nullified, the transmitter must corrupt the CRC by inverting all the CRC bits. When the flit is subsequently replayed, the transmitter must use a Flit Header. For latency-optimized flits, if the last TLP that must be nullified or poisoned is in the even half, the even CRC must be inverted; if the last TLP that must be nullified or poisoned is in the odd half, the odd CRC must be inverted. FEC is calculated on the transmit side using the inverted CRC in these scenarios.

## 256B Flit Mode Retry Buffers

Following PCIe Base Specification, in 256B Flit mode, the Physical Layer implements the transmit retry buffer and the optional receive retry buffer. Whereas the retry buffers are managed independently in the CXL.io link layer and the CXL.cachemem link layer in 68B Flit mode, there is a single unified transmit retry buffer that handles all retryable CXL traffic in 256B Flit mode. Similarly, in 256B Flit mode, there is a single unified receive retry buffer that handles all retryable CXL traffic in 256B Flit mode. Retry requests are on a 256-byte flit granularity even when using the latency-optimized 256B flit composed of 128-byte flit halves. Please refer to Section 6.2.3.1.2 for more details.

## 6.4 Link Training

## 6.4.1 PCIe Mode vs. Flex Bus.CXL Mode Selection

Upon exit from LTSSM Detect, a Flex Bus link begins training and completes link width negotiation and speed negotiation according to the PCIe LTSSM rules. During link training, the Downstream Port initiates Flex Bus mode negotiation via the PCIe alternate protocol negotiation mechanism. Flex Bus mode negotiation is completed before entering L0 at 2.5 GT/s. If Sync Header bypass is negotiated (applicable only to 8 GT/s, 16 GT/s, and 32 GT/s link speeds), Sync Headers are bypassed as soon as the link has transitioned to a speed of 8 GT/s or higher. For 68B Flit mode, the Flex Bus logical PHY transmits NULL flits after it sends the SDS Ordered Set as soon as it transitions to 8 GT/s or higher link speeds if CXL mode was negotiated earlier in the training process. These NULL flits are used in place of PCIe Idle Symbols to facilitate certain LTSSM transitions to L0 as described in Section 6.5. After the link has transitioned to its final speed, the link can start sending CXL traffic on behalf of the upper layers after the SDS Ordered Set is transmitted if that was what was negotiated earlier in the training process. For Upstream Ports, the physical layer notifies the upper layers that the link is up and available for transmission only after it has received a flit that was not generated by the physical layer of the partner Downstream Port (see Table 6-2 for 68B Flit mode and Table 6-6 for 256B Flit mode). To operate in CXL mode, the link speed must be at least 8 GT/s. If the link is unable to transition to a speed of 8 GT/s or greater after committing to CXL mode during link training at 2.5 GT/s, the link may ultimately fail to link up even if the device is PCIe capable.

## 6.4.1.1 Hardware Autonomous Mode Negotiation

Dynamic hardware negotiation of Flex Bus mode occurs during link training in the LTSSM Configuration state before entering L0 at Gen 1 speeds using the alternate protocol negotiation mechanism, facilitated by exchanging modified TS1 and TS2 Ordered Sets as defined by PCIe Base Specification. The Downstream Port initiates the negotiation process by sending TS1 Ordered Sets advertising its Flex Bus capabilities. The Upstream Port responds with a proposal based on its own capabilities and those advertised by the host. The host communicates the final decision of which capabilities to enable by sending modified TS2 Ordered Sets before or during Configuration.Complete.

Please refer to PCIe Base Specification for details on how the various fields of the modified TS1/TS2 OS are set. Table 6-9 shows how the modified TS1/TS2 OS is used for Flex Bus mode negotiation. The “Flex Bus Mode Negotiation Usage” column describes the deltas from the PCIe Base Specification definition that are applicable for Flex Bus mode negotiation. Additional explanation is provided in Table 6-10 and Table 6-11. The presence of Retimer1 and Retimer2 must be programmed into the Flex Bus Port DVSEC by software before the negotiation begins; if retimers are present, the relevant retimer bits in the modified TS1/TS2 OS are used.

Table 6-9. Modified TS1/TS2 Ordered Set for Flex Bus Mode Negotiation (Sheet 1 of 2)

<table><tr><td>Symbol Number</td><td>PCIe Description</td><td>Flex Bus Mode Negotiation Usage</td></tr><tr><td>0 through 4</td><td>See PCIe Base Specification Symbol</td><td></td></tr><tr><td>5</td><td>Training Control:Bits[5:0]: See PCIe Base SpecificationBits[7:6]:Modified TS1/TS2 Supported: See PCIe Base Specification for details</td><td>Bits[7:6]: Value is 11b</td></tr><tr><td>6</td><td>For Modified TS1:TS1 Identifier, Encoded as D10.2 (4Ah)For Modified TS2:TS2 Identifier, Encoded as D5.2 (45h)</td><td>TS1 Identifier during Phase 1 of Flex Bus mode negotiationTS2 Identifier during Phase 2 of Flex Bus mode negotiation</td></tr><tr><td>7</td><td>For Modified TS1:TS1 Identifier, Encoded as D10.2 (4Ah)For Modified TS2:TS2 Identifier, Encoded as D5.2 (45h)</td><td>TS1 Identifier during Phase 1 of Flex Bus mode negotiationTS2 Identifier during Phase 2 of Flex Bus mode negotiation</td></tr><tr><td>8-9</td><td>Bits[2:0]:Usage: See PCIe Base SpecificationBits[4:3]:Alternate Protocol Negotiation Status:- Alternate Protocol Negotiation Status when Usage is 010b- Otherwise, reserved (see PCIe Base Specification for details)Bits[15:5]:Alternate Protocol Details</td><td>Bits[2:0]: Value is 010b (indicating alternate protocols)Bits[4:3]:Alternate Protocol Negotiation Status: See PCIe Base SpecificationBits[7:5]:Alternate Protocol ID:- 000b = Flex BusBit[8]:Common ClockBits[15:9]:ReservedSeeTable 6-10for more information.</td></tr></table>

Table 6-9. Modified TS1/TS2 Ordered Set for Flex Bus Mode Negotiation (Sheet 2 of 2)

<table><tr><td>Symbol Number</td><td>PCIe Description</td><td>Flex Bus Mode Negotiation Usage</td></tr><tr><td>10-11</td><td>Alternate Protocol ID/Vendor ID:Alternate Protocol ID/Vendor ID when Usage = 010bSee PCIe Base Specification for descriptions that are applicable to other Usage values</td><td>1E98h</td></tr><tr><td>12-14</td><td>See PCIe Base SpecificationSpecific proprietary usage when Usage = 010b</td><td>Bits[7:0]: Flex Bus Mode Selection:- Bit[0]: PCIe Capable/Enable- Bit[1]: CXL.io Capable/Enable- Bit[2]: CXL.mem Capable/Enable- Bit[3]: CXL.cache Capable/Enable- Bit[4]: CXL 68B Flit and VH Capable/Enable (formerly known as CXL 2.0 Capable/Enable)- Bits[7:5]: ReservedBits[23:8]: Flex Bus Additional Info:- Bit[8]: Multi-Logical Device Capable/Enable- Bit[9]: Reserved- Bit[10]: Sync Header Bypass Capable/Enable- Bit[11]: Latency-Optimized 256B Flit Capable/Enable- Bit[12]: Retimer1 CXL Aware $^{1}$ - Bit[13]: Reserved- Bit[14]: Retimer2 CXL Aware $^{2}$ - Bit[15]: CXL.io Throttle Required at 64 GT/s- Bits[17:16]: CXL NOP Hint Info[1:0]- Bit[18]: PBR Flit Capable/Enable- Bits[23:19]: ReservedSee Table 6-11 for more information.</td></tr><tr><td>15</td><td>See PCIe Base Specification</td><td></td></tr></table>

1. Retimer1 is equivalent to Retimer X or Retimer Z in PCIe Base Specification.  
2. Retimer2 is equivalent to Retimer Y in PCIe Base Specification.

Table 6-10. Additional Information on Symbols 8-9 of Modified TS1/TS2 Ordered Set

<table><tr><td>Bit Field in Symbols 8-9</td><td>Description</td></tr><tr><td>Bit[8]: Common Clock</td><td>The Downstream Port uses this bit to communicate to retimers that there is a common reference clock. Depending on implementation, retimers may use this information to determine which features to enable.</td></tr></table>

Additional Information on Symbols 12-14 of Modified TS1/TS2 Ordered Sets (Sheet 1 of 2)

<table><tr><td>Bit Field in Symbols 12-14</td><td>Description</td></tr><tr><td>Bit[0]: PCIe Capable/Enable</td><td>The Downstream Port and Upstream Port advertise their capability in Phase 1. The Downstream Port communicates the results of the negotiation in Phase 2. $^{1}$ </td></tr><tr><td>Bit[1]: CXL.io Capable/Enable</td><td>The Downstream Port and Upstream Port advertise their capability in Phase 1 as set in the DVSEC Flex Bus Port Control register $^{2}$ . The Downstream Port communicates the results of the negotiation in Phase 2. This bit must be set to 1 if the CXL 68B Flit and VH Capable/Enable bit is set.</td></tr><tr><td>Bit[2]: CXL.mem Capable/Enable</td><td>The Downstream Port and Upstream Port advertise their capability in Phase 1 as set in the DVSEC Flex Bus Port Control register $^{2}$ . The Downstream Port communicates the results of the negotiation in Phase 2.</td></tr></table>

Table 6-11. Additional Information on Symbols 12-14 of Modified TS1/TS2 Ordered Sets (Sheet 2 of 2)

<table><tr><td>Bit Field in Symbols 12-14</td><td>Description</td></tr><tr><td>Bit[3]: CXL.cache Capable/Enable</td><td>The Downstream Port and Upstream Port advertise their capability in Phase 1 as set in the DVSEC Flex Bus Port Control register $^{2}$ . The Downstream Port communicates the results of the negotiation in Phase 2.</td></tr><tr><td>Bit[4]: CXL 68B Flit and VH Capable/Enable (formerly known as CXL 2.0 capable/ enable)</td><td>The Downstream Port and Upstream Port advertise their capability in Phase 1 as set in the DVSEC Flex Bus Port Control register $^{2}$ . The Downstream Port communicates the results of the negotiation in Phase 2. The Downstream Port must not enable this if PCIe Flit mode is enabled as described in PCIe Base Specification.</td></tr><tr><td>Bit[8]: Multi-Logical Device Capable/Enable</td><td>The Downstream Port and Upstream Port advertise their capability in Phase 1 as set in the DVSEC Flex Bus Port Control register $^{2}$ . An Upstream Switch Port must always advertise 0 in this bit. The Downstream Port communicates the results of the negotiation in Phase 2.</td></tr><tr><td>Bit[10]: Sync Header Bypass Capable/Enable</td><td>The Downstream Port, Upstream Port, and any retimers advertise their capability in Phase 1; the Downstream Port and Upstream Port advertise the value as set in the DVSEC Flex Bus Port Control register $^{2}$ . The Downstream Port communicates the results of the negotiation in Phase 2.Note:The Retimer must pass this bit unmodified from its Upstream Pseudo Port to its Downstream Pseudo Port. The retimer clears this bit if the retimer does not support this feature when passing from its Downstream Pseudo Port to its Upstream Pseudo Port, but it must never set this bit (only an Upstream Port can set this bit in that direction). If the retimer(s) do not advertise that they are CXL aware, the Downstream Port assumes that this feature is not supported by the Retimer(s) regardless of how this bit is set.Note:This bit is applicable only at 8 GT/s, 16 GT/s, and 32 GT/s link speeds.</td></tr><tr><td>Bit[11]: Latency-Optimized 256B Flit Capable/Enable</td><td>The Downstream Port and Upstream Port advertise their capability in Phase 1 as set in the DVSEC Flex Bus Port Control register $^{2}$ . The Downstream Port communicates the results of the negotiation in Phase2.See Section 6.2.3.1.2 for details of the latency-optimized 256B flit.Note:This bit is applicable only when PCIe Flit mode is negotiated.</td></tr><tr><td>Bit[12]: Retimer1 CXL Aware</td><td>Retimer1 advertises whether it is CXL aware in Phase 1. If Retimer1 is CXL aware, it must use the &quot;Sync Header Bypass Capable/Enable&quot; bit. $^{3}$ </td></tr><tr><td>Bit[14]: Retimer2 CXL Aware</td><td>Retimer2 advertises whether it is CXL aware in Phase 1. If Retimer2 is CXL aware, it must use the &quot;Sync Header Bypass Capable/Enable&quot; bit. $^{4}$ </td></tr><tr><td>Bit[15]: CXL.io Throttle Required at 64 GT/s</td><td>During Phase 1, an Upstream Port uses this bit to communicate to the Downstream Port that the Upstream Port does not support receiving consecutive CXL.io flits (including CXL.io NOP flits) when 64 GT/s link speed is negotiated (see Section 6.4.1.3 for more details). Downstream Ports are required to support this feature. The Downstream Port logs the value communicated by the partner Upstream Port in its DVSEC Flex Bus Port Status register (see Section 8.2.1.3.3).</td></tr><tr><td>Bits[17:16]: CXL NOP Hint Info[1:0]</td><td>During Phase 1, the Downstream Port and Upstream Port advertise whether they support injecting NOP flits in response to receiving NOP hints and also whether they require receiving a single NOP flit or two back-to-back NOP flits to switch over from a higher-latency FEC pipeline to a lower-latency pipeline. This field is encoded as follows:00b = No support for injecting NOP flits in response to receiving NOP hints.01b = Supports injecting NOP flits. Requires receiving a single NOP flit to switch over from a higher-latency FEC pipeline to a lower-latency pipeline.10b = Reserved.11b = Supports injecting NOP flits. Requires receiving two back-to-back NOP flits to switch over from a higher-latency FEC pipeline to a lower-latency pipeline.</td></tr><tr><td>Bit[18]: PBR (Port Based Routing) Flit Capable/Enable</td><td>The Upstream Port and Downstream Port advertise that they support PBR flits in Phase 1, as set in the DVSEC Flex Bus Port Control register $^{2}$ . The Downstream Port communicates the results of the negotiation in Phase 2. The Downstream Port must not enable PBR flits if PCIe Flit mode is not enabled as defined in PCIe Base Specification.</td></tr></table>

1. PCIe mode and CXL mode are mutually exclusive when the Downstream Port communicates the results of the negotiation in Phase 2.

2. See Section 8.2.1.3.2 for the DVSEC Flex Bus Port Control register definition.

3. Retimer1 is equivalent to Retimer X or Retimer Z in PCIe Base Specification.

4. Retimer2 is equivalent to Retimer Y in PCIe Base Specification.

Hardware autonomous mode negotiation is a two-phase process that occurs while in Configuration.Lanenum.Wait, Configuration.Lanenum.Accept, and Configuration.Complete before entering L0 at Gen 1 speed:

• Phase 1: The Downstream Port sends a stream of modified TS1 Ordered Sets advertising its Flex Bus capabilities; the Upstream Port responds by sending a stream of modified TS1 Ordered Sets indicating which Flex Bus capabilities it wishes to enable. This exchange occurs during Configuration.Lanenum.Wait and/or Configuration.Lanenum.Accept. At the end of this phase, the Downstream Port has enough information to make a final selection of which capabilities to enable. The Downstream Port uses the Flex Bus capabilities information received in the first two consecutively received modified TS1 Ordered Sets in which the Alternate Protocol Negotiation status indicates that the Upstream Port supports the requested protocol.

• Phase 2: The Downstream Port sends a stream of modified TS2 Ordered Sets to the Upstream Port to indicate whether the link should operate in PCIe mode or in CXL mode; for CXL mode, it also specifies which CXL protocols, modes, and features to enable. The Downstream Port must set the Flex Bus enable bits identically in the 16 consecutive modified TS2 Ordered Sets sent before transitioning to Configuration.Idle. The Upstream Port acknowledges the enable request by sending modified TS2 Ordered Sets with the same Flex Bus enable bits set. This exchange occurs during Configuration.Complete. CXL alternate protocol negotiation successfully completes only after the Downstream Port has confirmed that the Flex Bus enable bits reflected in the eight consecutive modified TS2 Ordered Sets it receives that causes the transition to Configuration.Idle match what it transmitted; otherwise, the Downstream Port logs an error in the Flex Bus Port Status register and the physical layer LTSSM returns to Detect. If the Upstream Port receives an enable request in which the Flex Bus enable bits are not a subset of what it advertised in Phase 1, the behavior is undefined.

The Flex Bus negotiation process is complete before entering L0 at 2.5 GT/s. At this point the upper layers may be notified of the decision. If CXL mode is negotiated, the physical layer enables all the negotiated modes and features only after reaching L0 at 8 GT/s or higher speed.

## Note:

If CXL is negotiated but the link does not achieve a speed of at least 8 GT/s, the link will fail to link up and go back to LTSSM Detect.

A flow chart describing the mode negotiation process during link training is provided in Figure 6-14. Note that while this flow chart represents the flow for several scenarios, it is not intended to cover all possible scenarios.

Figure 6-14. Flex Bus Mode Negotiation during Link Training (Sample Flow)  
![](images/20064a00fdd9eeea8278ffb5bfa3784e7799081603a38fcceef425ae8dfe54a7.jpg)

## 6.4.1.2 Virtual Hierarchy vs. Restricted CXL Device Negotiation

VH-capable devices support switching and hot add, features that are not supported in exclusive Restricted CXL Devices (eRCDs). This difference in supported features impacts the link training behavior. Table 6-12 specifies the Flex Bus physical layer link training result for all possible combinations of upstream and downstream components. The table was constructed based upon the following assumptions:

• VH-capable Endpoints and switches are required to support hot add as a downstream component.

• VH-capable Downstream Ports are not required to support hot add; however, this capability is enforced at the software level. The Flex Bus physical layer will allow the link to train successfully for hot-add scenarios if both the upstream component and downstream component are VH capable.

• For exclusive Restricted CXL Hosts (eRCHs), BIOS prevents CXL hot-add scenarios by disabling CXL alternate protocol negotiation before handing control over to the OS. The Flex Bus physical layer does not have to handle these scenarios.

• For VH-capable Downstream Ports, BIOS sets the Disable\_RCD\_Training bit in the DVSEC Flex Bus Port Control register before handing control to the OS. For a host, the Flex Bus physical layer uses the Disable\_RCD\_Training bit to distinguish between initial power-on scenarios and hot-add scenarios to determine appropriate link training behavior with eRCDs.

## Note:

In the context of this section, “VH-capable” was previously known as “CXL 2.0 and newer”, “eRCD” was previously known as a “CXL 1.1 capable device”, and “eRCH” was previously known as “CXL 1.1 capable host”.

Table 6-12. VH vs. RCD Link Training Resolution

<table><tr><td>Upstream Component</td><td>Downstream Component</td><td>Link Training Result</td></tr><tr><td>Host - VH capable</td><td>Switch</td><td>VH mode</td></tr><tr><td>Host - eRCH</td><td>Switch</td><td>Fail CXL alternate protocol negotiation</td></tr><tr><td>Host - VH capable</td><td>Endpoint - VH capable</td><td>VH mode</td></tr><tr><td>Host - VH capable</td><td>Endpoint - eRCD</td><td>RCD for initial power-on scenario; fail CXL alternate protocol negotiation for hot-add scenario</td></tr><tr><td>Host - eRCH</td><td>Endpoint - VH capable</td><td>RCD - assumes no hot add</td></tr><tr><td>Host - eRCH</td><td>Endpoint - eRCD</td><td>RCD - assumes no hot add</td></tr><tr><td>Switch</td><td>Endpoint - VH capable</td><td>VH mode</td></tr><tr><td>Switch</td><td>Endpoint - eRCD</td><td>RCD for initial power-on scenario; fail CXL alternate protocol negotiation for hot-add scenario</td></tr></table>

The motivation for forcing the Flex Bus physical layer to fail CXL training for certain combinations of upstream component and downstream component is to avoid unpredictable software behavior if the link were allowed to train. For the specific combination of an eRCH and a switch, the Upstream Switch Port is responsible for ensuring that CXL alternate protocol negotiation fails by returning a value of 01b in the Alternate Protocol Negotiation Status field of the modified TS1 to indicate that it does not support the requested protocol; this must occur during Phase 1 of the alternate protocol negotiation process after the Upstream Switch Port observes that the host is not VH capable.

## 6.4.1.2.1 Retimer Presence Detection

During CXL alternate protocol negotiation, the presence of a retimer impacts whether the Sync Header bypass optimization can be enabled as described in Table 6-11. While eRCH Downstream Ports rely on BIOS to program the Retimer1\_Present and Retimer2\_Present bits in the DVSEC Flex Bus Port Control register prior to the start of link training, VH-capable Downstream Ports must ignore those register bits because BIOS is not involved with Hot-Plug scenarios.

VH-capable Downstream Ports must determine retimer presence for CXL alternateprotocol negotiation by sampling the Retimers Present bit and Two Retimers Present bit in the received TS2 Ordered Sets. VH-capable Downstream Ports adhere to the following steps for determining and using retimer presence information:

1. During Polling.Configuration LTSSM state, the Downstream Port samples the Retimer Present bit and the Two Retimers Present bit for use during CXL alternate protocol negotiation. If the Retimer Present bit is set to 1 in the 8 consecutively received TS2 Ordered Sets that causes the transition to Configuration, then the Downstream Port must assume that a retimer is present for the purposes of CXL alternate protocol negotiation. If the Two Retimers Present bit is set to 1 in the 8 consecutively received TS2 Ordered Sets that causes the transition to Configuration, then the Downstream Port must assume that two retimers are present for the purposes of CXL alternate protocol negotiation.

2. During CXL alternate protocol negotiation, the Downstream Port uses the information sampled in step 1 along with the CXL Alternate Protocol Negotiation Status bits in the modified TS1 Ordered Set to determine whether to enable Sync Header bypass optimization. If a retimer was detected in step 1 on any lane associated with the configured link, then the Downstream Port assumes that a retimer is present. If two retimers were detected in step 1 on any lane associated with the configured link, then the Downstream Port assumes that two retimers are present.

3. During Configuration.Complete, per PCIe Base Specification, the Downstream Port captures “Retimer Present” and “Two Retimers Present” information from the received modified TS2 Ordered Sets into the Link Status 2 register. If the values sampled in this step are inconsistent with the values sampled during Polling.Configuration, then the Downstream Port logs an error in the DVSEC Flex Bus Port Status register, brings the LTSSM to Detect, and then retrains the link with Sync Header bypass optimization disabled.

## 6.4.1.3 256B Flit Mode

Certain protocol features, such as Back-Invalidate (BI), rely on 256B Flit mode. There is no explicit bit for 256B Flit mode negotiation. The following subsections describe 256B Flit mode negotiation, and Section 6.4.1.4 provides further details of how negotiation results in either 256B Flit mode or 68B Flit mode.

## 6.4.1.3.1 256B Flit Mode Negotiation

As shown in Table 6-4, 256B Flit mode is implied if PCIe Flit mode is enabled during PCIe link training as described in PCIe Base Specification. PCIe Flit mode is known prior to starting alternate protocol negotiation. No explicit bit is defined in the modified TS1/ TS2 Ordered Sets for negotiating 256B Flit mode. 256B Flit mode is supported only at 8 GT/s and higher speeds.

For 256B Flit mode, the Upstream and Downstream Ports additionally negotiate whether to enable the latency-optimized 256B flit format or the standard CXL flit format. See Section 6.2.3.1.2 and Table 6-9.

## 6.4.1.3.2 CXL.io Throttling

The Upstream Port must communicate to the Downstream Port during Phase 1 of alternate protocol negotiation if it does not support receiving consecutive CXL.io flits (including CXL.io NOP flits) at a link speed of 64 GT/s. For the purpose of this feature, consecutive CXL.io flits are two flits with Flit Type encoding of 01b that are not separated by either an intervening flit with a different Flit Type encoding or an intervening Ordered Set. Downstream Ports are required to support throttling transmission of CXL.io traffic to meet this requirement if the Upstream Port advertises this bandwidth limitation in the Modified TS1 Ordered Set (see Table 6-9). One possible usage model for this is Type 3 memory devices that need 64 GT/s link bandwidth for CXL.mem traffic but do not have much CXL.io traffic; this feature enables such devices to simplify their hardware to provide potential buffer and power savings.

## 6.4.1.3.3 NOP Insertion Hint Performance Optimization

Latency-optimized 256B Flit mode enables the Physical Layer to use a lower-latency path that bypasses FEC; however, whenever a CRC error is detected, the Physical Layer must switch over to a higher-latency path that includes the FEC logic. To switch back from the higher-latency FEC path to the lower-latency path, the Physical Layer relies on bubbles in the received data that occur due to SKP OSs or NOPs or flits that can be discarded while waiting for a specific sequence number during a replay or any other gaps. Note that NOPs or any other flits with valid DLLP payload cannot be discarded. Due to the 1E-6 bit error rate, the frequency of SKP OS insertion is insufficient to enable the Physical Layer to spend the majority of its time in the lower-latency path.

To address this, a device that detects a CRC error is permitted to send an NOP Insertion Hint to request the partner device to insert NOPs. The NOP insertion hint is defined as a NAK with a sequence number of 0. Upon receiving an NOP insertion hint, the Physical Layer may schedule a single NOP or two back-to-back NOPs to enable its link partner to switch back over to its low-latency path.

During link training, the Physical Layer communicates to its link partner whether the Physical Layer supports responding to NOP hints by inserting NOPs. The Physical Layer also communicates to its link partner whether the Physical Layer requires only a single NOP or whether it requires two back-to-back NOPs to switch over from its higherlatency FEC path to its lower-latency path.

## 6.4.1.4 Flit Mode and VH Negotiation

Table 6-13 specifies the negotiation results that the Downstream Port must communicate during Phase 2 depending on the modes advertised by both sides during Phase 1. For example, if both sides advertise PCIe Flit mode and Latency-Optimized 256B Flit mode, then the negotiation results in Latency-Optimized 256B Flit mode.

Table 6-13. Flit Mode and VH Negotiation

<table><tr><td colspan="4">Both Components Advertise Support during Phase 1 of Negotiation?</td><td rowspan="2">Phase 2 Negotiation Results</td></tr><tr><td>PCIe Flit Mode</td><td>PBR Flit Mode</td><td>Latency-Optimized 256B Flit Mode</td><td>68B Flit and VH Capable</td></tr><tr><td>Yes</td><td>Yes</td><td>Yes/No</td><td>Yes</td><td>PBR Flit mode, Standard 256B Flit mode</td></tr><tr><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Latency-Optimized 256B Flit mode</td></tr><tr><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Standard 256B Flit mode</td></tr><tr><td>No</td><td>No</td><td>No</td><td>Yes</td><td>68B Flit mode, VH mode</td></tr><tr><td>No</td><td>No</td><td>No</td><td>No</td><td>See Table 6-12 for VH mode vs. RCD mode; 68B flits</td></tr></table>

## 6.4.1.5 Flex Bus.CXL Negotiation with Maximum Supported Link Speed of 8 GT/s or 16 GT/s

If an eRCH or eRCD physical layer implementation supports Flex Bus.CXL operation only at a maximum speed of 8 GT/s or 16 GT/s, it must still advertise support of 32 GT/ s speed during link training at 2.5 GT/s to perform alternate protocol negotiation using modified TS1 and TS2 Ordered Sets. After the alternate protocol negotiation is complete, the Flex Bus logical PHY can then advertise the true maximum link speed that it supports as per PCIe Base Specification. It is strongly recommended that VHcapable devices support 32 GT/s link rate; however, a VH-capable device is permitted to use the algorithm described in this section to enable CXL alternate protocol negotiation if it does not support 32 GT/s link rate.

## IMPLEMENTATION NOTE

A CXL device that advertises support of 32 GT/s in early training when it does not truly support 32 GT/s link rate may have compatibility issues for Polling.Compliance and Loopback entry from Config.LinkWidthStart. Please see PCIe Base Specification for more details. Devices that do this must ensure that they provide a mechanism to disable this behavior for the purposes of Polling.Compliance and Loopback testing scenarios.

## 6.4.1.6 Link Width Degradation and Speed Downgrade

If the link is operating in Flex Bus.CXL and degrades to a lower speed or lower link width that is still compatible with Flex Bus.CXL mode, the link should remain in Flex Bus.CXL mode after exiting recovery without having to go through the process of mode negotiation again. If the link drops to a speed or width that is incompatible with Flex Bus.CXL and cannot recover, the link must go down to the LTSSM Detect state; any subsequent action is implementation specific.

## 68B Flit Mode: Recovery.Idle and Config.Idle Transitions to L0

PCIe Base Specification requires transmission and receipt of a specific number of consecutive Idle data Symbols on configured lanes to transition from Recovery.Idle to L0 or Config.Idle to L0 (see PCIe Base Specification) while in non-Flit mode. When the Flex Bus logical PHY is in CXL mode operating in 68B Flit mode, it looks for NULL flits instead of Idle Symbols to initiate the transition to L0. When in Recovery.Idle or Config.Idle, the next state is L0 if four consecutive NULL flits are received and eight NULL flits are sent after receiving one NULL flit; all other PCIe Base Specification rules regarding these transitions apply.

## 6.6 L1 Abort Scenario

Because the CXL ARB/MUX virtualizes the link state that is seen by the link layers and only requests the physical layer to transition to L1 when the link layers are in agreement, there may be a race condition that results in an L1 abort scenario. In this scenario, the physical layer may receive an EIOS or detect Electrical Idle when the ARB/MUX is no longer requesting entry to L1. In this scenario, the physical layer is required to initiate recovery on the link to bring it back to L0.

## 68B Flit Mode: Exit from Recovery

In 68B Flit mode, upon exit from recovery, the receiver assumes that any partial TLPs that were transmitted prior to recovery entry are terminated and must be retransmitted in full via a link-level retry. Partial TLPs include TLPs for which a subsequent EDB, Idle, or valid framing token were not received before entering recovery. The transmitter must satisfy any requirements to enable the receiver to make this assumption.

## 6.8 Retimers and Low Latency Mode

The CXL specification supports the following features that can be enabled to optimize latency: bypass of sync header insertion and use of a drift buffer instead of an elastic buffer. Enablement of Sync Header bypass is negotiated during the Flex Bus mode negotiation process described in Section 6.4.1.1. The Downstream Port, Upstream Port, and any retimers advertise their Sync Header bypass capability during Phase 1; and the Downstream Port communicates the final decision on whether to enable Sync Header bypass during Phase 2. Drift buffer mode is decided locally by each component. The rules for enabling each feature are summarized in Table 6-14; these rules are expected to be enforced by hardware.

Table 6-14. Rules of Enable Low-latency Mode Features

<table><tr><td>Feature</td><td>Conditions for Enabling</td><td>Notes</td></tr><tr><td>Sync Header Bypass</td><td>All components supportCommon reference clockNo retimer is present or retimer cannot add or delete SKPs (e.g., in low-latency bypass mode)Not in loopback mode</td><td></td></tr><tr><td>Drift BufferL(instead of elastic buffer)</td><td>Common reference clock</td><td>Each component can independently enable this (i.e., does not have to be coordinated). The physical layer logs in the Flex Bus Port DVSEC when this is enabled.</td></tr></table>

The Sync Header Bypass optimization applies only at 8 GT/s, 16 GT/s, and 32 GT/s link speeds. At 64 GT/s link speeds, 1b/1b encoding is used as specified in PCIe Base Specification; thus, the Sync Header Bypass optimization is not applicable. If PCIe Flit mode is not enabled and the Sync Header Bypass optimization is enabled, then the CXL specification dictates insertion of Ordered Sets at a fixed interval. If PCIe Flit mode is enabled or Sync Header Bypass is not enabled, the Ordered Set insertion rate follows PCIe Base Specification.

Table 6-15. Sync Header Bypass Applicability and Ordered Set Insertion Rate

<table><tr><td>Data Rate</td><td>PCIe Flit Mode</td><td>Sync Header Bypass Applicable</td><td>Ordered Set Insertion Interval while in Data Stream</td></tr><tr><td>8 GT/s, 16 GT/s, 32 GT/s</td><td>No</td><td>Yes (common clock only)</td><td>With Sync Header bypassed, after every 340 data blocks $^{1}$ ; With Sync Header enabled, per PCIe Base Specification</td></tr><tr><td>8 GT/s, 16 GT/s, 32 GT/s</td><td>Yes</td><td>Yes (common clock only)</td><td>Regardless of whether Sync Header is bypassed, per PCIe Base Specification (where flit interval refers to a 256B flit)</td></tr><tr><td>64 GT/s</td><td>Yes (required)</td><td>No</td><td>Per PCIe Base Specification (where flit interval refers to 256B flit)</td></tr></table>

1. See Section 6.8.1 for details.

## Note:

## 68B Flit Mode: SKP Ordered Set Frequency and L1/Recovery Entry

This section is applicable only for 68B Flit mode.

In Flex Bus.CXL mode, if Sync Header bypass is enabled, the following rules apply:

• After the SDS, the physical layer must schedule a control SKP OS or a standard SKP OS after every 340 data blocks, unless it is exiting the data stream.

The control SKP OSs are alternated with standard SKP OSs at 16 GT/s or higher speeds; at 8 GT/s, only standard SKP OSs are scheduled.

• When exiting the data stream, the physical layer must replace the scheduled control SKP OS (or SKP OS) with either an EIOS (for L1 entry) or EIEOS (for all other cases including recovery).

When Sync Header bypass optimization is enabled, retimers rely on the above mechanism to know when L1/recovery entry is occurring. When Sync Header bypass is not enabled, retimers must not rely on the above mechanism.

While the above algorithm dictates the control SKP OS and standard SKP OS frequency within the data stream, it should be noted that CXL devices must still satisfy the PCIe Base Specification requirement of control SKP OS and standard SKP OS insertion, which is at least once every 370 to 375 blocks when not operating in Separate Reference Clocks with Independent Spread Spectrum Clocking (SRIS), as defined in PCIe Base Specification.

Figure 6-15 illustrates a scenario where a NULL flit with implied EDS token is sent as the last flit before exiting the data stream in the case where Sync Header bypass is enabled. In this example, near the end of the 339th block, the link layer has no flits to send, so the physical layer inserts a NULL flit. Because there is exactly one flit’s worth of time before the next Ordered Set must be sent, a NULL flit with implied EDS token is used. In this case, the variable length NULL flit with EDS token crosses a block boundary and contains a 528-bit payload of 0s.

Figure 6-15. NULL Flit with EDS and Sync Header Bypass Optimization

<table><tr><td rowspan="36"></td><td>Lane 0</td><td>Lane 1</td><td>Lane 2</td><td>Lane 3</td><td></td></tr><tr><td colspan="2">ProtID=NULL w/EDS</td><td>00h</td><td>00h</td><td rowspan="2">Symbol 15</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 0</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 1</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 2</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 3</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 4</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 5</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 6</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 7</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 8</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 9</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 10</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 11</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 12</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 13</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td>Symbol 14</td></tr><tr><td>00h</td><td>00h</td><td>00h</td><td>00h</td><td rowspan="2">Symbol 15</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 0</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 1</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 2</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 3</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 4</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 5</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 6</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 7</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 8</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 9</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 10</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 11</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 12</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 13</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 14</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 15</td></tr></table>

Figure 6-16 illustrates a scenario where a NULL flit with implied EDS token is sent as the last flit before exiting the data stream in the case where 128b/130b encoding is used. In this example, the NULL flit contains only a 16-bit payload of 0s.  
Figure 6-16. NULL Flit with EDS and 128b/130b Encoding

<table><tr><td rowspan="19"></td><td>Lane 0</td><td>Lane 1</td><td>Lane 2</td><td>Lane 3</td><td></td></tr><tr><td colspan="2">ProtID=NULL w/EDS</td><td>00h</td><td>00h</td><td>Symbol 15</td></tr><tr><td>01b</td><td>01b</td><td>01b</td><td>01b</td><td>Sync Header</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 0</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 1</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 2</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 3</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 4</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 5</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 6</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 7</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 8</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 9</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 10</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 11</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 12</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 13</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 14</td></tr><tr><td>OS</td><td>OS</td><td>OS</td><td>OS</td><td>Symbol 15</td></tr></table>

## 7.0 Switching

## 7.1 Overview

This section provides an architecture overview of different CXL switch configurations.

## 7.1.1 Single VCS

A single VCS consists of a single CXL Upstream Port and one or more Downstream Ports as illustrated in Figure 7-1.

Figure 7-1. Example of a Single VCS

![](images/9f56bcd42bd0485aded14aa7739986e5e0325a1846dfe6b300f643afe11f7175.jpg)

A Single VCS is governed by the following rules:

• Must have a single USP

• Must have one or more DSPs

• DSPs must support operating in CXL mode or PCIe\* mode

• All non-MLD (includes PCIe and SLD) ports support a single Virtual Hierarchy below the vPPB

• Downstream Switch Port must be capable of supporting RCD mode

• Must support the CXL Extensions DVSEC for Ports (see Section 8.1.5)

• The DVSEC defines registers to support CXL.io decode to support RCD below the Switch and registers for CXL Memory Decode. The address decode for CXL.io is in addition to the address decode mechanism supported by vPPB.

• Fabric Manager (FM) is optional for a Single VCS

## 7.1.2 Multiple VCS

A Multiple VCS consists of multiple Upstream Ports and one or more Downstream Ports per VCS as illustrated in Figure 7-2.

## Figure 7-2. Example of a Multiple VCS with SLD Ports

![](images/ae00f982365c55e7d09a4ec7f5be89600b8b74e253bb910428521aaa6a8a6252.jpg)

A Multiple VCS is governed by the following rules:

• Must have more than one USP.

• Must have one or more DS vPPBs per VCS.

• The initial binding of upstream (US) vPPB to physical port and the structure of the VCS (including number of vPPBs, the default vPPB capability structures, and any initial bindings of downstream (DS) vPPBs to physical ports) is defined using switch vendor specific methods.

• Each DSP must be bound to a PPB or vPPB.

• FM is optional for Multiple VCS. An FM is required for a Multiple VCS that requires bind/unbind, or that supports MLD ports. Each DSP can be reassigned to a different VCS through the managed Hot-Plug flow orchestrated by the FM.

• When configured, each USP and its associated DS vPPBs form a Single VCS Switch and operate as per the Single VCS rules.

• DSPs must support operating in CXL mode or PCIe mode.

• All non-MLD, non-Fabric, and non-GFD HBR ports support a single Virtual Hierarchy below the Downstream Switch Port.

• DSPs must be capable of supporting RCD mode.

## 7.1.3 Multiple VCS with MLD Ports

A Multiple VCS with MLD Ports consists of multiple Upstream Ports and a combination of one or more Downstream MLD Ports, as illustrated in Figure 7-3.

## Figure 7-3. Example of a Multiple Root Switch Port with Pooled Memory Devices

![](images/6053c0e1ee29582d2f23e38d4ae67d83f9790f266e4c9dbd8fb4934ed0497a04.jpg)

A Multiple VCS with MLD Ports is governed by the following rules:

• More than one USP.

• One or more Downstream vPPBs per VCS.

• Each SLD DSP can be bound to a Single VCS.

• An MLD-capable DSP can be connected to up to 16 USPs.

• Each of the SLD DSPs can be reassigned to a different VCS through the managed Hot-Plug flow orchestrated by the FM.

• Each of the LD instances in an MLD component can be reassigned to a different VCS through the managed Hot-Plug flow orchestrated by the FM.

• When configured, each USP and its associated vPPBs form a Single VCS, and operate as per the Single VCS rules.

• DSPs must support operating in CXL mode or PCIe mode.

• All non-MLD ports support a single Virtual Hierarchy below the DSP.

• DSPs must be capable of supporting RCD mode.

## 7.1.4 vPPB Ordering

vPPBs within a VCS are ordered in the following sequence: the USP vPPB, then the DSP vPPBs in increasing Device Number, Function Number order. This means Function 0 of all vPPBs in order of Device Number, then all vPPBs enumerated at Function 1 in order of Device Number, etc.

For a switch with 65 DSP vPPBs whose USP vPPB was assigned a Bus Number of 3, that would result in the following vPPB ordering:

<table><tr><td>vPPB #</td><td>PCIe ID</td></tr><tr><td>0</td><td>USP 3:0.0</td></tr><tr><td>1</td><td>DSP 4:0.0</td></tr><tr><td>2</td><td>DSP 4:1.0</td></tr><tr><td>3</td><td>DSP 4:2.0</td></tr><tr><td></td><td>...</td></tr><tr><td>32</td><td>DSP 4:31.0</td></tr><tr><td>33</td><td>DSP 4:0.1</td></tr><tr><td>34</td><td>DSP 4:1.1</td></tr><tr><td></td><td>...</td></tr><tr><td>64</td><td>DSP 4:31.1</td></tr><tr><td>65</td><td>DSP 4:0.2</td></tr></table>

This ordering also applies in cases where multi-function vPPBs exist but not all 32 Device Numbers are assigned. For example, a switch with 8 DSP vPPBs whose USP vPPB was assigned a Bus Number of 3 could present its DSP vPPBs in such a way that the host enumeration would result in the following vPPB ordering:

<table><tr><td>vPPB #</td><td>PCIe ID</td></tr><tr><td>0</td><td>USP 3:0.0</td></tr><tr><td>1</td><td>DSP 4:0.0</td></tr><tr><td>2</td><td>DSP 4:1.0</td></tr><tr><td>3</td><td>DSP 4:2.0</td></tr><tr><td>4</td><td>DSP 4:0.1</td></tr><tr><td>5</td><td>DSP 4:1.1</td></tr><tr><td>6</td><td>DSP 4:2.1</td></tr><tr><td>7</td><td>DSP 4:0.2</td></tr><tr><td>8</td><td>DSP 4:1.2</td></tr></table>

## Switch Configuration and Composition

This section describes the CXL switch initialization options and related configuration and composition procedures.

## 7.2.1 CXL Switch Initialization Options

The CXL switch can be initialized using three different methods:

• Static

• FM boots before the host(s)

• FM and host boot simultaneously

## 7.2.1.1 Static Initialization

Figure 7-4 shows a statically initialized CXL switch with 2 VCSs. In this example, the downstream vPPBs are statically bound to ports and are available to the host at boot. Managed hot-add of Devices is supported using standard PCIe mechanisms.

## Figure 7-4. Static CXL Switch with Two VCSs

![](images/df0444754c0a9c0f6775226954742e886909c61bfdf0eba680119cb1eaa3d0bb.jpg)

Static Switch Characteristics:

• No support for MLD Ports

• No support for rebinding of ports to a different VCS

• No FM is required

• At switch boot, all VCSs and Downstream Port bindings are statically configured using switch vendor defined mechanisms (e.g., configuration file in SPI Flash)

• Supports RCD mode, CXL VH mode, or PCIe mode

• VCSs, including vPPBs, behave identically to a PCIe switch, along with the addition of supporting CXL protocols

• Each VCS is ready for enumeration when the host boots

• Hot-add and managed hot-remove are supported

• No explicit support for Async removal of CXL devices; Async removal requires that root ports implement CXL Isolation (see Section 12.3)

A switch that provides internal Endpoint functions is beyond the scope of this specification.

## 7.2.1.2 Fabric Manager Boots First

In cases where the FM boots first (prior to host(s)), the switch is permitted to be initialized as described in the example shown in Figure 7-5.

## Figure 7-5. Example of CXL Switch Initialization when FM Boots First

![](images/641a8d39a3b62f53e2ae4cd8142b8fbbf7ded627719a76a2ae551f06682cce08.jpg)

1. FM boots while hosts are held in reset.

2. All attached DSPs link up and are bound to FM-owned PPBs.

3. DSPs link up and the switch notifies the FM using a managed hot-add notification.

Figure 7-6. Example of CXL Switch after Initialization Completes  
![](images/5113bb231371ac6da83b40cfcfa10f44b66ab429f3c3468ffae894d082731be3.jpg)

As shown in the example above in Figure 7-6, the following steps are taken to configure the switch after initialization completes:

1. FM sends bind command BIND (VCS0, vPPB1, PHY\_PORT\_ID1) to the switch. The switch then configures virtual to physical binding.

2. Switch remaps vPPB virtual port numbers to physical port numbers.

3. Switch remaps vPPB connector definition (PERST#, PRSNT#) to physical connector.

4. Switch disables the link using PPB Link Disable.

5. At this point, all Physical downstream PPB functionality (e.g., Capabilities, etc.) maps directly to the vPPB including Link Disable, which releases the port for linkup.

6. The FM-owned PPB no longer exists for this port.

7. When the hosts boot, the switch is ready for enumeration.

## 7.2.1.3 Fabric Manager and Host Boot Simultaneously

Figure 7-7. Example of Switch with Fabric Manager and Host Boot Simultaneously  
![](images/340c4a496eb1818fe6e09aaafffd151b425237837ce28043fcf93507eb1e732b.jpg)

In the case where the switch, FM, and host boot at the same time:

1. VCSs are statically defined.

2. vPPBs within each VCS are unbound and presented to the host as Link Down.

3. Switch discovers downstream devices and presents them to the FM.

4. Host enumerates the VH and configures the DVSEC registers.

5. FM performs port binding to vPPBs.

6. Switch performs virtual to physical binding.

7. Each bound port results in a hot-add indication to the host.

Figure 7-8. Example of Simultaneous Boot after Binding  
![](images/0dcb7b6493d646bc35b8c0f70a1a7d276522a890fa6e41dc8c9b1fb2fea27935.jpg)

## 7.2.2 Sideband Signal Operation

The availability of slot sideband control signals is decided by the form-factor specifications. Any form factor can be supported, but if the form factor supports the signals listed in Table 7-1, the signals must be driven by the switch or connected to the switch for correct operation.

All other sideband signals have no constraints and are supported exactly as in PCIe.

Table 7-1. CXL Switch Sideband Signal Requirements

<table><tr><td>Signal Name</td><td>Signal Description</td><td>Requirement</td></tr><tr><td>USP PERST#</td><td>PCIe Reset provides a fundamental reset to the VCS</td><td>This signal must be connected to the switch if implemented</td></tr><tr><td>USP ATTN#</td><td>Attention button indicates a request to the host for a managed hot-remove of the switch</td><td>If hot-remove of the switch is supported, this signal must be generated by the switch</td></tr><tr><td>DSP PERST#</td><td>PCIe Reset provides a power-on reset to the downstream link partner</td><td>This signal must be generated by the switch if implemented</td></tr><tr><td>DSP PRSNT#</td><td>Out-of-band Presence Detect indicates that a device has been connected to the slot</td><td>This signal must be connected to the switch if implemented</td></tr><tr><td>DSP ATTN#</td><td>Attention button indicates a request to the host for a managed hot-remove of the downstream slot</td><td>If managed hot-remove is supported, this signal must be connected to the switch</td></tr></table>

This list provides the minimum sideband signal set to support managed Hot-Plug. Other optional sidebands signals such as Attention LED, Power LED, Manual Retention Latch, Electromechanical Lock, etc. may also be used for managed Hot-Plug. The behavior of these sideband signals is identical to PCIe.

## 7.2.3 Binding and Unbinding

This section describes the details of Binding and Unbinding of CXL devices to a vPPB.

## 7.2.3.1 Binding and Unbinding of a Single Logical Device Port

A Single Logical Device (SLD) port refers to a port that is bound to only one VCS. That port can be linked up with a PCIe device or a CXL Type 1, Type 2, or Type 3 SLD component. In general, the vPPB bound to the SLD port behaves the same as a PPB in a PCIe switch. An exception is that a vPPB can be unbound from any physical port. In this case the vPPB appears to the host as if it is in a Link Down state with no Presence Detect indication. If optional rebinding is desired, this switch must have an FM API support and FM connection. The Fabric Manager can bind any unused physical port to the unbound vPPB. After binding, all the vPPB port settings are applied to that physical port.

Figure 7-9 shows a switch with bound DSPs.

Figure 7-9. Example of Binding and Unbinding of an SLD Port  
![](images/d7695211f8b6ac0a98b967576bf4285e35edfb09325ee1698bc8e02afccb0c2b.jpg)

Figure 7-10 shows the state of the switch after the FM has executed an unbind command to vPPB2 in VCS0. Unbind of the vPPB causes the switch to assert Link Disable to the port. The port then becomes FM-owned and is controlled by the PPB settings for that physical port. Through the FM API, the FM has CXL.io access to each FM-owned SLD port or FM-owned LD within an MLD component. The FM can choose to prepare the logical device for rebinding by triggering FLR or CXL Reset. The switch prohibits any CXL.io access from the FM to a bound SLD port and any CXL.io access from the FM to a bound LD within an MLD component. The FM API does not support FM generation of CXL.cache or CXL.mem transactions to any port.

Figure 7-10. Example of CXL Switch Configuration after an Unbind Command  
![](images/cd25da07452f6acc8cb87228d6b8b1b67f109ed460f4c067b3abccee1e8e967c.jpg)  
Figure 7-11 shows the state of the switch after the FM executes the bind command to connect VCS1.vPPB1 to the unbound physical port. The successful command execution results in the switch sending a hot-add indication to Host 1. Enumeration, configuration, and operation of the host and Type 3 device is identical to a hot-add of a device.

Figure 7-11. Example of CXL Switch Configuration after a Bind Command  
![](images/e1f42515579fd5005a92bb12bd3647b82c416c01609cb65031777ec994fef6c5.jpg)

## 7.2.3.2 Binding and Unbinding of a Pooled Device

A pooled device contains multiple Logical Devices so that traffic over the physical port can be associated with multiple DS vPPBs. The switch behavior for binding and unbinding of an MLD component is similar to that of an SLD component, but with some notable differences:

1. The physical link cannot be impacted by binding and unbinding of a Logical Device within an MLD component. Thus, PERST#, Hot Reset, and Link Disable cannot be asserted, and there must be no impact to the traffic of other VCSs during the bind or unbind commands.

2. The physical PPB for an MLD port is always owned by the FM. The FM is responsible for port link control, AER, DPC, etc., and manages it using the FM API.

3. The FM may need to manage the pooled device to change memory allocations, enable the LD, etc.

Figure 7-12 shows a CXL switch after boot and before binding of any LDs within the pooled device. Note that the FM is not a PCIe Root Port and that the switch is responsible for enumerating the FMLD after any physical reset since the switch is responsible for proxying commands from FM to the device. The PPB of an MLD port is always owned by the FM since the FM is responsible for configuration and error handling of the physical port. After linkup the FM is notified that it is a Type 3 pooled device.

Figure 7-12. Example of a CXL Switch before Binding of LDs within Pooled Device  
![](images/770743de5ab9e7330ab70008f4ff1b5ca5256ff6685f45a9a988d635e1325376.jpg)  
The FM configures the pooled device for Logical Device 1 (LD 1) and sets its memory allocation, etc. The FM performs a bind command for the unbound vPPB 2 in VCS 0 to LD 1 in the Type 3 pooled device. The switch performs the virtual-to-physical translations such that all CXL.io and CXL.mem transactions that target vPPB 2 in VCS 0 are routed to the MLD port with LD-ID set to 1. Additionally, all CXL.io and CXL.mem transactions from LD 1 in the pooled device are routed according to the host configuration of VCS 0. After binding, the vPPB notifies the VCS 0 host of a hot-add the same as if it were binding a vPPB to an SLD port.

Figure 7-13 shows the state of the switch after binding LD 1 to VCS 0.  
Figure 7-13. Example of a CXL Switch after Binding of LD-ID 1 within Pooled Device  
![](images/ba6eda2feeafbc9cd3eaa84c36f06e7a917004624ba42a13ef8384632389cdd8.jpg)  
The FM configures the pooled device for Logical Device 0 (LD 0) and sets its memory allocation, etc. The FM performs a bind command for the unbound vPPB 1 in VCS 1 to LD 0 in the Type 3 pooled device. The switch performs the virtual to physical translations such that all CXL.io and CXL.mem transactions targeting the vPPB in VCS 1 are routed to the MLD port with LD-ID set to 0. Additionally, all CXL.io and CXL.mem transactions from LD-ID = 0 in the pooled device are routed to the USP of VCS 1. After binding, the vPPB notifies the VCS 1 host of a hot-add the same as if it were binding a vPPB to an SLD port.

Figure 7-14 shows the state of the switch after binding LD 0 to VCS 1.  
Figure 7-14. Example of a CXL Switch after Binding of LD-IDs 0 and 1 within Pooled Device  
![](images/381508338a6ad67223117ad6ac6056c08d8ef4fd5436dd253ee8a70e28df702e.jpg)  
After binding LDs to vPPBs, the switch behavior is different from a bound SLD Port with respect to control, status, error notification, and error handling. Section 7.3.4 describes the differences in behavior for all bits within each register.

## 7.2.4 PPB and vPPB Behavior for MLD Ports

An MLD port provides a virtualized interface such that multiple vPPBs can access LDs over a shared physical interface. As a result, the characteristics and behavior of a vPPB that is bound to an MLD port are different than the behavior of a vPPB that is bound to an SLD port. This section defines the differences between them. If not mentioned in this section, the features and behavior of a vPPB that is bound to an MLD port are the same as those for a vPPB that is bound to an SLD port.

This section uses the following terminology:

• Hardwire to 0 refers to status and optional control register bits that are initialized to 0. Writes to these bits have no effect.

• The term ‘Read/Write with no Effect’ refers to control register bits where writes are recorded but have no effect on operation. Reads to those bits reflect the previously written value or the initialization value if it has not been changed since initialization.

## 7.2.4.1 MLD Type 1 Configuration Space Header

Table 7-2. MLD Type 1 Configuration Space Header

<table><tr><td>Register</td><td>Register Fields</td><td>FM-owned PPB</td><td>All Other vPPBs</td></tr><tr><td rowspan="4">Bridge Control Register</td><td>Parity Error Response Enable</td><td>Supported</td><td>Hardwire to 0s</td></tr><tr><td>SERR# Enable</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>ISA Enable</td><td>Not supported</td><td>Not supported</td></tr><tr><td>Secondary Bus Reset (see Section 7.5 for SBR details for MLD ports)</td><td>Supported</td><td>Read/Write with no effect. Optional FM Event.</td></tr></table>

## 7.2.4.2 MLD PCI\*-compatible Configuration Registers

<table><tr><td>Register/Capability Structure</td><td>Capability Register Fields</td><td>FM-owned PPB</td><td>All vPPBs Bound to the MLD Port</td></tr><tr><td rowspan="6">Command Register</td><td>I/O Space Enable</td><td>Hardwire to 0s</td><td>Hardwire to 0s</td></tr><tr><td>Memory Space Enable</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Bus Master Enable</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Parity Error Response</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>SERR# Enable</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Interrupt Disable</td><td>Supported</td><td>Hardwire to 0s</td></tr><tr><td rowspan="4">Status Register</td><td>Interrupt Status</td><td>Hardwire to 0 (INTx is not supported)</td><td>Hardwire to 0s</td></tr><tr><td>Master Data Parity Error</td><td>Supported</td><td>Hardwire to 0s</td></tr><tr><td>Signaled System Error</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Detected Parity Error</td><td>Supported</td><td>Hardwire to 0s</td></tr></table>

## 7.2.4.3 MLD PCIe Capability Structure

Table 7-4. MLD PCIe Capability Structure (Sheet 1 of 3)

<table><tr><td>Register/Capability Structure</td><td>Capability Register Fields</td><td>FM-owned PPB</td><td>All vPPBs Bound to the MLD Port</td></tr><tr><td rowspan="3">Device Capabilities Register</td><td>Max_Payload_Size Supported</td><td>Configured by the FM to the max value supported by switch hardware and min value configured in all vPPBs</td><td>Mirrors PPB</td></tr><tr><td>Phantom Functions Supported</td><td>Hardwire to 0s</td><td>Hardwire to 0s</td></tr><tr><td>Extended Tag Field Supported</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Device Control Register</td><td>Max_Payload_Size</td><td>Configured by the FM to Max_Payload Size Supported</td><td>Read/Write with no effect</td></tr><tr><td>Link Capabilities Register</td><td>Link Bandwidth Notification Capability</td><td>Hardwire to 0s</td><td>Hardwire to 0s</td></tr></table>

Table 7-4. MLD PCIe Capability Structure (Sheet 2 of 3)

<table><tr><td>Register/Capability Structure</td><td>Capability Register Fields</td><td>FM-owned PPB</td><td>All vPPBs Bound to the MLD Port</td></tr><tr><td rowspan="2">Link Capabilities</td><td>ASPM Support</td><td>No L0s support</td><td>No L0s support</td></tr><tr><td>Clock Power Management</td><td>No PM L1 Substates support</td><td>No PM L1 Substates support</td></tr><tr><td rowspan="9">Link Control</td><td>ASPM Control</td><td>Supported</td><td>Switch only enables ASPM if all vPPBs that are bound to this MLD have enabled ASPM</td></tr><tr><td>Link Disable</td><td>Supported</td><td>Switch handles it as an unbind by discarding all traffic to/from this LD-ID</td></tr><tr><td>Retrain Link</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Common Clock Configuration</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Extended Synch</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Hardware Autonomous Width Disable</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Link Bandwidth Management Interrupt Enable</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Link Autonomous Bandwidth Interrupt Enable</td><td>Supported</td><td>Supported per vPPB. Each host can be notified of autonomous speed change</td></tr><tr><td>DRS Signaling Control</td><td>Supported</td><td>Switch sends DRS after receiving DRS on the link and after binding of the vPPB to an LD</td></tr><tr><td rowspan="6">Link Status register</td><td>Current Link Speed</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Negotiated Link Width</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Link Training</td><td>Supported</td><td>Hardwire to 0s</td></tr><tr><td>Slot Clock Configuration</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Data Link Layer Active</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Link Autonomous Bandwidth Status</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td rowspan="2">Slot Capabilities Register</td><td>Hot-Plug Surprise</td><td>Hardwire to 0s</td><td>Hardwired to 0s</td></tr><tr><td>Physical Slot Number</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td rowspan="8">Slot Status Register</td><td>Attention Button Pressed</td><td>Supported</td><td>Mirrors PPB or is set by the switch on unbind</td></tr><tr><td>Power Fault Detected</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>MRL Sensor Changed</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Presence Detect Changed</td><td>Supported</td><td>Mirrors PPB or is set by the switch on unbind</td></tr><tr><td>MRL Sensor State</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Presence Detect State</td><td>Supported</td><td>Mirrors PPB or set by the switch on bind or unbind</td></tr><tr><td>Electromechanical Interlock Status</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Data Link Layer State Changed</td><td>Supported</td><td>Mirrors PPB or set by the switch on bind or unbind</td></tr><tr><td>Device Capabilities 2 Register</td><td>OBFF Supported</td><td>Hardwire to 0s</td><td>Hardwire to 0s</td></tr></table>

Table 7-4. MLD PCIe Capability Structure (Sheet 3 of 3)

<table><tr><td>Register/Capability Structure</td><td>Capability Register Fields</td><td>FM-owned PPB</td><td>All vPPBs Bound to the MLD Port</td></tr><tr><td rowspan="5">Device Control 2 Register</td><td>ARI Forwarding Enable</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Atomic Op Egress Blocking</td><td>Supported</td><td>Mirrors PPB. Read/Write with no effect</td></tr><tr><td>LTR Mechanism Enabled</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Emergency Power Reduction Request</td><td>Supported</td><td>Read/Write with no effect. Optional FM notification.</td></tr><tr><td>End-End TLP Prefix Blocking</td><td>Supported</td><td>Mirrors PPB. Read/Write with no effect</td></tr><tr><td rowspan="8">Link Control 2 Register</td><td>Target Link Speed</td><td>Supported</td><td>Read/Write with no effect. Optional FM notification.</td></tr><tr><td>Enter Compliance</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Hardware Autonomous Speed Disable</td><td>Supported</td><td>Read/Write with no effect. Optional FM notification.</td></tr><tr><td>Selectable De-emphasis</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Transmit Margin</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Enter Modified Compliance</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Compliance SOS</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Compliance Preset/De-emphasis</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td rowspan="11">Link Status 2 Register</td><td>Current De-emphasis Level</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Equalization 8.0 GT/s Complete</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Equalization 8.0 GT/s Phase 1 Successful</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Equalization 8.0 GT/s Phase 2 Successful</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Equalization 8.0 GT/s Phase 3 Successful</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Link Equalization Request 8.0 GT/s</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Retimer Presence Detected</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Two Retimers Presence Detected</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Crosslink Resolution</td><td>Hardwire to 0s</td><td>Hardwire to 0s</td></tr><tr><td>Downstream Component Presence</td><td>Supported</td><td>Reflects the binding state of the vPPB</td></tr><tr><td>DRS Message Received</td><td>Supported</td><td>Switch sends DRS after receiving DRS on the link and after binding of the vPPB to an LD</td></tr></table>

Table 7-5. MLD Secondary PCIe Capability Structure

## 7.2.4.4 MLD PPB Secondary PCIe Capability Structure

All fields in the Secondary PCIe Capability Structure for a Virtual PPB shall behave identically to PCIe except the following:

<table><tr><td>Register/Capability Structure</td><td>Capability Register Fields</td><td>FM-owned PPB</td><td>All vPPBs Bound to the MLD Port</td></tr><tr><td rowspan="3">Link Control 3 Register</td><td>Perform Equalization</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Link Equalization Request Interrupt Enable</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Enable Lower SKP OS Generation Vector</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Lane Error Status Register</td><td>All fields</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Lane Equalization Control Register</td><td>All fields</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>Data Link Feature Capabilities Register</td><td>All fields</td><td>Supported</td><td>Hardwire to 0s</td></tr><tr><td>Data Link Feature Status Register</td><td>All fields</td><td>Supported</td><td>Hardwire to 0s</td></tr></table>

## 7.2.4.5 MLD Physical Layer 16.0 GT/s Extended Capability

All fields in the Physical Layer 16.0 GT/s Extended Capability Structure for a Virtual PPB shall behave identically to PCIe except the following:

<table><tr><td>Register/Capability Structure</td><td>Capability Register Fields</td><td>FM-owned PPB</td><td>All vPPBs Bound to the MLD Port</td></tr><tr><td>16.0 GT/s Status Register</td><td>All fields</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>16.0 GT/s Local Data Parity Mismatch Status Register</td><td>Local Data Parity Mismatch Status Register</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>16.0 GT/s First Retimer Data Parity Mismatch Status Register</td><td>First Retimer Data Parity Mismatch Status</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>16.0 GT/s Second Retimer Data Parity Mismatch Status Register</td><td>Second Retimer Data Parity Mismatch Status</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>16.0 GT/s Lane Equalization Control Register</td><td>Downstream Port 16.0 GT/s Transmitter Preset</td><td>Supported</td><td>Mirrors PPB</td></tr></table>

## 7.2.4.6 MLD Physical Layer 32.0 GT/s Extended Capability

Table 7-7. MLD Physical Layer 32.0 GT/s Extended Capability

<table><tr><td>Register/Capability Structure</td><td>Capability Register Fields</td><td>FM-owned PPB</td><td>All vPPBs Bound to the MLD Port</td></tr><tr><td>32.0 GT/s Capabilities Register</td><td>All fields</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>32.0 GT/s Control Register</td><td>All fields</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td rowspan="2">32.0 GT/s Status Register</td><td>Link Equalization Request 32.0 GT/s</td><td>Supported</td><td>Read/Write with no effect</td></tr><tr><td>All fields except Link Equalization Request 32.0 GT/s</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Received Modified TS Data 1 Register</td><td>All fields</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Received Modified TS Data 2 Register</td><td>All fields</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>Transmitted Modified TS Data 1 Register</td><td>All fields</td><td>Supported</td><td>Mirrors PPB</td></tr><tr><td>32.0 GT/s Lane Equalization Control Register</td><td>Downstream Port 32.0 GT/s Transmitter Preset</td><td>Supported</td><td>Mirrors PPB</td></tr></table>

## 7.2.4.7 MLD Lane Margining at the Receiver Extended Capability

MLD Lane Margining at the Receiver Extended Capability

<table><tr><td>Register/Capability Structure</td><td>Capability Register Fields</td><td>FM-owned PPB</td><td>All vPPBs Bound to the MLD Port</td></tr><tr><td>Margining Port Status Register</td><td>All fields</td><td>Supported</td><td>Always indicates Margining Ready and Margining Software Ready</td></tr><tr><td>Margining Lane Control Register</td><td>All fields</td><td>Supported</td><td>Read/Write with no effect</td></tr></table>

## 7.2.5 MLD ACS Extended Capability

CXL.io Requests and Completions are routed to the USP.

Table 7-9. MLD ACS Extended Capability

<table><tr><td>Register/Capability Structure</td><td>Capability Register Fields</td><td>FM-owned PPB</td><td>All vPPBs Bound to the MLD Port</td></tr><tr><td>ACS Capability Register</td><td>All fields</td><td>Supported</td><td>Supported because a vPPB can be bound to any port type</td></tr><tr><td rowspan="10">ACS Control Register</td><td>ACS Source Validation Enable</td><td>Hardwire to 0</td><td>Read/Write with no effect</td></tr><tr><td>ACS Translation Blocking Enable</td><td>Hardwire to 0</td><td>Read/Write with no effect</td></tr><tr><td>ACS P2P Request Redirect Enable</td><td>Hardwire to 1</td><td>Read/Write with no effect</td></tr><tr><td>ACS P2P Completion Redirect Enable</td><td>Hardwire to 1</td><td>Read/Write with no effect</td></tr><tr><td>ACS Upstream Forwarding Enable</td><td>Hardwire to 0</td><td>Read/Write with no effect</td></tr><tr><td>ACS P2P Egress Control Enable</td><td>Hardwire to 0</td><td>Read/Write with no effect</td></tr><tr><td>ACS Direct Translated P2P Enable</td><td>Hardwire to 0</td><td>Read/Write with no effect</td></tr><tr><td>ACS I/O Request Blocking Enable</td><td>Hardwire to 0</td><td>Read/Write with no effect</td></tr><tr><td>ACS DSP Memory Target Access Control</td><td>Hardwire to 0s</td><td>Read/Write with no effect</td></tr><tr><td>ACS Unclaimed Request Redirect Control</td><td>Hardwire to 0</td><td>Read/Write with no effect</td></tr></table>

## 7.2.6 MLD PCIe Extended Capabilities

All fields in the PCIe Extended Capability structures for a vPPB shall behave identically to PCIe.

## 7.2.7 MLD Advanced Error Reporting Extended Capability

AER in an MLD port is separated into Triggering, Notifications, and Reporting. Triggering and AER Header Logging is handled at switch ingress and egress using switch-vendorspecific means. Notification is also switch-vendor specific, but it results in the vPPB logic for all vPPBs that are bound to the MLD port being informed of the AER errors that have been triggered. The vPPB logic is responsible for generating the AER status and error messages for each vPPB based on the AER Mask and Severity registers.

vPPBs that are bound to an MLD port support all the AER Mask and Severity configurability; however, some of the Notifications are suppressed to avoid confusion.

The PPB has its own AER Mask and Severity registers and the FM is notified of error conditions based on the Event Notification settings.

Errors that are not vPPB specific are provided to the host with a header log containing all 1s data. The hardware header log is provided only to the FM through the PPB.

Table 7-10 lists the AER Notifications and their routing indications for PPBs and vPPBs.  
Table 7-10. MLD Advanced Error Reporting Extended Capability

<table><tr><td>Hardware Triggers</td><td>AER Error</td><td>FM-owned PPB</td><td>All vPPBs Bound to the MLD Port</td></tr><tr><td rowspan="23">AER Notifications</td><td>Data Link Protocol Error</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Surprise Down Error</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Poisoned TLP Received</td><td>Supported</td><td>Hardwire to 0</td></tr><tr><td>Flow Control Protocol Error</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Completer Abort</td><td>Supported</td><td>Supported to the vPPB that generated it</td></tr><tr><td>Unexpected Completion</td><td>Supported</td><td>Supported to the vPPB that received it</td></tr><tr><td>Receiver Overflow</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Malformed TLP</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>ECRC Error</td><td>Supported</td><td>Hardwire to 0</td></tr><tr><td>Unsupported Request</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>ACS Violation</td><td>Supported</td><td>Hardwire to 0</td></tr><tr><td>Uncorrectable Internal Error</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td> $MC^1$  Blocked</td><td>Supported</td><td>Hardwire to 0</td></tr><tr><td>Atomic Op Egress Block</td><td>Supported</td><td>Hardwire to 0</td></tr><tr><td>E2E TLP Prefix Block</td><td>Supported</td><td>Hardwire to 0</td></tr><tr><td>Poisoned TLP Egress block</td><td>Supported</td><td>Hardwire to 0</td></tr><tr><td>Bad TLP (correctable)</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Bad DLLP (correctable)</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Replay Timer Timeout (correctable)</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Replay Number Rollover (correctable)</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Other Advisory Non-Fatal (correctable)</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Corrected Internal Error Status (correctable)</td><td>Supported</td><td>Supported per vPPB</td></tr><tr><td>Header Log Overflow Status (correctable)</td><td>Supported</td><td>Supported per vPPB</td></tr></table>

1. Refers to Multicast.

## 7.2.8

## MLD DPC Extended Capability

Downstream Port Containment has special behavior for an MLD Port. The FM configures the AER Mask and Severity registers in the PPB and also configures the AER Mask and Severity registers in the FMLD in the pooled device. As in an SLD port an unmasked uncorrectable error detected in the PPB and an ERR\_NONFATAL and/or ERR\_FATAL received from the FMLD can trigger DPC.

Continuing the model of the ultimate receiver being the entity that detects and reports errors, the ERR\_FATAL and ERR\_NONFATAL messages sent by a Logical Device can trigger a virtual DPC in the PPB. When a virtual DPC is triggered, the switch discards all traffic received from and transmitted to that specific LD. The LD remains bound to the vPPB and the FM is also notified. Software triggered DPC also triggers virtual DPC on a vPPB.

When the DPC trigger is cleared the switch autonomously allows passing of traffic to/ from the LD. Reporting of the DPC trigger to the host is identical to PCIe.

Table 7-11. MLD PPB DPC Extended Capability

<table><tr><td>Register/ Capability Structure</td><td>Capability Register Fields</td><td>FM-owned PPB</td><td>All vPPBs Bound to the MLD Port</td></tr><tr><td rowspan="2">DPC Control Register</td><td>DPC Trigger Enable</td><td>Supported</td><td>Switch internally detected unmasked uncorrectable errors do not trigger virtual DPC</td></tr><tr><td>DPC Trigger Reason</td><td>Supported</td><td>Unmasked uncorrectable error is not a valid value</td></tr></table>

## 7.2.9 Switch Mailbox CCI

CXL Switch Mailbox CCIs optional. They are exposed as PCIe Endpoints with a Type 0 configuration space. In Single VCS and Multiple VCS, the Mailbox CCI is optional. If implemented, the Mailbox CCI shall be exposed to the Host in one of two possible configurations. In the first, it is exposed as an additional PCIe function in the Upstream Switch Port, as illustrated in Figure 7-15.

Figure 7-15. Multi-function Upstream vPPB

![](images/d74180310ee5242a98e3710bdbd27435d62c81ef5bd152149cc90503b4578d60.jpg)

Switch Mailbox CCIs may also be exposed in a VCS with no vPPBs. In this configuration, the Mailbox CCI device is the only PCIe function that is present in the Upstream Port, as illustrated in Figure 7-16.

Figure 7-16. Single-function Mailbox CCI

![](images/b26235dc49444c4c02dcf6a5dd5d8a7bfc6f37c632fe31898dbc035ce7428177.jpg)

# CXL.io, CXL.cachemem Decode and Forwarding

## 7.3.1 CXL.io

Within a VCS, the CXL.io traffic must obey the same request, completion, address decode, and forwarding rules for a Switch as defined in PCIe Base Specification. There are additional decode rules that are defined to support an eRCD connected to a switch (see Section 9.12.4).

## 7.3.1.1 CXL.io Decode

When a TLP is decoded by a PPB, it determines the destination PPB to route the TLP based on the rules defined in PCIe Base Specification. Unless specified otherwise, all rules defined in PCIe Base Specification apply for routing of CXL.io TLPs. TLPs must be routed to PPBs within the same VCS. Routing of TLPs to and from an FM-owned PPB need to follow additional rules as defined in Section 7.2.3. P2P inside a Switch complex is limited to PPBs within a VCS.

## 7.3.1.2 RCD Support

RCDs are not supported behind ports that are configured to operate as FM-owned PPBs. When connected behind a switch, RCDs must appear to software as RCiEP devices. The mechanism defined in this section enables this functionality.

Figure 7-17. CXL Switch with a Downstream Link Auto-negotiated to Operate in RCD Mode

![](images/c6915a97d7255a3d5e8b36223c556cd4a8e62e9645d3ab639765fa56bca3d811.jpg)  
The CXL Extensions DVSEC for Ports (see Section 8.1.5) defines the alternate MMIO and Bus Range Decode windows for forwarding of requests to eRCDs connected behind a Downstream Port.

## 7.3.2 CXL.cache

If the switch does not support CXL.cache protocol enhancements that enable multidevice scaling (as described in Section 8.2.4.28), only one of the CXL SLD ports in the VCS is allowed to be enabled to support Type 1 devices or Type 2 devices. Requests and Responses received on the USP are routed to the associated DSP and vice-versa. Therefore, additional decode registers are not required for CXL.cache for such switches.

If the switch supports CXL.cache protocol enhancements that enable multi-device scaling, more than one of the CXL SLD ports in the VCS can be configured to support Type 1 devices or Type 2 devices. Section 9.15.2 and Section 9.15.3 describe how such a CXL switch routes CXL.cache traffic.

CXL.cache is not supported over FM-owned PPBs.

## 7.3.3 CXL.mem

The HDM Decode DVSEC capability contains registers that define the Memory Address Decode Ranges for Memory. CXL.mem requests originate from the Host/RP and flow downstream to the Devices through the switch. CXL.mem responses originate from the Device and flow upstream to the RP.

## 7.3.3.1 CXL.mem Request Decode

All CXL.mem Requests received by the USP target one of the Downstream PPBs within the VCS. The address decode registers in the VCS determine the downstream VCS PPB to route the request. The VCS PPB may be a VCS-owned PPB or an FM-owned PPB. See Section 7.3.4 for additional routing rules.

## 7.3.3.2 CXL.mem Response Decode

CXL.mem Responses received by the DSP target one and only one Upstream Port. For VCS-owned PPB the responses are routed to the Upstream Port of that VCS. Responses received on an FM-owned PPB go through additional decode rules to determine the VCS ID to route the requests to. See Section 7.3.4 for additional routing rules.

## 7.3.4 FM-owned PPB CXL Handling

All PPBs are FM-owned. A PPB can be connected to a port that is disconnected, linked up as an RCD, CXL SLD, or CXL MLD. SLD components can be bound to a host or unbound. Unbound SLD components can be accessed by the FM using CXL.io transactions via the FM API. LDs within an MLD component can be bound to a host or unbound. Unbound LDs are FM-owned and can be accessed through the switch using CXL.io transactions via the FM API.

For all CXL.io transactions driven by the FM API, the switch acts as a virtual Root Complex for PPBs and Endpoints. The switch is responsible for enumerating the functions associated with that port and sending/receiving CXL.io traffic.

## 7.4 CXL Switch PM

## 7.4.1 CXL Switch ASPM L1

ASPM L1 for switch Ports is as defined in Chapter 10.0.

## 7.4.2 CXL Switch PCI-PM and L2

A vPPB in a VCS operates the same as a PCIe vPPB for handling of PME messages.

## 7.4.3 CXL Switch Message Management

CXL VDMs are of the “Local - Terminate at Receiver” type. When a switch is present in the hierarchy, the switch implements the message aggregation function and therefore all Host-generated messages terminate at the switch. The switch aggregation function is responsible for regenerating these messages on the Downstream Port. All messages and responses generated by the directly attached CXL components are aggregated and consolidated by the DSP and consolidated messages or responses are generated by the USP.

The PM message credit exchanges occur between the Host and Switch Aggregation port, and separately between the Switch Aggregation Port and device.

Table 7-12. CXL Switch Message Management

<table><tr><td>Message Type</td><td>Type</td><td>Switch Message Aggregation and Consolidation Responsibility</td></tr><tr><td>PM Reset Messages</td><td rowspan="4">Host Initiated</td><td rowspan="4">Host-generated requests terminate at Upstream Port, broadcast messages to all ports within VCS hierarchy</td></tr><tr><td>Sx Entry</td></tr><tr><td>GPF Phase 1 Request</td></tr><tr><td>GPF Phase 2 Request</td></tr><tr><td>PM Reset Acknowledge</td><td rowspan="4">Device Responses</td><td rowspan="4">Device-generated responses terminate at Downstream Port within VCS hierarchy. Switch aggregates responses from all other connected ports within VCS hierarchy.</td></tr><tr><td>Sx Entry</td></tr><tr><td>GPF Phase 1 Response</td></tr><tr><td>GPF Phase 2 Response</td></tr></table>

## 7.5 CXL Switch RAS

Table 7-13. CXL Switch RAS

<table><tr><td>Host Action</td><td>Description</td><td>Switch Action for Non-pooled Devices</td><td>Switch Action for Pooled Devices</td></tr><tr><td>Switch boot</td><td>Optional power-on reset pin</td><td>Assert PERST#Deassert PERST#</td><td>Assert PERST#Deassert PERST#</td></tr><tr><td>Upstream PERST# assert</td><td>VCS fundamental reset</td><td>Send Hot Reset</td><td>Write to MLD DVSEC to trigger LD Hot Reset of the associated LDNote: Only the FMLD provides the MLD DVSEC capability.</td></tr><tr><td>FM port reset</td><td>Reset of an FM-owned DSP</td><td>Send Hot Reset</td><td>Send Hot Reset</td></tr><tr><td>PPB Secondary Bus Reset</td><td>Reset of an FM-owned DSP</td><td>Send Hot Reset</td><td>Write to MLD DVSEC to trigger LD Hot Reset of all LDs</td></tr><tr><td>USP received Hot Reset</td><td>VCS fundamental reset</td><td>Send Hot Reset</td><td>Write to MLD DVSEC to trigger LD Hot Reset of the associated LD</td></tr><tr><td>USP vPPB Secondary Bus Reset</td><td>VCS US SBR</td><td>Send Hot Reset</td><td>Write to MLD DVSEC to trigger LD Hot Reset of the associated LD</td></tr><tr><td>DSP vPPB Secondary Bus Reset</td><td>VCS DS SBR</td><td>Send Hot Reset</td><td>Write to MLD DVSEC to trigger LD Hot Reset of the associated LD</td></tr><tr><td>Host writes FLR</td><td>Device FLR</td><td>No switch involvement</td><td>No switch involvement</td></tr><tr><td>Switch watchdog timeout</td><td>Switch fatal error</td><td>Equivalent to power-on reset</td><td>Equivalent to power-on reset</td></tr></table>

Because the MLD DVSEC only exists in the FMLD, the switch must use the FM LD-ID in the CXL.io configuration write transaction when triggering LD reset.

## 7.6 Fabric Manager Application Programming Interface

This section describes the Fabric Manager Application Programming Interface.

## 7.6.1 CXL Fabric Management

CXL devices can be configured statically or dynamically via a Fabric Manager (FM), an external logical process that queries and configures the system’s operational state using the FM commands defined in this specification. The FM is defined as the logical process that decides when reconfiguration is necessary and initiates the commands to perform configurations. It can take any form, including, but not limited to, software running on a host machine, embedded software running on a BMC, embedded firmware running on another CXL device or CXL switch, or a state machine running within the CXL device itself.

## 7.6.2 Fabric Management Model

CXL devices are configured by FMs through the Fabric Manager Application Programming Interface (FM API) command sets, as defined in Section 8.2.9.10, through a CCI. A CCI is exposed through a device’s Mailbox registers (see Section 8.2.8.4) or through an MCTP-capable interface. See Section 9.19 for details on the CCI processing of these commands.

Figure 7-18. Example of Fabric Management Model  
![](images/10beb224234813c186a4ab3667ad6e7c37851d5acadf0f4bdb1e4e72bf93f346.jpg)

FMs issue request messages and CXL devices issue response messages. CXL components may also issue the “Event Notification” request if notifications are supported by the component and the FM has requested notifications from the component using the Set MCTP Event Interrupt Policy command. See Section 7.6.3 for transport protocol details.

The following list provides a number of examples of connectivity between an FM and a component’s CCI, but should not be considered a complete list:

• An FM directly connected to a CXL device through any MCTP-capable interconnect can issue FM commands directly to the device. This includes delivery over MCTPcapable interfaces such as SMBus as well as VDM delivery over a standard PCIe tree topology where the responder is mapped to a CXL attached device.

• An FM directly connected to a CXL switch may use the switch to tunnel FM commands to MLD components directly attached to the switch. In this case, the FM issues the “Tunnel Management Command” command to the switch specifying the switch port to which the device is connected. Responses are returned to the FM by the switch. In addition to MCTP message delivery, the FM command set provides the FM with the ability to have the switch proxy config cycles and memory accesses to a Downstream Port on the FM’s behalf.

• An FM or part of the overall FM functionality may be embedded within a CXL component. The communication interface between such an embedded FM FW module and the component hardware is considered a vendor implementation detail and is not covered in this specification.

## 7.6.3 CCI Message Format and Transport Protocol

CCI commands are transmitted across MCTP-capable interconnects as MCTP messages using the format defined in Figure 7-19 and listed in Table 7-14.

Figure 7-19. CCI Message Format

<table><tr><td>31</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>18</td><td>17</td><td>16</td><td>15</td><td>14</td><td>13</td><td>12</td><td>11</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td><td>0</td><td>Byte Offset</td></tr><tr><td colspan="8">Command Opcode [7:0]</td><td colspan="8">Reserved</td><td colspan="8">Message Tag</td><td colspan="4">Reserved</td><td colspan="4">Message Category</td><td>000h</td></tr><tr><td>BO</td><td colspan="2">Reserved</td><td colspan="21">Message Payload Length</td><td colspan="8">Command Opcode [15:8]</td><td>004h</td></tr><tr><td colspan="16">Vendor Specific Extended Status</td><td colspan="16">Return Code</td><td>008h</td></tr><tr><td colspan="32">Message Payload(Variable Size)</td><td>00Ch...</td></tr></table>

Table 7-14. CCI Message Format (Sheet 1 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Bits[3:0]:Message Category:Type of CCI message:- 0h = Request- 1h = Response- All other encodings are reservedBits[7:4]:Reserved</td></tr><tr><td>1h</td><td>1</td><td>Message Tag:Tag number assigned to request messages by the Requester used to track response messages when multiple request messages are outstanding. Response messages shall use the tag number from the corresponding Request message.</td></tr><tr><td>2h</td><td>1</td><td>Reserved</td></tr><tr><td>3h</td><td>2</td><td>Command Opcode[15:0]:As defined inTable 8-37, Table 8-126, and Table 8-215.</td></tr><tr><td>5h</td><td>2</td><td>Message Payload Length[15:0]:Expressed in bytes. As defined in Table 8-37, Table 8-126, and Table 8-215.</td></tr><tr><td>7h</td><td>1</td><td>Bits[4:0]:Message Payload Length[20:16]:Expressed in bytes. As defined inTable 8-37, Table 8-126, and Table 8-215.Bits[6:5]:Reserved.Bit[7]:Background Operation (BO):As defined inSection 8.2.8.4.6.</td></tr></table>

Table 7-14. CCI Message Format (Sheet 2 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>8h</td><td>2</td><td>Return Code[15:0]: As defined in Table 8-34. Must be 0 for Request messages.</td></tr><tr><td>Ah</td><td>2</td><td>Vendor Specific Extended Status[15:0]: As defined in Section 8.2.8.4.6. Must be 0 for Request messages.</td></tr><tr><td>Ch</td><td>Varies</td><td>Message Payload: Variably sized payload for message in little-endian format. The length of this field is specified in the Message Payload Length[20:0] fields above. The format depends on Opcode and Message Category, as defined in Table 8-37, Table 8-126, and Table 8-215.</td></tr></table>

Commands from the FM API Command Sets may be transported as MCTP messages as defined in CXL Fabric Manager API over MCTP Binding Specification (DSP0234). All other CCI commands may be transported as MCTP messages as defined by the respective binding specification, such as CXL Type 3 Component Command Interface over MCTP Binding (DSP0281).

## 7.6.3.1 Transport Details for MLD Components

MLD components that do not implement an MCTP-capable interconnect other than their CXL interface shall expose a CCI through their CXL interface(s) using MCTP PCIe VDM Transport Binding Specification (DSP0238). FMs shall use the Tunnel Management Command to pass requests to the FM-owned LD, as illustrated in Figure 7-20.

Figure 7-20. Tunneling Commands to an MLD through a CXL Switch

![](images/3d89e305781c3e0344b4c0c03ca5ee074dc7803807df2039bab2a78c007db702.jpg)

## 7.6.4 CXL Switch Management

Dynamic configuration of a switch by an FM is not required for basic switch functionality, but is required to support MLDs or CXL fabric topologies.

## 7.6.4.1 Initial Configuration

The non-volatile memory of the switch stores, in a vendor-specific format, all necessary configuration settings that are required to prepare the switch for initial operation. This includes:

• Port configuration, including direction (upstream or downstream), width, supported rates, etc.

• Virtual CXL Switch configuration, including number of vPPBs for each VCS, initial port binding configuration, etc.

• CCI access settings, including any vendor-defined permission settings for management.

## 7.6.4.2 Dynamic Configuration

After initial configuration is complete and a CCI on the switch is operational, an FM can send Management Commands to the switch.

An FM may perform the following dynamic management actions on a CXL switch:

• Query switch information and configuration details

• Bind or Unbind ports

• Register to receive and handle event notifications from the switch (e.g., Hot-Plug, surprise removal, and failures)

When a switch port is connected to a downstream PCIe switch, and that port is bound to a vPPB, the management of that PCIe switch and its downstream device will be handled by the VCS’s host, not the FM.

## 7.6.4.3

## MLD Port Management

A switch with MLD Ports requires an FM to perform the following management activities:

• MLD discovery

• LD binding/unbinding

• Management Command Tunneling

## 7.6.5 MLD Component Management

The FM can connect to an MLD over a direct connection or by tunneling its management commands through the CCI of the CXL switch to which the device is connected. The FM can perform the following operations:

• Memory allocation and QoS Telemetry management

• Security (e.g., LD erasure after unbinding)

• Error handling

Figure 7-21. Example of MLD Management Requiring Tunneling  
![](images/62aad942db960f615095097c0887a328e8f7c4cf8acf69ca3ed0c55b636d5490.jpg)

## 7.6.6

## Management Requirements for System Operations

This section presents examples of system use cases to highlight the role and responsibilities of the FM in system management. These use case discussions also serve to itemize the FM commands that CXL devices must support to facilitate each specific system behavior.

## 7.6.6.1 Initial System Discovery

As the CXL system initializes, the FM can begin discovering all direct attached CXL devices across all supported media interfaces. Devices supporting the FM API may be discovered using transport specific mechanisms such as the MCTP discovery process, as defined in MCTP Base Specification (DSP0236).

When a component is discovered, the FM shall issue the Identify command (see Section 8.2.9.1.1) prior to issuing any other commands to check the component’s type and its maximum supported command message size. A return of “Retry Required” indicates that the component is not yet ready to accept commands. After receiving a successful response to the Identify request, the FM may issue the Set Response Message Limit command (see Section 8.2.9.1.4) to limit the size of response messages from the component based on the size of the FM’s receive buffer. The FM shall not issue any commands with input arguments such that the command’s response message exceeds the FM’s maximum supported message size. Finally, the FM issues Get Log, as defined in Section 8.2.9.5.2.1, to read the Command Effects Log to determine which command opcodes are supported.

## 7.6.6.2 CXL Switch Discovery

After a CXL switch is released from reset (i.e., PERST# has been deasserted), it loads its initial configuration from non-volatile memory. Ports configured as DS PPBs will be released from reset to link up. Upon detection of a switch, the FM will query its configuration, capabilities, and connected devices. The Physical Switch Command Set is required for all switches implementing FM API support. The Virtual Switch Command Set is required for all switches that support multiple host ports.

An example of an FM Switch discovery process is as follows:

1. FM issues Identify Switch Device to check switch port count, enabled port IDs, number of supported LDs, and enabled VCS IDs.

2. FM issues Get Physical Port State for each enabled port to check port configuration (US or DS), link state, and attached device type. This allows the FM to check for any port link-up issues and create an inventory of devices for binding. If any MLD components are discovered, the FM can begin MLD Port management activities.

3. If the switch supports multiple host ports, FM issues Get Virtual CXL Switch Info for each enabled VCS to check for all bound vPPBs in the system and create a list of binding targets.

## 7.6.6.3

## MLD and Switch MLD Port Management

MLDs must be connected to a CXL switch to share their LDs among VCSs. If an MLD is discovered in the system, the FM will need to prepare it for binding. A switch must support the MLD Port Command Set to support the use of MLDs. All MLD components shall support the MLD Component Command Set.

1. FM issues management commands to the device’s LD FFFFh using Tunnel Management Command.

2. FM can execute advanced or vendor-specific management activities, such as encryption or authentication, using the Send LD CXL.io Configuration Request and Send LD CXL.io Memory Request commands.

## 7.6.6.4 Event Notifications

Events can occur on both devices and switches. The event types and records are listed in Section 7.6.8 for FM API events and in Section 8.2.9.2 for component events. The Event Records framework is defined in Section 8.2.9.2.1 to provide a standard event record format that all CXL components shall use when reporting events to the managing entity. The managing entity specifies the notification method, such as MSI/ MSI-X, EFN VDM, or MCTP Event Notification. The Event Notification message can be signaled by a device or by a switch; the notification always flows toward the managing entity. An Event Record is not sent with the Event Notification message. After the managing entity knows that an event has occurred, the entity can use component commands to read the Event Record.

1. To facilitate some system operations, the FM requires event notifications so it can execute its role in the process in a timely manner (e.g., notifying hosts of an asserted Attention Button on an MLD during a Managed Hot-Removal). If supported by the device, the FM can check and modify the current event notification settings with the Events command set.

2. If supported by the device, the event logs can be read with the Get Event Records command to check for any error events experienced by the device that might impact normal operation.

## 7.6.6.5 Binding Ports and LDs on a Switch

Once all devices, VCSs, and vPPBs have been discovered, the FM can begin binding ports and LDs to hosts as follows:

1. FM issues the Bind vPPB command specifying a physical port, VCS ID and vPPB index to bind the physical port to the vPPB. An LD-ID must also be specified if the physical port is connected to an MLD. The switch is permitted to initiate a Managed Hot-Add if the host has already booted, as defined in Section 9.9.

2. Upon completion of the binding process, the switch notifies the FM by generating a Virtual CXL Switch Event Record.

## 7.6.6.6

## Unbinding Ports and LDs on a Switch

The FM can unbind devices or LDs from a VCS with the following steps:

1. FM issues the Unbind vPPB command specifying a VCS ID and vPPB index to unbind the physical port from the vPPB. The switch initiates a Managed Hot-Remove or Surprise Hot-Remove depending on the command options, as defined in PCIe Base Specification.

2. Upon completion of the unbinding process, the switch will generate a Virtual CXL Switch Event Record.

## 7.6.6.7 Hot-Add and Managed Hot-Removal of Devices

When a device is Hot-Added to an unbound port on a switch, the FM receives a notification and is responsible for binding as described in the steps below:

1. The switch notifies the FM by generating Physical Switch Event Records as the Presence Detect sideband signal is asserted and the port links up.

2. FM issues the Get Physical Port State command for the physical port that has linked up to discover the connected device type. The FM can now bind the physical port to a vPPB. If it’s an MLD, then the FM can proceed with MLD Port management activities; otherwise, the device is ready for binding.

When a device is Hot-Removed from an unbound port on a switch, the FM receives a notification. The switch notifies the FM by generating Physical Switch Event Records as the Presence Detect sideband is deasserted and the associated port links down.

1. The switch notifies the FM by generating Physical Switch Event Records as the Presence Detect sideband is deasserted and the associated port links down.

When an SLD or PCIe device is Hot-Added to a bound port, the FM can be notified but is not involved. When a Surprise or Managed Hot-Removal of an SLD or PCIe device occurs on a bound port, the FM can be notified but is not involved.

A bound port will not advertise support for MLDs during negotiation, so MLD components will link up as an SLD.

The FM manages managed hot-removal of MLDs as follows:

1. When the Attention Button sideband is asserted on an MLD port, the Attention state bit is updated in the corresponding PPB and vPPB CSRs and the switch notifies the FM and hosts with LDs that are bound and below that MLD port. The hosts are notified with the MSI/MSI-X interrupts assigned to the affected vPPB and a Virtual CXL Switch Event Record is generated.

2. As defined in PCIe Base Specification, hosts will read the Attention State bit in their vPPB’s CSR and prepare for removal of the LD. When a host is ready for the LD to be removed, it will set the Attention LED bit in the associated vPPB’s CSR. The

switch records these CSR updates by generating Virtual CXL Switch Event Records. The FM unbinds each assigned LD with the Unbind vPPB command as it receives notifications from each host.

3. When all host handshakes are complete, the MLD is ready for removal. The FM uses the Send PPB CXL.io Configuration Request command to set the Attention LED bit in the MLD port PPB to indicate that the MLD can be physically removed. The timeout value for the host handshakes to complete is implementation specific. There is no requirement for the FM to force the unbind operation, but it can do so using the “Simulate Surprise Hot-Remove” unbinding option in the Unbind vPPB command.

## 7.6.6.8 Surprise Removal of Devices

There are two kinds of surprise removals: physical removal of a device, and surprise Link Down. The main difference between the two is the state of the presence pin, which will be deasserted after a physical removal but will remain asserted after a surprise Link Down. The switch notifies the FM of a surprise removal by generating Virtual CXL Switch Event Records for the change in link status and Presence Detect, as applicable.

Three cases of Surprise Removal are described below:

• When a Surprise Removal of a device occurs on an unbound port, the FM must be notified.

• When a Surprise Removal of an SLD or PCIe device occurs on a bound port, the FM is permitted to be notified but must not be involved in any error handling operations.

• When a Surprise Removal of an MLD component occurs, the FM must be notified. The switch will automatically unbind any existing LD bindings. The FM must perform error handling and port management activities, the details of which are considered implementation specific.

## 7.6.7

## Fabric Management Application Programming Interface

The FM manages all devices in a CXL system via the sets of commands defined in the FM API. This specification defines the minimum command set requirements for each device type.

Note: CXL switches and MLDs require FM API support to facilitate the advanced system  
Table 7-15. FM API Command Sets

<table><tr><td>Command Set Name</td><td>HBR Switch FM API Requirement $^{1}$ </td><td>MLD FM API Requirement $^{1}$ </td></tr><tr><td>Physical Switch (Section 7.6.7.1)</td><td>M</td><td>P</td></tr><tr><td>Virtual Switch (Section 7.6.7.2)</td><td>O</td><td>P</td></tr><tr><td>MLD Port (Section 7.6.7.3)</td><td>O</td><td>P</td></tr><tr><td>MLD Component (Section 7.6.7.4)</td><td>P</td><td>M</td></tr><tr><td>Multi-Headed Device (Section 7.6.7.5)</td><td>P</td><td>P</td></tr><tr><td>DCD Management (Section 7.6.7.6)</td><td>P</td><td>O</td></tr><tr><td>PBR Switch (Section 7.7.13)</td><td>P</td><td>P</td></tr><tr><td>Global Memory Access Endpoint (Section 7.7.14)</td><td>P</td><td>P</td></tr></table>

1. M = Mandatory, O = Optional, P = Prohibited.

capabilities outlined in Section 7.6.6. FM API is optional for all other CXL device types.

Command opcodes are listed in Table 8-215. Table 8-215 also identifies the minimum command sets and commands that are required to implement defined system capabilities. The following subsections define the commands grouped in each command set. Within each command set, commands are marked as mandatory (M) or optional (O). If a command set is supported, the required commands within that set must be implemented, but only if the Device supports that command set. For example, the Get Virtual CXL Switch Information command is required in the Virtual Switch Command Set, but that set is optional for switches. This means that a switch does not need to support the Get Virtual CXL Switch Information command if it does not support the Virtual Switch Command Set.

All commands have been defined as stand-alone operations; there are no explicit dependencies between commands, so optional commands can be implemented or not implemented on a per-command basis. Requirements for the implementation of commands are driven instead by the desired system functionality.

## 7.6.7.1 Physical Switch Command Set

This command set is only supported by and must be supported by CXL switches that have FM API support.

## 7.6.7.1.1 Identify Switch Device (Opcode 5100h)

This command retrieves information about the capabilities and configuration of a CXL switch.

Possible Command Return Codes:

• Success

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-16. Identify Switch Device Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>1</td><td>Ingress Port ID: Ingress CCI port index of the received request message. For CXL/PCIe ports, this corresponds to the physical port number. For non-CXL/PCIe, this corresponds to a vendor-specific index of the buses that the device supports, starting at 0. For example, a request received on the second of 2 SMBuses supported by a device would return a 1.</td></tr><tr><td>01h</td><td>1</td><td>Reserved</td></tr><tr><td>02h</td><td>1</td><td>Number of Physical Ports: Total number of physical ports in the CXL switch, including inactive/disabled ports.</td></tr><tr><td>03h</td><td>1</td><td>Number of VCSs: Maximum number of virtual CXL switches that are supported by the CXL switch.</td></tr><tr><td>04h</td><td>20h</td><td>Active Port Bitmask: Bitmask that defines whether a physical port is enabled (1) or disabled (0). Each bit corresponds 1:1 with a port, with the least significant bit corresponding to Port 0.</td></tr><tr><td>24h</td><td>20h</td><td>Active VCS Bitmask: Bitmask that defines whether a VCS is enabled (1) or disabled (0). Each bit corresponds 1:1 with a VCS ID, with the least significant bit corresponding to VCS 0.</td></tr><tr><td>44h</td><td>2</td><td>Total Number of vPPBs: The number of virtual PPBs that are supported by the CXL switch across all VCSs.</td></tr><tr><td>46h</td><td>2</td><td>Number of Bound vPPBs: Total number of vPPBs, across all VCSs, that are bound.</td></tr><tr><td>48h</td><td>1</td><td>Number of HDM Decoders: Number of HDM decoders available per USP.</td></tr></table>

## 7.6.7.1.2 Get Physical Port State (Opcode 5101h)

This command retrieves the physical port information.

Possible Command Return Codes:

• Success

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-17. Get Physical Port State Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of Ports: Number of ports requested.</td></tr><tr><td>1h</td><td>Varies</td><td>Port ID List: 1-byte ID of requested port, repeated Number of Ports times.</td></tr></table>

Table 7-18. Get Physical Port State Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of Ports: Number of port information blocks returned.</td></tr><tr><td>1h</td><td>3</td><td>Reserved</td></tr><tr><td>4h</td><td>Varies</td><td>Port Information List: Port information block as defined in Table 7-19, repeated Number of Ports times.</td></tr></table>

Table 7-19. Get Physical Port State Port Information Block Format (Sheet 1 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Port ID</td></tr><tr><td>1h</td><td>1</td><td>Bits[3:0]:Current Port Configuration State:- 0h = Disabled- 1h = Bind in progress- 2h = Unbind in progress- 3h = DSP- 4h = USP- 5h = Fabric Port- Fh = Invalid Port_ID; all subsequent field values are undefined- All other encodings are reservedBit[4]:GAE Support:Indicates whether GAE support is present (1) or not present (0) on a port. Valid only for PBR switches if Current Port Configuration State is 4h (USP).Bits[7:5]:Reserved.</td></tr><tr><td>2h</td><td>1</td><td>Bits[3:0]:Connected Device Mode:Formerly known as Connected Device CXL Version. This field is reserved for all values of Current Port Configuration State except DSP.- 0h = Connection is not CXL or is disconnected- 1h = RCD mode- 2h = CXL 68B Flit and VH mode- 3h = Standard 256B Flit mode- 4h = CXL Latency-Optimized 256B Flit mode- 5h = PBR mode- All other encodings are reservedBits[7:4]:Reserved.</td></tr><tr><td>3h</td><td>1</td><td>Reserved</td></tr><tr><td>4h</td><td>1</td><td>Connected Device Type00h = No device detected01h = PCIe Device02h = CXL Type 1 device03h = CXL Type 2 device or HBR switch04h = CXL Type 3 SLD05h = CXL Type 3 MLD06h = PBR componentAll other encodings are reservedThis field is reserved ifSupported CXL Modesis 00h. This field is reserved for all values ofCurrent Port Configuration Stateexcept 3h (DSP) or 5h (Fabric Port).</td></tr><tr><td>5h</td><td>1</td><td>Supported CXL Modes:Formerly known as Connected CXL Version. Bitmask that defines which CXL modes are supported (1) or not supported (0) by this port:Bit[0]:RCD ModeBit[1]:CXL 68B Flit and VH CapableBit[2]:256B Flit and CXL CapableBit[3]:CXL Latency-Optimized 256B Flit CapableBit[4]:PBR CapableBits[7:5]:Reserved for future CXL useUndefined when the value is 00h.</td></tr></table>

Table 7-19. Get Physical Port State Port Information Block Format (Sheet 2 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>6h</td><td>1</td><td>Bits[5:0]:Maximum Link Width:Value encoding matches the Maximum Link Width field in the PCIe Link Capabilities register in the PCIe Capability structure.Bits[7:6]:Reserved.</td></tr><tr><td>7h</td><td>1</td><td>Bits[5:0]:Negotiated Link Width:Value encoding matches the Negotiated Link Width field in PCIe Link Capabilities register in the PCIe Capability structure.Bits[7:6]:Reserved.</td></tr><tr><td>8h</td><td>1</td><td>Bits[5:0]:Supported Link Speeds Vector:Value encoding matches the Supported Link Speeds Vector field in the PCIe Link Capabilities 2 register in the PCIe Capability structure.Bits[7:6]:Reserved.</td></tr><tr><td>9h</td><td>1</td><td>Bits[5:0]:Max Link Speed:Value encoding matches the Max Link Speed field in the PCIe Link Capabilities register in the PCIe Capability structure.Bits[7:6]:Reserved.</td></tr><tr><td>Ah</td><td>1</td><td>Bits[5:0]:Current Link Speed:Value encoding matches the Current Link Speed field in the PCIe Link Status register in the PCIe Capability structure.Bits[7:6]:Reserved.</td></tr><tr><td>Bh</td><td>1</td><td>LTSSM State:Current link LTSSM Major state:00h = Detect01h = Polling02h = Configuration03h = Recovery04h = L005h = L0s06h = L107h = L208h = Disabled09h = Loopback0Ah = Hot ResetAll other encodings are reservedLink substates should be reported through vendor-defined diagnostics commands.</td></tr><tr><td>Ch</td><td>1</td><td>First Negotiated Lane Number</td></tr><tr><td>Dh</td><td>2</td><td>Link State FlagsBit[0]:Lane Reversal State:- 0 = Standard lane ordering- 1 = Reversed lane orderingBit[1]:Port PCIe Reset State (PERST#):- 0 = Not in reset- 1 = In resetBit[2]:Port Presence Pin State (PRSNT#):- 0 = Not present- 1 = PresentBit[3]:Power Control State:- 0 = Power on- 1 = Power offBits[15:4]:Reserved</td></tr><tr><td>Fh</td><td>1</td><td>Supported LD Count:Number of additional LDs supported by this port. All ports must support at least one LD.</td></tr></table>

## 7.6.7.1.3 Physical Port Control (Opcode 5102h)

This command is used by the FM to control unbound ports and MLD ports, including issuing resets and controlling sidebands.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-20. Physical Port Control Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>PPB ID: Physical PPB ID, which corresponds 1:1 to associated physical port number.</td></tr><tr><td>1h</td><td>1</td><td>Port Opcode: Code that defines which operation to perform:00h = Assert PERST#01h = Deassert PERST#02h = Reset PPBAll other encodings are reserved</td></tr></table>

7.6.7.1.4 Send PPB CXL.io Configuration Request (Opcode 5103h)

This command sends CXL.io Config requests to the specified physical port’s PPB. This command is only processed for unbound ports and MLD ports.

Possible Command Return Codes:

• Success

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-21. Send PPB CXL.io Configuration Request Input Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>PPB ID: Target PPB&#x27;s physical port.</td></tr><tr><td>1h</td><td>3</td><td>Bits[7:0]: Register Number: As defined in PCIe Base SpecificationBits[11:8]: Extended Register Number: As defined in PCIe Base SpecificationBits[15:12]: First Dword Byte Enable: As defined in PCIe Base SpecificationBits[22:16]: ReservedBit[23]: Transaction Type:- 0 = Read- 1 = Write</td></tr><tr><td>4h</td><td>4</td><td>Transaction Data: Write data. Valid only for write transactions.</td></tr></table>

Table 7-22. Send PPB CXL.io Configuration Request Output Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>4</td><td>Return Data: Read data. Valid only for read transactions.</td></tr></table>

## 7.6.7.1.5 Get Domain Validation SV State (Opcode 5104h)

This command is used by the Host to check the state of the secret value.

Possible Command Return Codes:

• Success

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-23. Get Domain Validation SV State Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Secret Value State: State of the secret value:00h = Not set01h = SetAll other encodings are reserved</td></tr></table>

## 7.6.7.1.6 Set Domain Validation SV (Opcode 5105h)

This command is used by the Host to set the secret value of its VCS. The secret value can be set only once. This command will fail with Invalid Input if it is called more than once.

Possible Command Return Codes:

• Success

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-24. Set Domain Validation SV Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>10h</td><td>Secret Value: UUID used to uniquely identify a host hierarchy.</td></tr></table>

Get VCS Domain Validation SV State (Opcode 5106h)

## 7.6.7.1.7

This command is used by the FM to check the state of the secret value in a VCS.

Possible Command Return Codes:

• Success

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-25. Get VCS Domain Validation SV State Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>VCS ID: Index of VCS to query.</td></tr></table>

Table 7-26. Get VCS Domain Validation SV State Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Secret Value State: State of the secret value:00h = Not set01h = SetAll other encodings are reserved</td></tr></table>

7.6.7.1.8 Get Domain Validation SV (Opcode 5107h)

This command is used by the FM to retrieve the secret value from a VCS.

Possible Command Return Codes:

• Success

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-27. Get Domain Validation SV Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>VCS ID: Index of VCS to query.</td></tr></table>

Table 7-28. Get Domain Validation SV Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>10h</td><td>Secret Value: UUID used to uniquely identify a host hierarchy.</td></tr></table>

## 7.6.7.2 Virtual Switch Command Set

This command set is supported only by the CXL switch. It is required for switches that support more than one VCS. The following commands are defined:

Table 7-29. Virtual Switch Command Set Requirements

<table><tr><td>Command Name</td><td>Requirement $^{1}$ </td></tr><tr><td>Get Virtual CXL Switch Info</td><td>M</td></tr><tr><td>Bind vPPB</td><td>O</td></tr><tr><td>Unbind vPPB</td><td>O</td></tr><tr><td>Generate AER Event</td><td>O</td></tr></table>

1. M = Mandatory, O = Optional.

## 7.6.7.2.1 Get Virtual CXL Switch Info (Opcode 5200h)

This command retrieves information on a specified number of VCSs in the switch. Because of the possibility of variable numbers of vPPBs within each VCS, the returned array has variably sized elements.

Possible Command Return Codes:

• Success

• Invalid Input

• Internal Error

• Retry Required

• Invalid Payload Length

Command Effects:

• None

Table 7-30. Get Virtual CXL Switch Info Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Start vPPB: Specifies the ID of the first vPPB for each VCS to include in the vPPB information list in the response (bytes 4 – 7 in Table 7-32). This enables compatibility with devices that have small maximum command message sizes.</td></tr><tr><td>1h</td><td>1</td><td>vPPB List Limit: The maximum number of vPPB information entries to include in the response (bytes 4 – 7 in Table 7-32). This enables compatibility with devices that have small maximum command message sizes. This field shall have a minimum value of 1.</td></tr><tr><td>2h</td><td>1</td><td>Number of VCSs: Number of VCSs requested. This field shall have a minimum value of 1.</td></tr><tr><td>3h</td><td>Number of VCSs</td><td>VCS ID List: 1-byte ID of requested VCS, repeated Number of VCSs times.</td></tr></table>

Table 7-31. Get Virtual CXL Switch Info Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of VCSs: Number of VCS information blocks returned.</td></tr><tr><td>1h</td><td>3</td><td>Reserved</td></tr><tr><td>4h</td><td>Varies</td><td>VCS Information List: VCS information block as defined in Table 7-32, repeated Number of VCSs times.</td></tr></table>

Table 7-32. Get Virtual CXL Switch Info VCS Information Block Format

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Virtual CXL Switch ID</td></tr><tr><td>1h</td><td>1</td><td>VCS State: Current state of the VCS:00h = Disabled01h = EnabledFFh = Invalid VCS ID; all subsequent field values are invalidAll other encodings are reserved</td></tr><tr><td>2h</td><td>1</td><td>USP ID: Physical port ID of the local Upstream Port, or the local fabric physical port ID of a Downstream ES VCS. Valid only when the VCS is enabled.</td></tr><tr><td>3h</td><td>1</td><td>Number of vPPBs: Total number of vPPBs in the VCS. This value may be larger than the vPPB List Limit field specified in the request. In this case, the length of vPPB information list, starting at byte 4, is defined by &#x27;vPPB List Limit&#x27;, not by this field. vPPB information list consists of vPPB List Entry Count number of entries and each entry is 4B in length.vPPB List Entry Count=min(vPPB List Limit, Number of vPPBs).</td></tr><tr><td>4h</td><td>1</td><td>vPPB[Start vPPB] Binding Status00h = Unbound01h = Bind or unbind in progress02h = Bound Physical Port03h = Bound LD04h = Bound PIDAll other encodings are reserved</td></tr><tr><td>5h</td><td>2</td><td>For PBR Switches when Binding Status is 02h or 03h and for HBR Switches:Bits[7:0]: vPPB[Start vPPB] Bound Port ID:Physical port number of the bound port. Valid only when Binding Status is 02h or 03h.Bits[15:8]: vPPB[Start vPPB] Bound LD ID: ID of the LD that is bound to the port from the MLD on an associated physical port. Valid only when vPPB[Start vPPB] Binding Status is 03h; otherwise, the value is FFh.For PBR Switches when Binding Status is 04h:Bits[11:0]: vPPB[Start vPPB] Bound PID: PID of the bound vPPB, as defined in Section 7.7.12.3.Bits[15:12]: Reserved.</td></tr><tr><td>7h</td><td>1</td><td>Reserved</td></tr><tr><td>...</td><td></td><td>...</td></tr><tr><td>4 + (vPPB List Entry Count - 1) * 4</td><td>1</td><td>vPPB[Start vPPB + vPPB List Entry Count $^{1}$  - 1]Binding Status: As defined above.</td></tr><tr><td>5 + (vPPB List Entry Count - 1) * 4</td><td>1</td><td>vPPB[Start vPPB + vPPB List Entry Count $^{1}$  - 1] Bound Port ID: As defined above.</td></tr><tr><td>6 + (vPPB List Entry Count - 1) * 4</td><td>1</td><td>vPPB[Start vPPB + vPPB List Entry Count $^{1}$  - 1] Bound LD ID: As defined above.</td></tr><tr><td>7 + (vPPB List Entry Count - 1) * 4</td><td>1</td><td>Reserved</td></tr></table>

1. The vPPB information list length is defined by the lesser of the vPPB List Limit field in the command request and the Number of vPPBs field in the command response.

## 7.6.7.2.2 Bind vPPB (Opcode 5201h)

This command performs a binding operation on the specified vPPB. If the bind target is a physical port connected to a Type 1, Type 2, Type 3, or PCIe device or a physical port whose link is down, the specified physical port of the CXL switch is fully bound to the vPPB. If the bind target is a physical port connected to an MLD, then a corresponding LD-ID must also be specified.

All binding operations are executed as background commands. The switch notifies the FM of binding completion through the generation of event records, as defined in Section 7.6.6.

Possible Command Return Codes:

• Background Command Started

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

• Busy

Command Effects:

• Background Operation

## Table 7-33. Bind vPPB Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Virtual CXL Switch ID</td></tr><tr><td>1h</td><td>1</td><td>vPPB ID: Index of the vPPB within the VCS specified in the VCS ID.</td></tr><tr><td>2h</td><td>1</td><td>Physical Port ID</td></tr><tr><td>3h</td><td>1</td><td>Reserved</td></tr><tr><td>4h</td><td>2</td><td>LD ID: LD-ID if the target port is an MLD port. Must be FFFFh for other EP types.</td></tr></table>

## 7.6.7.2.3 Unbind vPPB (Opcode 5202h)

This command unbinds the physical port or LD from the virtual hierarchy vPPB. All unbinding operations are executed as background commands. The switch notifies the FM of unbinding completion through the generation of event records, as defined in Section 7.6.6.

Possible Command Return Codes:

• Unsupported

• Background Command Started

• Invalid Input

• Internal Error

• Retry Required

• Busy

Command Effects:

• Background Operation

Table 7-34. Unbind vPPB Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Virtual CXL Switch ID</td></tr><tr><td>1h</td><td>1</td><td>vPPB ID: Index of the vPPB within the VCS specified in the VCS ID.</td></tr><tr><td>2h</td><td>1</td><td>Bits[3:0]: Unbind Option:- 0h = Wait for port Link Down before unbinding- 1h = Simulate Managed Hot-Remove- 2h = Simulate Surprise Hot-Remove- All other encodings are reservedBits[7:4]: Reserved</td></tr></table>

## 7.6.7.2.4 Generate AER Event (Opcode 5203h)

This command generates an AER event on a specified VCS’s vPPB (US vPPB or DS vPPB). The switch must respect the Host’s AER mask settings.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-35. Generate AER Event Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Virtual CXL Switch ID</td></tr><tr><td>1h</td><td>1</td><td>vPPB Instance: The value of 0 represents USP. The values of 1 and above represent the DSP vPPBs in increasing Device Number, Function Number order, as defined in Section 7.1.4.</td></tr><tr><td>2h</td><td>2</td><td>Reserved</td></tr><tr><td>4h</td><td>4</td><td>AER ErrorBits[4:0]:If Severity=0, bit position of the error type in the AER Correctable Error Status register, as defined in PCIe Base SpecificationIf Severity=1, bit position of the error type in the AER Uncorrectable Error Status register, as defined in PCIe Base SpecificationBits[30:5]: ReservedBit[31]: Severity0 = Correctable Error1 = Uncorrectable Error</td></tr><tr><td>8h</td><td>20h</td><td>AER Header: TLP Header to place in AER registers, as defined in PCIe Base Specification.</td></tr></table>

## 7.6.7.3 MLD Port Command Set

This command set is applicable to CXL switches and MLDs. The following commands are defined:

Table 7-36. MLD Port Command Set Requirements

<table><tr><td rowspan="2">Command Name</td><td colspan="2">Requirement</td></tr><tr><td> $Switches^1$ </td><td> $MLDs^1$ </td></tr><tr><td>Tunnel Management Command</td><td>M</td><td>O</td></tr><tr><td>Send LD CXL.io Configuration Request</td><td>M</td><td>P</td></tr><tr><td>Send LD CXL.io Memory Request</td><td>M</td><td>P</td></tr></table>

1. M = Mandatory, O = Optional, P = Prohibited.

## 7.6.7.3.1 Tunnel Management Command (Opcode 5300h)

This command tunnels the provided command to LD FFFFh of the MLD on the specified port, using the transport defined in Section 7.6.3.1.

When sent to an MLD, this provided command is tunneled by the FM-owned LD to the specified LD, as illustrated in Figure 7-22.

Figure 7-22. Tunneling Commands to an LD in an MLD  
![](images/a356bd0aaecb9366bb2507f7eb6cf1c7f8a0c2d3c2eb8ac8bacef12b56e56054.jpg)  
The Management Command input payload field includes the tunneled command encapsulated in the CCI Message Format, as defined in Figure 7-19. This can include an additional layer of tunneling for commands issued to LDs in an MLD that is accessible only through a CXL switch’s MLD Port, as illustrated in Figure 7-23.

Figure 7-23. Tunneling Commands to an LD in an MLD through a CXL Switch  
![](images/b2200f4958101ada42e4901473b3a6ae5338cef94932cbe0567e6e9efecf31c0.jpg)

Response size varies, based on the tunneled FM command’s definition. Valid targets for the tunneled commands include switch MLD Ports, valid LDs within an MLD, and the LD Pool CCI in a Multi-Headed device. Tunneled commands sent to any other targets shall be discarded and this command shall return an “Invalid Input” return code. The FMowned LD (LD=FFFFh) is an invalid target in MLDs.

The LD Pool CCI in Multi-Headed devices is targeted using the “Target Type” field, as illustrated in Figure 7-24. This command shall return an “Invalid Input” return code failure if tunneling to the LD Pool CCI is not permitted on the CCI that receives the request.

Figure 7-24. Tunneling Commands to the LD Pool CCI in a Multi-Headed Device  
![](images/16635aff71725cfd906d00d9e8214bb5fb92ed9a631f9f0db64c98196829a7dd.jpg)  
A Multi-Headed device shall terminate the processing of a request that includes more than 3 layers of tunneling and return the Unsupported return code.

The Tunnel Management Command itself does not cause any Command Effects, but the Management Command provided in the request will cause Command Effects as per its definition.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-37. Tunnel Management Command Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Port or LD ID: Egress port ID for commands sent to a switch, or LD-ID for commands sent to an MLD. Valid only when Target Type is 0.</td></tr><tr><td>1h</td><td>1</td><td>Bits[3:0]:Target Type: Specifies the type of tunneling target for this command:0h = Port or LD based. Indicates that the &quot;Port or LD ID&quot; field is used to determine the target.1h = LD Pool CCI. Indicates that the tunneling target is the LD Pool CCI of a Multi-Headed device.All other encodings are reserved.Bits[7:4]:Reserved</td></tr><tr><td>2h</td><td>2</td><td>Command Size:Number of valid bytes inManagement Command.</td></tr><tr><td>4h</td><td>Varies</td><td>Management Command:Request message formatted in the CCI Message Format as defined inFigure 7-19.</td></tr></table>

Table 7-38. Tunnel Management Command Response Payload

<table><tr><td>Byte offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>2</td><td>Response Length: Number of valid bytes in Response Message.</td></tr><tr><td>2h</td><td>2</td><td>Reserved</td></tr><tr><td>4h</td><td>Varies</td><td>Response Message: Response message formatted in the CCI Message Format as defined in Figure 7-19.</td></tr></table>

## 7.6.7.3.2 Send LD CXL.io Configuration Request (Opcode 5301h)

This command allows the FM to read or write the CXL.io Configuration Space of an unbound LD or FMLD. The switch will convert the request into CfgRd/CfgWr TLPs to the target device. Invalid Input Return Code shall be generated if the requested LD is bound.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-39. Send LD CXL.io Configuration Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>PPB ID: Target PPB&#x27;s physical port.</td></tr><tr><td>1h</td><td>3</td><td>Bits[7:0]: Register Number: As defined in PCIe Base SpecificationBits[11:8]: Extended Register Number: As defined in PCIe Base SpecificationBits[15:12]: First Dword Byte Enable: As defined in PCIe Base SpecificationBits[22:16]: ReservedBit[23]: Transaction Type:- 0 = Read- 1 = Write</td></tr><tr><td>4h</td><td>2</td><td>LD ID: Target LD-ID.</td></tr><tr><td>6h</td><td>2</td><td>Reserved</td></tr><tr><td>8h</td><td>4</td><td>Transaction Data: Write data. Valid only for write transactions.</td></tr></table>

## Table 7-40. Send LD CXL.io Configuration Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>4</td><td>Return Data: Read data. Valid only for read transactions.</td></tr></table>

## 7.6.7.3.3 Send LD CXL.io Memory Request (Opcode 5302h)

This command allows the FM to batch read or write the CXL.io Memory Space of an unbound LD or FMLD. The switch will convert the request into MemRd/MemWr TLPs to the target device. Invalid Input Return Code shall be generated if the requested LD is bound.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-41. Send LD CXL.io Memory Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>1</td><td>Port ID: Target MLD port.</td></tr><tr><td>01h</td><td>2</td><td>Bits[11:0]: ReservedBits[15:12]: First Dword Byte Enable: As defined in PCIe Base SpecificationBits[19:16]: Last Dword Byte Enable: As defined in PCIe Base SpecificationBits[22:20]: ReservedBit[23]: Transaction Type:- 0 = Read- 1 = Write</td></tr><tr><td>04h</td><td>2</td><td>LD ID: Target LD-ID.</td></tr><tr><td>06h</td><td>2</td><td>Transaction Length: Transaction length in bytes, up to a maximum of 4 KB (1000h).</td></tr><tr><td>08h</td><td>8</td><td>Transaction Address: The target HPA that points into the target device&#x27;s MMIO Space.</td></tr><tr><td>10h</td><td>Varies</td><td>Transaction Data: Write data. Valid only for write transactions.</td></tr></table>

Table 7-42. Send LD CXL.io Memory Request Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>2</td><td>Return Size: Number of successfully transferred bytes.</td></tr><tr><td>2h</td><td>2</td><td>Reserved</td></tr><tr><td>4h</td><td>Varies</td><td>Return Data: Read data. Valid only for read transactions.</td></tr></table>

## 7.6.7.4 MLD Component Command Set

This command set is only supported by, and must be supported by, MLD components implementing FM API support. These commands are processed by MLDs. When an FM is connected to a CXL switch that supports the FM API and does not have a direct connection to an MLD, these commands are passed to the MLD using the Tunnel Management Command. The following commands are defined:

Table 7-43. MLD Component Command Set Requirements

<table><tr><td>Command Name</td><td>Requirement $^{1}$ </td></tr><tr><td>Get LD Info</td><td>M</td></tr><tr><td>Get LD Allocations</td><td>M</td></tr><tr><td>Set LD Allocations</td><td>O</td></tr><tr><td>Get QoS Control</td><td>M</td></tr><tr><td>Set QoS Control</td><td>M</td></tr><tr><td>Get QoS Status</td><td>O</td></tr><tr><td>Get QoS Allocated BW</td><td>M</td></tr><tr><td>Set QoS Allocated BW</td><td>M</td></tr><tr><td>Get QoS BW Limit</td><td>M</td></tr><tr><td>Set QoS BW Limit</td><td>M</td></tr></table>

1. M = Mandatory, O = Optional.

## 7.6.7.4.1 Get LD Info (Opcode 5400h)

This command retrieves the configurations of the MLD.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-44. Get LD Info Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Memory Size: Total device memory capacity.</td></tr><tr><td>8h</td><td>2</td><td>LD Count: Number of logical devices supported.</td></tr><tr><td>Ah</td><td>1</td><td>QoS Telemetry Capability: Optional QoS Telemetry for memory MLD capabilities for management by an FM (see Section 3.3.4).Bit[0]: Egress Port Congestion Supported: When set, the associated feature is supported and the Get QoS Status command must be implemented (see Section 3.3.4.3.9).Bit[1]: Temporary Throughput Reduction Supported: When set, the associated feature is supported (see Section 3.3.4.3.5).Bits[7:2]: Reserved.</td></tr></table>

## 7.6.7.4.2 Get LD Allocations (Opcode 5401h)

This command retrieves the memory allocations of the MLD.

Possible Command Return Codes:

• Success

• Unsupported

• Internal Error

• Retry Required

• Invalid Payload Length

Command Effects:

• None

Table 7-45. Get LD Allocations Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Start LD ID: ID of the first LD in the LD Allocation List.</td></tr><tr><td>1h</td><td>1</td><td>LD Allocation List Limit: Maximum number of LD information blocks returned. This field shall have a minimum value of 1.</td></tr></table>

Table 7-46. Get LD Allocations Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of LDs: Number of LDs enabled in the device.</td></tr><tr><td>1h</td><td>1</td><td>Memory Granularity: This field specifies the granularity of the memory sizes configured for each LD:0h = 256 MB1h = 512 MB2h = 1 GBAll other encodings are reserved</td></tr><tr><td>2h</td><td>1</td><td>Start LD ID: ID of the first LD in the LD Allocation List.</td></tr><tr><td>3h</td><td>1</td><td>LD Allocation List Length: Number of LD information blocks returned. This value is the lesser of the request&#x27;s &#x27;LD Allocation List Limit&#x27; and response&#x27;s &#x27;Number of LDs&#x27;.</td></tr><tr><td>4h</td><td>Varies</td><td>LD Allocation List: LD Allocation blocks for each LD, as defined in Table 7-47, repeated LD Allocation List Length times.</td></tr></table>

## Table 7-47. LD Allocations List Format

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>8</td><td>Range 1 Allocation Multiplier: Memory Allocation Range 1 for LD. This value is multiplied with Memory Granularity to calculate the memory allocation range in bytes.</td></tr><tr><td>8h</td><td>8</td><td>Range 2 Allocation Multiplier: Memory Allocation Range 2 for LD. This value is multiplied with Memory Granularity to calculate the memory allocation range in bytes.</td></tr></table>

## 7.6.7.4.3 Set LD Allocations (Opcode 5402h)

This command sets the memory allocation for each LD. This command will fail if the device fails to allocate any of the allocations defined in the request. The allocations provided in the response reflect the state of the LD allocations after the command is processed, which allows the FM to check for partial success.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

• Invalid Payload Length

Command Effects:

• Configuration Change after Cold Reset

• Configuration Change after Conventional Reset

• Configuration Change after CXL Reset

• Immediate Configuration Change

• Immediate Data Change

Table 7-48. Set LD Allocations Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of LDs: Number of LDs to configure. This field shall have a minimum value of 1.</td></tr><tr><td>1h</td><td>1</td><td>Start LD ID: ID of the first LD in the LD Allocation List.</td></tr><tr><td>2h</td><td>2</td><td>Reserved</td></tr><tr><td>4h</td><td>Varies</td><td>LD Allocation List: LD Allocation blocks for each LD, starting at Start LD ID, as defined in Table 7-47, repeated Number of LDs times.</td></tr></table>

Table 7-49. Set LD Allocations Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of LDs: Number of LDs configured.</td></tr><tr><td>1h</td><td>1</td><td>Start LD ID: ID of the first LD in the LD Allocation List.</td></tr><tr><td>2h</td><td>2</td><td>Reserved</td></tr><tr><td>4h</td><td>Varies</td><td>LD Allocation List: Updated LD Allocation blocks for each LD, starting at Start LD ID, as defined in Table 7-47, repeated Number of LDs times.</td></tr></table>

7.6.7.4.4 Get QoS Control (Opcode 5403h)

This command retrieves the MLD’s QoS control parameters.

Possible Command Return Codes:

• Success

• Internal Error

• Retry Required

• Invalid Payload Length

Command Effects:

• None

Payload for Get QoS Control Response, Set QoS Control Request, and Set QoS Control Response (Sheet 1 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>QoS Telemetry Control: Default is 00h.• Bit[0]: Egress Port Congestion Enable: See Section 3.3.4.3.9• Bit[1]: Temporary Throughput Reduction Enable: See Section 3.3.4.3.5• Bits[7:2]: Reserved</td></tr><tr><td>1h</td><td>1</td><td>Egress Moderate Percentage: Threshold in percent for Egress Port Congestion mechanism to indicate moderate congestion. Valid range is 1-100. Default is 10.</td></tr><tr><td>2h</td><td>1</td><td>Egress Severe Percentage: Threshold in percent for Egress Port Congestion mechanism to indicate severe congestion. Valid range is 1-100. Default is 25.</td></tr></table>

Table 7-50. Payload for Get QoS Control Response, Set QoS Control Request, and Set QoS Control Response (Sheet 2 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>3h</td><td>1</td><td>Backpressure Sample Interval: Interval in ns for Egress Port Congestion mechanism to take samples. Valid range is 0-15. Default is 8 (800 ns of history for 100 samples). Value of 0 disables the mechanism. See Section 3.3.4.3.4.</td></tr><tr><td>4h</td><td>2</td><td>ReqCmpBasis: Estimated maximum sustained sum of requests and recent responses across the entire device, serving as the basis for QoS Limit Fraction. Valid range is 0-65,535. Value of 0 disables the mechanism. Default is 0. See Section 3.3.4.3.7.</td></tr><tr><td>6h</td><td>1</td><td>Completion Collection Interval: Interval in ns for Completion Counting mechanism to collect the number of transmitted responses in a single counter. Valid range is 0-255. Default is 64 (1.024 us of history, given 16 counters). See Section 3.3.4.3.10.</td></tr></table>

## 7.6.7.4.5 Set QoS Control (Opcode 5404h)

This command sets the MLD’s QoS control parameters, as defined in Table 7-50. The device must complete the set operation before returning the response. The command response returns the resulting QoS control parameters, as defined in the same table. This command will fail, returning Invalid Input, if any of the parameters are outside their valid range.

Possible Command Codes:

• Success

• Invalid Input

• Internal Error

• Retry Required

• Invalid Payload Length

Command Effects:

• Immediate Policy Change

Payload for Set QoS Control Request and Response is documented in Table 7-50.

## 7.6.7.4.6 Get QoS Status (Opcode 5405h)

This command retrieves the MLD’s QoS Status. This command is mandatory if the Egress Port Congestion Supported bit is set (see Table 7-44).

Possible Command Return Codes:

• Success

• Unsupported

• Internal Error

• Retry Required

• Invalid Payload Length

Command Effects:

• None

Table 7-51. Get QoS Status Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Backpressure Average Percentage: Current snapshot of the measured Egress Port average congestion. See Section 3.3.4.3.4.</td></tr></table>

## 7.6.7.4.7 Get QoS Allocated BW (Opcode 5406h)

This command retrieves the MLD’s QoS allocated bandwidth on a per-LD basis (see Section 3.3.4.3.7).

Possible Command Return Codes:

• Success

• Invalid Input

• Internal Error

• Retry Required

• Invalid Payload Length

Command Effects:

• None

Table 7-52. Payload for Get QoS Allocated BW Request

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of LDs: Number of LDs queried. This field shall have a minimum value of 1.</td></tr><tr><td>1h</td><td>1</td><td>Start LD ID: ID of the first LD in the QoS Allocated BW List.</td></tr></table>

Table 7-53. Payload for Get QoS Allocated BW Response

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of LDs: Number of LDs queried.</td></tr><tr><td>1h</td><td>1</td><td>Start LD ID: ID of the first LD in the QoS Allocated BW List.</td></tr><tr><td>2h</td><td>Number of LDs</td><td>QoS Allocation Fraction: Byte array of allocated bandwidth fractions for LDs, starting at Start LD ID. The valid range of each array element is 0-255. Default value is 0. Value in each byte is the fraction multiplied by 256.</td></tr></table>

## 7.6.7.4.8 Set QoS Allocated BW (Opcode 5407h)

This command sets the MLD’s QoS allocated bandwidth on a per-LD basis, as defined in Section 3.3.4.3.7. The device must complete the set operation before returning the response. The command response returns the resulting QoS allocated bandwidth, as defined in the same table. This command will fail, returning Invalid Input, if any of the parameters are outside their valid range.

Possible Command Return Codes:

• Success

• Invalid Input

• Internal Error

• Retry Required

• Invalid Payload Length

Command Effects:

• Configuration Change after Cold Reset

• Configuration Change after Conventional Reset

• Configuration Change after CXL Reset

• Immediate Configuration Change

• Immediate Data Change

Table 7-54. Payload for Set QoS Allocated BW Request, and Set QoS Allocated BW Response

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of LDs: Number of LDs configured.</td></tr><tr><td>1h</td><td>1</td><td>Start LD ID: ID of the first LD in the QoS Allocated BW List.</td></tr><tr><td>2h</td><td>Number of LDs</td><td>QoS Allocation Fraction: Byte array of allocated bandwidth fractions for LDs, starting at Start LD ID. The valid range of each array element is 0-255. Default value is 0. Value in each byte is the fraction multiplied by 256.</td></tr></table>

## 7.6.7.4.9 Get QoS BW Limit (Opcode 5408h)

This command retrieves the MLD’s QoS bandwidth limit on a per-LD basis (see Section 3.3.4.3.7).

Possible Command Return Codes:

• Success

• Invalid Input

• Internal Error

• Retry Required

• Invalid Payload Length

Command Effects:

• None

Table 7-55. Payload for Get QoS BW Limit Request

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of LDs: Number of LDs queried. This field shall have a minimum value of 1.</td></tr><tr><td>1h</td><td>1</td><td>Start LD ID: ID of the first LD in the QoS BW Limit List.</td></tr></table>

Table 7-56. Payload for Get QoS BW Limit Response

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of LDs: Number of LDs queried.</td></tr><tr><td>1h</td><td>1</td><td>Start LD ID: ID of the first LD in the QoS BW Limit List.</td></tr><tr><td>2h</td><td>Number of LDs</td><td>QoS Limit Fraction: Byte array of allocated bandwidth limit fractions for LDs, starting at Start LD ID. The valid range of each array element is 0-255. Default value is 0. Value in each byte is the fraction multiplied by 256.</td></tr></table>

## 7.6.7.4.10 Set QoS BW Limit (Opcode 5409h)

This command sets the MLD’s QoS bandwidth limit on a per-LD basis, as defined in Section 3.3.4.3.7. The device must complete the set operation before returning the response. The command response returns the resulting QoS bandwidth limit, as defined in the same table. This command will fail, returning Invalid Input, if any of the parameters are outside their valid range. This command will fail, returning Internal Error, if the device was able to set the QoS BW Limit for some of the LDs in the request, but not all the LDs.

Possible Command Return Codes:

• Success

• Invalid Input

• Internal Error

• Retry Required

• Invalid Payload Length

Command Effects:

• Configuration Change after Cold Reset

• Configuration Change after Conventional Reset

• Configuration Change after CXL Reset

• Immediate Configuration Change

• Immediate Data Change

Table 7-57. Payload for Set QoS BW Limit Request, and Set QoS BW Limit Response

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of LDs: Number of LDs configured.</td></tr><tr><td>1h</td><td>1</td><td>Start LD ID: ID of the first LD in the QoS BW Limit List.</td></tr><tr><td>2h</td><td>Number of LDs</td><td>QoS Limit Fraction: Byte array of allocated bandwidth limit fractions for LDs, starting at Start LD ID. The valid range of each array element is 0-255. Default value is 0. Value in each byte is the fraction multiplied by 256.</td></tr></table>

## 7.6.7.5 Multi-Headed Device Command Set

The Multi-Headed device command set includes commands for querying the Head-to-LD mapping in a Multi-Headed device. Support for this command set is required on the LD Pool CCI of a Multi-Headed device.

## 7.6.7.5.1 Get Multi-Headed Info (Opcode 5500h)

This command retrieves the number of heads, number of supported LDs, and Head-to-LD mapping of a Multi-Headed device.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-58. Get Multi-Headed Info Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Start LD ID: ID of the first LD in the LD Map.</td></tr><tr><td>1h</td><td>1</td><td>LD Map List Limit: Maximum number of LD Map entries returned. This field shall have a minimum value of 1.</td></tr></table>

## Table 7-59. Get Multi-Headed Info Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of LDs: Total number of LDs in the LD Pool. This field shall have a minimum value of 1.</td></tr><tr><td>1h</td><td>1</td><td>Number of Heads: Total number of CXL heads. This field shall have a minimum value of 1.</td></tr><tr><td>2h</td><td>2</td><td>Reserved</td></tr><tr><td>4h</td><td>1</td><td>Start LD ID: ID of the first LD in the LD Map.</td></tr><tr><td>5h</td><td>1</td><td>LD Map Length: Number of LD Map entries returned.LD Map Length = Min (LD Map List Limit. (Number of LDs - Start LD ID))</td></tr><tr><td>6h</td><td>2</td><td>Reserved</td></tr><tr><td>8h</td><td>LD Map Length</td><td>LD Map: Port number of the head to which each LD is assigned, starting at Start LD ID, repeated LD Map Length times. A value of FFh indicates that LD is not currently assigned to a head.</td></tr></table>

## 7.6.7.5.2 Get Head Info (Opcode 5501h)

This command retrieves information for one or more heads.

This command fails with the Invalid Input return code if the values of the Start Head and Number of Heads fields request the information for a non-existent head.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-60. Get Head Info Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Start Head: Specifies the ID of the first head information block requested.</td></tr><tr><td>1h</td><td>1</td><td>Number of Heads: Number of head information blocks requested.</td></tr></table>

Table 7-61. Get Head Info Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Number of Heads: Number of head information blocks returned.</td></tr><tr><td>1h</td><td>3</td><td>Reserved</td></tr><tr><td>4h</td><td>Varies</td><td>Head Information List: Head information block as defined in Table 7-62, repeated Number of Heads times.</td></tr></table>

Table 7-62. Get Head Info Head Information Block Format

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Port Number: Value encoding matches the Port Number field in the PCIe Link Capabilities register in the PCIe Capability structure.</td></tr><tr><td>1h</td><td>1</td><td>Bits[5:0]: Maximum Link Width: Value encoding matches the Maximum Link Width field in the PCIe Link Capabilities register in the PCIe Capability structureBits[7:6]: Reserved</td></tr><tr><td>2h</td><td>1</td><td>Bits[5:0]: Negotiated Link Width: Value encoding matches the Negotiated Link Width field in the PCIe Link Capabilities register in the PCIe Capability structureBits[7:6]: Reserved</td></tr><tr><td>3h</td><td>1</td><td>Bits[5:0]: Supported Link Speeds Vector: Value encoding matches the Supported Link Speeds Vector field in the PCIe Link Capabilities 2 register in the PCIe Capability structureBits[7:6]: Reserved</td></tr><tr><td>4h</td><td>1</td><td>Bits[5:0]: Max Link Speed: Value encoding matches the Max Link Speed field in the PCIe Link Capabilities register in the PCIe Capability structureBits[7:6]: Reserved</td></tr><tr><td>5h</td><td>1</td><td>Bits[5:0]: Current Link Speed: Value encoding matches the Current Link Speed field in the PCIe Link Status register in the PCIe Capability structureBits[7:6]: Reserved</td></tr><tr><td>6h</td><td>1</td><td>LTSSM State: Current link LTSSM Major state:00h = Detect01h = Polling02h = Configuration03h = Recovery04h = L005h = L0s06h = L107h = L208h = Disabled09h = Loopback0Ah = Hot ResetAll other encodings are reservedLink substates should be reported through vendor-defined diagnostics commands.</td></tr><tr><td>7h</td><td>1</td><td>First Negotiated Lane Number</td></tr><tr><td>8h</td><td>1</td><td>Link State FlagsBit[0]: Lane Reversal State:- 0 = Standard lane ordering- 1 = Reversed lane orderingBit[1]: Port PCIe Reset State (PERST#):- 0 = Not in reset- 1 = In resetBits[7:2]: Reserved</td></tr></table>

## 7.6.7.6 DCD Management Command Set

The DCD Management command set includes commands for querying and configuring Dynamic Capacity. It is used by the FM to manage memory assignment within a DCD. Memory management for GFDs is defined in Section 8.2.9.9.10.

## 7.6.7.6.1 Get DCD Info (Opcode 5600h)

This command retrieves the number of supported hosts, total Dynamic Capacity of the device, and supported region configurations. To retrieve the corresponding DCD info for a GFD, see Section 8.2.9.9.10.1.

Possible Command Return Codes:

• Success

• Unsupported

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-63. Get DCD Info Response Payload (Sheet 1 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>1</td><td>Number of Hosts: Total number of hosts that the device supports. This field shall have a minimum value of 1.</td></tr><tr><td>01h</td><td>1</td><td>Number of Supported DC Regions: The device shall report the total number of Dynamic Capacity Regions available per host. DCDs shall report between 1 and 8 regions. All other encodings are reserved.</td></tr><tr><td>02h</td><td>2</td><td>Reserved</td></tr><tr><td>04h</td><td>2</td><td>Bits[3:0]: Supported Add Capacity Selection Policies: Bitmask that specifies the selection policies, as defined in Section 7.6.7.6.5, that the device supports when capacity is added. At least one policy shall be supported. A value of 1 indicates that a policy is supported, and a value of 0 indicates that a policy is not supported:- Bit[0]: Free- Bit[1]: Contiguous- Bit[2]: Prescriptive- Bit[3]: Must be 0Bits[15:4]: Reserved</td></tr><tr><td>06h</td><td>2</td><td>Reserved</td></tr><tr><td>08h</td><td>2</td><td>Bits[1:0]: Supported Release Capacity Removal Policies: Bitmask that specifies the removal policies, as defined in Section 7.6.7.6.6, that the device supports when capacity is released. At least one policy shall be supported. A value of 1 indicates that a policy is supported, and a value of 0 indicates that a policy is not supported:- Bit[0]: Tag-based- Bit[1]: PrescriptiveBits[15:2]: Reserved</td></tr><tr><td>0Ah</td><td>1</td><td>Sanitize on Release Configuration Support Mask: Bitmask, where bit position corresponds to region number, indicating whether the Sanitize on Release capability is configurable (1) or not configurable (0) for that region.</td></tr><tr><td>0Bh</td><td>1</td><td>Reserved</td></tr><tr><td>0Ch</td><td>8</td><td>Total Dynamic Capacity: Total memory media capacity of the device available for dynamic assignment to any host in multiples of 256 MB.</td></tr></table>

Table 7-63. Get DCD Info Response Payload (Sheet 2 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>14h</td><td>8</td><td>Region 0 Supported Block Size Mask: Indicates the block sizes that the region supports. Each bit indicates a power of 2 supported block size, where bit n being set indicates that block size 2^n is supported. Bits[5:0] and bits[63:52] shall be 0. At least one block size shall be supported.</td></tr><tr><td>1Ch</td><td>8</td><td>Region 1 Supported Block Size Mask: As defined in Region 0 Supported Block Size Mask. Valid only if Number of Supported Regions &gt; 1.</td></tr><tr><td>24h</td><td>8</td><td>Region 2 Supported Block Size Mask: As defined in Region 0 Supported Block Size Mask. Valid only if Number of Supported Regions &gt; 2.</td></tr><tr><td>2Ch</td><td>8</td><td>Region 3 Supported Block Size Mask: As defined in Region 0 Supported Block Size Mask. Valid only if Number of Supported Regions &gt; 3.</td></tr><tr><td>34h</td><td>8</td><td>Region 4 Supported Block Size Mask: As defined in Region 0 Supported Block Size Mask. Valid only if Number of Supported Regions &gt; 4.</td></tr><tr><td>3Ch</td><td>8</td><td>Region 5 Supported Block Size Mask: As defined in Region 0 Supported Block Size Mask. Valid only if Number of Supported Regions &gt; 5.</td></tr><tr><td>44h</td><td>8</td><td>Region 6 Supported Block Size Mask: As defined in Region 0 Supported Block Size Mask. Valid only if Number of Supported Regions &gt; 6.</td></tr><tr><td>4Ch</td><td>8</td><td>Region 7 Supported Block Size Mask: As defined in Region 0 Supported Block Size Mask. Valid only if Number of Supported Regions &gt; 7.</td></tr></table>

## 7.6.7.6.2 Get Host DC Region Configuration (Opcode 5601h)

This command retrieves the Dynamic Capacity configuration for a specified host.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-64. Get Host DC Region Configuration Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>2</td><td>Host ID: For an LD-FAM device, the LD-ID of the host interface configuration to query.</td></tr><tr><td>2h</td><td>1</td><td>Region Count: The maximum number of region configurations to return in the output payload.</td></tr><tr><td>3h</td><td>1</td><td>Starting Region Index: Index of the first requested region.</td></tr></table>

Table 7-65. Get Host DC Region Configuration Response Payload (Sheet 1 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>2</td><td>Host ID: For an LD-FAM device, the LD-ID of the host interface configuration returned.</td></tr><tr><td>2h</td><td>1</td><td>Number of Available Regions: As defined in Get Dynamic Capacity Configuration Output Payload.</td></tr></table>

Table 7-65. Get Host DC Region Configuration Response Payload (Sheet 2 of 2)

<table><tr><td>3h</td><td>1</td><td>Number of Regions Returned: The number of entries in the Region Configuration List.</td></tr><tr><td>4h</td><td>Varies</td><td>Region Configuration List: DC Region Info for region specified via Starting Region Index input field. The format of each entry is defined in Table 7-66.</td></tr><tr><td>Varies</td><td>4</td><td>Total Number of Supported Extents: Total number of extents that the device supports on this LD.</td></tr><tr><td>Varies</td><td>4</td><td>Number of Available Extents: Remaining number of extents that the device supports, as defined in Section 9.13.3.3.</td></tr><tr><td>Varies</td><td>4</td><td>Total Number of Supported Tags: Total number of Tag values that the device supports on this LD.</td></tr><tr><td>Varies</td><td>4</td><td>Number of Available Tags: Remaining number of Tag values that the device supports, as defined in Section 9.13.3.3.</td></tr></table>

Table 7-66. DC Region Configuration

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>8</td><td>Region Base: As defined in Table 8-165.</td></tr><tr><td>08h</td><td>8</td><td>Region Decode Length: As defined in Table 8-165.</td></tr><tr><td>10h</td><td>8</td><td>Region Length: As defined in Table 8-165.</td></tr><tr><td>18h</td><td>8</td><td>Region Block Size: As defined in Table 8-165.</td></tr><tr><td>20h</td><td>1</td><td>Note: More than one bit may be set at a time.• Bits[1:0]: Reserved• Bit[2]: NonVolatile: As defined in the Flags field of Device Scoped Memory Affinity Structure defined in Coherent Device Attribute Table (CDAT) Specification• Bit[3]: Sharable: As defined in the Flags field of Device Scoped Memory Affinity Structure defined in CDAT Specification• Bit[4]: Hardware Managed Coherency: As defined in the Flags field of Device Scoped Memory Affinity Structure defined in CDAT Specification• Bit[5]: Interconnect specific Dynamic Capacity Management: As defined in the Flags field of Device Scoped Memory Affinity Structure defined in CDAT Specification• Bit[6]: Read-Only: As defined in the Flags field of Device Scoped Memory Affinity Structure defined in CDAT Specification• Bit[7]: Reserved</td></tr><tr><td>21h</td><td>3</td><td>Reserved</td></tr><tr><td>24h</td><td>1</td><td>• Bit[0]: Sanitize on Release: As defined in Table 8-165• Bits[7:1]: Reserved</td></tr><tr><td>25h</td><td>3</td><td>Reserved</td></tr></table>

## 7.6.7.6.3 Set DC Region Configuration (Opcode 5602h)

This command sets the configuration of a DC Region. This command shall be processed only when all capacity has been released from the region on all LDs. The device shall generate an Event Record of type Region Configuration Updated upon successful processing of this command.

This command shall fail with Unsupported under the following conditions:

• When all capacity has been released from the DC Region on all hosts, and one or more blocks are allocated to the specified region

• When the Sanitize on Release field does not match the region’s configuration, as reported from the Get Host DC Region Configuration, and the device does not support reconfiguration of the Sanitize on Release setting, as advertised by the

Sanitize on Release Configuration Support Mask in the Get DCD Info response payload

This command shall fail with Invalid Security State under the following condition:

• In support of confidential computing, if the device has been locked while utilizing secure CXL TSP interfaces, the device shall reject any attempts to change the DCD configuration by returning Invalid Security State status. See Section 11.5 for details on locking a device and locked device behavior.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

• Invalid Security State

Command Effects:

• Configuration Change after Cold Reset

• Configuration Change after Conventional Reset

• Configuration Change after CXL Reset

• Immediate Configuration Change

• Immediate Data Change

Table 7-67. Set DC Region Configuration Request and Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>1</td><td>Region ID: Specifies which region to configure. Valid range is from 0 to 7.</td></tr><tr><td>1h</td><td>3</td><td>Reserved</td></tr><tr><td>4h</td><td>8</td><td>Region Block Size: As defined in Table 8-165.</td></tr><tr><td>Ch</td><td>1</td><td>Bit[0]: Sanitize on Release: As defined in Table 8-165Bits[7:1]: Reserved</td></tr><tr><td>Dh</td><td>3</td><td>Reserved</td></tr></table>

## 7.6.7.6.4 Get DC Region Extent Lists (Opcode 5603h)

This command retrieves the Dynamic Capacity Extent List for a specified host.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• None

Table 7-68. Get DC Region Extent Lists Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0h</td><td>2</td><td>Host ID: For an LD-FAM device, the LD-ID of the host interface.</td></tr><tr><td>2h</td><td>2</td><td>Reserved</td></tr><tr><td>4h</td><td>4</td><td>Extent Count: The maximum number of extents to return in the output response. The device may not return more extents than requested; however, it can return fewer extents. 0 is valid and allows the FM to retrieve the Total Extent Count and Extent List Generation Number without retrieving any extent data.</td></tr><tr><td>8h</td><td>4</td><td>Starting Extent Index: Index of the first requested extent. A value of 0 will retrieve the first extent in the list.</td></tr></table>

Table 7-69. Get DC Region Extent Lists Response Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>2</td><td>Host ID: For an LD-FAM device, the LD-ID of the host interface query.</td></tr><tr><td>02h</td><td>2</td><td>Reserved</td></tr><tr><td>04h</td><td>4</td><td>Starting Extent Index: Index of the first extent in the list.</td></tr><tr><td>08h</td><td>4</td><td>Returned Extent Count: The number of extents returned in Extent List[ ].</td></tr><tr><td>0Ch</td><td>4</td><td>Total Extent Count: The total number of extents in the list.</td></tr><tr><td>10h</td><td>4</td><td>Extent List Generation Number: A device-generated value that is used to indicate that the list has changed.</td></tr><tr><td>14h</td><td>4</td><td>Reserved</td></tr><tr><td>18h</td><td>Varies</td><td>Extent List[ ]: Extent list for the specified host as defined in Table 8-51.</td></tr></table>

## 7.6.7.6.5 Initiate Dynamic Capacity Add (Opcode 5604h)

This command initiates the addition of Dynamic Capacity to the specified region on a host. This command shall complete when the device initiates the Add Capacity procedure, as defined in Section 8.2.9.2.2. The processing of the actions initiated in response to this command may or may not result in a new entry in the Dynamic Capacity Event Log. To perform Dynamic Capacity Add on a GFD, see Section 8.2.9.9.10.7.

A Selection Policy is specified to govern the device’s selection of which memory resources to add:

• Free: Unassigned extents are selected by the device, with no requirement for contiguous blocks

• Contiguous: Unassigned extents are selected by the device and shall be contiguous

• Prescriptive: Extent list of capacity to assign is included in the request payload

• Enable Shared Access: Enable access to extent(s) previously added to another host in a DC Region that reports the “Sharable” flag, as designated by the specified tag value

See Section 9.13.3.2 for examples of how this command may be used to set up different types of sharing arrangements.

The command shall fail with Invalid Input under the following conditions:

• When the command is sent with an invalid Host ID, or an invalid region number, or an unsupported Selection Policy

• When the Length field is not a multiple of the Block size and the Selection Policy is either Free or Contiguous

The command, with selection policy Enable Shared Access, shall also fail with Invalid Input under the following conditions:

• When the specified region is not Sharable

• When the tagged capacity is already mapped to any Host ID via a non-Sharable region

• When the tagged capacity cannot be added to the requested region due to deviceimposed restrictions

• When the same tagged capacity is currently accessible by the same LD

The command shall fail with Resources Exhausted when the length of the added capacity plus the current capacity present in all extents associated with the specified region exceeds the decode length for that region, or if there is insufficient contiguous space to satisfy a request with Selection Policy set to Contiguous.

The command shall fail with Invalid Extent List under the following conditions:

• When the Selection Policy is set to Prescriptive and the Extent Count is invalid

• When the Selection Policy is set to Prescriptive and any of the DPAs are already accessible to the same LD

The command shall fail with Resources Exhausted if the Extent List would cause the device to exceed its extent or tag tracking ability.

The command shall fail with Retry Required if its execution would cause the specified LD’s Dynamic Capacity Event Log to overflow.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

• Invalid Extent List

• Resources Exhausted

Command Effects:

• Configuration Change after Cold Reset

• Configuration Change after Conventional Reset

• Configuration Change after CXL Reset

• Immediate Configuration Change

• Immediate Data Change

Table 7-70. Initiate Dynamic Capacity Add Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>2</td><td>Host ID: For an LD-FAM device, the LD-ID of the host interface to which the capacity is being added.</td></tr><tr><td>02h</td><td>1</td><td>Bits[3:0]:Selection Policy: Specifies the policy to use for selecting which extents comprise the added capacity:- 0h = Free- 1h = Contiguous- 2h = Prescriptive- 3h = Enable Shared Access- All other encodings are reservedBits[7:4]:Reserved</td></tr><tr><td>03h</td><td>1</td><td>Region Number: Dynamic Capacity Region to which the capacity is being added. Valid range is from 0 to 7. This field is reserved when the Selection Policy is set to Prescriptive.</td></tr><tr><td>04h</td><td>8</td><td>Length: The number of bytes of capacity to add. Always a multiple of the configured Region Block Size returned in Get DCD Info. Shall be &gt;0. This field is reserved when the Selection Policy is set to Prescriptive or Enable Shared Access.</td></tr><tr><td>0Ch</td><td>10h</td><td>Tag: Context field utilized by implementations that make use of the Dynamic Capacity feature. This field is reserved when the Selection Policy is set to Prescriptive.</td></tr><tr><td>1Ch</td><td>4</td><td>Extent Count: The number of extents in the Extent List. Present only when the Selection Policy is set to Prescriptive.</td></tr><tr><td>20h</td><td>Varies</td><td>Extent List: Extent list of capacity to add as defined inTable 8-51. Present only when the Selection Policy is set to Prescriptive.</td></tr></table>

## 7.6.7.6.6 Initiate Dynamic Capacity Release (Opcode 5605h)

This command initiates the release of Dynamic Capacity from a host. This command shall complete when the device initiates the Remove Capacity procedure, as defined in Section 8.2.9.9.9. The processing of the actions initiated in response to this command may or may not result in a new entry in the Dynamic Capacity Event Log. To perform Dynamic Capacity removal on a GFD, see Section 8.2.9.9.10.8.

A removal policy is specified to govern the device’s selection of which memory resources to remove:

• Tag-based: Extents are selected by the device based on tag, with no requirement for contiguous extents

• Prescriptive: Extent list of capacity to release is included in request payload

To remove a host’s access to the shared extent, the FM issues Initiate Dynamic Capacity Release Request with Selection Policy=Tag-Based with the Host ID associated with that host. The Tag field must match the Tag value used during Capacity Add. The host access can be removed in any order. The physical memory resources and tag associated with a shared extent shall remain assigned and unavailable for re-use until that extent has been released from all hosts that have been granted access.

The command shall fail with Invalid Input under the following conditions:

• When the command is sent with an invalid Host ID, or an invalid region number, or an unsupported Removal Policy

• When the command is sent with a Removal Policy of Tag-based and the input Tag does not correspond to any currently allocated capacity

• When Sanitize on Release is set but is not supported by the device

• When the Tag represents sharable capacity, and the Extent List covers only a portion of the capacity associated with the Tag

The command shall fail with Resources Exhausted when the length of the removed capacity exceeds the total assigned capacity for that region or for the specified tag when the Removal Policy is set to Tag-based.

The command shall fail with Invalid Extent List when the Removal Policy is set to Prescriptive and the Extent Count is invalid or when the Extent List includes blocks that are not currently assigned to the region.

The command shall fail with Retry Required if its execution would cause the specified LD’s Dynamic Capacity Event Log to overflow, unless the Forced Removal flag is set, in which case the removal occurs regardless of whether an Event is logged.

The command shall fail with Resources Exhausted if the Extent List would cause the device to exceed its extent or tag tracking ability.

Possible Command Return Codes:

• Success

• Unsupported

• Invalid Input

• Internal Error

• Retry Required

• Invalid Extent List

• Resources Exhausted

Command Effects:

• Configuration Change after Cold Reset

• Configuration Change after Conventional Reset

• Configuration Change after CXL Reset

• Immediate Configuration Change

• Immediate Data Change

Table 7-71. Initiate Dynamic Capacity Release Request Payload (Sheet 1 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>2</td><td>Host ID: For an LD-FAM device, the LD-ID of the host interface from which the capacity is being released.</td></tr><tr><td>02h</td><td>1</td><td>FlagsBits[3:0]:Removal Policy: Specifies the policy to use for selecting which extents comprise the released capacity:- 0h = Tag-based- 1h = Prescriptive- All other encodings are reservedBit[4]:Forced Removal:- 1 = Device does not wait for a Release Dynamic Capacity command from the host. Host immediately loses access to released capacity.Bit[5]:Sanitize on Release:- 1 = Device shall sanitize all released capacity as a result of this request using the method described inSection 8.2.9.9.5.1. If this is a shared capacity, the sanitize operation shall be performed after the last host has released the capacity.Bits[7:6]:Reserved</td></tr><tr><td>03h</td><td>1</td><td>Reserved</td></tr><tr><td>04h</td><td>8</td><td>Length: The number of bytes of capacity to remove. Always a multiple of the configured Region Block Size returned in Get DCD Info. Shall be &gt; 0. This field is reserved when the Removal Policy is set to Prescriptive.</td></tr></table>

Table 7-71. Initiate Dynamic Capacity Release Request Payload (Sheet 2 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0Ch</td><td>10h</td><td>Tag: Optional opaque context field utilized by implementations that make use of the Dynamic Capacity feature. This field is reserved when the Removal Policy is set to Prescriptive.</td></tr><tr><td>1Ch</td><td>4</td><td>Extent Count: The number of extents in the Extent List. Present only when the Removal Policy is set to Prescriptive.</td></tr><tr><td>20h</td><td>Varies</td><td>Extent List: Extent list of capacity to release as defined in Table 8-51. Present only when the Removal Policy is set to Prescriptive.</td></tr></table>

## 7.6.7.6.7 Dynamic Capacity Add Reference (Opcode 5606h)

This command prevents the tagged sharable capacity from being sanitized, freed, and/ or reallocated, regardless of whether it is currently visible to any hosts via extent lists. The tagged capacity will remain allocated, and contents will be preserved even if all DCD Extents that reference it are removed.

This command has no effect and will return Success if the FM has already added a reference to the tagged capacity.

This command shall return Invalid Input if the Tag in the payload does not match an existing sharable tag.

Possible Command Return Codes:

• Success

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• Configuration Change after Cold Reset

• Configuration Change after Conventional Reset

• Configuration Change after CXL Reset

• Immediate Configuration Change

## Table 7-72. Dynamic Capacity Add Reference Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>10h</td><td>Tag: Tag that is associated with the memory capacity to be preserved.</td></tr></table>

## 7.6.7.6.8 Dynamic Capacity Remove Reference (Opcode 5607h)

This command removes a reference to tagged sharable capacity that was previously added via Dynamic Capacity Add Reference (see Section 7.6.7.6.7). If there are no remaining extent lists that reference the tagged capacity, the memory will be freed and sanitized if appropriate.

This command shall return Invalid Input if the Tag in the payload does not match an existing sharable tag.

Possible Command Return Codes:

• Success

• Invalid Input

• Internal Error

• Retry Required

Command Effects:

• Configuration Change after Cold Reset (if freed)

• Configuration Change after Conventional Reset (if freed)

• Configuration Change after CXL Reset (if freed)

• Immediate Configuration Change (if freed)

Table 7-73. Dynamic Capacity Remove Reference Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>10h</td><td>Tag: Tag that is associated with the memory capacity.</td></tr></table>

7.6.7.6.9 Dynamic Capacity List Tags (Opcode 5608h)

This command allows an FM to re-establish context by receiving a list of all existing tags, with bitmaps indicating which LDs have access, and a flag indicating whether the FM holds a reference.

Possible Command Return Codes:

• Success

• Invalid Input

• Internal Error

Command Effects:

• None

Table 7-74. Dynamic Capacity List Tags Request Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>04h</td><td>Starting Index: Index of the first tag to return.</td></tr><tr><td>04h</td><td>04h</td><td>Max Tags: Maximum number of tags to return in the response payload. If Max Tags is 0, no tags list will be returned; however, the Generation Number shall be valid.</td></tr></table>

Table 7-75. Dynamic Capacity List Tags Response Payload (Sheet 1 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>4</td><td>Generation Number: Generation number of the tags list. This number shall change every time the remainder of the command&#x27;s payload would change.</td></tr><tr><td>04h</td><td>4</td><td>Total Number of Tags: Maximum number of tags to return in the response payload.</td></tr><tr><td>08h</td><td>4</td><td>Number of Tags Returned: Number of tags returned in the Tags List.</td></tr></table>

Table 7-75. Dynamic Capacity List Tags Response Payload (Sheet 2 of 2)

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>0Ch</td><td>1</td><td>Validity BitmapBit[0]: Reference Bitmaps Valid: A value of 1 indicates that the Reference Bitmap fields in the Tags List are valid. This bit shall be 0 for GFDs and 1 for all other device types.Bit[1]: Pending Reference Bitmaps Valid: A value of 1 indicates that the Pending Reference Bitmap fields in the Tags List are valid. This bit shall be 0 for GFDs and 1 for all other device types.Bits[7:2]: Reserved.</td></tr><tr><td>0Dh</td><td>3</td><td>Reserved</td></tr><tr><td>10h</td><td>Varies</td><td>Tags List: List of Dynamic Capacity Tag Information structures. The format of each entry is defined in Table 7-76.</td></tr></table>

Table 7-76. Dynamic Capacity Tag Information

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>10h</td><td>Tag: Tag that is associated with the memory capacity.</td></tr><tr><td>10h</td><td>1</td><td>FlagsBit[0]: FM Holds Reference: When set, this bit indicates that the FM holds a reference on this Tag.Bits[7:1]: Reserved.</td></tr><tr><td>11h</td><td>3</td><td>Reserved</td></tr><tr><td>14h</td><td>20h</td><td>Reference Bitmap: Each 1 indicates an LD that has accepted the capacity associated with this tag. Bit 0 of the first byte represents LD 0, and bit 7 of the last byte represents LD 255. This field is reserved if the Reference Bitmaps Valid bit is not set in the Dynamic Capacity List Tags Response Payload (see Table 7-75).</td></tr><tr><td>34h</td><td>20h</td><td>Pending Reference Bitmap: Each 1 indicates an LD for which the tagged capacity has been added with no host response yet. Bit 0 of the first byte represents LD 0, and bit 7 of the last byte represents LD 255. This field is reserved if the Pending Reference Bitmaps Valid bit is not set in the Dynamic Capacity List Tags Response Payload (see Table 7-75).</td></tr></table>

## 7.6.8 Fabric Management Event Records

The FM API uses the Event Records framework defined in Section 8.2.9.2.1. This section defines the format of event records specific to Fabric Management activities.

## 7.6.8.1 Physical Switch Event Records

Physical Switch Event Records define events that are related to physical switch ports, as defined in Table 7-77.

Table 7-77. Physical Switch Events Record Format

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>30h</td><td>Common Event Record: See corresponding common event record fields defined in Section 8.2.9.2.1. The Event Record Identifier field shall be set to 77cf9271-9c02-470b-9fe4-bc7b75f2da97, which identifies a Physical Switch Event Record.</td></tr><tr><td>30h</td><td>1</td><td>Physical Port ID: Physical Port that is generating the event.</td></tr><tr><td>31h</td><td>1</td><td>Event Type: Identifies the type of event that occurred:00h = Link State Change01h = Slot Status Register Updated</td></tr><tr><td>32h</td><td>2</td><td>Slot Status Register: As defined in PCIe Base Specification.</td></tr><tr><td>34h</td><td>1</td><td>Reserved</td></tr><tr><td>35h</td><td>1</td><td>Bits[3:0]: Current Port Configuration State: See Table 7-19Bits[7:4]: Reserved</td></tr><tr><td>36h</td><td>1</td><td>Bits[3:0] Connected Device Mode: See Table 7-19Bits[7:4]: Reserved</td></tr><tr><td>37h</td><td>1</td><td>Reserved</td></tr><tr><td>38h</td><td>1</td><td>Connected Device Type: See Table 7-19</td></tr><tr><td>39h</td><td>1</td><td>Supported CXL Modes: See Table 7-19</td></tr><tr><td>3Ah</td><td>1</td><td>Bits[5:0]: Maximum Link Width: Value encoding matches the Maximum Link Width field in the PCIe Link Capabilities register in the PCIe Capability structureBits[7:6]: Reserved</td></tr><tr><td>3Bh</td><td>1</td><td>Bits[5:0]: Negotiated Link Width: Value encoding matches the Negotiated Link Width field in the PCIe Link Capabilities register in the PCIe Capability structureBits[7:6]: Reserved</td></tr><tr><td>3Ch</td><td>1</td><td>Bits[5:0]: Supported Link Speeds Vector: Value encoding matches the Supported Link Speeds Vector field in the PCIe Link Capabilities 2 register in the PCIe Capability structureBits[7:6]: Reserved</td></tr><tr><td>3Dh</td><td>1</td><td>Bits[5:0]: Max Link Speed: Value encoding matches the Max Link Speed field in the PCIe Link Capabilities register in the PCIe Capability structureBits[7:6]: Reserved</td></tr><tr><td>3Eh</td><td>1</td><td>Bits[5:0]: Current Link Speed: Value encoding matches the Current Link Speed field in the PCIe Link Status register in the PCIe Capability structureBits[7:6]: Reserved</td></tr><tr><td>3Fh</td><td>1</td><td>LTSSM State: See Section 7.6.7.1.</td></tr><tr><td>40h</td><td>1</td><td>First Negotiated Lane Number: Lane number of the lowest lane that has negotiated.</td></tr><tr><td>41h</td><td>2</td><td>Link state flags: See Section 7.6.7.1.</td></tr><tr><td>43h</td><td>3Dh</td><td>Reserved</td></tr></table>

## 7.6.8.2 Virtual CXL Switch Event Records

Virtual CXL Switch Event Records define events that are related to VCSs and vPPBs, as defined in Table 7-78.

Table 7-78. Virtual CXL Switch Event Record Format

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>30h</td><td>Common Event Record: See corresponding common event record fields defined in Section 8.2.9.2.1. The Event Record Identifier field shall be set to 40d26425-3396-4c4d-a5da-3d47263af425, which identifies a Virtual Switch Event Record.</td></tr><tr><td>30h</td><td>1</td><td>VCS ID</td></tr><tr><td>31h</td><td>1</td><td>vPPB ID</td></tr><tr><td>32h</td><td>1</td><td>Event Type: Identifies the type of event that occurred:00h = Binding Change01h = Secondary Bus Reset02h = Link Control Register Updated03h = Slot Control Register Updated</td></tr><tr><td>33h</td><td>1</td><td>vPPB Binding Status: Current vPPB binding state, as defined in Table 7-32. If Event Type is 00h, this field contains the updated binding state of a vPPB following the binding change. Successful bind and unbind operations generate events to the Informational Event Log. Failed bind and unbind operations generate events to the Warning Event Log.</td></tr><tr><td>34h</td><td>1</td><td>vPPB Port ID: Current vPPB bound port ID, as defined in Table 7-32. If Event Type is 00h, this field contains the updated binding state of a vPPB following the binding change. Successful bind and unbind operations generate events to the Informational Event Log. Failed bind and unbind operations generate events to the Warning Event Log.</td></tr><tr><td>35h</td><td>1</td><td>vPPB LD ID: Current vPPB bound LD-ID, as defined in Table 7-32. If Event Type is 00h, this field contains the updated binding state of a vPPB following the binding change. Successful bind and unbind operations generate events to the Informational Event Log. Failed bind and unbind operations generate events to the Warning Event Log.</td></tr><tr><td>36h</td><td>2</td><td>Link Control Register Value: Current Link Control register value, as defined in PCIe Base Specification.</td></tr><tr><td>38h</td><td>2</td><td>Slot Control Register Value: Current Slot Control register value, as defined in PCIe Base Specification.</td></tr><tr><td>3Ah</td><td>46h</td><td>Reserved</td></tr></table>

## 7.6.8.3 MLD Port Event Records

MLD Port Event Records define events that are related to switch ports connected to MLDs, as defined in Table 7-79.

## Table 7-79. MLD Port Event Records Payload

<table><tr><td>Byte Offset</td><td>Length in Bytes</td><td>Description</td></tr><tr><td>00h</td><td>30h</td><td>Common Event Record: See corresponding common event record fields defined in Section 8.2.9.2.1. The Event Record Identifier field shall be set to 8dc44363-0c96-4710-b7bf-04bb99534c3f, which identifies an MLD Port Event Record.</td></tr><tr><td>30h</td><td>1</td><td>Event Type: Identifies the type of event that occurred:00h = Error Correctable Message Received. Events of this type shall be added to the Warning Event Log.01h = Error Non-Fatal Message Received. Events of this type shall be added to the Failure Event Log.02h = Error Fatal Message Received. Events of this type shall be added to the Failure Event Log.</td></tr><tr><td>31h</td><td>1</td><td>Port ID: ID of the MLD port that is generating the event.</td></tr><tr><td>32h</td><td>2</td><td>Reserved</td></tr><tr><td>34h</td><td>8</td><td>Error Message: The first 8 bytes of the PCIe error message (ERR_COR, ERR_NONFATAL, or ERR_FATAL) that is received by the switch.</td></tr><tr><td>3Ch</td><td>44h</td><td>Reserved</td></tr></table>

## 7.7 CXL Fabric Architecture

The CXL fabric architecture adds new features to scale from a node to a rack-level interconnect to service the growing computational needs in many fields. Machine learning/AI, drug discovery, agricultural and life sciences, materials science, and climate modeling are some of the fields with significant computational demand. The computation density required to meet the demand is driving innovation in many areas, including near and in-memory computing. CXL Fabric features provide a robust path to build flexible, composable systems at rack scale that are able to capitalize on simple load/store memory semantics or Unordered I/O (UIO).

CXL fabric extensions allow for topologies of interconnected fabric switches using 12-bit PIDs (SPIDs/DPIDs) to uniquely identify up to 4096 Edge Ports. The following are the main areas of change to extend CXL as an interconnect fabric for server composability and scale-out systems:

• Expand the size of CXL fabric using Port Based Routing and 12-bit PIDs.

• Enable support for G-FAM devices (GFDs). A GFD is a highly scalable memory resource that is accessible by all hosts and all peer devices.

• Host and device peer communication may be enabled using UIO. A future ECN is planned to complete the definition for this use case.

Figure 7-25. High-level CXL Fabric Diagram  
![](images/4726af391572d08e03a2e76a35acaec9ab7d1fd1ceba6133a3d3bf185482e10e.jpg)

Figure 7-25 is a high-level illustration of a routable CXL Fabric. The fabric consists of one or more interconnected fabric switches. In this figure, there are “n” Switch Edge Ports (SEP ) on the Fabric where each Edge Port can connect to a CXL host root port or a CXL/PCIe device (Dev). As shown, a Fabric Manager (FM) connects to the CXL Fabric and may connect to selected endpoints over an out-of-band management network. The management network may be a simple 2-wire interface, such as SMBus, I2C, I3C, or a complex fabric such as Ethernet. The FM is responsible for the initialization and setup of the CXL Fabric and the assignment of devices to different Virtual Hierarchies. Extensions to FM API (see Section 7.6) to handle cross-domain traffic will be taken up as a future ECN.

Initially, the FM binds a set of devices to the host’s Virtual Hierarchies, essentially composing a system. After the system has booted, the FM may add or remove devices from the system using fabric bind and unbind operations. These system changes are presented to the hosts by the fabric switches as managed Hot-Add and Hot-Remove events as described in Section 9.9. This allows for dynamic reconfiguration of systems that are composed of hosts and devices.

Root ports on the CXL Fabric may be part of the same or different domains. If the root ports are in different domains, hardware coherency across those root ports is not a requirement. However, devices that support sharing (including MLDs, Multi-Headed devices, and GFDs) may support hardware-managed cache coherency across root ports in multiple domains.

## 7.7.1 CXL Fabric Use Case Examples

Following are a few examples of systems that may benefit from using CXL-switched Fabric for low-latency communication.

## 7.7.1.1 Machine-learning Accelerators

Accelerators used for machine-learning applications may use a dedicated CXL-switched Fabric for direct communication between devices in different domains. The same Fabric may also be used for sharing GFDs among accelerators. Each host and accelerator of same color shown in Figure 7-26 (basically, those that are directly above and below one another) belongs to a single domain. Accelerator devices can use UIO transactions to access memory on other accelerator and GFDs. In such a system, each accelerator is attached to a host and expected to be hardware-cache coherent with the host when using a CXL link. Communication between accelerators across domains is via the I/O coherency model. Device caching of data from another device memory (HDM or PDM) requires software-managed coherency with appropriate cache flushes and barriers. A

Switch Edge ingress port is expected to implement a common set of address decoders that is to be used for Upstream Ports and Downstream Ports. Implementations may enable a dedicated CXL Fabric for accelerators using features available in this revision. However, it is not fully defined by the specification. Peer communication is defined in Section 7.7.9.

Figure 7-26. ML Accelerator Use Case  
![](images/e2e981c72ff8ed249c82ad6b5bb9ce2a63e1b219aefc5b9faa80c68fb3582841.jpg)

## 7.7.1.2 HPC/Analytics Use Case

High-performance computing and Big Data Analytics are two areas that may also benefit from a dedicated CXL Fabric for host-to-host communication and sharing of G-FAM. CXL.mem or UIO may be used to access GFDs. Some G-FAM implementations may enable cross-domain hardware cache coherency. Software cache coherency may still be used for shared-memory implementations. Host-to-host communication is defined in Section 7.7.3.

NICs may be used to directly move data from network storage to G-FAM devices, using the UIO traffic class. CXL.mem and UIO use fabric address decoders to route to target GFDs that are members of many domains.

## Figure 7-27. HPC/Analytics Use Case

![](images/b247733ebdb9ee831c319bb19809f3f17000aee791a331ba39d3ff1336d04f7a.jpg)

## 7.7.1.3 Composable Systems

Support for multi-level switches with PBR fabric extensions provides additional capabilities for building software-composable systems. In Figure 7-28, a leaf/spine switch architecture is shown in which all resources are attached to the leaf switches. Each domain may span multiple switches. All devices must be bound to a host or an FM. Cross-domain traffic is limited to CXL.mem and UIO transactions.

Composing systems from resources within a single leaf switch allows for low-latency implementations. In such implementations, a spine switch is used only for crossdomain and G-FAM accesses.

Figure 7-28. Sample System Topology for Composable Systems  
![](images/860659af19de8646ea2b5b123f188f3830da20c898e6365f232c9484bdab941a.jpg)

## 7.7.2 Global-Fabric-Attached Memory (G-FAM)

## 7.7.2.1 Overview

G-FAM provides a highly scalable memory resource that is accessible by all hosts and peer devices within a CXL fabric. G-FAM ranges can be assigned exclusively to a single host/peer requester or can be shared by multiple hosts/peers. When shared, multirequester cache coherency can be managed by either software or hardware. Access rights to G-FAM ranges are enforced by decoders in Requester Edge ports and the target GFD.

GFD HDM space can be accessed by hosts/peers from multiple domains using CXL.mem, and by peer devices from multiple domains using CXL.io UIO. GFDs implement no PCI configuration space, and they are configured and managed instead via Global Memory Access Endpoints (GAEs) in Edge USPs or via out-of-band mechanisms.

Unlike an MLD, which has a separate Device Physical Address (DPA) space for each host/peer interface (LD), a GFD has one DPA space that is common across all hosts and peer devices. The GFD translates the Host Physical Address (HPA)<sup>1</sup> in each incoming request into a DPA, using per-requester translation information that is stored within the GFD Decoder Table. To create shared memory, two or more HPA ranges (each from a different requester) are mapped to the same DPA range. When the GFD needs to issue a BISnp, the GFD translates the DPA into an HPA for the associated host using the same GFD decoder information.

When a GFD receives a request, the requester is identified by the SPID in the request, which is referred to as the Requester PID or RPID. Using this term avoids confusion when describing messages that the GFD sends to the requester, where the RPID is used for the DPID, and the GFD PID is used for the SPID.

All memory capacity on a GFD is managed by the Dynamic Capacity (DC) mechanisms, as defined in Section 8.2.9.9.9. A GFD allows each requester to access up to 8 RPID non-overlapping decoders, where the maximum number of decoders per SPID is implementation dependent. Each decoder has a translation from HPA space to the common DPA space, a flag that indicates whether cache coherency is maintained by software or hardware, and information about multi-GFD interleaving, if used. For each requester, the FM may define DC Regions in DPA space and convey this information to the host via a GAE. It is expected that the host will program the Fabric Address Segment Table (FAST) decoders and GFD decoders for all RPIDs in its domain to map the entire DPA range of each DC Region that needs to be accessed by the host or by one of its associated accelerators.

G-FAM memory ranges can be interleaved across any power-of-two number of GFDs from 2 to 256, with an Interleave Granularity of 256B, 512B, 1 KB, 2 KB, 4 KB, 8 KB, or 16 KB. GFDs that are located anywhere within the CXL fabric, as defined in Section 2.7, may be used to contribute memory to an Interleave Set.

If a GFD supports UIO Direct P2P to HDM (see Section 7.7.9.1), all GFD ports shall support UIO, and for each GFD link whose link partner also supports UIO, VC3 shall be auto-enabled by the ports (see Section 7.7.11.5.1).

## 7.7.2.2 Host Physical Address View

Hosts that access G-FAM shall allocate a contiguous address range for Fabric Address space within their Host Physical Address (HPA) space, as shown in Figure 7-29. The Fabric Address range is defined by the FabricBase and FabricLimit registers. All host requests that fall within the Fabric Address range are routed to a selected CXL port. Hosts that use multiple CXL ports for G-FAM may either address interleave requests across the ports or may allocate a Fabric Address space for each port.

G-FAM requests from a host flow to a PBR Edge USP. In the USP, the Fabric Address range is divided into N equal-sized segments. A segment may be any power-of-two size from 64 GB to 8 TB, and must be naturally aligned. The number of segments implemented by a switch is implementation dependent. Host software is responsible for configuring the segment size so that the number of segments times the segment size fully spans the Fabric Address space. The FabricBase and FabricLimit registers can be programmed to any multiple of the segment size.

Each segment has an associated GFD or Interleave Set of GFDs. Requests whose HPA falls anywhere within the segment are routed to the specified GFD or to a GFD within the Interleave Set. Segments are used only for request routing and may be larger than the accessible portion of a GFD. When this occurs, the accessible portion of the GFD starts at address offset zero within the segment. Any requests within the segment that are above the accessible portion of the GFD will fail to positively decode in the GFD and will be handled as described in Section 8.2.4.20.

Host interleaving across root ports is entirely independent from GFD interleaving. Address bits that are used for root port interleaving and for GFD interleaving may be fully overlapping, partially overlapping, or non-overlapping. When the host uses root port interleaving, FabricBase, FabricLimit, and segment size in the corresponding PBR Edge USPs must be identically configured.

## 7.7.2.3 G-FAM Capacity Management

Figure 7-29. Example Host Physical Address View  
![](images/d63eb5ea564c60b753f244ec3129bbaedae26bb70831459ef0cf405579a99287.jpg)

GFDs are managed using CCIs like all other classes of CXL components. A GFD requires support for the PBR Link CCI message format, as defined in Section 7.7.11.6, on its CXL link and may optionally implement additional MCTP-based CCIs (e.g., SMBus).

G-FAM relies exclusively on the Dynamic Capacity (DC) mechanism for capacity management, as described in Section 8.2.9.9.9. GFDs have no “legacy” static capacity as shown in the left side of Figure 9-24 in Chapter 9.0. Dynamic Capacity for G-FAM has much in common with the Dynamic Capacity for LD-FAM:

• Both have identical concepts for DC Regions, Extents, and Blocks

• Both support up to 8 DC Regions per host/peer interface

• DC-related parameters in the CDAT for each are identical

• Mailbox commands for each are highly similar; however, the specific Mailbox access methods are considerably different

— For LD-FAM, the Mailbox for each host’s LD is accessed via LD structures

— For G-FAM, management for each host is defined in Section 7.7.2.6

An LD-FAM DCD (i.e., DCD-capable SLDs or MLDs) allocates memory capacity and binds it to a specific Host ID in one operation. A GFD allocates Dynamic Capacity to a named Memory Group in one operation and binds specific Host IDs to named Memory Groups in a separate operation. Thus, the GFD requires different DCD Management commands than LD-FAM DCDs.

In contrast to LD-FAM, each GFD has a single DPA space instead of a separate DPA space per host. G-FAM DPA space is organized by Device Media Partitions (DMPs), as shown in Figure 7-30. DMPs are DPA ranges with certain attributes. A fundamental DMP attribute is the media type (e.g., DRAM or PM). A DMP attribute that is configured by the FM is the DC Block size. DMPs expose all GFD memory that is assignable for host use.

The rules for DMPs are as follows:

• Each GFD contains 1-4 DMPs, whose size is configured by the FM.

• Each DC Region consists of part or all of one DMP assigned to a host/peer. Each DC Region can be mapped into an RPID’s HPA space using the GFD Decoder Table.

• Each DC Region inherits associated DMP attributes.

## Figure 7-30. Example HPA Mapping to DMPs

![](images/61aa4f46b6ad4b904dd3068ff85ce123c6e03f2819dd625c2c8dc8deab0dc442.jpg)  
Table 7-80 lists the key differences between LD-FAM and G-FAM.

Table 7-80. Differences between LD-FAM and G-FAM (Sheet 1 of 2)

<table><tr><td>Feature or Attribute</td><td>LD-FAM</td><td>G-FAM</td></tr><tr><td>Number of supported hosts</td><td>16 max</td><td>1000s architecturally;100s more realistic</td></tr><tr><td>Support for DMPs</td><td>No</td><td>Yes</td></tr><tr><td>Architected FM API support for DMP configuration by the FM</td><td>N/A</td><td>Yes</td></tr></table>

Table 7-80. Differences between LD-FAM and G-FAM (Sheet 2 of 2)

<table><tr><td>Feature or Attribute</td><td>LD-FAM</td><td>G-FAM</td></tr><tr><td>Routing and decoders used for HDM addresses</td><td>Interleave RP routing by host HDM DecoderInterleave VH routing in USPHDM Decoder or LDST decoder1-10 HDM Decoders in each LD</td><td>Interleave RP routing by host HDM DecoderInterleave fabric routing in USP FAST and Interleave DPID Table (IDT)1-8 GFD Decoders per RPID in the GFD</td></tr><tr><td>Interleave Ways (IW)</td><td> $\frac{1}{2}/4/8/16$  plus 3/6/12</td><td>2-256 in powers of 2</td></tr><tr><td>DC Block Size</td><td>Powers of 2, as indicated by Region * Supported Block Size Mask</td><td>64 MB and up in powers of 2</td></tr></table>

Additional differences exist in how MLDs and GFDs process requests. An MLD has three types of decoders that operate sequentially on incoming requests:

• Per-LD HDM decoders translate from HPA space to a per-LD DPA space, removing the interleaving bits

• Per-LD decoders determine within which per-LD DC Region the DPA resides, and then whether the addressed DC block within the Region is accessible by the LD

• Per-LD implementation-dependent decoders translate from the DPA to the media address

A GFD has two types of decoders that operate sequentially on incoming requests:

• Per-RPID GFD decoders translate from HPA space to a common DPA space, removing the interleaving bits. This DPA may be used as the media address directly or via a simple mapping.

• A common decoder determines within which Device Media Partition (DMP) the DPA is located, and then whether the block that is addressed within the DMP is accessible by the RPID.

## 7.7.2.4 G-FAM Request Routing, Interleaving, and Address Translations

The mechanisms for GFD request routing, interleaving, and address translations within both the Edge ingress port and the GFD are shown in Figure 7-31. GFD requests may arrive either at an Edge USP from a host or at an Edge DSP from a peer device. This is referred to as the Edge request port.

Figure 7-31. G-FAM Request Routing, Interleaving, and Address Translations  
![](images/4b42afad6f790158fe52eb828e8285d41f3eda33c48794208cbf299af657d8b0.jpg)  
The Edge request port shall decode the request HPA to determine the DPID of the target GFD using the $\mathsf { F A S T ^ { 1 } }$ and the Interleave DPID Table (IDT). The FAST contains one entry per segment. The FAST depth must be a power-of-two but is implementation dependent. The segment size is specified by the FSegSz[2:0] register as defined in Table 7-81. The FAST entry accessed is determined by bits X:Y of the request address, where Y = log2 of the segment size in bytes and $\mathsf { X } = \mathsf { \dot { Y } } + \mathsf { l o g } 2$ of the FAST depth in entries. The maximum Fabric Address space and the HPA bits that are used to address the FAST are shown in Table 7-81 for all supported segment sizes for some example FAST depths. For a host with a 52-bit HPA, the maximum Fabric Address space is 4 PB minus one segment each above and below the Fabric Address space for local memory and for MMIO, as shown in Figure 7-29.

Table 7-81. Fabric Segment Size Table<sup>1</sup>

<table><tr><td rowspan="2">FSegSz[2:0]</td><td rowspan="2">Fabric Segment Size</td><td colspan="4">FAST Depth (Entries)</td></tr><tr><td>256</td><td>1K</td><td>4K</td><td>16K</td></tr><tr><td>000b</td><td>64 GB</td><td>16 TBHPA[43:36]</td><td>64 TBHPA[45:36]</td><td>256 TBHPA[47:36]</td><td>1 PBHPA[49:36]</td></tr><tr><td>001b</td><td>128 GB</td><td>32 TBHPA[44:37]</td><td>128 TBHPA[46:37]</td><td>512 TBHPA[48:37]</td><td>2 PBHPA[50:37]</td></tr><tr><td>010b</td><td>256 GB</td><td>64 TBHPA[45:38]</td><td>256 TBHPA[47:38]</td><td>1 PBHPA[49:38]</td><td>4 PB - 512 GBHPA[51:38]</td></tr><tr><td>011b</td><td>512 GB</td><td>128 TBHPA[46:39]</td><td>512 TBHPA[48:39]</td><td>2 PBHPA[50:39]</td><td></td></tr><tr><td>100b</td><td>1 TB</td><td>256 TBHPA[47:40]</td><td>1 PBHPA[49:40]</td><td>4 PB - 2 TBHPA[51:40]</td><td></td></tr><tr><td>101b</td><td>2 TB</td><td>512 TBHPA[48:41]</td><td>2 PBHPA[50:41]</td><td></td><td></td></tr><tr><td>110b</td><td>4 TB</td><td>1 PBHPA[49:42]</td><td>4 PB - 8 TBHPA[51:42]</td><td></td><td></td></tr><tr><td>111b</td><td>8 TB</td><td>2 PBHPA[50:43]</td><td></td><td></td><td></td></tr></table>

1. LDST Segment Size (LSegSz) uses the same encodings as those defined for FSegSz.

Each FAST entry contains a valid bit (V), the number of interleaving ways (Intlv), the interleave granularity (Gran), and a DPID or IDT index (DPID/IX). The encodings for the Intlv and Gran fields are defined in Table 7-82 and Table 7-83, respectively. If the HPA is between FabricBase and FabricLimit inclusive and the FAST entry valid bit is set, then there is a FAST hit, and the FAST is used to determine the DPID. Otherwise, the target device is determined by other architected decoders.

Table 7-82. Segment Table Intlv[3:0] Field Encoding

<table><tr><td>Intlv[3:0]</td><td>GFD Interleaving Ways</td></tr><tr><td>0h</td><td>Interleaving is disabled</td></tr><tr><td>1h</td><td>2-way interleaving</td></tr><tr><td>2h</td><td>4-way interleaving</td></tr><tr><td>3h</td><td>8-way interleaving</td></tr><tr><td>4h</td><td>16-way interleaving</td></tr><tr><td>5h</td><td>32-way interleaving</td></tr><tr><td>6h</td><td>64-way interleaving</td></tr><tr><td>7h</td><td>128-way interleaving</td></tr><tr><td>8h</td><td>256-way interleaving</td></tr><tr><td>9h – Fh</td><td>Reserved</td></tr></table>

Table 7-83. Segment Table Gran[3:0] Field Encoding

<table><tr><td>Gran [3:0]</td><td>GFD Interleave Granularity</td></tr><tr><td>0h</td><td>256B</td></tr><tr><td>1h</td><td>512B</td></tr><tr><td>2h</td><td>1 KB</td></tr><tr><td>3h</td><td>2 KB</td></tr><tr><td>4h</td><td>4 KB</td></tr><tr><td>5h</td><td>8 KB</td></tr><tr><td>6h</td><td>16 KB</td></tr><tr><td>7h – Fh</td><td>Reserved</td></tr></table>

Note that FabricBase and FabricLimit may be used to restrict the amount of the FAST used. For example, for a host with a 52-bit HPA space, if the FAST is accessed using HPA[51:40] without restriction, then it would consume the entire HPA space. In this case, FabricBase and FabricLimit must be set to restrict the Fabric Address space to the desired range of HPA space. This has the effect of reducing the number of entries in the FAST that are being used.

FabricBase and FabricLimit may also be used to allow the FAST to start at an HPA that is not a multiple of the FAST depth. For example, for a host with a 52-bit HPA space, if 2 PB of Fabric Address space is needed to start at an HPA of 1 PB, then a 4K entry FAST with 512 GB segments can be accessed using HPA[50:39] with FabricBase set to 1 PB and FabricLimit set to 3 PB. HPAs 1 PB to 2 PB-1 will then correspond to FAST entries 2048 to 4095, while HPAs 2 PB to 3 PB-1 will wrap around and correspond to FAST entries 0 to 2047. When programming FabricBase, FabricLimit, and segment size, care must be taken to ensure that a wraparound does not occur that would result in aliasing multiple HPAs to the same segment.

On a FAST hit, if the FAST Intlv field is 0h, then GFD interleaving is not being used for this segment and the DPID/IX field contains the GFD’s DPID. If the Intlv field is nonzero, then the Interleave Way is selected from the HPA using the Gran and Intlv fields, and then added to the DPID/IX field to generate an index into the IDT. The IDT defines the set of DPIDs for each Interleave Set that is accessible by the Edge request port. For an N-way Interleave Set, the set of DPIDs is determined by N contiguous entries in the IDT, with the first entry pointed to by DPID/IX which may be anywhere in the IDT. The IDT depth is implementation dependent.

After the GFD’s DPID is determined, a request that contains the SPID of the Edge request port and the unmodified HPA is sent to the target GFD. The GFD shall then use the SPID to access the GFD Decoder Table (GDT) to select the decoders that are associated with the requester. Note that a host and its associated CXL devices will each have a unique RPID, and therefore each will use a different entry in the GDT. The GDT provides up to 8 decoders per RPID. Each decoder within a GFD Decoder Table entry contains structures defined in Section 8.2.9.9.10.19.

The GFD shall then compare, in parallel, the request HPA against all decoders to determine whether the request hits any decoder’s HPA range. To accomplish this, for each decoder, a DPA offset is calculated by first subtracting HPABase from HPA and then removing the interleaving bits. The LSB of the interleaving bits to remove is determined by the interleave granularity and the number of bits to remove is determined by the interleave ways. If offset ≥ 0, offset < DPALen, and the Valid bit is set, then the request hits within that decoder. If only one decoder hits, then the DPA is calculated by adding DPABase to the offset. If zero or multiple decoders hit, then an access error is returned.

After the request HPA is translated to DPA, the RPID and the DPA are used to perform the Dynamic Capacity access check, as described in Section 7.7.2.5, and to access the GFD snoop filter. The design of the snoop filter is beyond the scope of this specification.

When the snoop filter needs to issue a back-invalidate to a host/peer, the DPA is translated to an HPA by performing the HPA-to-DPA steps in reverse. The RPID is used to access the GDT to select the decoders for the requester, which may be the host itself or one of its devices that performs Direct P2P. The GFD shall then compare, in parallel, the DPA against all selected decoders to determine whether the back-invalidate hits any decoder’s DPA range.

This is accomplished by first calculating DPA offset = DPA – DPABase, and then testing whether offset ≥ 0, offset < DPALen, and the decoder is valid. If only one decoder hits, then the HPA is calculated by inserting the interleaving bits into the offset and then adding it to HPABase. When inserting the interleaving bits, the LSB is determined by interleave granularity, the number of bits is determined by the interleaving ways, and the value of the bits is determined by the way within the interleave set. If zero or multiple decoders hit, then an internal snoop filter error has occurred which will be handled as defined in a future specification update.

After the HPA is calculated, a BISnp with the GFD’s SPID and HPA is issued to the Edge Port containing the FAST decoder of the host/peer that owns this HDM-DB Region, using the PID stored in the snoop filter as the DPID. The FAST decoder then optionally checks whether the HPA is located within the FAST decoder’s Fabric Address space. The DPID and SPID are then removed, and the BISnp is then issued to the host/peer in HBR format.

## IMPLEMENTATION NOTE

It is recommended that a PBR switch size structures to support the typical to full scale of a PBR fabric.

It is recommended that the FAST have 4K to 16K entries.

It is recommended that the IDT have 4K to 16K entries to support a sufficient number of interleave groups and interleave ways to cover all GFDs in a system.

## 7.7.2.5 G-FAM Access Protection

G-FAM access protection is available at three levels of the hierarchy (see Figure 7-32):

• The first level of protection is through the host’s (or peer device’s) page tables. This fine-grained protection is used to restrict the Fabric Address space that is accessible by each process to a subset of that which is accessible by the host/peer.

• The second level of protection is described in the GAE in the form of the Global Memory Mapping Vector (GMV), described in Section 7.7.2.6.

• The third level of protection is at the target GFD itself and is fine grained. This section describes this third level of GFD protection.

Figure 7-32. Memory Access Protection Levels  
![](images/cba3b1d6a2b4cc4060070109ddcc73cf8ba21c7f022f6335904fd6a91326d156.jpg)

The GFD’s DPA space is divided into one or more Device Media Partitions (DMPs). Each DMP is defined by a base address within DPA space (DMPBase), a length (DMPLength), and a block size (DMPBlockSize). DMPBase and DMPLength must be a multiple of 256 MB, while DMPBlockSize must be a power-of-two size in bytes. The DMPBlockSize values that are supported by a device are device dependent and are defined in the GFD Supported Block Size Mask register. Each GFD decoder targets the DPA range of a DC Region within a single DMP (i.e., must not straddle DMP boundaries). The DC Region’s block size is determined by the associated DMP’s block size. The number of DMPs is device-implementation dependent. Unique DMPs are typically used for different media types (e.g., DRAM, NVM, etc.) and to provide sufficient DC block sizes to meet customer needs.

The GFD Dynamic Capacity protection mechanism is shown in Figure 7-33. To support scaling to 4096 CXL requesters, the GFD DC protection mechanism uses a concept called Memory Groups. A Memory Group is a set of DMP blocks that can be accessed by the same set of requesters. The maximum number of Memory Groups (NG) that are supported by a GFD is implementation dependent. Each DMP block is assigned a Memory Group ID (GrpID), using a set of Memory Group Tables (MGTs). There is one MGT per DMP. Each MGT has one entry per DMP block within the DMP, with entry 0 in the MGT corresponding to Block 0 within the DMP. The depth of each MGT is implementation dependent. DPA is decoded to determine within which DMP a request falls, and then that DMP’s MGT is used to determine the GrpID. The GrpID width is X = ceiling (log<sub>2</sub> (NG) ) bits. For example, a device with 33 to 64 groups would require 6-bit GrpIDs.

In parallel with determining the GrpID for a request, the Request SPID is used to index the SPID Access Table (SAT) to produce a vector that identifies which Memory Groups the SPID is allowed to access (GrpAccVec). After the GrpID for a request is determined, the GrpID is used to select a GrpAccVec bit to determine whether access is allowed.