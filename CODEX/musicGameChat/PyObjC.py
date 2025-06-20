import sys
import objc
from Cocoa import (
    NSApplication, NSApp, NSWindow, NSButton, NSTextField, NSView,
    NSRect, NSPoint, NSSize, NSBackingStoreBuffered, NSRunningApplication,
    NSApplicationActivateIgnoringOtherApps
)

class MenuDelegate(objc.lookUpClass('NSObject')):
    signedInAs = None

    def init(self):
        self = objc.super(MenuDelegate, self).init()
        if self is None:
            return None
        self.window = None
        self.status_label = None
        return self

    def applicationDidFinishLaunching_(self, notification):
        frame = NSRect(NSPoint(100, 100), NSSize(350, 300))
        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            frame,
            15,  # titled, closable, miniaturizable, resizable
            NSBackingStoreBuffered,
            False
        )
        self.window.setTitle_("Music Game Menu")

        content = self.window.contentView()

        # Status label
        self.status_label = NSTextField.alloc().initWithFrame_(NSRect(NSPoint(20, 240), NSSize(300, 24)))
        self.status_label.setEditable_(False)
        self.status_label.setBezeled_(False)
        self.status_label.setDrawsBackground_(False)
        self.status_label.setStringValue_("Not signed in.")
        content.addSubview_(self.status_label)

        # Buttons
        actions = [
            ("Register", self.register_),
            ("Sign In", self.signIn_),
            ("Display User Names", self.displayUsers_),
            ("Display High Scores", self.displayHigh_),
            ("Exit", self.exit_)
        ]
        for i, (title, action) in enumerate(actions):
            btn = NSButton.alloc().initWithFrame_(NSRect(NSPoint(20, 200 - i*40), NSSize(300, 32)))
            btn.setTitle_(title)
            btn.setTarget_(self)
            btn.setAction_(action)
            content.addSubview_(btn)

        self.window.makeKeyAndOrderFront_(None)
        # Bring app to front
        NSRunningApplication.currentApplication().activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

    def update_status(self):
        if self.signedInAs:
            self.status_label.setStringValue_(f"Signed in as: {self.signedInAs}")
        else:
            self.status_label.setStringValue_("Not signed in.")

    def register_(self, sender):
        self.status_label.setStringValue_("Register clicked (implement logic)")

    def signIn_(self, sender):
        self.signedInAs = "example_user"
        self.update_status()

    def displayUsers_(self, sender):
        self.status_label.setStringValue_("Display Users clicked (implement logic)")

    def displayHigh_(self, sender):
        self.status_label.setStringValue_("Display High Scores clicked (implement logic)")

    def exit_(self, sender):
        NSApp().terminate_(None)

if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    delegate = MenuDelegate.alloc().init()
    app.setDelegate_(delegate)
    app.run()