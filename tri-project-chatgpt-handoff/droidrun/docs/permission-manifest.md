# Permission Manifest

Portal APK (`com.droidrun.portal`) and DroidRun Host — Complete Permission Inventory

---

## Android Permissions (Portal APK)

### 1. Accessibility Service

| Field | Value |
|---|---|
| Permission | `android.permission.BIND_ACCESSIBILITY_SERVICE` |
| Grant type | User-approved via Settings → Accessibility |
| Risk level | **HIGH** |
| Mandatory | **Yes — DroidRun cannot function without this** |

**What it enables:** Reads the full UI accessibility tree (all visible element labels, positions, and properties). Injects synthetic input events (taps, swipes, key presses) without hardware interaction.

**Why it's required:** The Accessibility Service is the only non-root API that allows programmatic UI introspection and input injection on a standard Android device.

**What it can access:** All on-screen content from all apps while the service is enabled, including text fields, notifications visible in other apps, and interactive elements.

**Removable:** No. Removing this permission makes the Portal APK non-functional for its core purpose.

**Revocation path:** Settings → Accessibility → Downloaded Apps → DroidRun Portal → toggle off. Portal will still run but all UI interaction and observation will fail.

---

### 2. Display Over Other Apps (SYSTEM_ALERT_WINDOW)

| Field | Value |
|---|---|
| Permission | `android.permission.SYSTEM_ALERT_WINDOW` |
| Grant type | User-approved via Settings → Apps → Special app access |
| Risk level | **MEDIUM** |
| Mandatory | No |

**What it enables:** Allows Portal to display overlay UI elements on top of other running apps. Used for DroidRun status indicators and visual feedback during automation.

**Removable:** Yes. Disabling this permission removes visual overlay elements but does not affect core automation functionality.

**Revocation path:** Settings → Apps → DroidRun Portal → Display over other apps → toggle off.

---

### 3. Notification Access

| Field | Value |
|---|---|
| Permission | `android.permission.BIND_NOTIFICATION_LISTENER_SERVICE` |
| Grant type | User-approved via Settings → Notifications → Notification access |
| Risk level | **LOW** |
| Mandatory | No |

**What it enables:** Reads active notifications from all apps, including notification title, content, and package origin.

**What it can access:** All notifications from all installed apps (messages, emails, system alerts, etc.).

**Removable:** Yes. Disabling this permission prevents DroidRun agents from reading or responding to device notifications.

**Revocation path:** Settings → Notifications → Notification access → DroidRun Portal → toggle off.

---

### 4. Battery Optimization Exemption

| Field | Value |
|---|---|
| Permission | `REQUEST_IGNORE_BATTERY_OPTIMIZATIONS` |
| Grant type | User-approved via Settings → Battery → Battery optimization |
| Risk level | **LOW** |
| Mandatory | No (but strongly recommended for remote use) |

**What it enables:** Exempts Portal from Android's battery optimization, which would otherwise kill the process when idle. Required for long-running or background automation tasks.

**Removable:** Yes. Without this exemption, Android may kill the Portal process during inactivity, causing connection failures.

**Revocation path:** Settings → Battery → Battery optimization → All apps → DroidRun Portal → Optimize.

---

### 5. DroidRun Keyboard (Input Method Service)

| Field | Value |
|---|---|
| Permission | `android.permission.BIND_INPUT_METHOD` |
| Grant type | User-approved via Settings → General management → Keyboard |
| Risk level | **MEDIUM** |
| Mandatory | No |

**What it enables:** Provides a system keyboard input method that DroidRun can use to programmatically type text into apps that support the standard input method interface.

**What it can access:** All text entered via the keyboard, including passwords if the field does not use `textPassword` input type.

**Removable:** Yes. Without this, DroidRun falls back to `adb input text` for text injection, which is slower and may not work in all apps.

**Revocation path:** Settings → General management → Keyboard list and default → remove DroidRun Keyboard from enabled keyboards.

---

### 6. Connect to MobileRun

| Field | Value |
|---|---|
| Permission | Unknown |
| Grant type | Unknown |
| Risk level | **Unknown — Needs Verification** |
| Mandatory | Unknown |

**What it enables:** This permission appears in the DroidRun Portal permission list but its purpose has not been definitively verified. Likely relates to the `mobilerun-sdk` dependency.

**Action needed:** Inspect the Portal APK manifest (`aapt dump permissions com.droidrun.portal.apk`) and review `mobilerun-sdk` source to determine what this permission grants.

---

### 7. Internet (Implicit)

| Field | Value |
|---|---|
| Permission | `android.permission.INTERNET` |
| Grant type | Automatic (declared in manifest, no user prompt) |
| Risk level | **LOW** |
| Mandatory | Yes |

**What it enables:** Allows Portal to open the HTTP server socket on port 8080 that DroidRun communicates with.

**Scope:** The HTTP server binds to `localhost` (127.0.0.1) only. It is not directly accessible from the network except via `adb forward`.

---

## Host-Side Permissions (Windows)

### ADB Debugging Authorization

| Field | Value |
|---|---|
| Authorization type | ADB trust (RSA key pair) |
| Location | `%USERPROFILE%\.android\adbkey` (host), device authorization store |
| Risk level | **HIGH** (authorizes full ADB access) |

ADB authorization grants the host the ability to: install/uninstall APKs, read/write device storage (scoped), run shell commands, capture screenshots, forward ports, and start/stop processes.

The host's ADB key is generated once and stored at `%USERPROFILE%\.android\adbkey`. The corresponding public key is accepted by the device after user approval on the device screen. Once accepted, authorization persists until revoked from the device.

**Revocation path:** Settings → Developer options → Revoke USB debugging authorizations.

---

### Windows User Environment Variable Access

| Field | Value |
|---|---|
| Storage location | HKEY_CURRENT_USER\Environment |
| Variables | DROIDRUN_DEEPSEEK_KEY, DROIDRUN_OPENROUTER_KEY |
| Risk level | **MEDIUM** |

API keys are stored as Windows user-scoped environment variables. They are readable by any process running under the same Windows user account. They are not accessible to other Windows users or to processes running under SYSTEM.

**Risk:** Any process running as the current user can read these environment variables. This includes all applications, scripts, and shell sessions launched by that user.

**Mitigation:** Variables are user-scoped (not machine-scoped), not written to disk files, and not included in DroidRun logs.

---

## Permission Summary

| Permission | Required | Risk | Impact if Removed |
|---|---|---|---|
| Accessibility Service | **Mandatory** | High | Portal non-functional |
| Display over other apps | Optional | Medium | No visual overlays |
| Notification access | Optional | Low | No notification reading |
| Battery exemption | Recommended | Low | Portal may be killed in background |
| DroidRun Keyboard | Optional | Medium | Falls back to adb input |
| Connect to MobileRun | Unknown | Unknown | Unknown |
| Internet (implicit) | Mandatory | Low | Portal HTTP server cannot start |
| ADB authorization | Mandatory (host) | High | No device connection |
| Windows env vars | Required (host) | Medium | API keys not available |
