#! /usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import os
import shlex

os_info = os.uname()
config_name ="/boot/config-" + os_info.release
config_name ="./config-5.3.18-63.ga82cef8-default"
config_name ="./config-5.10.0-0.rc1.20201028gited8780e3f2ec.57.fc34.aarch64"
config_name ="./config-5.9.4-1.g1043b8d-default"
#config_name ="./config-5.3.18-52.g8062a67-default"
configs = [
    "^CONFIG_SERIAL_EARLYCON_ARM_SEMIHOST", # FUJITSU-5
    "^CONFIG_BOOT_PRINTK_DELAY", # FUJITSU-5
    "^CONFIG_NR_CPUS=", # FUJITSU-6
    "^CONFIG_ACPI_PCI_SLOT", # FUJITSU-7
    "^CONFIG_HOTPLUG_PCI_ACPI", # FUJITSU-7
    "^CONFIG_SENSORS_ACPI_POWER", # FUJITSU-7
    "^CONFIG_BUG_ON_DATA_CORRUPTION", # FUJITSU-8 
    "^CONFIG_ARM64_CRYPTO", # FUJITSU-11
    "^CONFIG_ARCH_RANDOM",# FUJITSU-12
    "^CONFIG_ARM64_AS_HAS_MTE", #  FUJITSU-15
    "^CONFIG_ARM64_MTE", #  FUJITSU-15
    "^CONFIG_ARM64_BTI", # FUJITSU-16
    "^CONFIG_ARM64_BTI_KERNEL", # FUJITSU-16
    "^CONFIG_CC_HAS_BRANCH_PROT_PAC_RET_BTI", # FUJITSU-16
    "^CONFIG_ARM64_AMU_EXTN", # FUJITSU-18
    "^CONFIG_IPMI_SSIF", # FUJITSU-24
    "^CONFIG_DEBUG_FS", # FUJITSU-26
    "^CONFIG_ACPI_APEI", # FUJITSU-26
    "^CONFIG_ACPI_APEI_EINJ", # FUJITSU-26
    "^CONFIG_ARM_SDE_INTERFACE", # FUJITSU-33
    "^CONFIG_ACPI_APEI_MEMORY_FAILURE", # FUJITSU-33
    "^CONFIG_RTC_DRV_EFI", # FUJITSU-34
    "^CONFIG_I2C_SCMI" #FUJITSU-35
    ]
flags = [
    "sve", # sve
    "aes", # aes
    "rng",# FUJITSU-12
    "dcpodp", # FUJITSU-13
    "mte", #  FUJITSU-15
    "bti", # FUJITSU-16
    "bf16", # FUJITSU-19
    "i8mm" # FUJITSU-20    
    ]


total=0
fail=0
ok_count=0
#
# Checking for KCONFIGS
#
print ('checking KCONFIGS..')
print ("Checking KCONFIGS from " + config_name + "\n")
for key in configs:
    cmd = "grep " + key + " "  + config_name
#    print(cmd)
    tokens = shlex.split(cmd)
    c = subprocess.run(tokens)
    if c.returncode > 0:
        print( '\033[32m'+ key + '\033[0m is not found')
        fail+=1
    else:
       ok_count+=1
    total+=1
#
# Checking for CPU Feature flags
#

lscpu = subprocess.run('/usr/bin/lscpu',stdout = subprocess.PIPE)
cpuflags=lscpu.stdout.decode("utf8")
cpuflags="TEST-Flags: fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpuid asimdrdm fcma dcpop sve"
print ('checking flags..')
print ("Checking CPU flags from " + cpuflags + "\n")
for element in flags:
    if cpuflags.find(element) > 0:
        print( element + ' is found')
        ok_count+=1
    else:
        print( '\033[32m'+ element + '\033[0m is not found')        
        fail+=1
    total+=1

#
# Print results
print('\nRESULTS ok=', ok_count,' fail=', fail, ' total=', total)
