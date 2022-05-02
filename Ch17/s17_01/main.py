#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name：    main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2022.05.02   18:35
-------------------------------------------------------------------------------
   @Change:   2022.05.02
-------------------------------------------------------------------------------
"""

import sys
from PyQt5.QtWidgets import QApplication
from Ch17.s17_01.cdialog import *


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = CDialog()
    widget.show()
    sys.exit(app.exec_())

