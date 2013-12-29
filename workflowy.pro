TARGET = workflowy
TEMPLATE = app

SOURCES += contents/code/workflowy.py

target.path = /usr/local/bin

desktop.path = /usr/share/applications
desktop.files += workflowy.desktop

INSTALLS += target desktop

OTHER_FILES += \
    README.md \
    LICENSE