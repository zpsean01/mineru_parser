## B.6.3 \_BCM (Set the Brightness Level)

This method allows OSPM to set the brightness level of a built-in display output device.

The OS will only set levels that were reported via the \_BCL method. This method is required if \_BCL is implemented.

Arguments:(1)

Arg0 - An Integer containing the new brightness level

Return Value:

```txt
None
```

Example:

```javascript
Method (_BCM, 1) { // Set the requested level }
```

The method will be called in response to a power source change or at the specific request of the end user, for example, when the user presses a function key that represents brightness control.

## B.6.4 \_BQC (Brightness Query Current level)

This optional method returns the current brightness level of a built-in display output device. If present, it must be set by the platform for initial brightness.

Arguments:

None

## Return Value:

An Integer containing the current brightness level (must be one of the values returned from the \_BCL method)

## B.6.5 \_DDC (Return the EDID for this Device)

This method returns an EDID (Extended Display Identification Data) structure that represents the display output device. This method is required for integrated LCDs that do not have another standard mechanism for returning EDID data.

Arguments:

Arg0 - An Integer containing a code for the return data length:

```txt
1 - Return 128 bytes of data
2 - Return 256 bytes of data
3 - Return 384 bytes of data
4 - Return 512 bytes of data
```

## Return Value:

Either a Bufer containing the requested data (of the length specified in Arg0), or an Integer (value 0) if Arg0 was invalid

Example:

```autohotkey
Method (_DDC, 2) {
    (LEqual (Arg0, 1)) { Return (Buffer(128){ ,,,, }, ) }
    If (LEqual (Arg0, 2)) { Return (Buffer(256){ ,,,, }, ) }
    Return (0)
}
```

The bufer will later be interpreted as an EDID data block. The format of this data is defined by the VESA EDID specification.

## B.6.6 \_DCS (Return the Status of Output Device)

This method is required if hotkey display switching is supported.

## Arguments:

None

## Return Value:

An Integer containing the device status (32 bits) (see Table B-5 below).

Table B-5: Output Device Status

<table><tr><td>Bits</td><td>Definition</td></tr><tr><td>0</td><td>Output connector exists in the system now</td></tr><tr><td>1</td><td>Output is activated</td></tr><tr><td>2</td><td>Output is ready to switch</td></tr><tr><td>3</td><td>Output is not defective (it is functioning properly)</td></tr><tr><td>4</td><td>Device is attached (this is optional)</td></tr><tr><td>31:5</td><td>Reserved (must be zero)</td></tr></table>

## Example:

• If the output signal is activated by \_DSS, \_DCS returns 0x1F or 0x0F.

• If the output signal is inactivated by \_DSS, \_DCS returns 0x1D or 0x0D.

• If the device is not attached or cannot be detected, \_DCS returns 0x0xxxx and should return 0x1xxxx if it is attached.

• If the output signal cannot be activated, \_ DCS returns 0x1B or 0x0B.

• If the output connector does not exist (when undocked), \_DCS returns 0x00.

## B.6.7 \_DGS (Query Graphics State)

This method is used to query the state (active or inactive) of the output device. This method is required if hotkey display switching is supported.

Arguments:

None

Return Value:

An Integer containing the device state (32 bits) (see Table B-6 below)

Table B-6: Device State for \_DGS

<table><tr><td>Bits</td><td>Definition</td></tr><tr><td>0</td><td>0 - Next desired state is inactive / 1 - Next desired state is active</td></tr><tr><td>31:1</td><td>Reserved (must be zero)</td></tr></table>

The desired state represents what the user wants to activate or deactivate, based on the special function keys the user pressed. OSPM will query the desired state when it receives the display toggle event (described earlier).

## B.6.8 \_DSS (Device Set State)

OSPM will call this method when it determines the outputs can be activated or deactivated. OSPM will manage this to avoid flickering as much as possible. This method is required if hotkey display switching is supported.

## Arguments:(1)

Arg0 - An Integer containing the new device state (32 bits) (see Table B-7 below)

## Return Value:

None

Table B-7: Device State for \_DSS

<table><tr><td>Bits</td><td>Definition</td></tr><tr><td>0</td><td>0 - Set output device to inactive state 1 - Set output device to active state</td></tr><tr><td>30</td><td>0 - Do whatever Bit [31] requires 1 - Don’t do actual switching, but need to change _DGS to next state</td></tr><tr><td>31</td><td>0 - Don’t do actual switching, just cache the change1 - If Bit [30] = 0, commit actual switching, including any _DSS with MSB=0 called beforeIf Bit [30] = 1, don’t do actual switching, change _DGS to next state</td></tr><tr><td>29:1</td><td>Reserved (must be zero)</td></tr></table>

## Example Usage:

OS may call in such an order to turn of CRT, and turn on LCD:

