%define device t5

%define mkbootimg_cmd mkbootimg --cmdline 'console=ttyMSM0,115200,n8 androidboot.console=ttyMSM0 earlycon=msm_serial_dm,0xc1b0000 selinux=0 audit=0 androidboot.hardware=qcom user_debug=31 msm_rtb.filter=0x37 ehci-hcd.park=3 lpm_levels.sleep_disabled=1 sched_enable_hmp=1 sched_enable_power_aware=1 service_locator.enable=1 swiotlb=2048 androidboot.configfs=true androidboot.usbcontroller=a800000.dwc3 firmware_class.path=/vendor/firmware_mnt/image loop.max_part=7 systemd.legacy_systemd_cgroup_controller=yes' --kernel %{kernel} --ramdisk %{initrd} --base 0x00000000 --pagesize 4096 --kernel_offset 0x00008000 --ramdisk_offset 0x01000000 --second_offset 0x00f00000 --tags_offset 0x00000100 --board '' --output

%define root_part_label userdata
%define factory_part_label system_b

%define display_brightness_path /sys/class/leds/lcd-backlight/max_brightness
%define display_brightness 255

%include initrd/droid-hal-device-img-boot.inc

