# check_config
Checking tool for Liux kernel-config and cpu-flags for some reason


# execute


```
(localhost) # ./check_config.py
checking KCONFIGS..
Checking KCONFIGS from ./config-5.9.4-1.g1043b8d-default

^CONFIG_SERIAL_EARLYCON_ARM_SEMIHOST is not found
^CONFIG_BOOT_PRINTK_DELAY is not found
CONFIG_NR_CPUS=480
CONFIG_ACPI_PCI_SLOT=y
CONFIG_HOTPLUG_PCI_ACPI=y
^CONFIG_SENSORS_ACPI_POWER is not found
^CONFIG_BUG_ON_DATA_CORRUPTION is not found
CONFIG_ARM64_CRYPTO=y
CONFIG_ARCH_RANDOM=y
^CONFIG_ARM64_AS_HAS_MTE is not found
^CONFIG_ARM64_MTE is not found
CONFIG_ARM64_BTI=y
CONFIG_ARM64_BTI_KERNEL=y
CONFIG_ARM64_BTI_KERNEL=y
CONFIG_CC_HAS_BRANCH_PROT_PAC_RET_BTI=y
CONFIG_ARM64_AMU_EXTN=y
CONFIG_IPMI_SSIF=m
CONFIG_DEBUG_FS=y
CONFIG_DEBUG_FS_ALLOW_ALL=y
CONFIG_ACPI_APEI=y
CONFIG_ACPI_APEI_GHES=y
CONFIG_ACPI_APEI_PCIEAER=y
CONFIG_ACPI_APEI_SEA=y
CONFIG_ACPI_APEI_MEMORY_FAILURE=y
CONFIG_ACPI_APEI_EINJ=m
CONFIG_ACPI_APEI_ERST_DEBUG=m
CONFIG_ACPI_APEI_EINJ=m
CONFIG_ARM_SDE_INTERFACE=y
CONFIG_ACPI_APEI_MEMORY_FAILURE=y
CONFIG_RTC_DRV_EFI=y
^CONFIG_I2C_SCMI is not found
checking flags..
Checking CPU flags from TEST-Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm fcma dcpop sve

sve is found
aes is found
rng is not found
dcpodp is not found
mte is not found
bti is not found
bf16 is not found

RESULTS ok= 18  fail= 12  total= 30
(localhost) #

```