```javascript
CRT._DSS(0);
LCD._DSS(80000001L);
or:
LCD._DSS(1);
CRT._DSS(80000000L);
```

OS may call in such an order to force platform runtime firmware to make \_DGS jump to next state without actual CRT, LCD switching:

```javascript
CRT._DSS(40000000L);
LCD._DSS(C0000001L);
```

## B.7 Notifications Specific to Output Devices

Output devices may need to know about external, asynchronous events. In order, each of these events corresponds to accommodate that, pressing a key or button on the following machine. Using these notifications is not appropriate if no physical device exists that is associated with them. OSPM may ignore any of these notifications if, for example the current user does not have permission to change the state of the output device. These notifications are only valid for Output Devices.

Table B-8: Notification Values for Output Devices

<table><tr><td>Value</td><td>Description</td></tr><tr><td>0x85</td><td>Cycle Brightness. Used to notify OSPM that the output device brightness should be increased by one level. Used to notify OSPM that the user pressed a button or key that is associated with cycling brightness. A useful response by OSPM would be to increase output device brightness by one or more levels. (Levels are defined in _BCL.) If the brightness level is currently at the maximum value, it should be set to the minimum level.</td></tr><tr><td>0x86</td><td>Increase Brightness. Used to notify OSPM that the output device brightness should be increased by one or more levels as defined by the _BCL object. Used to notify OSPM that the user pressed a button or key that is associated with increasing brightness. If the brightness level is currently at the maximum value, OSPM may should ignore the notification.</td></tr><tr><td>0x87</td><td>Decrease Brightness. Used to notify OSPM that the output device brightness should be decreased by one or more levels as defined by the _BCL object. Used to notify OSPM that the user pressed a button or key that is associated with decreasing device brightness. If the brightness level is currently at the minimum value, OSPM may should ignore the notification.</td></tr><tr><td>0x88</td><td>Zero Brightness. Used to notify OSPM that the output device brightness should be zeroed, effectively turning off any lighting that is associated with the device. Used to notify OSPM that the user pressed a button or key associated with zeroing device brightness. This is not to be confused with putting the device in a D3 state. While the brightness may be decreased to zero, the device may still be displaying, using only ambient light.</td></tr><tr><td>0x89</td><td>Display Device Off. Used to notify OSPM that the device should be put in an off state, one that is not active or visible to the user, usually D3, but possibly D1 or D2. Used to notify OSPM that the user pressed a low power button or key associated with putting the device in an off state. There is no need for a corresponding “device on” notification, for two reasons. First, OSPM may choose to toggle device state when this event is pressed multiple times. Second, OSPM may (and probably will) choose to turn the monitor on whenever the user types on the keyboard, moves the mouse, or otherwise indicates that he or she is attempting to interact with the machine.</td></tr></table>

## B.8 Notes on State Changes

It is possible to have any number of simultaneous active output devices. It is possible to have 0, 1, 2 . . . and so on active output devices. For example, it is possible for both the LCD device and the CRT device to be active simultaneously. It is also possible for all display outputs devices to be inactive (this could happen in a system where multiple graphics cards are present).

The state of the output device is separate from the power state of the device. The “active” state represents whether the image being generated by the graphics adapter would be sent to this particular output device. A device can be powered of or in a low-power mode but still be the active output device. A device can also be in an of state but still be powered on.

Example of the display-switching mechanism:

The laptop has three output devices on the VGA adapter. At this moment in time, the panel and the TV are both active, while the CRT is inactive. The automatic display-switching capability has been disabled by OSPM by calling \_DOS(0), represented by global variable display\_switching = 0.

The platform runtime firmware, in order to track the state of these devices, will have three global variable to track the state of these devices. There are currently initialized to:

crt\_active - 0 panel\_active - 1 tv\_active - 1

The user now presses the display toggle switch, which would switch the TV output to the CRT.

The platform runtime firmware first updates three temporary variables representing the desired state of output devices:

want\_crt\_active - 1 want\_panel\_active - 1 want\_tv\_active - 0

Then the platform runtime firmware checks the display\_switching variable. Because this variable is set to zero, the platform runtime firmware does not do any device reprogramming, but instead generates a Notify (VGA, 0x80/0x81) event for the display. This event will be sent to OSPM.

OSPM will call the \_DGS method for each enumerated output device to determine which devices should now be active. OSPM will determine whether this is possible, and will reconfigure the internal data structure of the OS to represent this state change. The graphics modes will be recomputed and reset.

Finally, OSPM will call the \_DSS method for each output device it has reconfigured.

## ò Note

OSPM may not have called the \_DSS routines with the same values and the \_DGS routines returned, because the user may be overriding the default behavior of the hardware-switching driver or operating system-provided UI. The data returned by the \_DGS method (the want\_XXX values) are only a hint to the OS as to what should happen with the output devices.

