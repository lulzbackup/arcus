# FindSIP.py
#
# Copyright (c) 2007, Simon Edwards <simon@simonzone.com>
# Redistribution and use is allowed according to the terms of the BSD license.
# For details see the accompanying COPYING-CMAKE-SCRIPTS file.

import sys
import os.path

try:
    # Try the old sipconfig. Many Linux distros still ship this in their packages.
    import sipconfig
    sipcfg = sipconfig.Configuration()
    
    sip_version = sipcfg.sip_version
    sip_version = sipcfg.sip_version
    sip_version_str = sipcfg.sip_version_str
    sip_bin = sipcfg.sip_bin
    default_sip_dir = sipcfg.default_sip_dir
    sip_inc_dir = sipcfg.sip_inc_dir

except ImportError:
    try:
        # Collect the info from the sip module and guess the rest.
        import sip
        from distutils import sysconfig
        
        sip_version = sip.SIP_VERSION
        sip_version_str = sip.SIP_VERSION_STR
        
        exe = sys.executable
        if exe is None:
            sys.exit(1)
        base_path = os.path.dirname(exe)
        sip_bin = os.path.join(base_path, "Lib\\site-packages\\PyQt5\\sip.exe")
        if not os.path.exists(sip_bin):
            sys.exit(1)
                
        sip_inc_dir = os.path.join(base_path, "Lib\\site-packages\\PyQt5\\include\\")
        if not os.path.exists(sip_inc_dir):
            sys.exit(1)

        default_sip_dir = os.path.join(base_path, "Lib\\site-packages\\PyQt5\\sip\\")
        if not os.path.exists(default_sip_dir):
            sys.exit(1)
        
    except ImportError:
        sys.exit(1)
        
print("sip_version:%06.0x" % sip_version)
print("sip_version_num:%d" % sip_version)
print("sip_version_str:%s" % sip_version_str)
print("sip_bin:%s" % sip_bin)
print("default_sip_dir:%s" % default_sip_dir)
print("sip_inc_dir:%s" % sip_inc_dir)
