# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cetko/projects/gns3/gns3-gui/gns3/modules/vmware/ui/vmware_vm_configuration_page.ui'
#
# Created by: PyQt5 UI code generator 5.5
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VMwareVMConfigPageWidget(object):

    def setupUi(self, VMwareVMConfigPageWidget):
        VMwareVMConfigPageWidget.setObjectName("VMwareVMConfigPageWidget")
        VMwareVMConfigPageWidget.resize(494, 381)
        self.verticalLayout = QtWidgets.QVBoxLayout(VMwareVMConfigPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTabWidget = QtWidgets.QTabWidget(VMwareVMConfigPageWidget)
        self.uiTabWidget.setObjectName("uiTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.uiACPIShutdownCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiACPIShutdownCheckBox.setObjectName("uiACPIShutdownCheckBox")
        self.gridLayout.addWidget(self.uiACPIShutdownCheckBox, 5, 0, 1, 2)
        self.uiCategoryComboBox = QtWidgets.QComboBox(self.tab)
        self.uiCategoryComboBox.setObjectName("uiCategoryComboBox")
        self.gridLayout.addWidget(self.uiCategoryComboBox, 2, 1, 1, 1)
        self.uiSymbolLabel = QtWidgets.QLabel(self.tab)
        self.uiSymbolLabel.setObjectName("uiSymbolLabel")
        self.gridLayout.addWidget(self.uiSymbolLabel, 1, 0, 1, 1)
        self.uiConsolePortLabel = QtWidgets.QLabel(self.tab)
        self.uiConsolePortLabel.setObjectName("uiConsolePortLabel")
        self.gridLayout.addWidget(self.uiConsolePortLabel, 3, 0, 1, 1)
        self.uiConsolePortSpinBox = QtWidgets.QSpinBox(self.tab)
        self.uiConsolePortSpinBox.setMaximum(65535)
        self.uiConsolePortSpinBox.setObjectName("uiConsolePortSpinBox")
        self.gridLayout.addWidget(self.uiConsolePortSpinBox, 3, 1, 1, 1)
        self.uiEnableConsoleCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiEnableConsoleCheckBox.setObjectName("uiEnableConsoleCheckBox")
        self.gridLayout.addWidget(self.uiEnableConsoleCheckBox, 4, 0, 1, 2)
        self.uiHeadlessModeCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiHeadlessModeCheckBox.setChecked(False)
        self.uiHeadlessModeCheckBox.setObjectName("uiHeadlessModeCheckBox")
        self.gridLayout.addWidget(self.uiHeadlessModeCheckBox, 6, 0, 1, 2)
        self.uiBaseVMCheckBox = QtWidgets.QCheckBox(self.tab)
        self.uiBaseVMCheckBox.setEnabled(True)
        self.uiBaseVMCheckBox.setObjectName("uiBaseVMCheckBox")
        self.gridLayout.addWidget(self.uiBaseVMCheckBox, 7, 0, 1, 2)
        self.uiNameLabel = QtWidgets.QLabel(self.tab)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiSymbolLineEdit = QtWidgets.QLineEdit(self.tab)
        self.uiSymbolLineEdit.setObjectName("uiSymbolLineEdit")
        self.horizontalLayout_7.addWidget(self.uiSymbolLineEdit)
        self.uiSymbolToolButton = QtWidgets.QToolButton(self.tab)
        self.uiSymbolToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiSymbolToolButton.setObjectName("uiSymbolToolButton")
        self.horizontalLayout_7.addWidget(self.uiSymbolToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.uiCategoryLabel = QtWidgets.QLabel(self.tab)
        self.uiCategoryLabel.setObjectName("uiCategoryLabel")
        self.gridLayout.addWidget(self.uiCategoryLabel, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 138, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.uiTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiPortNameFormatLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.uiPortNameFormatLineEdit.setText("")
        self.uiPortNameFormatLineEdit.setObjectName("uiPortNameFormatLineEdit")
        self.gridLayout_2.addWidget(self.uiPortNameFormatLineEdit, 2, 2, 1, 1)
        self.uiPortNameFormatLabel = QtWidgets.QLabel(self.tab_2)
        self.uiPortNameFormatLabel.setObjectName("uiPortNameFormatLabel")
        self.gridLayout_2.addWidget(self.uiPortNameFormatLabel, 2, 0, 1, 1)
        self.uiPortSegmentSizeLabel = QtWidgets.QLabel(self.tab_2)
        self.uiPortSegmentSizeLabel.setObjectName("uiPortSegmentSizeLabel")
        self.gridLayout_2.addWidget(self.uiPortSegmentSizeLabel, 3, 0, 1, 1)
        self.uiAdaptersSpinBox = QtWidgets.QSpinBox(self.tab_2)
        self.uiAdaptersSpinBox.setMinimum(0)
        self.uiAdaptersSpinBox.setMaximum(10)
        self.uiAdaptersSpinBox.setObjectName("uiAdaptersSpinBox")
        self.gridLayout_2.addWidget(self.uiAdaptersSpinBox, 0, 2, 1, 1)
        self.uiPortSegmentSizeSpinBox = QtWidgets.QSpinBox(self.tab_2)
        self.uiPortSegmentSizeSpinBox.setMaximum(128)
        self.uiPortSegmentSizeSpinBox.setSingleStep(4)
        self.uiPortSegmentSizeSpinBox.setObjectName("uiPortSegmentSizeSpinBox")
        self.gridLayout_2.addWidget(self.uiPortSegmentSizeSpinBox, 3, 2, 1, 1)
        self.uiAdaptersLabel = QtWidgets.QLabel(self.tab_2)
        self.uiAdaptersLabel.setObjectName("uiAdaptersLabel")
        self.gridLayout_2.addWidget(self.uiAdaptersLabel, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(248, 178, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 8, 1, 1, 2)
        self.uiAdapterTypesComboBox = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiAdapterTypesComboBox.sizePolicy().hasHeightForWidth())
        self.uiAdapterTypesComboBox.setSizePolicy(sizePolicy)
        self.uiAdapterTypesComboBox.setObjectName("uiAdapterTypesComboBox")
        self.gridLayout_2.addWidget(self.uiAdapterTypesComboBox, 5, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)
        self.uiUseAnyAdapterCheckBox = QtWidgets.QCheckBox(self.tab_2)
        self.uiUseAnyAdapterCheckBox.setObjectName("uiUseAnyAdapterCheckBox")
        self.gridLayout_2.addWidget(self.uiUseAnyAdapterCheckBox, 7, 0, 1, 3)
        self.uiFirstPortNameLabel = QtWidgets.QLabel(self.tab_2)
        self.uiFirstPortNameLabel.setObjectName("uiFirstPortNameLabel")
        self.gridLayout_2.addWidget(self.uiFirstPortNameLabel, 1, 0, 1, 1)
        self.uiFirstPortNameLineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.uiFirstPortNameLineEdit.setObjectName("uiFirstPortNameLineEdit")
        self.gridLayout_2.addWidget(self.uiFirstPortNameLineEdit, 1, 2, 1, 1)
        self.uiUseUbridgeCheckBox = QtWidgets.QCheckBox(self.tab_2)
        self.uiUseUbridgeCheckBox.setObjectName("uiUseUbridgeCheckBox")
        self.gridLayout_2.addWidget(self.uiUseUbridgeCheckBox, 6, 0, 1, 3)
        self.uiTabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.uiTabWidget)

        self.retranslateUi(VMwareVMConfigPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(VMwareVMConfigPageWidget)

    def retranslateUi(self, VMwareVMConfigPageWidget):
        _translate = QtCore.QCoreApplication.translate
        VMwareVMConfigPageWidget.setWindowTitle(_translate("VMwareVMConfigPageWidget", "VMware VM configuration"))
        self.uiACPIShutdownCheckBox.setText(_translate("VMwareVMConfigPageWidget", "Enable ACPI shutdown"))
        self.uiSymbolLabel.setText(_translate("VMwareVMConfigPageWidget", "Symbol:"))
        self.uiConsolePortLabel.setText(_translate("VMwareVMConfigPageWidget", "Console port:"))
        self.uiEnableConsoleCheckBox.setText(_translate("VMwareVMConfigPageWidget", "Enable remote console"))
        self.uiHeadlessModeCheckBox.setText(_translate("VMwareVMConfigPageWidget", "Start VM in headless mode"))
        self.uiBaseVMCheckBox.setText(_translate("VMwareVMConfigPageWidget", "Use as a linked base VM (experimental)"))
        self.uiNameLabel.setText(_translate("VMwareVMConfigPageWidget", "Name:"))
        self.uiSymbolToolButton.setText(_translate("VMwareVMConfigPageWidget", "&Browse..."))
        self.uiCategoryLabel.setText(_translate("VMwareVMConfigPageWidget", "Category:"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab), _translate("VMwareVMConfigPageWidget", "General settings"))
        self.uiPortNameFormatLabel.setText(_translate("VMwareVMConfigPageWidget", "Name format:"))
        self.uiPortSegmentSizeLabel.setText(_translate("VMwareVMConfigPageWidget", "Segment size:"))
        self.uiAdaptersLabel.setText(_translate("VMwareVMConfigPageWidget", "Adapters:"))
        self.label.setText(_translate("VMwareVMConfigPageWidget", "Type:"))
        self.uiUseAnyAdapterCheckBox.setText(_translate("VMwareVMConfigPageWidget", "Allow GNS3 to use any configured VMware adapter"))
        self.uiFirstPortNameLabel.setText(_translate("VMwareVMConfigPageWidget", "First port name:"))
        self.uiUseUbridgeCheckBox.setText(_translate("VMwareVMConfigPageWidget", "Use uBridge for network connections"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab_2), _translate("VMwareVMConfigPageWidget", "Network"))