If the display-switching variable is set to 1, then the platform runtime firmware would not send the event, but instead would automatically reprogram the devices to switch outputs. Any legacy display notification mechanism could also be performed at this time.

## APPENDIX C: DEPRECATED CONTENT

This section lists content (if any) that is being deprecated from the ACPI specification in this release.

## A

ACPI Hardware, 16 ACPI Machine Language (AML), 16 ACPI Namespace, 16 ACPI Non-Volatile-Sleeping Memory (NVS)., 835 ACPI Reclaim Memory., 835 ACPI registers., 834 ACPI Source Language (ASL), 17 Add-in Card, 16 Add-in display adapter, 1114 Address Range Scrub (ARS), 17 Advanced Configuration and Power Interface (ACPI), 16 Advanced Programmable Interrupt Controller (APIC), 16 Appliance PC, 124

## B

Battery management, 29 BIOS, 17 Boot Firmware, 17 Boot-up display adapter, 1114 Built-in display adapter, 1114

## C

C0 Processor Power State, 27 C1 Processor Power State, 28 C2 Processor Power State, 28 C3 Processor Power State, 28 Cache memory configuration., 834 Central Processing Unit (CPU) or Processor, 17 Component, 17 Configuration / Plug and Play, 29 Control Method, 17 CPU configuration., 834

## D

D0 (Fully-On), 26 D1, 26 D2, 26 D3 (Of ), 25

D3hot, 25 Desktop, 124 Device, 17 Device and processor performance management, 29 Device Context, 18 Device Firmware, 18 Device Physical Address (DPA), 18 Device power management, 29 Differentiated System Description Table (DSDT), 18 Display device, 1114

## E

Embedded Controller, 18 Embedded Controller Interface, 18 Emulation mode, 608 Enterprise Server, 124 Expansion ROM Firmware, 18 eXtended Root System Description Table (XSDT), 23

## F

Firmware, 18 Firmware ACPI Control Structure (FACS), 18 Firmware Storage Device, 18 Fixed ACPI Description Table (FADT), 18 Fixed Feature Events, 19 Fixed Feature Registers, 19 Fixed Features, 19 Functional device configuration., 834

## G

G0 Working, 24 G1 Sleeping, 24 G2/S5 Soft Off, 24 G3 Mechanical Off, 24 General-Purpose Event Registers, 19 Generic Feature, 19 Generic Interrupt Controller (GIC), 19 Global System Status, 19

## H

HBA, 608 Host Processor, 19 Host Processor Boot Firmware, 19 Host Processor Runtime Firmware, 19 Hybrid Device, 608

## I

I/O APIC, 20 I/O SAPIC, 20 Ignored Bits, 19 Intel Architecture-Personal Computer (IA-PC), 20

## L

Label Storage Area, 20 Legacy, 20 Legacy BIOS, 20 Legacy Hardware, 20 Legacy OS, 20 Local APIC, 20 Local SAPIC, 20

## M

Management Firmware, 20 Memory controller configuration., 834 Mobile, 124 Multiple APIC Description Table (MADT), 20

## N

Namespace, 20 Native mode, 608 Native SATA aware, 608 Non-Host Processor, 20 Non-native SATA aware, 608 NVDIMM, 21

## O

Object, 21 Object name, 21 Operating System-directed Power Management (OSPM), 21 Option ROM Firmware, 21 Output device, 1114

## P

P0 Performance State, 28 P1 Performance State, 28 Package, 21 Performance Server, 124 Peripheral, 21 Persistent Memory (pmem), 21 Platform, 21

## Index

Platform Boot Firmware, 21 Platform Firmware, 21 Platform Runtime Firmware, 21 Pn Performance State, 28 Power Button, 21 Power Management, 21 Power Resources, 22 Power Sources, 22 Processor power management, 29

## R

Register Grouping, 22 Reserved Bits, 22 Root System Description Pointer (RSDP), 22 Root System Description Table (RSDT), 22 Runtime Firmware, 22

## S

S1 Sleeping State, 27 S2 Sleeping State, 27 S3 Sleeping State, 27 S4 Non-Volatile Sleep, 24 S4 Sleeping State, 27 S5 Soft Off State, 27 Secondary System Description Table (SSDT), 22 Sleep Button, 22 Smart Battery Subsystem, 22 Smart Battery Table, 22 SMBus Controller, 30 SMBus Interface, 22 Software, 22 SOHO Server, 124 System, 23 System BIOS, 23 System Context, 23 System Control Interrupt (SCI), 23 System Events, 29 System Management Bus (SMBus), 23 System Management Interrupt (SMI), 23 System Physical Address (SPA), 22 System power management, 29

## T

Tablet, 124 Thermal management, 30 Thermal States, 23

## U

UEFI, 23 UEFI Drivers, 23

## W

Workstation, 124