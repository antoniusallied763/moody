import Foundation
import IOKit.hid

let manager = IOHIDManagerCreate(kCFAllocatorDefault, IOOptionBits(kIOHIDOptionsTypeNone))
IOHIDManagerSetDeviceMatching(manager, nil)
let _ = IOHIDManagerOpen(manager, IOOptionBits(kIOHIDOptionsTypeNone))
if let devices = IOHIDManagerCopyDevices(manager) as? [IOHIDDevice] {
    for device in devices {
        if let name = IOHIDDeviceGetProperty(device, kIOHIDProductKey as CFString) as? String {
            if name.lowercased().contains("accelerometer") {
                let page = IOHIDDeviceGetProperty(device, kIOHIDPrimaryUsagePageKey as CFString) as? Int ?? -1
                let usage = IOHIDDeviceGetProperty(device, kIOHIDPrimaryUsageKey as CFString) as? Int ?? -1
                print("Found \(name): Page=\(page), Usage=\(usage)")
            }
        }
    }
}
